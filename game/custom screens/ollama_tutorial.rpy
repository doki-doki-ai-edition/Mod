init -10 python:
    import json

    class OllamaImages:
        def __init__(self, image, desc):
            self.image = image
            self.desc = desc


    def image_list():
        dir_path = config.basedir + "/game/assets/configs/tutorials.json"
        img_list = []

        with open(dir_path, "r") as f:
            tutorial = json.load(f)
        
        for num, value in enumerate(tutorial["ollama"]):
            img_list.append(OllamaImages(value["image"], value["desc"]))

        return img_list


# Example character data
define images = image_list()

default index = 0
default current_image = images[index]



init -5 python:
    def update_image(new_index):
        store.index = new_index
        store.current_image = images[new_index]


screen tutorial_screen:
    tag menu
    add "menu_bg"



    # Main Image and arrows underneath
    vbox:
        xalign 0.4 yalign 0.5
        add current_image.image xalign 0.0 yalign 0.6 zoom 0.75

        # Nav buttons
        hbox:
            style_prefix "arrows"

            xalign 0.5
            yalign 0.97
            spacing 20

            textbutton "<" action If(
                index > 0, 
                true=Function(update_image, index - 1), 
                false=Function(update_image, len(images) - 1)
            )

            text "Page [index]" style "character_name_style"

            textbutton ">" action If(
                index < len(images) - 1, 
                true=Function(update_image, index + 1), 
                false=Function(update_image, 0)
            )



    null width 30

    # Description section
    frame:
        background "assets/imgs/gui/bio_box.png"
        xalign 1
        yalign 0.4
        padding (790, 130, 160, 220)

        # Image info
        vbox:
            xfill True
            box_wrap True
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                text "[current_image.desc]" size 22 justify True




    textbutton _("Return"):
        style "return_button"

        action Return()

