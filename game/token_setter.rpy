init python:
    class tokenSetter:

        def set_token():
            TOKEN = {}
            try:
                with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json") as f:
                    TOKEN = json.load(f)
            except FileNotFoundError:
                with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json", 'w') as f:
                    json.dump({}, f)


            TOKEN['GROQ'] = persistent.chatToken

            with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json", 'w') as f:
                json.dump(TOKEN, f)
