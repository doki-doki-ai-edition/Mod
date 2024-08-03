init python:
    import os
    import random
    import requests


    class TextModel:


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
                result = data["choices"][0]["message"]["content"]

                renpy.log(f"RAW RESPONSE: {result}")

                if "[END]" not in result:
                    return result.strip() + " [END]"
                return  result.strip()

            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                return False, f"<Error> {e}"






