init python:
    import os
    import json
    import binascii
    import os

    class Data:

        def __init__(self, path_to_user_dir):
            self.path_to_user_dir = path_to_user_dir


        @property
        def getLastMessage(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                return json.load(f)[-1]["content"]

        @property
        def getChathistory(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                return json.load(f)

        @property
        def getLastMessageClean(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                reply = json.load(f)[-1]["content"]

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

            if "[CONTENT]" in reply:
                reply = reply.split("[CONTENT]")[1].strip()
            elif "[NARRATION]" in reply:
                reply = reply.split("[NARRATION]")[1].strip()
            else:
                # Typically this means that the model didnt return a proper content field
                reply = "ERROR"

            return reply

        def updateSceneData(self, key, value):
            with open(self.path_to_user_dir + "/scenedata.json", 'r') as f:
                scenedata = json.load(f)

            scenedata[key] = value

            with open(self.path_to_user_dir + "/scenedata.json", 'w') as f:
                json.dump(scenedata, f, indent=2)
            return value


        def getSceneData(self, key):
            try:
                with open(self.path_to_user_dir + "/scenedata.json", 'r') as f:
                    return json.load(f)[key]
            except TypeError:
                return None










    class Configs:

        @property
        def config(self):
            with open(f'{config.basedir}/PRIVATE_TOKENS_DO_NOT_SHARE.json', 'r') as f:
                _config = json.load(f)
            return _config

        @property
        def bg_scenes(self):
            with open(f'{config.basedir}/game/assets/configs/bg_scenes.json', 'r') as f:
                bg_scenes = json.load(f)
            return bg_scenes

        @property
        def characters(self):
            with open(f'{config.basedir}/game/assets/configs/characters.json', 'r') as f:
                chars = json.load(f)
            return chars


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




    class Info:

        @property
        def getExamplePrompts(self):
            with open(config.basedir + "/game/assets/prompts/prompt_templates.json", "r") as f:
                example = json.load(f)
            return example

        @property
        def getReminder(self):
            with open(config.basedir + "/game/assets/prompts/reminder.json", "r") as f:
                reminder = json.load(f)
            return reminder

        @property
        def getMaleChicken(self):
            return "cock"

        @property
        def getSpaceLines(self):
            space_lines = {
                1: {
                    "name": "making-friends",
                    "file": "<from 0 to 74>audio/sfx/_space-lines.mp3",
                    "time": 76
                },
                2: {
                    "name": "same-room",
                    "file": "<from 102 to 128>audio/sfx/_space-lines.mp3",
                    "time": 26
                },
                3: {
                    "name": "favorite-color",
                    "file": "<from 150 to 174>audio/sfx/_space-lines.mp3",
                    "time": 24
                },
                4: {
                    "name": "sayori-(graphic)",
                    "file": "<from 219 to 318>audio/sfx/_space-lines.mp3",
                    "time": 99
                },
                5: {
                    "name": "festival",
                    "file": "<from 363 to 398>audio/sfx/_space-lines.mp3",
                    "time": 35
                },
                6: {
                    "name": "japan",
                    "file": "<from 439 to 498>audio/sfx/_space-lines.mp3",
                    "time": 59
                }
            }
            return space_lines
