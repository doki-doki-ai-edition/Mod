# Credits: Character Bio template by Retronika & iiTzWolfyy


init -10 python:
    import json
    
    class BioCharacter:
        def __init__(self, name, bio, image, logo, chibi=None, chibi_hover=None):
            self.name = name
            self.bio = bio
            self.image = image
            self.logo = logo
            self.chibi = chibi
            self.chibi_hover = chibi_hover


    def selection_list():
        dir_path = config.basedir + "/game/assets/configs/custom_characters"
        chars = {}

        for filename in os.listdir(dir_path):
            if filename.endswith('.json'):
                with open(os.path.join(dir_path, filename), 'r') as f:
                    data = json.load(f)
                    chars.update(data)

        with open(f'{config.basedir}/game/assets/configs/characters.json', 'r') as f:
            default_chars = json.load(f)
            chars.update(default_chars)

        bio_list = []
        for name in chars:
            bio_list.append(BioCharacter(name, chars[name]["bio"], chars[name]["image"], chars[name]["logo"], chars[name]["chibi"], chars[name]["chibi_hover"]))
        return bio_list


    def change_backstory():
        renpy.call_in_new_context("custom_backstory_label")

# Example character data
define characters = selection_list()

default index = 0
default current_character = characters[index]

init -5 python:
    def update_character(new_index):
        store.index = new_index
        store.current_character = characters[new_index]

transform single_chibi:
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    repeat

transform both_chibis:
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    repeat

screen bio_screen:
    tag menu

    add "menu_bg"

    vbox: # Character name, logo, and chibi
        xalign 0.1
        yalign 0.1
        spacing 10
        text "[current_character.name]" style "character_name_title" xalign 0.5
        null height 5
        add current_character.logo xalign 0.5 size(300, 300)
        null height 30
        if current_character.chibi is not None:
            imagebutton:
                xalign 0.5
                action NullAction()
                idle current_character.chibi
                if current_character.chibi_hover is None:
                    at transform:
                        xalign 0.5
                        on hover:
                            single_chibi
                        on idle:
                            easeout_quad .1 yoffset 0
                else:
                    hover current_character.chibi_hover
                    at transform:
                        xalign 0.5
                        on hover:
                            both_chibis
                        on idle:
                            easeout_quad .1 yoffset 0

    vbox: # Main sprite and arrows underneath
        xalign 0.4 yalign 0.5
        add current_character.image xalign 0.0 yalign 0.6 zoom 0.5

        # Nav buttons
        hbox:
            style_prefix "arrows"

            xalign 0.5
            yalign 0.97
            spacing 20

            textbutton "<" action If(
                index > 0, 
                true=Function(update_character, index - 1), 
                false=Function(update_character, len(characters) - 1)
            )

            text [current_character.name] style "character_name_style"

            textbutton ">" action If(
                index < len(characters) - 1, 
                true=Function(update_character, index + 1), 
                false=Function(update_character, 0)
            )

    null width 30

    # Bio section
    frame:
        background "assets/imgs/gui/bio_box.png"
        xalign 1
        yalign 0.4
        padding (790, 130, 160, 220)
        vbox: # Character info
            xfill True
            box_wrap True
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                text "[current_character.bio]" size 22 justify True


    frame: # Previous apperances
        background None
        xalign 5
        yalign 0.6
        padding (790, 455, 160, 10)
        hbox:
            xfill True
            box_wrap True
            textbutton "Begin" action [SetVariable("character_name", current_character.name.lower()), Hide("bio_screen"), Jump("nameWorld_label")] style "return_button"
            textbutton "Edit" action [SetVariable("character_name", current_character.name.lower()), Function(change_backstory)] style "return_button"


    textbutton _("Return"):
        style "return_button"

        action Return()

style character_name_style:
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#000", 0, 0), (2, "#000", 2, 2)]

style character_name_title is character_name_style:
    size 45
    xalign 0.5

style arrows_button is gui_button
style arrows_button_text is gui_button_text

style arrows_button:
    size_group "arrows"
    properties gui.button_properties("arrows_button")

style arrows_button_text:
    properties gui.button_text_properties("arrows_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#000", 0, 0), (2, "#000", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]