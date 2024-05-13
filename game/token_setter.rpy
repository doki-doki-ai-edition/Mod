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


            if not TOKEN.get('GPT'):
                TOKEN['GPT'] = persistent.chatToken
            if not TOKEN.get('GROQ'):
                TOKEN['GROQ'] = persistent.chatToken
            if not TOKEN.get('GETIMG'):
                TOKEN['getimgToken'] = persistent.imgToken
            if not TOKEN.get('stableImgToken'):
                TOKEN['STABLEIMG'] = persistent.imgToken

            with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json", 'w') as f:
                json.dump(TOKEN, f)
