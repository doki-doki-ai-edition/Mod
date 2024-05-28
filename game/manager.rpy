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

    retrycount = 3

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

        @staticmethod
        def context_to_progress_story(msg):
            rng = random.randint(1,3)
            context = ""

            with open(f"{config.basedir}/game/assets/prompts/progress_story.json") as f:
                structs = json.load(f)
            if rng == 1:
                context += structs["1"]
            elif rng == 2:
                context += structs["2"]
            elif rng == 3:
                context += structs["3"]

            return msg + context



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

            if self.character_name == "monika" and face == "nonchalant":
                Configs().create_from_hex(f"{config.basedir}/game/images/monika/nonchalant.chr", f"{config.basedir}/game/images/monika/nonchalant.png")
            else:
                Configs().delete_egg(f"{config.basedir}/game/images/monika/nonchalant.png")

            for h in head_sprite:
                if h == face.lower():
                    self.dbase.updateSceneData("head_sprite", head_sprite[h])

                    if h in full_sprite_emotions:
                        self.dbase.updateSceneData("left_sprite", char_name["none"])
                        self.dbase.updateSceneData("right_sprite", char_name["none"])
                        return

            if head_sprite in full_sprite_emotions:
                self.dbase.updateSceneData("left_sprite", char_name["none"])
                self.dbase.updateSceneData("right_sprite", char_name["none"])
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

            char = getContent('[CHAR]', '[CONTENT]')
            face = getContent('[FACE]', '[BODY]')
            body = getContent('[BODY]', '[CONTENT]')
            scene = getContent('[SCENE]', '[NARRATION]')

            reply = reply.replace('[END]', '')
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
            elif "[NARRATION]" in reply:
                reply = reply.split("[NARRATION]")[1].strip()
            else:
                # Typically this means that the model didnt return a proper content field
                reply = "ERROR"

            return reply, char, face, body, scene



        def removePlaceholders(self):
            """remove placeholders in json files"""
            level_normal = Info().getExamplePrompts[f"level2_{self.character_name}"]
            level_zone = Info().getExamplePrompts[f"level2_{self.character_name}_zone"]
            spacezone = self.dbase.getSceneData("zone")

            renpy.log(f">>> rmvPlace func: spacezone is {spacezone}")
            renpy.log(f">>> rmvPlace func (PERSISTENT): spacezone is {spacezone}")
            raw_examples = level_normal if spacezone != True else  level_zone

            if spacezone != "true":
                bg_scenes = [s for s in Configs().bg_scenes["default"]] + [s for s in Configs().bg_scenes["checks"]]
                emotions = ', '.join([e for e in Configs().characters[self.character_name.title()]['head']])
                backgrounds = ', '.join(bg_scenes)

                string = raw_examples[0]['content'].replace("<name>", persistent.playername)
                string = string.replace("<char>", self.character_name)
                string = string.replace("<emotions>", emotions)
                string = string.replace("<backgrounds>", backgrounds)

                string = raw_examples[0]['content'] = string
                raw_examples[0]['content'] = string

            return raw_examples




        def retryPrompt(self, reply, current_emotion, current_body):
            """If the generated response doesnt use the emotions specified in the characters.json list
            eg. '[FACE] super shy' then remind the ai to only use what's in
            the list and redo the response
            """
            if current_emotion and current_body:
                if (reply.startswith("[FACE]")) and (current_emotion not in Configs().characters[self.character_name.title()]["head"]) or ("explain" not in current_body and "relaxed" not in current_body):
                    print("<<retrying>>")
                    return True
            return False



        def checkForError(self, reply):
            """If An error happened with the API, return the Error"""
            try:
                if reply[0] == False:
                    false_return = reply[0]
                    error_message = reply[1]
                    return false_return, error_message
            except TypeError:
                return False

        def checkForRepeat(self):
            """Checks if {RST} is sent more than once and falls back on a
            default prompt"""
            spacezone = self.dbase.getSceneData("zone")
            if  spacezone != "true":
                if len(self.chathistory) >=4 and len(self.chathistory) <= 8:
                    amnt = 0
                    for rst in self.chathistory:
                        if "{RST}" in rst['content']:
                            amnt += 1

                    if amnt >= 2:
                        self.chathistory = Info().getReminder['backup_prompt']



        def modelChoices(self, prompt):
            groq = chat_model_dict["groq"]["suggested"] + chat_model_dict["groq"]["other"]
            openai = chat_model_dict["openai"]["suggested"] + chat_model_dict["openai"]["other"]

            if persistent.chatModel in groq:
                return TextModel().getGroq(prompt=prompt)
            elif persistent.chatModel in openai:
                return TextModel().getGPT(prompt=prompt)
            else:
                return TextModel().getLLM(prompt=prompt)


        def ai_response(self, userInput):
            """Gets ai generated text based off given prompt"""

            reminder = ""
            spacezone = self.dbase.getSceneData("zone")

            renpy.log(f">>> ai response func: spacezone is {spacezone}")
            if spacezone != "true":
                emotions = ', '.join([e for e in Configs().characters[self.character_name.title()]['head']])
                parts = ', '.join([e for e in Configs().characters[self.character_name.title()]['left']]) # "explain" and "relaxed" (which honestly should prob just use a number system)
                reminder = "" if self.retrying == False else Info().getReminder["emotes"].replace("<emotes>", emotions).replace("<body>", parts).replace("<char>", self.character_name)



            # Log user input
            self.chathistory.append({"role": "user", "content": userInput + reminder})

            examples = self.removePlaceholders()
            contextAndUserMsg = examples + self.chathistory if spacezone != "true" else self.chathistory
            response = self.modelChoices(contextAndUserMsg) if userInput.lower() != Info().getReminder["nc"] else "[FACE] playful smile [BODY] relaxed [CONTENT] Nice rooster bro."


            # If An error happened with the API, return the Error
            check_error = self.checkForError(response)
            if check_error:
                return check_error[1]


            reply, _, face, body, scene = self.removeKeywords(response)


            # If the AI responds w/ an emotion/body not listed, redo the response
            if spacezone != "true":
                global retrycount
                self.retrying = self.retryPrompt(response, face, body)
                if self.retrying:
                    retrycount -= 1
                    if retrycount <= 0:
                        self.retrying = False
                        retrycount = 3
                    else:
                        self.chathistory.pop()
                        return self.ai_response(userInput)


            # Log AI input
            response = self.safeResponse(response)
            self.chathistory.append({"role": "assistant", "content": response})

            self.controlMood(face, body)
            self.controlBackground(scene)

            #self.checkForRepeat()

            with open(f"{self.full_path}/chathistory.json", 'w') as f:
                json.dump(self.chathistory, f, indent=2)
            return reply


