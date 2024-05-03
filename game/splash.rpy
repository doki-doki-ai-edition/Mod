
image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:
    $ quick_menu = False
    scene tos2

    "This is a Doki Doki Literature Club fan game that is not affiliated with Team Salvato."
    "It is designed to be played only after the official game has been completed."
    "You can download Doki Doki Literature Club at: http://ddlc.moe"
    python:
        s_kill_early = None
        m_deleted = False
        s_deleted = False

        try:
            renpy.file("../characters/monika.chr")
        except:
            with open(f"{config.basedir}/characters/monika.chr", 'w') as f:
                f.write("c29tZSBzZWNyZXRzIGFyZSBiZXN0IGxlZnQgdW50b3VjaGVk")
            m_deleted = True

        try:
            renpy.file("../characters/sayori.chr")
            Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        except: pass
    
    if s_kill_early:
        pass
        #jump now_everyone_can_be_happy
    if m_deleted:
        return Show(screen="dialog", message="You accidentally deleted me? It's okay! Mistakes happen.", ok_action=Hide("dialog"))
    if s_deleted:
        return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
            ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))



    if persistent.playername == 'Sayori':
        return Show(screen="dialog", message="It's far too early for that, please wait a bit longer.",  ok_action=Hide("dialog"))
    elif persistent.playername == 'Monika':
        return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))

    if persistent.playername == None:
        $ persistent.playername = renpy.input("What is your name?", "User", allow=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789").strip()


    if persistent.freedom != None:
        jump ai_mod_notice

    scene black
    with Pause(1)

    show text "Please remember that this is just a game and\nthe Doki's aren't actually real." with dissolve
    $ renpy.pause(3, hard=True)
    hide text with dissolve
    with Pause(1.3)
    return


label reset_LLM:
    $ persistent.chatModel = None
    $ persistent.chatToken = None
    jump ai_mod_notice
    return


label ai_mod_notice:
    scene tos
    if persistent.chatModel == None:
        "IMPORTANT NOTICE: Paying for OpenAI's API is not required to play this mod. You're able to use any API/LLM model you want 100 percent free (You just need to know what you're doing but instructions for those not as tech savvy will be coming out soon)"
        "None of the money, tokens, messages etc. are recieved by me or any entity related to me in accordance to DDLC's IP Guidelines"
        "OpenAI is currently the only model built-in in for your own convinience."
        "I am not sponsered/partnered with openAI or any API contained in this project and make no profit from this."
        "Because the built-in A.I. models arent locally hosted, you can follow the steps listed on the github page. https://github.com/syntax-z/DOKI-DOKI-AI-EDITION"
        "If you aren't able to do that at this moment, you can skip all these steps and change them in the settings later."

        menu:
            "By playing [config.name] you agree that you understand that paying for any API as an extention to this mod is your optional choice and is not at all required to play."
            "I agree.":
                pass

        "Which Language model would you like to use?"
        "1 is for 'chatGPT' (recommended)"
        $ chatModel = renpy.input("Which AI model would you like to use? (enter '1')", "1", allow="1").strip()
        if chatModel == "1":
            "You chose chatGPT!"
        #elif chatModel == "2":
        #    "You choose Bard!"
        else:
            "Not a valid chat model, change this in the settings once you get the chance!"

        # Ensures that if the user exited out of the game before completing the steps, they can finish
        # when they reload
        $ persistent.chatModel = chatModel
        $ renpy.save_persistent()

    if persistent.chatToken == None:
        "Do NOT share any of your tokens to ANYONE. Your tokens will be used here strictly for generating responses."
        "If someone you do not trust gets it, they can send multiple request to the API, costing you money."
        "If you think your token has somehow been exposed, you can reset it on the API's official page."
        $ chatToken = renpy.input("Enter your openAI (chatGPT) token: ").strip()

        "If you misclicked or entered the wrong token by accident, you can always change it in the settings."

        $ persistent.chatToken = chatToken
        $ renpy.save_persistent()

    if persistent.imgModel == None:
        "Which Image generation model would you like to use?"
        "1 is for 'getimgai' (recommended) and 2 is for 'stablediffusionapi' (You can tweak these later in the settings)"
        $ imgModel = renpy.input("Which Image generation model would you like to use?(1 or 2)", "1", allow="12").strip()
        if imgModel == "1":
            "You chose getimgai!"
        elif imgModel == "2":
            "You choose stablediffusionapi!"
        else:
            "Not a valid image model, change this in the settings once you get the chance!"

        "(reminder) Because the A.I. models arent locally hosted, please follow the steps listed on the github page. https://github.com/syntax-z/DOKI-DOKI-AI-EDITION"
        "(reminder) If you aren't able to do that at this moment, you can skip the next step and change them in the settings later."

        $ persistent.imgModel = imgModel
        $ renpy.save_persistent()

    if persistent.imgToken == None:
        $ imgToken = renpy.input("Enter your image generation token: ").strip()
        "If you misclicked or entered the wrong token by accident, you can always change it in the settings."
        $ persistent.imgToken = imgToken
        $ renpy.save_persistent()

    return



    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    #$ restore_relevant_characters()
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")


    $ basedir = config.basedir.replace('\\', '/')



    $ config.allow_skipping = False



label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return