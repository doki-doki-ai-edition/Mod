


label start:

    if persistent.freedom:
        init python:
            config.has_autosave = False
            config.has_quicksave = False
            config.autosave_on_quit = False
            config.autosave_on_choice = False

        $ input_popup_gui = True
        if num: # Avoid NoneType error
            if num >=0:
                jump AICharacter
                return

        stop music fadeout 0.5

        scene theme with dissolve
        call screen chatmode_screen
    else:
        $ chapter = 0


        $ _dismiss_pause = config.developer


        $ s_name = "???"
        $ m_name = "Girl 3"
        $ n_name = "Girl 2"
        $ y_name = "Girl 1"

        $ quick_menu = True
        $ style.say_dialogue = style.normal
        $ in_sayori_kill = None
        $ allow_skipping = True
        $ config.allow_skipping = True


        if persistent.playthrough == 0:
            $ chapter = 0
            call ch0_main from _call_ch0_main
        return




label gamemode_label:
    scene theme
    call screen gamemode_screen
    return


label nameWorld_label:
    scene theme
    $ chatFolderName = renpy.input("Name This Realm: ", "realm", allow=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_").strip() 

    $ motto = renpy.random.randint(1,300)
    if motto == 15:    
        scene black with dissolve
        play sound "audio/sfx/can you hear me.mp3"
        $ renpy.pause(11, hard=True)

    if chatmode_num == 0:
        jump AICharacter
    else:
        # Currently disabled
        #jump justMonika_Storymode
        pass
    return



################################################################################
## Character's Realm
################################################################################

define monika = Character("Monika", color="#ffffff", window_style="textbox_monika", who_outlines=[ (3, "#77a377") ])
default choice = None

label AICharacter:
    $ tokenSetter.set_token_persist()
    stop music
    $ custom_quick_menu = True
    scene black with dissolve

    $ user_chats = ManageChat_Folders(character_name=character_name)
    $ load = None # Used to check if a file has been loaded

    # "num" is a default value set to None. If a number is
    # assigned to it, that means the user is opening an old file
    if num:
        if num >= 0:
            $ load = True
            $ path = "chats/"+persistent.chatFolderName[num]
            $ check = CheckData(character_name=character_name, full_path=path+"/")
            $ memory = check.historyCheck(gamemode="justMonika", chatmode=0, load=True)
            $ convo = Convo(character_name=character_name, chat_history=memory, full_path=path+"/", load=True)
    else:
        $ path = user_chats.create_folder(name=chatFolderName)

        $ user_chats.create_chat_history()
        $ user_chats.create_world_history()

        $ check = CheckData(character_name=character_name, full_path=path+"/")
        $ memory = check.historyCheck(gamemode="justMonika", chatmode=0) # Adds Freechat Prompt
        $ check.usernameCheck() # Adds your username to prompt
        $ convo = Convo(character_name=character_name, chat_history=memory, full_path=path+"/")

    if convo.ai_art_mode == False:
        image _bg:
            "bg/[convo.scene]"
        scene _bg
    else:
        image ai_bg:
            zoom 1.5
            "bg/[convo.scene]"
        scene ai_bg

    # placeholder text (Will rely on json data later for when users load a file)
    "..."

    while True:
        if load == True:
            $ user_msg = "continue {remember to never speak as the MC, continue the story.}"
            $ load = False
            $ convo.proceed = True
        elif convo.proceed == "First": # The prompt template was just generated 
            $ user_msg = "{RPT}"
        elif convo.rnd == 6: # Makes the narration/Character add on to what they were saying
            $ user_msg = "continue"
        else:
            $ user_msg = renpy.input("Enter a message: ")
            if convo.rnd == 1:
                $ user_msg = convo.context_to_progress_story(user_msg)
            if convo.rnd == 2:
                $ user_msg = convo.enforce_static_emotes(user_msg)

        $ final_msg = convo.ai_response(user_msg)

        if convo.zone == "True":
            #jump now_everyone_can_be_happy
            pass
        elif convo.zone == "Zone":
            jump monika_zone

        if convo.NARRATION:
            # Narrator is speaking | Also the reason why I'm not using 1 if statement is because for whatever
            # reason, the cache of the previous img doesn't fully reset & the "zoom" remains the same.
            # The AI bg can only be 1024 x 1024 (max) and to fill the screen I need to use zoom.
            # I could import Pillow and resize it that way but installing it isnt working atm.
            if convo.ai_art_mode == False:
                image _bg:
                    "bg/[convo.scene]"
                scene _bg
            else:
                image ai_bg:
                    "bg/[convo.scene]"
                    zoom 1.5
                scene ai_bg

            "[final_msg]"
        else:
            # Char is speaking
            image head:
                "images/[convo.char]/[convo.head_sprite]"
                zoom 0.80
                yoffset 40
                uppies
            image leftside:
                "images/[convo.char]/[convo.leftside_sprite]"
                zoom 0.80
                yoffset 40
                uppies
            image rightside:
                "images/[convo.char]/[convo.rightside_sprite]"
                zoom 0.80
                yoffset 40
                uppies

            if convo.scene != "coffee.jpg":
                show head
                show leftside
                show rightside

            #if convo.NARRATION == False and convo.voice_mode == True:
            #    play sound "audio/vocals/monika.wav"
            monika "[final_msg]"
    return





label monika_zone:
    $ show_quick_menu = False
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
    #show room_mask as rm:
        #size (320,180)
        #pos (30,200)
    #show room_mask2 as rm2:
        #size (320,180)
        #pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1


    $ show_quick_menu = True
    #scene black with dissolve

    $ chatFolderName = "monikaZone"

    $ user_chats = ManageChat_Folders("monika")

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
            $ user_msg = "continue {continue the character monologue here and remember to never speak as me}"

        else:
            $ user_msg = renpy.input("Enter a message: ")
            $ wait_time = 5
        
        $ final_msg = f"{convo.ai_response(user_msg)}"
        if convo.NARRATION == False and convo.voice_mode == True:
            play sound "audio/vocals/monika.wav"
        monika "[final_msg]"
    return



label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return