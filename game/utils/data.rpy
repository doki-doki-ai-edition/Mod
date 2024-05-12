init python:
    import os
    import json


    class Data:

        def __init__(self, path_to_user_dir):
            self.path_to_user_dir = path_to_user_dir

        @property
        def getMetadata(self):
            with open(self.path_to_user_dir + "/metadata.json", 'r') as f:
                return json.load(f)

        @property
        def getLastMessage(self):
            with open(self.path_to_user_dir + "/chathistory.json", 'r') as f:
                return json.load(f)[-1]["content"]

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
        def getModelDetails(self):
            with open(f'{config.basedir}/game/assets/configs/model_details.json', 'r') as f:
                modelDetails = json.load(f)
            return modelDetails

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
