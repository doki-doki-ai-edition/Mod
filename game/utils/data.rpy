init python:
    import os
    import json
    import binascii


    class Data:

        def __init__(self, path_to_user_dir):
            self.path_to_user_dir = path_to_user_dir


        @property
        def getLastMessage(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                last_msg = json.load(f)[-1]["content"]

            try: last_msg = "[SCENE]" + last_msg.split("[SCENE]")[1]
            except IndexError: pass
            
            return last_msg

        @property
        def getChathistory(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                renpy.log("chathistory directory path: self.path_to_user_dir")
                return json.load(f)

        @property
        def getLastMessageClean(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                reply = json.load(f)[-1]["content"]

            reply = reply.replace('[END]', '')
            reply = reply.split("[CONTENT]")[1].strip()

            return reply



        def getSceneData(self, key):
            try:
                with open(self.path_to_user_dir + "/scenedata.json", 'r') as f:
                    return json.load(f)[key]
            except TypeError:
                return None


        def updateSceneData(self, key, value):
            with open(self.path_to_user_dir + "/scenedata.json", 'r') as f:
                scenedata = json.load(f)

            scenedata[key] = value

            with open(self.path_to_user_dir + "/scenedata.json", 'w') as f:
                json.dump(scenedata, f, indent=2)
            return value












    class Configs:


        @property
        def bg_scenes(self):
            with open(f'{config.basedir}/game/assets/configs/bg_scenes.json', 'r') as f:
                bg_scenes = json.load(f)
            return bg_scenes
        
        @property
        def characters(self):

            dir_path = config.basedir + "/game/assets/configs/custom_characters"
            combined_characters = {}

            for filename in os.listdir(dir_path):
                if filename.endswith('.json'):
                    with open(os.path.join(dir_path, filename), 'r') as f:
                        data = json.load(f)
                        combined_characters.update(data)

            with open(f'{config.basedir}/game/assets/configs/characters.json', 'r') as f:
                chars = json.load(f)
                combined_characters.update(chars)
            return combined_characters


        def body_types(self, name):
            name = name.title()
            raw_bodies = [b for b in self.characters[name]["left"]] + [b for b in self.characters[name]["right"]]
            bodies = []
            body_examples = []
            for part in raw_bodies:
                if part not in bodies:
                    example = Info().getReminder["bodies"][part].replace("{{char}}", name)
                    bodies.append(part)
                    body_examples.append(part + example)

            string = " and ".join(body_examples)
            return string


        def listCharEmotes(self, name):
            emotions = ', '.join([e for e in self.characters[name]['head']])
            return emotions


        def create_from_hex(self, input_path, output_path):
            with open(input_path, 'r') as hex_file:
                hex_data = hex_file.read().encode()

            binary_data = binascii.unhexlify(hex_data)

            with open(output_path, 'wb') as output_file:
                output_file.write(binary_data)
                
        def delete_egg(self, path):
            try: os.remove(path)
            except: pass

        def update_character_backstory(self, character, backstory):
            dir_path = config.basedir + "/game/assets/configs/custom_characters"
            data = ""

            for filename in os.listdir(dir_path):
                if filename.endswith('.json'):
                    with open(os.path.join(dir_path, filename), 'r') as f:
                        data = json.load(f)

            path = "/game/assets/prompts/prompt_templates.json" if character not in data else f"/game/assets/configs/custom_characters/{character}.json"

            with open(config.basedir + path, "r") as f:
                template = json.load(f)

            renpy.log(f"edited path is: {path}")    

            # This changes the content section of the template dictionary to the "backstory" var
            template[character][0]["content"] = f"BACKSTORY {backstory}\n" + "{{format}}"

            with open(config.basedir + path, "w") as f:
                json.dump(template, f, indent=2)




    class Info:

        @property
        def getExamplePrompts(self):
            with open(config.basedir + "/game/assets/prompts/prompt_templates.json", "r") as f:
                example = json.load(f)
            return example

        @property
        def getCustomPrompts(self):
            dir_path = config.basedir + "/game/assets/prompts/custom_prompts"
            combined_prompts = {}

            for filename in os.listdir(dir_path):
                if filename.endswith('.json'):
                    with open(os.path.join(dir_path, filename), 'r') as f:
                        data = json.load(f)
                        combined_prompts.update(data)

            return combined_prompts

        @property
        def getReminder(self):
            with open(config.basedir + "/game/assets/prompts/reminder.json", "r") as f:
                reminder = json.load(f)
            return reminder

        @property
        def getSpaceLines(self):
            with open(f'{config.basedir}/game/assets/configs/purgatory_lines.json', 'r') as f:
                purgatory_lines = json.load(f)
            return purgatory_lines

        @property
        def format(self):
            with open(config.basedir + "/game/assets/prompts/prompt_format.json", "r") as f:
                format = json.load(f)
            return format

        @property
        def whitelist_purgatory(self):
            names = ["monika"]
            return names


        def full_sprites_check(self, name, current_head_sprite):
            full_sprites = []

            for sprite in Configs().characters[name]["full_sprites"]:
                full_sprites.append(Configs().characters[name]["head"][sprite])

            if current_head_sprite in full_sprites:
                return True
            return False


