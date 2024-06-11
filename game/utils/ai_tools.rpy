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






