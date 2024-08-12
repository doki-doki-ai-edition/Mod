init python:
    import os
    import random
    import requests
    import ollama
    import httpx


    class TextModel:


        def getLLM(self, prompt):
            seed = random.random() if persistent.seed == "random" else persistent.seed 

            options = ollama.Options(temperature=float(f".{persistent.temp}"), stop=["[INST", "[/INST", "[END]"],
            num_ctx=int(persistent.context_window), seed=seed, num_predict=200)

            try:
                response = ollama.chat(model=persistent.chatModel, messages=prompt, options=options)
                result = response['message']['content']

                renpy.log(f"RAW RESPONSE: {result}")

                if "[END]" not in result:
                    return result.strip() + " [END]"
                return result.strip()

            except httpx.ConnectError:
                return False, "<|Error|> You don't have ollama running."
            except ollama.ResponseError as e:
                if e.status_code == 404:
                    return False, f"<|Error|> You dont have the model \"{persistent.chatModel}\" installed! Go to settings and install this model (if it exists)."
                return False, f"<|Error|> {e.error}"






