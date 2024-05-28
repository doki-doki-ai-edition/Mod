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


    $ SetVariable("spacezone", None)
    $ persistent.purgatory = False
    $ renpy.save_persistent()

    $ tokenSetter.set_token()
    $ resume = None # Used to check if a file has been loaded
    $ chatFolderName = "monikaZone"

    ###########################
    # Monologue
    ###########################
    $ Configs().create_from_hex(f"{config.basedir}/game/audio/sfx/space.monika", f"{config.basedir}/game/audio/sfx/_space-lines.mp3")
    $ space_line = Info().getSpaceLines[2]["file"]
    $ space_line_time = Info().getSpaceLines[2]["time"]
    $ rnd_line = renpy.random.randint(1, 6)

    if persistent.first_space == True:
        $ renpy.sound.play(f"{space_line}", channel="sound", loop=None)

        $ persistent.first_space = False
        $ renpy.save_persistent()
    else:
        $ rnd_line = rnd_line if rnd_line != 4 else 1
        $ space_line = Info().getSpaceLines[rnd_line]["file"]
        $ space_line_time = Info().getSpaceLines[rnd_line]["time"]
        $ renpy.sound.play(f"{space_line}", channel="sound", loop=None)

    $ renpy.pause(space_line_time, hard=True)
    $ Configs().delete_egg(f"{config.basedir}/game/audio/sfx/_space-lines.mp3")



    # "num" is a default value set to None. If a number is
    # assigned to it, that means the user is opening an old file
    if num != None:
        if num >= 0:
            $ resume = True
            $ pathSetup = f"{config.basedir}/chats/"+persistent.chatFolderName[num]
            $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

            $ chatSetup = SetupChat(chat_name=persistent.chatFolderName[num], character_name=f"{current_char}")
            $ memory = Data(path_to_user_dir=pathSetup).getChathistory
            $ SetVariable("num", None)


    else:
        $ chatSetup = SetupChat(chat_name=chatFolderName, character_name=f"{character_name}")
        $ pathSetup = chatSetup.setup()
        $ renpy.log(f">>> pathSetup is: {pathSetup}")
        $ convo = chatSetup.chat(path=pathSetup, userInput="umm...", chathistory=Info().getExamplePrompts[f"level2_monika_zone"])
        $ DataSetup = Data(path_to_user_dir=pathSetup)
        $ DataSetup.updateSceneData("zone", "true")



    $ memory = Data(path_to_user_dir=pathSetup).getChathistory

    if resume:
        $ last_msg = Data(path_to_user_dir=pathSetup).getLastMessageClean

        if current_char == "monika":
            monika "[last_msg]"

    else:
        $ renpy.say(None, convo)





    ###########################
    # Main Event Loop
    ###########################
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