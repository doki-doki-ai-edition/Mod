
image menu_bg:
    topleft
    "assets/imgs/gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "assets/imgs/gui/menu_bg.png"
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
    "assets/imgs/gui/menu_art_s_g.png"
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
    "assets/imgs/gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "assets/imgs/gui/logo.png"
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

image rlly:
    truecenter
    zoom 2.45
    "assets/imgs/rlly.png"


label splashscreen:
    $ quick_menu = False
    scene tos2

    if persistent.firstrun:
        "This is a Doki Doki Literature Club mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed."
        "You can download Doki Doki Literature Club at: https://ddlc.moe"

        menu:
            "Do you understand?"

            "Yes.":
                "Yes."

            "Whatever.":
                play sound "assets/audio/sfx/vine-boom.mp3"
                show rlly
                hide rlly with Dissolve(3)
                "Whatever."

        "In order for the mod to work correctly please remember to install ollama by going to \"ollama.com\"."
        "Simply download the application and run it."
        "No GUI will popup, it'll simply run on your device with a small icon displayed in your taskbar."
        "Open up a terminal on your device and type \"ollama pull llama3.1\"."
        "You should be good to go."

        menu:
            "Do you understand?"

            "Yes.":
                "Yes."

            "Whatever.":
                play sound "assets/audio/sfx/vine-boom.mp3"
                show rlly
                hide rlly with Dissolve(3)
                "Whatever."

        "There is a far more detailed setup guide and examples of how the mod works in the Main Menu of the game, just click \"Help\"."

    jump ai_mod_notice



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


    return


label ai_mod_notice:
    scene tos

    if persistent.firstrun:
        $ persistent.firstrun = False
        $ renpy.save_persistent()
        "IMPORTANT NOTICE: This mod was made for the purpose of having fun interactions with the characters in a more visual way that goes beyond just text."
        "But it is important to keep in mind of the following:"
        "The characters are not real. They do not have emotions. They cannot be offended. They cannot be hurt. What you are interacting with in the simplest of terms is an advanced word guesser."
        "I want to ensure that most people playing are at the very least mindful of this and can distinguish reality from fiction."
        "Have fun!"
        show text "Any voices you hear is not AI generated." with dissolve
        $ renpy.pause(4, hard=True)
        "..."
    else:
        "REMINDER: The characters are not real. They do not have emotions. They cannot be offended. They cannot be hurt. What you are interacting with in the simplest of terms is an advanced word guesser."
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
    $ persistent.in_game = False
    $ renpy.save_persistent()
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