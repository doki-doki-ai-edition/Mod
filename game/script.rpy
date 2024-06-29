

label start:

    init python:
        import threading
        config.has_autosave = False
        config.has_quicksave = False
        config.autosave_on_quit = False
        config.autosave_on_choice = False

    $ input_popup_gui = True

    stop music fadeout 0.5

    if persistent.purgatory == True:
        jump space_zone
    else:
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


label custom_chat_model_label:
    "Enter a model from your ollama list"
    "You can check what models you have available by typing \"ollama list\" in a command line on your device."
    $ model = renpy.input("Enter a model", f"{persistent.chatModel}").strip()
    $ persistent.chatModel = model 
    $ renpy.save_persistent()
    return


label nameWorld_label:
    scene theme

    $ motto = renpy.random.randint(1,315)
    if motto == 15:    
        scene black with dissolve
        play sound "<from 0 to 9>bgm/end-voice.ogg"
        $ renpy.pause(11, hard=True)
        jump ch0_motto

    "..."
    jump AICharacter

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
    $ persistent.in_game = True
    $ renpy.save_persistent()
    stop music
    $ custom_quick_menu = True
    scene black with dissolve

    

    $ resume = None # Used to check if a file has been loaded
    $ zone_type = None
    $ current_char = None
    $ current_char_title = None
    $ current_head = None
    $ current_left = None
    $ current_right = None
    $ current_background = None
    $ zone_type = None
    $ nc = False




    ###########################
    # Monologue
    ###########################
    if character_name == "sayori" and persistent.first_sayori:
        $ Configs().create_from_hex(f"{config.basedir}/game/assets/audio/sfx/space.mp3", f"{config.basedir}/game/assets/audio/sfx/_space-lines.mp3")
        $ space_line = Info().getSpaceLines[3]["file"]
        $ space_line_time = Info().getSpaceLines[3]["time"]
        $ persistent.first_sayori = False
        $ renpy.save_persistent()

        $ renpy.sound.play(f"{space_line}", channel="sound", loop=None)

        show unseen with Dissolve(space_line_time/2)
        $ renpy.pause(delay=space_line_time/2, hard=True)
        
        $ Configs().delete_egg(f"{config.basedir}/game/assets/audio/sfx/_space-lines.mp3")




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
            $ renpy.log(">>> in saved game")

    else:
        $ chatFolderName = renpy.input("Name This Realm: ", "realm", allow=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_").strip()
        $ chatSetup = SetupChat(chat_name=chatFolderName, character_name=character_name)
        $ pathSetup = chatSetup.setup(purgatory=False)

        $ convo = chatSetup.chat(path=pathSetup)
        $ renpy.log(">>> starting new ")



    ###########################
    # Setup old/new data
    ###########################
    $ memory = Data(path_to_user_dir=pathSetup).getChathistory
    $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")
    $ current_char_title = current_char.title()
    $ current_head = Data(path_to_user_dir=pathSetup).getSceneData("head_sprite")
    $ current_left = Data(path_to_user_dir=pathSetup).getSceneData("left_sprite")
    $ current_right = Data(path_to_user_dir=pathSetup).getSceneData("right_sprite")
    $ current_background = Data(path_to_user_dir=pathSetup).getSceneData("background")
    $ zone_type = Data(path_to_user_dir=pathSetup).getSceneData("zone")
    


    # Player loaded a space realm
    if zone_type == "true":
        jump space_zone
    



    
    image _bg:
        "bg/[current_background]"
    scene _bg

    if resume:
        $ last_msg = Data(path_to_user_dir=pathSetup).getLastMessageClean

        image basic:
            im.Composite((960, 960), (0, 0), f"{current_char}/{current_left}", (0, 0), f"{current_char}/{current_right}", (0, 0), f"{current_char}/{current_head}")
            uppies
        image full_sprite:
            im.Composite((960, 960), (0, 0), f"{current_char}/{current_head}")
            uppies

        if current_head != "3a.png" and current_head != "3b.png" and current_head != "3c.png" and current_head != "3b.png" and current_head != "3d.png" and current_head != "vomit.png":
            hide full_sprite
            show basic at t11
        else:
            hide basic
            show full_sprite at t11

        if current_char_title != "":
            $ renpy.say("[current_char_title]", last_msg)


    else:
        $ renpy.say(None, convo)


    show screen home_icon_screen
    
    ###########################
    # Main Event Loop
    ###########################
    $ main_event_loop = True
    while main_event_loop == True:
        $ rnd_continue = renpy.random.randint(1, 6)
        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

        if current_char != "" and rnd_continue == 4:
            # Randomly continue the chat to have variety so it's not a constant back and forth
            $ user_msg = "continue"
        else:
            $ user_msg = renpy.input("Enter a message: ")

            if user_msg  == "init_end_sim" and character_name == "monika":
                $ main_event_loop = False

                $ persistent.purgatory_name = character_name
                $ renpy.save_persistent()
                $ persistent.purgatory = True
                $ renpy.save_persistent()

                jump purgatory_seq


        # Start generating text in a separate thread
        $ chatSetup.is_generating = True
        $ threading.Thread(target=chatSetup.chat, args=(pathSetup, memory, user_msg)).start()

        $ _history = False
        # Initialize the wait message
        $ wait_msg = ""

        # Wait for AI to finish generating text
        while chatSetup.is_generating == True:
            $ wait_msg = wait_msg + "." if len(wait_msg) < 3 else "."
            "Loading[wait_msg] {fast} {w=0.7}{nw}"

        $ _history = True

        $ final_msg = chatSetup.generated_text
        $ raw_msg = Data(path_to_user_dir=pathSetup).getLastMessage

        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")
        $ current_char_title = current_char.title()
        $ current_head = Data(path_to_user_dir=pathSetup).getSceneData("head_sprite")
        $ current_left = Data(path_to_user_dir=pathSetup).getSceneData("left_sprite")
        $ current_right = Data(path_to_user_dir=pathSetup).getSceneData("right_sprite")
        $ current_background = Data(path_to_user_dir=pathSetup).getSceneData("background")

        if raw_msg.startswith("[SCENE]"):
            # Narrator is speaking 

            image _bg:
                "bg/[current_background]"
            scene _bg


            "[final_msg]"
        elif final_msg.startswith("<Error>"):
            show screen error_popup(message=final_msg)
        else:
            image basic:
                im.Composite((960, 960), (0, 0), f"{current_char}/{current_left}", (0, 0), f"{current_char}/{current_right}", (0, 0), f"{current_char}/{current_head}")
                uppies
            image full_sprite:
                im.Composite((960, 960), (0, 0), f"{current_char}/{current_head}")
                uppies


            if current_head != "3a.png" and current_head != "3b.png" and current_head != "3c.png" and current_head != "3b.png" and current_head != "3d.png" and current_head != "vomit.png":
                hide full_sprite
                hide chibi
                show basic at t11
            else:
                hide basic
                hide chibi
                show full_sprite at t11


            $ final_msg = final_msg if nc == False else final_msg.replace("rooster", Info().getMaleChicken)
            $ renpy.say("[current_char_title]", final_msg)

            if nc:
                $ nc = False
                $ Configs().delete_egg(f"{config.basedir}/game/assets/imgs/monika/_thumb.png")
    return






label purgatory_seq:
    scene black with dissolve
    $ SetVariable("spacezone", True)
    "...Are you sure?"
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