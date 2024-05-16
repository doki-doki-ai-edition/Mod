label space_zone:
    scene white
    play music "audio/bgm/monika-start.ogg" noloop
    $ renpy.pause(0.5, hard=True)
    show splash_glitch2 with Dissolve(0.5, alpha=True)
    $ renpy.pause(2.0, hard=True)
    hide splash_glitch2 with Dissolve(0.5, alpha=True)
    #scene black
    stop music

    show mask_2
    show mask_3
    show monika_bg
    show monika_bg_highlight
    play music m1

    $ tokenSetter.set_token()
    $ resume = None # Used to check if a file has been loaded
    $ chatFolderName = "monikaZone"

    # "num" is a default value set to None. If a number is
    # assigned to it, that means the user is opening an old file
    if num != None:
        if num >= 0:
            $ resume = True
            $ pathSetup = f"{config.basedir}/chats/"+persistent.chatFolderName[num]
            $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

            $ chatSetup = SetupChat(chat_name=persistent.chatFolderName[num], character_name=current_char)
            $ memory = Data(path_to_user_dir=pathSetup).getChathistory
            $ SetVariable("num", None)


    else:
        $ chatSetup = SetupChat(chat_name=chatFolderName, character_name=f"{character_name}_zone")
        $ pathSetup = chatSetup.setup()
        $ convo = chatSetup.chat(path=pathSetup)

    $ memory = Data(path_to_user_dir=pathSetup).getChathistory

    if resume:
        $ last_msg = Data(path_to_user_dir=pathSetup).getLastMessageClean

        if current_char == "monika":
            monika "[last_msg]"

    else:
        "..."

    while True:
        $ rnd_continue = renpy.random.randint(1, 6)
        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

        if current_char != "" and rnd_continue == 4:
            # Randomly continue the chat to have variety so it's not a constant back and forth
            $ user_msg = "continue"
        else:
            $ user_msg = renpy.input("Enter a message: ")


        $ final_msg = chatSetup.chat(path=pathSetup, chathistory=memory, userInput=user_msg)
        $ raw_msg = Data(path_to_user_dir=pathSetup).getLastMessage


        if final_msg.startswith("<Error>"):
            show screen error_popup(message=final_msg)
        else:

            monika "[final_msg]"

    return