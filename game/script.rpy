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



label custom_backstory_label:
    "Enter your own backstory for this character. You can also navigate to \"game/assets/prompts/prompt_templates.json\" and edit the \"content\" section manually."
    $ raw_prompt = Info().getExamplePrompts[character_name][0]["content"].split("{{format}}")[0].replace("BACKSTORY", "")
    $ player_prompt = renpy.input(prompt=" ", default=f"{raw_prompt}", exclude="}{", screen="input_long").strip()
    
    $ Configs().update_character_backstory(character=character_name, backstory=player_prompt)
    "Successfully changed backstory!"
    return




label start:

    init python:
        import threading
        config.has_autosave = False
        config.has_quicksave = False
        config.autosave_on_quit = False
        config.autosave_on_choice = False

        def string_splitter(str, length):
            # A simple regex pattern to split text into sentences
            sentence_endings = re.compile(r'(?<=[.!?]) +')
            sentences = sentence_endings.split(str)

            wrapped_sentences = []
            current_part = ''

            for sentence in sentences:
                # Check if adding the current sentence would exceed the length
                if len(current_part) + len(sentence) < length:
                    current_part += sentence + ' '
                else:
                    # If current part is not empty, add it to wrapped sentences
                    if current_part:
                        wrapped_sentences.append(current_part.strip())
                    # Start a new part
                    current_part = sentence + ' '

            # Add any remaining text to the wrapped sentences
            if current_part.strip():
                wrapped_sentences.append(current_part.strip())

            wrapped_sentences.reverse()
            return wrapped_sentences

    $ input_popup_gui = True

    stop music fadeout 0.5

    if persistent.purgatory == True:
        jump space_zone
    else:
        call screen bio_screen
        

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

        # Start generating text in a separate thread
        $ chatSetup.is_generating = True
        $ threading.Thread(target=chatSetup.chat, args=(pathSetup, [], "hello")).start()

        $ _history = False
        $ wait_msg = ""

        # Wait for AI to finish generating text
        while chatSetup.is_generating == True:
            # If you want to add a popup menu or some sort of animation, you can do so here
            $ wait_msg = wait_msg + "." if len(wait_msg) < 3 else "."
            "Loading[wait_msg] {fast} {w=0.7}{nw}"

        $ _history = True

        $ renpy.log(">>> starting new ")
        $ convo = chatSetup.generated_text



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


    # If the background is a default DDLC image then use images.rpa, otherwise use the custom path
    if current_background in ["bedroom.png", "club.png", "class.png", "closet.png", "corridor.png", "house.png", "kitchen.png", "sayori_bedroom.png", "residential.png"]:
        image _bg:
            im.Composite((1280, 720), (0, 0), f"bg/{current_background}")
        scene _bg
    else:
        image custom_bg:
            im.Composite((1280, 720), (0, 0), f"assets/imgs/bg/{current_background}")
        scene custom_bg


    # If the character is a default DDLC sprite then use images.rpa, otherwise use the custom path
    if current_char in ["monika", "sayori", "natsuki", "yuri"]:
        image basic:
            im.Composite((960, 960), (0, 0), f"{current_char}/{current_left}", (0, 0), f"{current_char}/{current_right}", (0, 0), f"{current_char}/{current_head}")
            uppies
        image full_sprite:
            im.Composite((960, 960), (0, 0), f"{current_char}/{current_head}")
            uppies

    else:
        image custom_basic:
            im.Composite((960, 960), (0, 0), f"assets/imgs/characters/{current_char_title}/{current_left}", (0, 0), f"assets/imgs/characters/{current_char_title}/{current_right}", (0, 0), f"assets/imgs/characters/{current_char_title}/{current_head}")
            uppies
        image custom_full_sprite:
            im.Composite((960, 960), (0, 0), f"assets/imgs/characters/{current_char_title}/{current_head}")
            uppies





    if current_char in ["monika", "sayori", "natsuki", "yuri"]:
        if Info().full_sprites_check(current_char_title, current_head) != True:
            hide full_sprite
            show basic at t11
        else:
            hide basic
            show full_sprite at t11
    else:
        if Info().full_sprites_check(current_char_title, current_head) != True:
            hide custom_full_sprite
            show custom_basic at t11
        else:
            hide custom_basic
            show custom_full_sprite at t11
        


    if resume:
        $ last_msg = Data(path_to_user_dir=pathSetup).getLastMessageClean
        $ messages = string_splitter(last_msg, 255)

        while messages:
            $ message = messages.pop()
            if len(messages) > 0:
                $ message += '...'
            $ renpy.say("[current_char_title]", message)
    else:
        $ renpy.say("[current_char_title]", convo)


    show screen home_icon_screen
    
    ###########################
    # Main Event Loop
    ###########################
    $ main_event_loop = True
    while main_event_loop == True:
        $ user_msg = ""
        $ rnd_continue = renpy.random.randint(1, 6)
        $ current_char = Data(path_to_user_dir=pathSetup).getSceneData("character")

        if current_char != "" and rnd_continue == 4:
            # Randomly continue the chat to have variety so it's not a constant back and forth
            $ user_msg = "continue"
        else:
            while user_msg.strip() == "":
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


        if final_msg.startswith("<Error>"):
            show screen error_popup(message=final_msg)
        else:


            # If the background is a default DDLC image then use images.rpa, otherwise use the custom path
            if current_background in ["bedroom.png", "club.png", "class.png", "closet.png", "corridor.png", "house.png", "kitchen.png", "sayori_bedroom.png", "residential.png"]:
                image _bg:
                    im.Composite((1280, 720), (0, 0), f"bg/{current_background}")
                scene _bg
            else:
                image custom_bg:
                    im.Composite((1280, 720), (0, 0), f"assets/imgs/bg/{current_background}")
                scene custom_bg


            # If the character is a default DDLC sprite then use images.rpa, otherwise use the custom path
            if current_char in ["monika", "sayori", "natsuki", "yuri"]:
                image basic:
                    im.Composite((960, 960), (0, 0), f"{current_char}/{current_left}", (0, 0), f"{current_char}/{current_right}", (0, 0), f"{current_char}/{current_head}")
                    uppies
                image full_sprite:
                    im.Composite((960, 960), (0, 0), f"{current_char}/{current_head}")
                    uppies
                
            else:
                image custom_basic:
                    im.Composite((960, 960), (0, 0), f"assets/imgs/characters/{current_char_title}/{current_left}", (0, 0), f"assets/imgs/characters/{current_char_title}/{current_right}", (0, 0), f"assets/imgs/characters/{current_char_title}/{current_head}")
                    uppies
                image custom_full_sprite:
                    im.Composite((960, 960), (0, 0), f"assets/imgs/characters/{current_char_title}/{current_head}")
                    uppies



            if current_char in ["monika", "sayori", "natsuki", "yuri"]:
                if Info().full_sprites_check(current_char_title, current_head) != True:
                    hide full_sprite
                    show basic at t11
                else:
                    hide basic
                    show full_sprite at t11
            else:
                if Info().full_sprites_check(current_char_title, current_head) != True:
                    hide custom_full_sprite
                    show custom_basic at t11
                else:
                    hide custom_basic
                    show custom_full_sprite at t11

            $ messages = string_splitter(final_msg, 255)

            while messages:
                $ message = messages.pop()
                if len(messages) > 0:
                    $ message += '...'
                $ renpy.say("[current_char_title]", message)

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