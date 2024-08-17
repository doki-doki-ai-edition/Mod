label apikey_label:
    $ apikey = renpy.input("Enter API Key", f"{persistent.chatToken}").strip()
    $ persistent.chatToken = apikey
    $ renpy.save_persistent()
    return


label custom_chat_model_label:
    "Enter a model from your ollama list"
    "You can check what models you have available by typing \"ollama list\" in a command line on your device."
    $ model = renpy.input("Enter a model", f"{persistent.chatModel}").strip()
    $ persistent.chatModel = model 
    $ renpy.save_persistent()
    return



label custom_backstory_label:
    "Enter your own backstory for this character. You can also navigate to \"game/assets/prompts/prompt_templates.json\" and edit the \"content\" section manually."
    if character_name in Info().getExamplePrompts:
        $ raw_prompt = Info().getExamplePrompts[character_name][0]["content"].split("{{format}}")[0].replace("BACKSTORY", "")
    else:
        $ raw_prompt = Info().getCustomPrompts[character_name][0]["content"].split("{{format}}")[0].replace("BACKSTORY", "")

    $ player_prompt = renpy.input(prompt=" ", default=f"{raw_prompt}", exclude="}{", screen="input_long").strip()
    
    $ Configs().update_character_backstory(character=character_name, backstory=player_prompt)
    "Successfully changed backstory!"
    return




label setup_model_label:
    menu:
        "Would you like a tutorial on how to download a model? Or simply download a model now?"

        "Tutorial":
            jump tutorial_label

        "Download Model":
            jump download_model_label



label tutorial_label:
    call screen tutorial_screen
    return





init python:
    from tqdm import tqdm
    import ollama
    import httpx

    def download_model(model_name):
        global is_downloading
        global download_progress
        global download_text

        is_downloading = True
        download_progress = ""
        download_text = ""
        try:
            current_digest, bars = '', {}
            for progress in ollama.pull(model_name, stream=True):
                digest = progress.get('digest', '')
                if digest != current_digest and current_digest in bars:
                    bars[current_digest].close()

                if not digest:
                    print(progress.get('status'))
                    continue

                if digest not in bars and (total := progress.get('total')):
                    bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', ascii=True, unit='B', unit_scale=True)

                if completed := progress.get('completed'):
                    bars[digest].update(completed - bars[digest].n)

                download_progress = bars[digest]
                current_digest = digest

            is_downloading = False
            download_text = "done"
        except httpx.ConnectError:
            download_text = "<|Error|> You don't have ollama running."
        except ollama.ResponseError as e:
            download_text = f"<|Error|> {e.error}"




label download_model_label:
    "Enter the name of an AI model you want to download from ollama.com/library"

    $ model = renpy.input("Install a model").strip()
    $ renpy.invoke_in_thread(download_model, model)

    $ _history = False

    # Wait for download to finish
    while is_downloading == True:
        # An Error happened, so stop the current session and return to lobby
        if download_text.startswith("<|Error|>"):
            $ download_text = download_text.replace("<|Error|>", "")
            show screen error_popup(message=download_text)
            "Returning to main menu..."
            return
        else:
            "[download_progress] {fast} {w=0.7}{nw}"


    if download_text == "done":
        "Download Complete! Restart the game and select the model"

    return