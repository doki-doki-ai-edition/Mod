init offset = -1










style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style textbox_monika is window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)



style textbox_sayori is window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_sayori.png", xalign=0.5, yalign=1.0)


style textbox_natsuki is window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)


style textbox_yuri is window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_yuri.png", xalign=0.5, yalign=1.0)



init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

    background ConditionSwitch(
        "_last_say_who == 'm'", Frame("gui/namebox_monika.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign),
        "_last_say_who == 's'", Frame("gui/namebox_sayori.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign),
        "_last_say_who == 'n'", Frame("gui/namebox_natsuki.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign),
        "_last_say_who == 'y'", Frame("gui/namebox_yuri.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign),
        "_last_say_who == 'n_default'", Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign),
        )
    padding gui.namebox_borders.padding

style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)


style window_sayori is window:
    background Image("gui/textbox_sayori.png", xalign=0.5, yalign=1.0)

style window_natsuki is window:
    background Image("gui/textbox_natsuki.png", xalign=0.5, yalign=1.0)

style window_yuri is window:
    background Image("gui/textbox_yuri.png", xalign=0.5, yalign=1.0)




style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat











image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xanchor 0.0
            xpos gui.text_xpos
            xsize 774
            ypos 55

            text prompt style "input_prompt"
            input id "input"


    # window:

    #     has vbox:
    #         xpos gui.text_xpos
    #         xanchor 0.5
    #         ypos gui.text_ypos

    #     text prompt style "input_prompt"
    #     input id "input"




screen input_long(prompt):
    style_prefix "input"

    frame:
        background Frame("gui/frame.png", Borders(25, 25, 25, 25))
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        vbox:
            text prompt style "input_prompt"
        vbox:
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign
    color '#fff'
    outlines [ (2, "#ffffff"), (2, "#000") ]

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.0
    text_align 0.5
    outlines [ (2, "#ffffff"), (2, "#000") ]










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []







screen quick_menu():


    zorder 100

    if custom_quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") #action Skip()
            textbutton _("Auto") #action Preference("auto-forward", "toggle")
            textbutton _("Save") #action ShowMenu('save')
            textbutton _("Load") #action ShowMenu('load')


            textbutton _("Settings") action ShowMenu('preferences')

    elif quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')


            textbutton _("Settings") action ShowMenu('preferences')







default quick_menu = True




style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []











init python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

    def FinishEnterModelName():
        persistent.chatModel = chatModel
        renpy.save_persistent()
        renpy.hide_screen("model_name_input")

    def FinishEnterAPIKey():
        persistent.chatToken = chatToken
        renpy.save_persistent()
        renpy.hide_screen("APIKey_name_input")

    def FinishEnterContextWindow():
        persistent.context_window = context_window
        renpy.save_persistent()
        renpy.hide_screen("context_window_popup")
        renpy.show_screen("llm_model_config_screen")

    def FinishEnterTemp():
        persistent.temp = temp
        renpy.save_persistent()
        renpy.hide_screen("temp_window_popup")
        renpy.show_screen("llm_model_config_screen")

    def FinishEnterSeed():
        persistent.seed = seed
        renpy.save_persistent()
        renpy.hide_screen("seed_window_popup")
        renpy.show_screen("llm_model_config_screen")

    def FinishResetModelConfig():
        persistent.seed = default_seed
        persistent.temp = default_temp
        persistent.context_window = default_context_window
        renpy.save_persistent()
        renpy.hide_screen("reset_config_window_popup")
        renpy.show_screen("llm_model_config_screen")

    def FinishUpdateModelName(modelname):
        persistent.chatModel = modelname
        renpy.save_persistent()


    def FinishEnterPromptHeader():
        persistent.prompt_header = prompt_header
        renpy.save_persistent()
        renpy.hide_screen("prompt_header_input")
        renpy.show_screen("llm_model_config_screen")


    def SwitchToModelConfig():
        renpy.hide_screen("preferences")

    def SwitchToSettings():
        renpy.hide_screen("llm_model_config_screen")




screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1 or persistent.purgatory:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

            else:

                textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                #textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            if persistent.in_game == False:
                textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
            else:
                textbutton _("Load Game") action Show(screen="basic_popup", title="Info", message="Go to the Main Menu before loading a game.", ok_action=NullAction())

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Main Menu") action MainMenu()
                else:
                    textbutton _("Main Menu") action NullAction()

            textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



            if renpy.variant("pc"):


                textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]


                textbutton _("Quit") action Quit(confirm=not main_menu)
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]








screen main_menu():


    style_prefix "main_menu" tag menu

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame




        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size











screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "assets/imgs/gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu

    use custom_save_screen()

    


screen load():
    tag menu

    use custom_save_screen()


init python:
    def FileActionMod(name, page=None, **kwargs):
        return FileAction(name)


#default num = None
init python:
    import os
    chats = ""
    try: chats = os.listdir(f"{config.basedir}/chats")
    except FileNotFoundError: pass
    

screen file_slots(title):
    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            order_reverse True


            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)




screen custom_save_screen():
    modal True
    zorder 10
    add "assets/imgs/bg/theme.png"
    use game_menu(_("Load"), scroll="viewport"):

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:
                null height 50
                textbutton "Back":
                    style_prefix "navigation_button_text"

                    xpos 20
                    
                    hover_sound "gui/sfx/hover.ogg"
                    activate_sound "gui/sfx/select.ogg"
                    action Hide("custom_save_screen")


            vbox:
                if chats == "":
                    pass
                else:
                    $ chat_list = []
                    for i, folder in enumerate(chats):
                        textbutton folder:
                            xpos 250
                            ypos 120
                            action [SetVariable("num", i), Hide("custom_save_screen"), Jump("nameWorld_label")]
                        $ chat_list.append(folder)
                        null width 20
                    $ persistent.chatFolderName = chat_list



screen select_model_name_screen():
    modal True
    zorder 10
    add "assets/imgs/bg/theme.png"

    $ fav_local_models = chat_model_dict["llms"]["suggested"]
    $ other_local_models = chat_model_dict["llms"]["other"]


    $ important_info = "Type \"ollama run (model name)\" in a console on your computer.\nFor example: ollama run llama3" if llm_mode == True else "Make sure you're using the correct API key for the model name you select."
    use game_menu(_("Models"), scroll="viewport"):

        vbox:
            null height 50
            textbutton _("Back") action [Return(), renpy.hide_screen("select_model_name_screen")]


        vbox:
            style_prefix "slider"
            box_wrap True

            vbox:
                label _(f"Current Model: {persistent.chatModel}")
                textbutton _("Important Info") action Show(screen="basic_popup", title="Info", message=important_info, ok_action=NullAction())



            vbox:
                if llm_mode == True:
                    label _(f"Suggested Models")
                    for model in fav_local_models:
                        textbutton _(f"{model}") action Show(screen="basic_popup", title="Local Models", message="Sucessfully updated model!", ok_action=Function(FinishUpdateModelName, model))

                    label _(f"Other Models")
                    for model in other_local_models:
                        textbutton _(f"{model}") action Show(screen="basic_popup", title="Local Models", message="Sucessfully updated model!", ok_action=Function(FinishUpdateModelName, model))


                textbutton _("Custom Model") action Jump("custom_chat_model_label")










screen llm_model_config_screen():
    modal True
    zorder 10
    use game_menu(_("Config"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

            vbox:
                textbutton _("Back") action [Return(), renpy.hide_screen("preferences"), renpy.hide_screen("llm_model_config_screen")]

            vbox:
                null height 50
                textbutton _("Use Default Settings") action Show(screen="reset_config_window_popup", message="Relaunch the game.", ok_action=Function(FinishResetModelConfig))
                


            null height (4 * gui.pref_spacing)

            vbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _(f"Context Window: {context_window}")

                    hbox:
                        textbutton _("Change") action Show(screen="context_window_popup", message="Enter a number", ok_action=Function(FinishEnterContextWindow))
                        textbutton _("Info") action [Show(screen="info_context_window_popup", message="Context Window", ok_action=Hide("info_context_window_popup")), Return(), renpy.hide_screen("preferences"), renpy.hide_screen("llm_model_config_screen")]

                    label _(f"Temperature: 0.{temp}")

                    hbox:
                        textbutton _("Change") action Show(screen="temp_window_popup", message="Enter a number 0-9", ok_action=Function(FinishEnterTemp))
                        textbutton _("Info") action [Show(screen="info_temp_popup", message="Temperature", ok_action=Hide("info_temp_popup")), Return(), renpy.hide_screen("preferences"), renpy.hide_screen("llm_model_config_screen")]

                vbox:

                    label _(f"Seed: {seed}")

                    hbox:
                        textbutton _("Change") action Show(screen="seed_window_popup", message="Enter a number", ok_action=Function(FinishEnterSeed))
                        textbutton _("Info") action [Show(screen="info_seed_popup", message="Seed", ok_action=Hide("info_seed_popup")), Return(), renpy.hide_screen("preferences"), renpy.hide_screen("llm_model_config_screen")]









style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []









screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "radio"
                    label _("AI Type")
                    textbutton _("LLM") action [SetVariable("llm_mode", True)]





            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")


                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:
                    textbutton _("Model Name") action ShowMenu("select_model_name_screen")
                vbox:
                    textbutton _("Model Config") action ShowMenu("llm_model_config_screen")
                vbox:
                    textbutton _("Change Username") action Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName))




    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
















screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



screen reset_config_window_popup(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action




screen model_name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("chatModel")


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action






screen APIKey_name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("chatToken")


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action




screen context_window_popup(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("context_window") allow "0123456789"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



screen temp_window_popup(message, ok_action):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("temp") length 1 allow "0123456789"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



screen seed_window_popup(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "Random" value VariableInputValue("seed") allow "0123456789"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action







screen info_context_window_popup(message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        label _("The maximum amount of tokens (messages) that will be remembered. Higher=More tokens remembered but this will consume a lot of RAM if you're using an LLM"):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



screen info_temp_popup(message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        label _("How creative the model will be with responses. (Higher=More creative but 0.6 is highly recommended for this)"):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action



screen info_seed_popup(message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        label _("Same responses. Selecting a specific seed will always return the same response if your message is written the same."):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action


screen info_prompt_popup(message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        label _("level1 is the basic prompt that uses far less tokens and level2 is more detailed but uses more tokens. In the main menu click \"Help\" to learn more."):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action






screen error_popup(message):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action Play("sound", gui.activate_sound)

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _("ERROR"):
            style "confirm_prompt"
            xalign 0.5

        label _(message):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Hide("error_popup")



screen basic_popup(title, message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(title):
            style "confirm_prompt"
            xalign 0.5

        label _(message):
            style "confirm_prompt"


        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide("basic_popup"), ok_action]










################################################################################
## Characters
################################################################################


default chatmode_num = None


################################################################
## Home Icon
################################################################ 

transform home_size:
    zoom 0.45

screen home_icon_screen():
    modal False
    imagebutton:
        xpos 1200
        ypos 35
        idle "assets/imgs/gui/overlay/home_fill.png"
        hover "assets/imgs/gui/overlay/home_nofill.png"

        hover_sound "gui/sfx/hover.ogg"
        activate_sound "gui/sfx/select.ogg"
        at home_size
        action MainMenu()






screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action





style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")








screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size