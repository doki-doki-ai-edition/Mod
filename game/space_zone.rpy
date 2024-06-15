label space_zone:
    scene white
    play music "bgm/monika-start.ogg" noloop
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

    $ persistent.in_game = True
    $ renpy.save_persistent()

    $ purg_name = persistent.purgatory_name
    $ purg_name_title = purg_name.title()

    $ persistent.purgatory = False
    $ renpy.save_persistent()
    $ persistent.purgatory_name = ""
    $ renpy.save_persistent()

    $ tokenSetter.set_token()
    $ resume = None # Used to check if a file has been loaded
    $ chatFolderName = f"{purg_name}_purgatory"

    ###########################
    # Monologue
    ###########################
    $ Configs().create_from_hex(f"{config.basedir}/game/assets/audio/sfx/space.mp3", f"{config.basedir}/game/assets/audio/sfx/_space-lines.mp3")
    $ space_line = Info().getSpaceLines[1]["file"]
    $ space_line_time = Info().getSpaceLines[1]["time"]
    $ rnd_line = renpy.random.randint(0, 5)

    if persistent.first_space == True:
        $ renpy.sound.play(f"{space_line}", channel="sound", loop=None)

        $ persistent.first_space = False
        $ renpy.save_persistent()
    else:
        $ rnd_line = rnd_line if rnd_line != 3 else 0
        $ space_line = Info().getSpaceLines[rnd_line]["file"]
        $ space_line_time = Info().getSpaceLines[rnd_line]["time"]
        $ renpy.sound.play(f"{space_line}", channel="sound", loop=None)

    $ renpy.pause(space_line_time, hard=True)
    $ Configs().delete_egg(f"{config.basedir}/game/assets/audio/sfx/_space-lines.mp3")


    call screen home_icon_screen
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
        $ chatSetup = SetupChat(chat_name=chatFolderName, character_name=f"{purg_name}")
        $ pathSetup = chatSetup.setup(purgatory=True)
        $ renpy.log(f">>> pathSetup is: {pathSetup}")
        $ DataSetup = Data(path_to_user_dir=pathSetup)
        $ DataSetup.updateSceneData("zone", "true")
        $ DataSetup.updateSceneData("character", f"{purg_name}")
        $ convo = chatSetup.chat(path=pathSetup, userInput="umm...", chathistory=Info().getExamplePrompts[f"level2_{purg_name}_purgatory"])



    $ memory = Data(path_to_user_dir=pathSetup).getChathistory

    if resume:
        $ last_msg = Data(path_to_user_dir=pathSetup).getLastMessageClean

        if current_char == "monika":
            monika "[last_msg]"

    else:
        $ renpy.say("[purg_name_title]", convo)



    $ counter = 0
    $ special_check = False
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
            $ counter += 1



        if counter >= 6 and persistent.first_scare == False:
            hide monika_bg
            hide monika_bg_highlight
            show monika_scare
            play sound "sfx/mscare.ogg"
            $ persistent.first_scare = True
            $ renpy.save_persistent()
            $ special_check = True
            $ user_msg = user_msg + " *I also suddenly scream really loudly because you just scared me*"

        $ final_msg = chatSetup.chat(path=pathSetup, chathistory=memory, userInput=user_msg)
        $ raw_msg = Data(path_to_user_dir=pathSetup).getLastMessage


        if final_msg.startswith("<Error>"):
            show screen error_popup(message=final_msg)
        else:
            if special_check:
                $ renpy.pause(10, hard=True)
                "..."
                $ special_check = False
            hide monika_scare
            show monika_bg
            show monika_bg_highlight
            $ renpy.say("[purg_name_title]", final_msg)

    return