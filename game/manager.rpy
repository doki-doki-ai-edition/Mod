init python:
    import json
    import os
    import random
    import requests
    import math
    import time
    import base64
    import io
    import re


    with open(config.basedir + "/game/assets/prompts/prompt_templates.json", "r") as f:
        prompt = json.load(f)


    class AIManager():
        def __init__(self, character_name, chathistory, full_path, resume=False):
            self.character_name = character_name
            self.chathistory = chathistory
            self.full_path = full_path
            self.resume = resume
            self.NARRATION = False
            self.rnd = random.randint(1,7)
            self.retrying = False
            self.dbase = Data(path_to_user_dir=self.full_path)




        def get_char_name(self, aireply):
            # WIP method that should be used when multiple
            # characters are speaking
            if "[CHAR]" in aireply:
                pass    
            return self.character_name




        def controlMood(self, face, body):
            """Display different facial expressions"""
            spacezone = self.dbase.getSceneData("zone")
            if spacezone == "true":
                return self.dbase.updateSceneData("character", self.character_name)
            
            if not face or not body: return


            char_name = Configs().characters[self.character_name.title()]
            full_sprite_emotions = char_name["full_sprites"] # dont render "left" or "right" body sprites if head_sprite returns smthing from this list
            head_sprite = char_name["head"]
            leftside_sprite = char_name["left"]
            rightside_sprite = char_name["right"]

            self.dbase.updateSceneData("character", self.character_name)

            for h in head_sprite:
                if h == face.lower():
                    self.dbase.updateSceneData("head_sprite", head_sprite[h])

            if head_sprite in full_sprite_emotions:
                return


            for l in leftside_sprite:
                if body == body.lower():
                    self.dbase.updateSceneData("left_sprite", leftside_sprite[l])

            for rr in rightside_sprite:
                if rr == body.lower():
                    self.dbase.updateSceneData("right_sprite", rightside_sprite[rr])




        def controlBackground(self, scene):
            """Display different background image"""
            if not scene: return

            bg_scenes = Configs().bg_scenes
            for key in ('default', 'checks'):
                if scene in bg_scenes[key]:
                    return self.dbase.updateSceneData("background", bg_scenes[key][scene])

            return self.dbase.updateSceneData("background", bg_scenes['checks']["clubroom"])



            
        def safeResponse(self, raw_response):
            """A response that's not entirely raw. If the AI
            speaks out of character but still returns the correct
            format, only capture the format it outputs"""
            clean_response = raw_response
            spacezone = self.dbase.getSceneData("zone")
            if "[SCENE]" in clean_response:
                clean_response = "[SCENE]" + clean_response.split("[SCENE]")[1]

            elif spacezone == "true":
                clean_response =  "[CONTENT]" + clean_response.split("[CONTENT]")[1].strip()


            if "[CONTENT]" in clean_response:
                clean_response = re.sub(r'\*.*?\*', '', clean_response) # gets rid of anything in asterisks

            return clean_response




        def removeKeywords(self, reply):
            """Get rid of keywords and return a clean string"""

            def getContent(start, end, reply=reply):
                try:
                    content = reply.split(start)[1].split(end)[0].strip()
                    return content
                except IndexError:
                    return None
                except AttributeError:
                    return None

            char = getContent('[CHAR]', '[CONTENT]') # Currently unused, just a placeholder once the usage of multiple chars is implemented
            face = getContent('[FACE]', '[BODY]')
            body = getContent('[BODY]', '[CONTENT]')
            scene = getContent('[SCENE]', '[FACE]')

            reply = reply.split('[END]')[0] # remove anything after [END]
            if scene:
                # Sometimes a model responds w/ text before [SCENE]
                # This removes any text before and only keeps [SCENE] and
                # everything that comes after it
                reply = "[SCENE] " + reply.split("[SCENE]")[1]

            if "[CONTENT]" in reply:
                reply = reply.split("[CONTENT]")[1].strip()

                # If the character replies with smthing like *giggles* remove it.
                # (and yes im using regex here)
                reply = re.sub(r'\*.*?\*', '', reply)
                # If the character replies with smthing like [silence] remove it.
                reply = re.sub(r'\[.*?\]', '', reply)
            else:
                # Typically this means that the model didnt return a proper content field
                reply = "ERROR"

            return reply, char, face, body, scene



        def removePlaceholders(self):
            """remove placeholders in json files"""
            level_zone = ""
            
            try: level_normal = Info().getExamplePrompts[f"{self.character_name}"]
            except KeyError: level_normal = Info().getCustomPrompts[f"{self.character_name}"]


            if self.character_name in Info().whitelist_purgatory:
                level_zone = Info().getExamplePrompts[f"{self.character_name}_purgatory"]

            spacezone = self.dbase.getSceneData("zone")

            renpy.log(f">>> rmvPlace func: spacezone is {spacezone}")
            renpy.log(f">>> rmvPlace func (PERSISTENT): spacezone is {spacezone}")
            raw_examples = level_normal if spacezone != "true" else  level_zone


            bg_scenes = [s for s in Configs().bg_scenes["default"]]
            emotions = ', '.join([e for e in Configs().characters[self.character_name.title()]['head']]) if spacezone != "true" else ""
            backgrounds = ', '.join(bg_scenes)

            if spacezone != "true":
                string = raw_examples[0]['content'].replace("{{format}}", Info().format["roleplay"])
            else:
                string = raw_examples[0]['content'].replace("{{format}}", Info().format["purgatory"])

            string = string.replace("{{char}}", self.character_name)
            string = string.replace("{{emotes}}", emotions)
            string = string.replace("{{scenes}}", backgrounds)
            string = string.replace("{{user}}", persistent.playername)
            string = string.replace("{{body}}", Configs().body_types(self.character_name.title()))

            string = raw_examples[0]['content'] = string
            raw_examples[0]['content'] = string

            if spacezone != "true":
                with open(self.full_path + f"/full_history.json", 'w') as f:
                    json.dump(raw_examples + self.chathistory, f, indent=2)

            return raw_examples




        def checkForContextLimit(self, range=120, contains_system_prompt=False):
            """Estimates the amount of tokens in the chathistory.
            If the max context window for an LLM is set to (for eg.) 1024 then if the tokens
            exceed that amount, the start of the chathistory will be deleted.
            
            Both the user message and the assistant message.

            Args:
                range -- the amount of words it will take before clearing up the chat. eg.
                        if the max context window is 1024, with a range of 40 and the current
                        context of the chathistory is >= 984 then it will delete the chat (first 2 msgs or more)
                        once the current tokens reach 984 or higher.
                
                contains_system_prompt -- Determines if the first index should be deleted or skipped
                                        (which would typically be the system prompt)
            """

            max_tokens = int(persistent.context_window)
            delete_pos = 0 if contains_system_prompt == False else 1
            current_tokens = self.count_tokens()

            # Continues to delete the chat from the top if
            # The current_tokens is still greater than max_tokens
            while (current_tokens) >= max_tokens - range:
                self.chathistory.pop(0 + delete_pos)
                self.chathistory.pop(1 + delete_pos)
                with open(f"{self.full_path}/chathistory.json", 'w') as f:
                    json.dump(self.chathistory, f, indent=2)
                print("***POPPED 2 MESSAGES***")
                current_tokens = self.count_tokens()




        def count_tokens(self):
            current_tokens = 0
            for content in self.chathistory:
                words_amnt = len(content['content'].split())
                current_tokens += words_amnt
            return current_tokens



        def checkForError(self, reply):
            """If An error happened with the API, return the Error"""
            try:
                if reply[0] == False:
                    false_return = reply[0]
                    error_message = reply[1]
                    return false_return, error_message
            except TypeError:
                return False




        def checkForPurgatory(self):
            """This puts the prompt template into the
            chathistory file instead of having it be empty."""
            spacezone = self.dbase.getSceneData("zone")
            if spacezone == "true":
                with open(f"{self.full_path}/chathistory.json", 'w') as f:
                    json.dump(self.chathistory, f, indent=2)


        def checkForBadFormat(self, response):
            """attempts to fix incorrectly formatted responses"""
            spacezone = self.dbase.getSceneData("zone")
            if spacezone == "true":
                if not response.startswith("[CONTENT]"):
                    return "[CONTENT] Hmm..."
                return response


            if "[SCENE]" not in response or "[FACE]" not in response or "[BODY]" not in response or "[CONTENT]" not in response:
                response = "[SCENE] clubroom [FACE] happy [BODY] relaxed [CONTENT] ... [END]"

            if "[BODY]" in response:
                body = response.split("[BODY]")[1].split("[CONTENT]")[0].strip()

                if body not in Configs().body_types(self.character_name):
                    response = response.replace(body, "relaxed")

            if "[FACE]" in response:
                face = response.split("[FACE]")[1].split("[BODY]")[0].strip()
                emotions = ', '.join([e for e in Configs().characters[self.character_name.title()]['head']])

                if face not in emotions:
                    random_face = random.choice([e for e in Configs().characters[self.character_name.title()]['head']])
                    response = response.replace(face, random_face)
            return response



        def modelChoices(self, prompt):
            return TextModel().getLLM(prompt=prompt)


        def ai_response(self, userInput):
            """Gets ai generated text based off given prompt"""

            reminder = ""
            spacezone = self.dbase.getSceneData("zone")

            renpy.log(f">>> ai response func: spacezone is {spacezone}")
            if spacezone != "true":
                emotions = ', '.join([e for e in Configs().characters[self.character_name.title()]['head']])
                parts =  Configs().body_types(self.character_name.title())
                reminder = "" if self.retrying == False else Info().getReminder["emotes"].replace("{{emotes}}", emotions).replace("{{body}}", parts).replace("{{char}}", self.character_name)

            self.checkForPurgatory()

            # Log user input
            self.chathistory.append({"role": "user", "content": userInput + reminder})

            # Make sure the user's msg doesn't go over the context window
            self.checkForContextLimit()
            examples = self.removePlaceholders()
            contextAndUserMsg = examples + self.chathistory if spacezone != "true" else self.chathistory

            response = self.modelChoices(contextAndUserMsg)
            response = ' '.join(response.split())   # Get rid of any extra spaces
            response = self.checkForBadFormat(response)

            
            # If An error happened with the API, return the Error
            check_error = self.checkForError(response)
            if check_error:
                return check_error[1]

            reply, _, face, body, scene = self.removeKeywords(response)


            # Log AI input
            response = self.safeResponse(response)
            response = response.split('[END]')[0] + " [END]"


            if response.startswith("[FACE]") and "[BODY]" not in response:
                response = Info().getReminder["generic_response"]

            self.chathistory.append({"role": "assistant", "content": response})

            self.controlMood(face, body)
            self.controlBackground(scene)

            with open(f"{self.full_path}/chathistory.json", 'w') as f:
                json.dump(self.chathistory, f, indent=2)
            return reply


