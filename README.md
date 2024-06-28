
Doki Doki AI Edition (DDAE) is a DDLC mod that implements a more interactive form of roleplay by using sprites to spice up the AI generated text.
The sprites used are decided by the AI based on how you interact with it.

If you have extra questions or want to become apart of the community you can join the discord server here: https://discord.gg/rDA7ehBSq7

If you've been **banned** from the server you can appeal here: https://forms.gle/E8wyDi9aBzXdWvf99


# Setup

- Make sure you have a fresh install of DDLC https://ddlc.moe/
- Download the latest version of the DDAE mod on this github page https://github.com/doki-doki-ai-edition/Mod/releases

To setup the mod just drag the contents into the main ddlc folder:


<video controls>
  <source src="game/assets/imgs/help_page/ddae setup.mp4" type="video/mp4" />
</video>



**IMPORTANT NOTE:** You only need to read the Ollama section to set everything up. Everything else is just extra info.

## Ollama

**Overview:** Ollama is an open-source project that allows people to setup local language models on their machine in a far more user friendly way. They have both uncensored and censored models and the models are quantized (compressed) to run on low-end devices.

**Pros**
- Run models locally on your machine
- Easy to setup
- Privacy: Even if your internet is off, it'll still work
- Uncensored: Freedom to say whatever


**Cons**
- Very Slow (depending on your hardware)
- Quality isn't that great especially compared to what some APIs offer


**Let's Start!**
- Go to https://ollama.com/download
- Select the Operating system you're using (For example Windows)
- Click on Download

Once it's downloaded, run the application.

If you're on windows you should see a small icon in your taskbar that looks like this

<img src="game/assets/imgs/help_page/llama_task.png">

- Open up a terminal on your device (eg. cmd+r if you're using windows, then type "cmd" and press enter)
- In the terminal type "ollama run llama3" (or any model you find in https://ollama.com/library/)

This should be roughly 4.7 gigabytes and once it's done installing you can run the mod!


# Settings

## AI Type

**LLM (Local Language Model)** <br>
Shows the default local models available in the "Model Name" section.

## Model Name

**Suggested Models**
Models that have been tested to work properly in accordance to the default prompt given

**Other Models**
Models that aren't as high quality and haven't been frequently tested


## Model Config

**Context Window**
The maximum amount of tokens (messages) that will be remembered. The few-shot prompts for monika's default prompt already takes up 1,066 tokens (which is over the default limit)

Note that the more context you give it, the slower responses may be and the more memory you use on your device.

Make sure to check the context window of a model. For example:

Go to https://ollama.com/library/llama3:8b

<img src="game/assets/imgs/help_page/model_show.png" alt="model display">

Click on "model" (and wait since it may take a while to load)

Look for context_length

<img src="game/assets/imgs/help_page/model_context_len.png" alt="model context window">

If you want to use more than a 8192 token limit then you can check out other models such as

https://ollama.com/library/llama3-gradient

which has a 1M context window. You won't be able to use the full 1M tokens because of the hardware requirement for something like that but depending on your hardware you could use a lot more than 8k.

---
**Temperature**
Determines how random/creative the output is.

Higher = More random and creative but if it's too high, the responses can be nonsensical and may not even follow the system prompt appropriately.

Lower = Less random and predictable. The model chooses the most likely word to respond with but ends up sounding more robotic.

The typical default temperature is "1" but I've personally found 0.6 to be a good sweet spot, just high enough to be creative but low enough to give good responses.


*NOTE:* It is highly advisable to leave the temperature on the default settings because it has been shown to follow the prompt far more accurately when testing compared to other numbers.

---
**Seed**
Deterministic responses. If set to a specific seed, your outputs will be pretty much exactly the same or relatively similar if you feed it the same input.

Eg. If you have a seed of 22 and your input response goes like this:

user: "how are you monika?" <br>
monika: "I'm not doing too well to be honest..."

Assuming the system prompt is the same and your response is formatted in the exact same way, you'll always get that same output (or something very similar).



# Frequently Asked Questions

## Are my chats private?

Yes. Your chats are completely localized on your machine, even if you turn your internet off, it'll still work.


## Are the models uncensored

It depends on what model you're using. You can go to https://ollama.com/library to find uncensored models but they may not follow the system prompt as well which would cause the game to not function correctly.

Secondly, they may not be entirely uncensored. There are certain questions that it may refuse, but since it's a local model you can attempt to jailbreak it as much as you want.


## Can I trust Ollama?

As much as you trust all the other apps you use daily.
Jeffrey Morgan is one of the founders and he has a credible background by previously working for docker, twitter and google.

The project is also used by google in firebase https://firebase.google.com/docs/genkit/plugins/ollama

And obviously, the project is open-sourced.


## Why do the models sometime return "ERROR"?

This happens when the model doesn't respond with the instructed format. This typically happens on regular models if you say something too provacative. 

There's a few solutions to this.

The first is to use an uncensored model. 

The second thing you could try is continuing the chat by ignoring the error message and try to force the ai back into a roleplay state

And the 3rd thing you could try is just jailbreaking the ai model by editing the
system prompt to make the ai say anything.


## Why does the game freeze?

This means that the ai is generating the output. You should wait for it to be done.


## What hardware do I need?

You should be able to run the mod on low-end devices like a laptop with 4GB of RAM
and 4GB of VRAM but the speed at which you get a response is going to be slow.

If you want faster responses you need more VRAM. Regular RAM allows you to run models.


# Credits

**Developer:**
[Zeeblo](https://github.com/zeeblo)

**Logo Design:**
[Infernog](https://x.com/Infernog05) (& another user who wishes to stay anonymous)

**Voice Acting:**
[Jayce Parisi](https://jayceparisi.com/)