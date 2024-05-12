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


            if not TOKEN.get('gptToken'):
                TOKEN['gptToken'] = persistent.chatToken
            if not TOKEN.get('getimgToken'):
                TOKEN['getimgToken'] = persistent.imgToken
            if not TOKEN.get('stableImgToken'):
                TOKEN['stableImgToken'] = persistent.imgToken

            with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json", 'w') as f:
                json.dump(TOKEN, f)
