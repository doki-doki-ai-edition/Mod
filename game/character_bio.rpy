# Credits: Character Bio template by Retronika & iiTzWolfyy


init -10 python:
    class BioCharacter:
        def __init__(self, name, bio, appear, image, logo, chibi=None, chibi_hover=None):
            self.name = name
            self.bio = bio
            self.appear = appear
            self.image = image
            self.logo = logo
            self.chibi = chibi
            self.chibi_hover = chibi_hover

# Example character data
define characters = [
    BioCharacter("Monika", "President of the Literature Club, Monika is best known for her stellar looks, superb athleticism, and being at the top of her class. Much like a book, though, there's a lot more to her than what's on the surface...\n\nHeight: 5'1'' / 160.02cm\nWeight: 125lbs / 56.7kg\nEye Color: Green\nEthnicity: Unknown", "Doki Doki Literature Club!  (2017)\nMonika After Story               (2017)\nDDLC Plus!                             (2021)", "gui/menu_art_m.png", "assets/imgs/gui/logo.png", "gui/poemgame/m_sticker_1.png", "gui/poemgame/m_sticker_2.png"),
    BioCharacter("Natsuki", "An aficionado at all things baking and unhesitant to put you in your place, Natsuki brings equal amounts of sweet and sour to the table...not specifically for you, or anything. No calling her cute!\n\nHeight: 4'11'' / 149.86cm\nWeight: 92.5lbs / 42kg\nEye Color: Magenta\nEthnicity: Japan", "Doki Doki Literature Club!  (2017)\nExit Music                               (2018)\nDDLC Plus!                              (2021)", "gui/menu_art_n.png", "assets/imgs/gui/logo.png", "gui/poemgame/n_sticker_1.png", "gui/poemgame/n_sticker_2.png"),
    BioCharacter("Sayori", "A best friend to the very end! Sayori's trademark smiles and clumsy attitude never fail to lift the spirits of nearly anyone she meets. Don't be too fooled by it, though, for those who smile the widest tend to cry the hardest...\n\nHeight: 5'2'' / 157.48cm\nWeight: 119lbs / 54kg\nEye Color: Blue\nEthnicity: Japan", "Doki Doki Literature Club!  (2017)\nSalvation                                 (2018)\nDDLC Plus!                              (2021)", "gui/menu_art_s.png", "assets/imgs/gui/logo.png", "gui/poemgame/s_sticker_1.png", "gui/poemgame/s_sticker_2.png"),
    BioCharacter("Yuri", "When she's not buried in the world of books, Yuri shyly brings an air of serenity to wherever she goes, sometimes accompanied by a hot cup of tea. Trust in her eyes goes a long way, so be sure to never break hers.\n\nHeight: 5'5'' / 165.1cm\nWeight: 130lbs / 59kg\nEye Color: Purple\nEthnicity: Japan", "Doki Doki Literature Club!  (2017)\nFallen Angel                           (2019)\nDDLC Plus!                              (2021)", "gui/menu_art_y.png", "assets/imgs/gui/logo.png", "gui/poemgame/y_sticker_1.png", "gui/poemgame/y_sticker_2.png")
]

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
        xalign 1
        yalign 0.4
        padding (790, 455, 160, 10)
        vbox:
            xfill True
            box_wrap True
            text "[current_character.appear]" size 20 justify True


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