init python:
    class tokenSetter:

        def set_token():
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

            openai.api_key = TOKEN['gptToken']
            getimgToken = TOKEN['getimgToken']
            stable_token = TOKEN['stableImgToken']
            #vocal_token = cs_config['VOCAL_TOKEN']

        def set_token_persist():
            # openai.api_key = persistent.chatToken
            # getimgToken = persistent.imgToken
            # stable_token = persistent.imgToken

            with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json") as f:
                TOKEN = json.load(f)

            openai.api_key = TOKEN['gptToken']
            getimgToken = TOKEN['getimgToken']
            stable_token = TOKEN['stableImgToken']