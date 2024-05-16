label monika_zone:
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

    #scene black with dissolve

    $ chatFolderName = "monikaZone"

    $ user_chats = ManageChat_Folders()

    # "num" is a default value set to None. If a number is
    # assigned to it, that means the user is opening an old file
    if num:
        if num >= 0:
            $ path = "chats/"+persistent.chatFolderName[num]
    else:
        $ path = user_chats.create_folder(name=chatFolderName)

        $ user_chats.create_chat_history()
        $ user_chats.create_world_history()

    $ check = CheckData(full_path=path+"/")
    $ memory = check.historyCheck(gamemode="monikaZone", chatmode=0) # Adds Freechat Prompt
    $ check.usernameCheck() # Adds your username to prompt
    $ convo = Convo(chat_history=memory, full_path=path+"/")

    $ wait_time = 5
    while True:
        $ wait_time -= 1
        if wait_time > 0: # Determines if you can respond yet
            $ user_msg = "continue"

        else:
            $ user_msg = renpy.input("Enter a message: ")
            $ wait_time = 5
        
        $ final_msg = f"{convo.ai_response(user_msg)}"
        if convo.NARRATION == False and convo.voice_mode == True:
            play sound "audio/vocals/monika.wav"
        monika "[final_msg]"
    return