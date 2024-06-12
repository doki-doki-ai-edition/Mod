


define config.name = "Doki Doki AI Edition"





define gui.show_name = False




define config.version = "0.1.0"





define gui.about = _("")






define build.name = "DDAE"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.debug_sound = True













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 1
















define config.save_directory = "DDAE-1454445547"







define config.window_icon = "assets/imgs/gui/window_icon.png"



define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## The following variables take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##  * matches all characters, except the directory separator.
    ##  ** matches all characters, including the directory separator.
    ##
    ## Examples:
    ##  "*.txt" matches txt files in the base directory.
    ##  "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories.
    ##  "**.psd" matches psd files anywhere in the project.

    # These variables declare the packages to build your mod that is Team Salvato
    # IPG compliant. Do not mess with these variables whatsoever.
    if renpy.version_tuple == (6, 99, 12, 4, 2187):
        build.package(build.directory_name + "Mod", 'zip', 'mod', description="Ren'Py 6 DDLC Compliant Mod")
    else:
        build.package(build.directory_name + "Renpy7Mod", 'zip', 'windows linux mac renpy mod',
        description="Ren'Py 7 DDLC Compliant Mod")

    # These variables declare the archives that will be made to your packaged mod.
    # To add another archive, make a build.archive variable like in this example:
    build.archive("scripts", 'mod')
    build.archive("assets", 'mod')

    # Do not touch these lines. This is so Ren'Py can add your mods' py file
    # and a special launcher for Linux and macOS to run your mod. 
    build.renpy_patterns.remove(('renpy.py', ['all']))
    build.classify_renpy("renpy.py", "renpy all")
    
    build.early_base_patterns.remove(('*.sh', None))
    build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
    build.classify("*.sh", None)
    
    #############################################################
    # These variables classify packages for PC and Android platforms.
    # Make sure to add 'all' to your build.classify variable if you are planning
    # to build your mod on Android like in this example.
    #   Example: build.classify("game/**.pdf", "scripts all")
    build.classify("game/assets/**", "assets all")
    build.classify("game/presplash.png", "scripts all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.md", None)
    build.classify("game/**/README.md", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") ## Backwards Compatibility
    build.classify("game/tl/**", "scripts all") ## Translation Folder
    build.classify("game/mod_extras/**.rpyc", "scripts") ## Extra Features (Backwards Compatibility)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')
    build.classify('README.linux', 'linux')
   
    # This sets' README.html as documentation
    build.documentation('README.html')

    build.include_old_themes = False



