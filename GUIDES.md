# Change character sprite

**When adding a new character do the following**


- add new folder w/ sprites
- add new name to characters.json
- add new name to prompt_templates.json



### New folder

- Create a new folder in `game\assets\imgs\characters`
- The name of the folder should be the name of your character (Make sure the first letter is capitalized)

<img src="game/assets/imgs/help_page/folder name.png">

- Fill the folder with character sprites
- The images should ideally be 960x960

<img src="game/assets/imgs/help_page/custom char sprites.png">

### character.json

- go to `game\assets\configs\characters.json`
- Copy Yuri's template (the last thing in the file) and paste it in a separate line
- Rename it to the character you want

<img src="game/assets/imgs/help_page/char json.png">

Make sure you add a COMMA after the bracket above the character u just added

<img src="game/assets/imgs/help_page/char json comma.png">


Now replace the default emotions in the "head" section with the ones you actually want your character to display.

The emotions that don't end in `.png` is what the AI will see.
Just add the .png sprites you have in your characters folder.

```json

    "Sam":{
        "full_sprites": [],
        "head": {
            "angry": "angry.png",
            "determined": "determined.png",
            "glad": "glad.png",
            "happy": "happy.png",
            "laugh": "laugh.png",
            "nervous": "nervous.png",
            "neutral": "neutral.png",
            "really angry": "really angry.png",
            "really happy": "really happy.png",
            "sad": "sad.png",
            "surprised": "surprised.png"
        },
        "left": {
            "explain": "2l.png",
            "relaxed": "1l.png"
        },
        "right": {
            "explain": "2r.png",
            "relaxed": "1r.png"
        },
        "bio": "When she's not buried in the world of books, Yuri shyly brings an air of serenity to wherever she goes, sometimes accompanied by a hot cup of tea. Trust in her eyes goes a long way, so be sure to never break hers.\n\nHeight: 5'5'' / 165.1cm\nWeight: 130lbs / 59kg\nEye Color: Purple\nEthnicity: Japan",
        "image": "gui/menu_art_y.png",
        "logo": "assets/imgs/gui/logo.png",
        "chibi": "gui/poemgame/y_sticker_1.png",
        "chibi_hover": "gui/poemgame/y_sticker_2.png"
    }
```

If your sprites are just 1 image combined together then add all of the emotions in "head" into `full_sprites` as well.

```json
    "Sam":{
        "full_sprites": [
            "angry",
            "determined",
            "glad",
            "happy",
            "laugh",
            "nervous",
            "neutral",
            "really angry",
            "really happy",
            "sad",
            "surprised"
        ],
        "head": {
            "angry": "angry.png",
            "determined": "determined.png",
            "glad": "glad.png",
            "happy": "happy.png",
            "laugh": "laugh.png",
            "nervous": "nervous.png",
            "neutral": "neutral.png",
            "really angry": "really angry.png",
            "really happy": "really happy.png",
            "sad": "sad.png",
            "surprised": "surprised.png"
        },
        "left": {
            "explain": "2l.png",
            "relaxed": "1l.png"
        },
        "right": {
            "explain": "2r.png",
            "relaxed": "1r.png"
        },
        "bio": "When she's not buried in the world of books, Yuri shyly brings an air of serenity to wherever she goes, sometimes accompanied by a hot cup of tea. Trust in her eyes goes a long way, so be sure to never break hers.\n\nHeight: 5'5'' / 165.1cm\nWeight: 130lbs / 59kg\nEye Color: Purple\nEthnicity: Japan",
        "image": "gui/menu_art_y.png",
        "logo": "assets/imgs/gui/logo.png",
        "chibi": "gui/poemgame/y_sticker_1.png",
        "chibi_hover": "gui/poemgame/y_sticker_2.png"
    }
```


In the "left" and "right" section just change the `.png` to any `.png` in your character sprite folder, it doesn't matter.


```json
        "left": {
            "explain": "surprised.png",
            "relaxed": "surprised.png"
        },
        "right": {
            "explain": "surprised.png",
            "relaxed": "surprised.png"
        },
```

Now change the "bio" section to actually give info of who your character is


```json
        "bio": "Sam is a college student that majors in art. He hates Monika with a passion and is constantly angry about being trapped in this world",
```

The "image" section will be what's displayed when you go to select a character. You can simply put in one of the sprites in your characters folder if you don't have a custom image.

<img src="game/assets/imgs/help_page/char select image.png">


Put the path to your image file. Eg. In my case it will be this

```json
"image": "assets/imgs/characters/Sam/angry.png",
```


The "chibi" and "chibi_hover" should be set as `null` unless you have a chibi version of the sprite you want to use.

```json
    "chibi": null,
    "chibi_hover": null
```

You should be done with this section now! The whole thing should look like this now.

```json

    "Sam":{
        "full_sprites": [
            "angry",
            "determined",
            "glad",
            "happy",
            "laugh",
            "nervous",
            "neutral",
            "really angry",
            "really happy",
            "sad",
            "surprised"
        ],
        "head": {
            "angry": "angry.png",
            "determined": "determined.png",
            "glad": "glad.png",
            "happy": "happy.png",
            "laugh": "laugh.png",
            "nervous": "nervous.png",
            "neutral": "neutral.png",
            "really angry": "really angry.png",
            "really happy": "really happy.png",
            "sad": "sad.png",
            "surprised": "surprised.png"
        },
        "left": {
            "explain": "surprised.png",
            "relaxed": "surprised.png"
        },
        "right": {
            "explain": "surprised.png",
            "relaxed": "surprised.png"
        },
        "bio": "Sam is a college student that majors in art. He hates Monika with a passion and is constantly angry about being trapped in this world",
        "image": "assets/imgs/characters/Sam/angry.png",
        "logo": "assets/imgs/gui/logo.png",
        "chibi": null,
        "chibi_hover": null
    }
```


### prompt_template.json

- go to `game\assets\prompts\prompt_templates.json`
- Add the name of the character you want
- Reference the structure you see in the file.
- Add background information about your character
- Make sure at the end of your message, you have "{{format}}" just like the other things in the file.



# Default Backgrounds

**When adding a new background do the following**

- add new background image in `game\images\bg`
- add new background name in `game\assets\configs`

Once you've added the images you want in `game\images\bg`

- go to `game\assets\configs`
- remove the default background images (if you want, you don't have to)
- add the name of your background image in the "default" dictionary.

eg. I want to add a "park" as a default background.

The name of my background image is "park-day-1.png" so this is how I'd write it in the json

```json
    "default": {
        "park": "park-day-1.png",
    }
```

You'll notice that there's another key in the json called "checks".
Everything inside "checks" is a backup just incase the AI doesn't correctly spell something correctly.

For example, all the default backgrounds are injected into the system prompt by default and we display a scene by using 1 of those injected scenes
but what if the AI "hallucinates" and doesn't correctly spell the default scene correctly?

"checks" is used as a potential typo that the AI may make so that it falls back onto the correct scene.

so for example

```json
    "checks": {
        "parks": "park-day-1.png"
    }
```

maybe instead of the ai returning "park" like we instructed, it returns "parks". This check here ensures that we get the appropriate scene and not something else.