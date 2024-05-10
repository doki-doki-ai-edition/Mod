init python:
    import os
    import random



    THIS_PATH = os.path.dirname(os.path.realpath(__file__))
    PATH = os.path.dirname(THIS_PATH)

    class AIGen:

        def __init__(self):
            self.config = ""
            self.openai_client = ""
            self.groq_client = ""




        def getGPT(self, prompt):
            pass





        def getGroq(self, prompt, user_id):
            """Using Groq's API to quickly use large models"""
            pass

