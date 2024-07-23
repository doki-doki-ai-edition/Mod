# Add character sprite

**When adding a new character do the following**


- add new folder w/ sprites at `game\assets\imgs\characters`
- add new name to `game\assets\configs\custom_characters`
- add new name to `game\assets\prompts\custom_prompts`



### New folder

- Create a new folder in `game\assets\imgs\characters`
- The name of the folder should be the name of your character (Make sure the first letter is capitalized)

<img src="game/assets/imgs/help_page/folder name.png">

- Fill the folder with character sprites
- The images should ideally be 960x960

<img src="game/assets/imgs/help_page/custom char sprites.png">

### character.json

- Go to `game\assets\configs\custom_characters`
- Make a `.json` file with the title of your character. In my case it's "sam"

<img src="game/assets/imgs/help_page/sam folder json.png">

- Copy this template (replace "Sam" with your own character name)


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
            "explain": "",
            "relaxed": ""
        },
        "right": {
            "explain": "",
            "relaxed": ""
        },
        "bio": "",
        "image": "",
        "logo": "assets/imgs/gui/logo.png",
        "chibi": null,
        "chibi_hover": null
    }
```

Make sure the name is capitalized. For example, notice how it's "Sam" and not "sam".

Now replace the default emotions in the "head" section with the ones you actually want your character to display.

The emotions that you see ending with `.png` is the character sprites we added in 
`game\assets\imgs\characters\Sam`



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
            "explain": "",
            "relaxed": ""
        },
        "right": {
            "explain": "",
            "relaxed": ""
        },
        "bio": "",
        "image": "",
        "logo": "assets/imgs/gui/logo.png",
        "chibi": null,
        "chibi_hover": null
    }
```


In the "left" and "right" section just add any `.png` in your character sprite folder, it doesn't matter.


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

You should be done with this section now! The whole file should look like this now.

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


### Custom Prompts

- go to `game\assets\prompts\custom_prompts`
- Add the name of the character you want

<img src="game/assets/imgs/help_page/folder char name.png">

- Create a format that looks like this (with your own backstory)

```json

{
    "sam": [
        {
            "role": "system",
            "content": "BACKSTORY \nSam is a college student that majors in art. He hates Monika with a passion and is constantly angry about being trapped in this world. {{format}}"
        }
    ]
}
```

- Make sure the **name** of your character is all **lowercased.** And make sure that at the end of your BACKSTORY you have `{{format}}`




# Add Default Backgrounds

**When adding a new background do the following**

- add new background image in `game\assets\imgs\bg`
- add new background name in `game\assets\configs`

Once you've added the images you want in `game\assets\imgs\bg`

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