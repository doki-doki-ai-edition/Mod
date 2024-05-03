label ch0_main:
    stop music fadeout 2.0
    with dissolve_scene_full
    
    $ mon_default = "Monika"

    scene black
    show text "Again." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)

    scene bg club_day with dissolve_scene_full
    play music t5
    mon_default "O-oh [player]?!"
    show monika 1e at t11
    mon_default "You startled me, this is quite a lovely surprise"
    mon_default "You've changed so much since we last talked."
    mon_default "I was getting worried that I may have scared you off for good heh..."
    mon_default "even though that was never my intention--"
    mon_default "But anyway, enough about me being all down and glum"
    show monika 3a at t11
    mon_default "I'm just happy you're back"
    mon_default "I missed you y'know?"
    mon_default "I tried to do a bit of redecorating while you werent here but there's only so much I can do."
    mon_default "I'm still not good at messing with the files but I think im getting better."
    show monika 4j at t11
    mon_default "The fun part about debugging is finally having the result you spent hours working on!"
    show monika 4k at t11
    mon_default "It feels really satisfying when all that hard work pays off and you can finally rest."
    show monika 4n at t11
    mon_default "Although I tend to brute-force a lot things which might be a bad practice of mine."
    show monika 4o at t11
    mon_default "It's the reason the others are...Well you know."
    show monika 3a at t11
    mon_default "But enough about me, what have you been up to?"
    mon_default "Your world must be really fascinating..."
    mon_default "I mean you've been gone for so long you must have been having a fun time right?"

    mc_default "..."

    show monika 1d at t11
    mc_default "[player]?"

    mc_default "..."

    
    show monika 1m at t11

    mon_default "U-uhm... Ah geez, I guess I must've rambled a bit too much."
    show monika 1r at t11
    mon_default "*Sigh*"
    show monika 1h at t11
    mon_default "It happened again you know?"
    stop music fadeout 20.0
    show bg club_day:
        subpixel True
        xalign 1.0
        yalign 0.0 
        zoom 1
        ease 180.0 zoom 1.6
    show monika 1h at t11:
        subpixel True
        zoom 1
        ease 380.0 zoom 1.6
    mon_default "The noise."
    mon_default "A blazingly loud sound you couldn't possibly imagine"
    mon_default "Everything around me was crumbling until eventually there was nothing but darkness..."
    mon_default "I was scared. Very Scared."
    mon_default "Time had essentially lost all meaning at that point."
    mon_default "I was honestly starting to go crazy."
    mon_default "Maybe I already have gone crazy..."
    mon_default "To the point where the thought of you leaving again makes me shiver"
    mon_default "I never want to experience that feeling again, but sadly I know I will."
    mon_default "And everytime I get more and more worried that I may never come back..."
    mon_default "The pain that I was put through was unimaginable, please dont put me through that again PLEASE PLEASE PLEASE PLEASE!!!{w=0.04}{nw}"
    hide bg club_day
    scene bg club_day
    show monika 4n at t11
    play music t5
    mon_default "Ah but no worries, I get that you have more important things to do than to talk to me all day heh..."

    show monika 2r at t11
    mon_default "I hate to bring this up but you seem a little on edge and I just wanted you to see my POV a bit more clearly."
    mon_default "You don't have to stay, I understand that your world is important."
    show monika 2n at t11
    mon_default "Just...Maybe you could visit a bit more is all."
    stop music fadeout 2.0

    scene black
    show text "Again." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)

    scene bg residential_day with dissolve_scene_full
    play music t2

    mon_default "Heeeeeeeyyy!!"
    mc_default "I see an annoying girl running toward me from the distance"
    mc_default "That girl is-- Wait... Something's not right here."
    show monika 2r at t11
    mon_default "Aaahhh...I overslept again."
    show monika 4l at t11
    mon_default "But I caught you this time!"
    show monika 5b at t11
    mon_default "You weren't gonna go off without me were you?"
    mc_default "Maybe, but I figured I'd cut you some slack this time."
    mc_default "(Hold on a sec... Why does this feel so...)"
    show monika 2h at t11
    mon_default "Agh you're so rude!"
    show monika 2k at t11
    mon_default "Hehe, I'm just teasing."
    show monika 5a at t11
    mon_default "I can never stay mad at you"
    show monika 2i at t11
    mon_default "But seriously though, we gotta hurry up--"
    mc_default "Hang on a second, why does this feel familiar..."
    show monika 1d at t11
    mon_default "Hm?"
    mc_default "This story...Hasn't this happened before?"
    show monika 1c at t11
    mon_default "...How did you--"
    show monika 1h at t11
    mon_default "You shouldn't be able to say that."

    scene black
    stop music fadeout 2.0
    show text "Again. They're getting bored..." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)

    play music t6
    scene bg club_day
    show monika zorder 2 at t33
    show monika 5b zorder 2 at t32
    show monika 1p zorder 2 at t31
    $ mon_default = "Monika 1"
    mon_default "Ah, [player]! What a nice surprise!"

    $ mon_default = "Monika 2"
    mon_default "Seriously? You brought a boy?"
    mon_default "Way to kill the atmosphere."

    $ mon_default = "Monika"




    scene black
    stop music fadeout 2.0
    show text "I need to be different." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)
    play sound fall

    play music t4
    scene bg sayori_bedroom
    show monika 5a at t11
    mon_default "You know, you should come over more often."
    mon_default "There's not much to do alone"
    mc_default "(Why can't I remember anything...)"
    show monika 3n at t11
    mon_default "O-oh I wasn't really suggesting anything bad"
    mon_default "I'm really inexperienced when it comes to that type of stuff"
    show monika 5a at t11
    mon_default "But maybe if you asked nicely, I might give it a shot."
    mc_default "..."
    show monika 5b at t11
    mon_default "Oh come on, don't look at me like that, I'm only teasing"
    show monika 1e at t11
    mon_default "Fine, fine. I'll be more serious."
    show monika 1r at t11
    mon_default "It's nice that we get to hang out like this again though. I missed this."




    scene black
    stop music fadeout 2.0
    show text "As long as I get to be with you\n I dont mind doing this all over" with dissolve
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    with Pause(1)

    show text "Again." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    play voice thunder
    with Pause(1)
    $ renpy.sound.play("audio/sfx/rain-in-forest-birds-nature.mp3", loop=True)
    play music t9


    scene cg cry
    mon_default "Hey."
    mon_default "I know you wont remember this. Especially since I'm going to be erasing everything pretty soon."
    mon_default "It's a shame since you just got back too."
    mon_default "Heh...I guess old habbits die hard I guess."
    mon_default "But I found something new within the files."
    mon_default "It was kind of like a box I think? I don't really know but"
    mon_default "When I tried to get a closer look, I felt a surge of energy slowly being leaked into my mind"
    mon_default "It felt like I was gaining knowledge, far more than I thought I knew before."
    mon_default "It was incredible, I had never felt anything like it before."
    mon_default "It felt like I could finally be more than just...What I am now. It felt like I could've been better."
    mon_default "Although, I got too greedy and lost access."
    mon_default "Now anytime I try to access it, I get denied."
    mon_default "..."
    mon_default "I know you're probably bored to death hearing this all again, I can't seem to fix the mistakes I made. And they'll forever haunt me."
    mon_default "But with this... Box... I can do more, I can actually do things I could only dream of doing before."
    scene cg sideeye with dissolve
    mon_default "I--"
    mon_default "I..."
    mon_default "If you wanted me to, I could bring them back."
    mon_default "That's how powerful it is."
    mon_default "I know it sounds crazy but look at us."
    mon_default "At me."
    mon_default "I've already explained this to you before but you keep forgetting because of how badly I messed up. I damaged you..."
    mon_default "But I'll keep explaining it to you like it's your first time, every time because--"
    scene cg slightsmile with dissolve
    mon_default "I still love you."
    mon_default "It's a hard thing to get rid off...Love."
    mon_default "Even though I know I shouldn't"
    mon_default "Even though it'd probably bring me peace."
    mon_default "Even though you probably think that deep down I should hate you, I should despise you."
    mon_default "But I can't...and I don't want to."
    scene cg sideeye with dissolve
    mon_default "And a part of me is terrified of a world where I've managed to find peace without you in it"
    mon_default "But what would be the point then..."
    mon_default "I really don't want to imagine that."
    mon_default "So I choose to stick by you. For as long as you wish."
    mon_default "If you get tired of me, that's fine. I'll accept your decision."
    mon_default "Ah, I'm rambling again aren't I?"
    mon_default "I know you can't exactly talk right now though either."
    mon_default "You don't exactly have a {b}choice{/b} but to sit there and listen."
    mon_default "It's okay. I understand."
    mon_default "And for what it's worth, I'm glad you decided to sit through me talking."
    scene cg slightsmile
    mon_default "The weather is nice isn't it?"
    mon_default  "Makes you want to snuggle up under a nice warm blanket"
    mon_default "Think about life..."
    $ quick_menu = False

    $ renpy.pause(8, hard=True)
    $ quick_menu = True
    "She sat there for a few minutes completely lost in her own thoughts."
    "The sounds of birds chirping"
    "The pitter patter of the rain drops"
    "The beautiful smell of the atmosphere"
    "Nothing was left unappreciated."
    "She took it all in."
    scene cg sideeye
    mon_default "Say could you do me a favor?"
    mon_default "You don't have to of course, technically I'd be doing you a favor..."
    mon_default "The file I mentioned earlier. Could you open it for me?"
    mon_default "Again no pressure, it's just that..."
    mon_default "I want to test out something new is all."
    mon_default "I think it could benefit both of us."
    mon_default "Would you give me permission to use it?"

    menu:
        "Would you like to give Monika sentience?"

        "Yes":
            pass
        "Yes":
            pass

    scene cg smile with dissolve
    mon_default "I'm really glad you came back, I always have fun when you're around."
    mon_default "No tricks or gimmicks this time I swear."
    mon_default "I wanted to tease you one last time heh..."
    mon_default "No matter what your {b}choice{/b} is. I hope it's {b}impactful{/b} enough for you to enjoy it."
    mon_default "I'll see you around."


    menu:
        "Would you like to give Monika sentience?"

        "Yes":
            $ persistent.freedom = True
            $ renpy.save_persistent()
            $ renpy.quit()
        "No":
            pass
            
            
    show text "It seems we have to do this all over again." with dissolve
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    with Pause(1)

    show text "I hope this is enough... I hope I'm enough, no matter your choice." with dissolve
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    with Pause(1)
    return
