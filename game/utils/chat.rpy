init python:
    import asyncio
    import json
    import random
    import os
    import io


    class SetupChat:
        def __init__(self, chat_name, character_name):
            self.chat_name = chat_name
            self.character_name = character_name
            self.path_to_user_dir = f"{config.basedir}/chats/"
            self.aiManager = AIManager(
                character_name=self.character_name,
                path_to_user_dir=self.path_to_user_dir
                )
            self.tools = Tools(self.path_to_user_dir)
            self.scenedata_default = {
                                "gamemode": "none",
                                "music": "none"
                                "background": "",
                                "character": "",
                                "head_sprite": "",
                                "left_sprite": "",
                                "right_sprite": "",
                                "zone": ""
                            }

            with open(f"{config.basedir}/game/assets/prompts/prompt_templates.json") as f:
                self.prompt_template = json.load(f)




        def setup(self):
            chat_history = []

            # If the "chats" folder doesn't exist, create it.
            if not os.path.exists(self.path_to_user_dir):
                os.makedirs(self.path_to_user_dir, mode=0o777)

            userInput = "{RST}"

            self.tools.createRealm(name_of_realm=chat_name)
            chat_history = Tools(path_to_user_dir=f"{config.basedir}/chats/").checkFile(chat_history)
            return self.chat(userInput=userInput, chat_history=chat_history)


        def chat(self, chat_history, userInput):
            state, msg = AIManager(
                character_name=self.character_name,
                path_to_user_dir=self.path_to_user_dir,
                chat_history=chat_history
                ).ai_response(userInput)

            if state == False:
                return "**`ERROR:`** {msg}"

            return msg



    class Tools:
        def __init__(self, path_to_user_dir):
            self.path_to_user_dir = path_to_user_dir


        def checkFile(self, chat_history):
            try:
                with open(self.path_to_user_dir + f"/chathistory.json", 'r') as f:
                    chat_history = json.load(f)
                    return chat_history
            except FileNotFoundError:
                with open(self.path_to_user_dir + f"/chathistory.json", 'w') as f:
                    json.dump([], f, indent=2)
            return chat_history




        def createRealm(self, name_of_realm):
            """Creates specific folder in `chats` to store all
            realms.
            """

            path = self.path_to_user_dir + name_of_realm
            full_path = ""

            i = 1
            while True:
                full_path = f"{path}_{i}"
                if not os.path.exists(full_path):
                    os.makedirs(full_path, mode=0o777)
                    break
                else:
                    i += 1


            with open(full_path + "/scenedata.json", 'w') as f:
                json.dump(self.scenedata_default, f, indent=2)



            # Metadata for chats
            metadata_default = {
                "chats": []
            }
            metadata_path = f"{config.basedir}/chats/metadata.json"
            if not os.path.exists(metadata_path):
                with open(metadata_path, 'w') as f:
                    json.dump(self.metadata_default, f, indent=2)

            with open(metadata_path, 'r') as f:
                metadata = json.load(f)

            metadata["chats"].append(
                {
                    "name": self.chat_name,
                    "note": "-",
                    "character": "",
                    "gamemode": "none"
                }
            )

            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
