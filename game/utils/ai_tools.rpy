init python:
    from openai import OpenAI
    from utils.data import Configs, Misc
    import os
    import random
    import openai


    THIS_PATH = os.path.dirname(os.path.realpath(__file__))
    PATH = os.path.dirname(THIS_PATH)

    class AIGen:

        def __init__(self):
            self.config = Configs().config
            self.safety_settings = Configs().getModelDetails["safety_settings"]
            self.openai_client = OpenAI(api_key=self.config['GPT_TOKEN'])
            self.groq_client = ""




        def getGPT(self, prompt):
            try:
                response = await self.openai_client.chat.completions.create(
                    model="gpt-4-1106-preview", # gpt-4-1106-preview, gpt-4-turbo, gpt-4-turbo-2024-04-09, gpt-3.5-turbo-1106, gpt-3.5-turbo-16k
                    max_tokens=200,
                    temperature=0.6,
                    stop='[END]',
                    messages=prompt
                )

                # Remove everything after [END] but still append it to the end of the msg
                # This is so the AI still attempts to generate [END] for every msg.
                response = response.choices[0].message.content + " [END]"
                return response
            except openai.APIConnectionError as e:
                print("The server could not be reached")
                print(e.__cause__)  # an underlying Exception, likely raised within httpx.
                return False, "The server could not be reached"
            except openai.RateLimitError as e:
                print("A 429 status code was received; we should back off a bit.")
                return False, "A 429 status code was received; we should back off a bit."
            except openai.APIStatusError as e:
                print("Another non-200-range status code was received")
                print(e.status_code)
                print(e.response)
                return False, "Another non-200-range status code was received"





    async def getGroq(self, prompt, user_id):
        """Using Groq's API to quickly use large models"""
        try:

            with open(f'{PATH}/data/keys/{user_id}.key', "rb") as f:
                password = f.read()

            token = await ec().decrypt_password(password)
            groq_client = Groq(api_key=token)

            response = groq_client.chat.completions.create(
                model="llama3-70b-8192", # mixtral-8x7b-32768, llama2-70b-4096, gemma-7b-it, llama3-70b-8192
                max_tokens=200,
                temperature=0.6,
                stop=['[INST', '[/INST', '[END]'],
                messages=prompt
            )

            # Remove everything after [END] but still append it to the end of the msg
            # This is so the AI still attempts to generate [END] for every msg.
            response = response.choices[0].message.content + " [END]"
            return response
        except GroqError as e:
            if e.response.status_code == 429:
                return False, "Rate limit exceeded."
            else:
                return False, f"An error occurred: {e}"

