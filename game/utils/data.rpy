init python:
    import os
    import json

    THIS_PATH = os.path.dirname(os.path.realpath(__file__))
    PATH = os.path.dirname(THIS_PATH)

    class Data:

        def __init__(self, path_to_user_dir, id):
            self.path_to_user_dir = path_to_user_dir
            self.id = id

        @property
        async def getFullScene(self):
            with open(self.path_to_user_dir + f"/scenedata_{self.id}.png", 'rb') as f:
                return f.read()


        @property
        async def getMetadata(self):
            with open(self.path_to_user_dir + f"/metadata.json", 'r') as f:
                return json.load(f)


        async def updateFullScene(self, value):
            with open(self.path_to_user_dir + f"/scenedata_{self.id}.png", 'wb') as f:
                f.write(value)


        async def updateSceneData(self, key, value):
            with open(self.path_to_user_dir + f"/scenedata_{self.id}.json", 'r') as f:
                scenedata = json.load(f)

            scenedata[key] = value

            with open(self.path_to_user_dir + f"/scenedata_{self.id}.json", 'w') as f:
                json.dump(scenedata, f, indent=2)
            return value


        async def getSceneData(self, key):
            try:
                with open(self.path_to_user_dir + f"/scenedata_{self.id}.json", 'r') as f:
                    return json.load(f)[key]
            except TypeError:
                return None




    class Configs:

        @property
        def config(self):
            with open(f'{config.basedir}/config.json', 'r') as f:
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
        def thread_info(self):
            with open(config.basedir + "/assets/info/thread_info.json", "r") as f:
                info = json.load(f)
            return info[0]

        @property
        def getDokis(self):
            with open(config.basedir + "/assets/info/dokis.json", "r") as f:
                dokis = json.load(f)
            return dokis
        
        @property
        async def getHelpInfo(self):
            with open(config.basedir +'/assets/info/cmds.json', 'r') as f:
                desc = json.load(f)
            return desc
        
        @property
        def getExamplePrompts(self):
            with open(config.basedir + "/assets/prompts/prompt_template.json", "r") as f:
                example = json.load(f)
            return example
        
        @property
        def getReminder(self):
            with open(config.basedir + "/assets/info/reminder.json", "r") as f:
                reminder = json.load(f)
            return reminder
        




    class Misc:
        
        @property
        async def getDummyText(self):
            with open(f'{config.basedir}/game/assets/misc/dummy_msgs.json') as f:
                misc = json.load(f)
            return misc