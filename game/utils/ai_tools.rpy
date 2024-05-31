init python:
    import os
    import random
    import requests


    class TextModel:

        def __init__(self):
            self.tokens = Configs().config


        def getGPT(self, prompt):
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.tokens['GPT']}"
            }
            payload = {
                "model": persistent.chatModel, # gpt-4-1106-preview, gpt-4-turbo, gpt-4-turbo-2024-04-09, gpt-3.5-turbo-1106, gpt-3.5-turbo-16k
                "max_tokens": 200,
                "temperature": float(f".{persistent.temp}"),
                "stop": "[END]",
                "messages": prompt
            }

            try:
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"] + " [END]"

            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                return False, f"<Error> {e}"




        def getGroq(self, prompt):
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.tokens['GROQ']}"
            }
            payload = {
                "model": persistent.chatModel, # llama3-70b-8192, llama3-8b-8192, mixtral-8x7b-32768
                "max_tokens": 200,
                "temperature": float(f".{persistent.temp}"),
                "stop": "[END]",
                "messages": prompt
            }

            try:
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"] + " [END]"

            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                return False, f"<Error> {e}"




        def getLLM(self, prompt):
            if persistent.seed == "random":
                options = {
                    "options": {
                        "temperature": float(f".{persistent.temp}"),
                        "stop": ['[INST', '[/INST', '[END]'],
                        "num_ctx": int(persistent.context_window)
                        }
                }
            else:
                options = {
                    "options": {
                        "temperature": float(f".{persistent.temp}"),
                        "stop": ['[INST', '[/INST', '[END]'],
                        "num_ctx": int(persistent.context_window),
                        "seed": persistent.seed
                        }
                }

            response = requests.post(
                "http://localhost:11434/v1/chat/completions",
                json={"model": persistent.chatModel, "messages": prompt, "stream": False,
                    "options": options["options"]},
            )

            try:
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"] + " [END]"

            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                return False, f"<Error> {e}"






    # Will be unusable in the mod, just a placeholder
    class ImageModel:


        def getimgai(self, guide):
            url = "https://api.getimg.ai/v1/stable-diffusion/text-to-image"
            with open(f"{config.basedir}/game/assets/prompts/img_generation.json") as f:
                scene = json.load(f)

            with open(config.basedir + "/PRIVATE_TOKENS_DO_NOT_SHARE.json") as f:
                TOKEN = json.load(f)

            payload = {
                "model": "dark-sushi-mix-v2-25",
                "prompt":  scene["getimg"]["prompt"].replace("<guide>", guide),
                "negative_prompt": scene["stable"]["negative"],
                "width": 1024,
                "height": 1024,
                "steps": 30,
                "guidance": 9,
                "output_format": "png"
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {TOKEN['getimgToken']}"
            }

            r = requests.post(url, json=payload, headers=headers).json()
            guide = guide + ".png"
            if "error" not in r:
                with open(f"{config.basedir}/game/images/bg_temp/{guide}", "wb") as f:
                    f.write(base64.b64decode(r["image"]))
                    self.update_in_saved_actions("Scene", guide)
                    self.scene = guide
                    self.ai_art_mode = True
            else:
                self.ai_art_mode = False





        def stableimg(self, guide):
            url = "https://stablediffusionapi.com/api/v3/text2img"
            with open(f"{config.basedir}/game/assets/prompts/img_generation.json") as f:
                scene = json.load(f)

            payload = json.dumps({
            "key": stable_token,
            "prompt": scene["stable"]["prompt"].replace("<guide>", guide),
            "negative_prompt": scene["stable"]["negative"],
            "width": "1024",
            "height": "1024",
            "samples": "1",
            "num_inference_steps": "31",
            "seed": None,
            "guidance_scale": 9,
            "safety_checker": "yes",
            "multi_lingual": "no",
            "panorama": "no",
            "self_attention": "no",
            "upscale": "no",
            "model_id": "midjourney",
            "scheduler": "DDPMScheduler",
            "vae": "sd-ft-mse",
            "lora": "more_details",
            "webhook": None,
            "track_id": None
            })

            headers = {
            'Content-Type': 'application/json'
            }

            guide = guide + ".png"
            response = requests.request("POST", url, headers=headers, data=payload, timeout=25)
            if response.status_code == 201 or response.status_code == 200:
                response_data = json.loads(response.text)
                with open(config.basedir + f"/game/images/bg/ai_imgs.json", "w") as f:
                    json.dump(response_data, f, indent=2)
                with open(config.basedir + f"/game/images/bg/ai_imgs.json", "r") as f:
                    ai_art = json.load(f)

                # Wait for "output" key to be returned by the API.
                # Would do this asynchronously but i've failed to do so atm.
                try: url = ai_art["output"][0]
                except (IndexError, KeyError):
                    time.sleep(25)
                    try: url = ai_art["output"][0]
                    except (IndexError, KeyError): return guide
                response = requests.get(url)

                with open(config.basedir + f"/game/images/bg/{guide}", "wb") as f:
                    f.write(response.content)

                self.update_in_saved_actions("scene", guide)
                self.scene = guide
                self.ai_art_mode = True
            else:
                self.ai_art_mode = False

            return guide

        def generate_ai_background(self, guide):
            """Generates unique AI background if it doesn't already exist in the bg folder"""
            ai_art_path = config.basedir + "/game/images/bg/"+ guide + ".png"
            if os.path.exists(ai_art_path):
                guide = guide + ".png"
                self.update_in_saved_actions("scene", guide)
                self.scene = guide
                self.ai_art_mode = True
                return self.scene

            # if persistent.imgModel == "1":
            #     return self.getimgai(guide)
            # elif persistent.imgModel == "2":
            #     return self.stableimg(guide)

            if os.path.exists(config.basedir + "/getimg.txt"):
                return self.getimgai(guide)
            elif os.path.exists(config.basedir + "/stable.txt"):
                return self.stableimg(guide)


