


label start:

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

    return




label gamemode_label:
    scene theme
    call screen gamemode_screen
    return

label apikey_label:
    $ apikey = renpy.input("Enter API Key", f"{persistent.chatToken}").strip()
    $ persistent.chatToken = apikey
    $ renpy.save_persistent()
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
define sayori = Character("Sayori", color="#ffffff", window_style="textbox_sayori", who_outlines=[ (3, "#7795a3") ])
define natsuki = Character("Natsuki", color="#ffffff", window_style="textbox_natsuki", who_outlines=[ (3, "#a3779f") ])
define yuri = Character("Yuri", color="#ffffff", window_style="textbox_yuri", who_outlines=[ (3, "#8f77a3") ])

default choice = None

label AICharacter:
    $ tokenSetter.set_token()
    stop music
    $ custom_quick_menu = True
    scene black with dissolve

    $ chatSetup = SetupChat(chat_name=chatFolderName, character_name=character_name)
    $ resume = None # Used to check if a file has been loaded

    # "num" is a default value set to None. If a number is
    # assigned to it, that means the user is opening an old file
    if num:
        if num >= 0:
            $ resume = True
            $ path = "chats/"+persistent.chatFolderName[num]

    else:
        $ pathSetup = chatSetup.setup()
        $ convo = chatSetup.chat(path=pathSetup)


    $ current_background = Data(path_to_user_dir=pathSetup).getSceneData("background")


    image _bg:
        "bg/[current_background]"
    scene _bg

    # placeholder text (Will rely on json data later for when users load a file)
    "..."

    while True:
        $ rnd_continue = renpy.random.randint(1, 6)
        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

        if resume == True:
            $ user_msg = "continue {remember to never speak as the MC, continue the story.}"
            $ resume = False
        elif current_char != "" and rnd_continue == 4:
            $ user_msg = "continue"
        else:
            $ user_msg = renpy.input("Enter a message: ")

            if user_msg  == "(init_end_sim)":
                jump monika_zone


        $ final_msg = chatSetup.chat(path=pathSetup, userInput=user_msg)
        $ raw_msg = Data(path_to_user_dir=pathSetup).getLastMessage

        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")
        $ current_head = Data(path_to_user_dir=pathSetup).getSceneData("head_sprite")
        $ current_left = Data(path_to_user_dir=pathSetup).getSceneData("left_sprite")
        $ current_right = Data(path_to_user_dir=pathSetup).getSceneData("right_sprite")
        $ current_background = Data(path_to_user_dir=pathSetup).getSceneData("background")

        if raw_msg.startswith("[SCENE]"):
            # Narrator is speaking | Also the reason why I'm not using 1 if statement is because for whatever
            # reason, the cache of the previous img doesn't fully reset & the "zoom" remains the same.
            # The AI bg can only be 1024 x 1024 (max) and to fill the screen I need to use zoom.
            # I could import Pillow and resize it that way but installing it isnt working atm.

            image _bg:
                "bg/[current_background]"
            scene _bg


            "[final_msg]"
        elif final_msg.startswith("<Error>"):
            show screen error_popup(message=final_msg)
        else:
            # Char is speaking
            image head:
                "images/[current_char]/[current_head]"
                zoom 0.80
                yoffset 40
                uppies
            image leftside:
                "images/[current_char]/[current_left]"
                zoom 0.80
                yoffset 40
                uppies
            image rightside:
                "images/[current_char]/[current_right]"
                zoom 0.80
                yoffset 40
                uppies


            show head
            show leftside
            show rightside


            #if convo.NARRATION == False and convo.voice_mode == True:
            #    play sound "audio/vocals/monika.wav"

            if character_name == "monika":
                monika "[final_msg]"
            if character_name == "sayori":
                sayori "[final_msg]"
            if character_name == "natsuki":
                natsuki "[final_msg]"
            if character_name == "yuri":
                yuri "[final_msg]"
    return





label monika_zone:

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