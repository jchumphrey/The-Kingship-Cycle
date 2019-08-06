#Ch 4 part 4
label WoodlandTrek:
    $ renpy.fix_rollback()
    stop music fadeout 1.0
    play music "music/Autumn_Forest.ogg" fadein 1.0
    scene bg latewoods
    with fade
    play sound "sound/forestWalk.ogg"
    #Walking back, with who changes depending on the kid. You won't reach intended destination
    "Your companions and you walk through the forest slowly, the growing darkness surrounding you all."
    "Night is close and you're on the right track to get home before the dark falls totally."
    "But your mind is heavy."
    if faekid == 1:
        "The faery kid and [fp] gone, heading for the mound, you can't help feel uneasy about the forest again."
        "You trust Cait to get the task done, but it may be a few days until she returns."
        "It's just her relationship with the inhuman things."
    elif faekid == 2:
        "You glance over towards the faery kid and Cait, following along behind. The child was asleep in her arms, still that antlered rabbit that started this."
        "Was it the right choice to go along to the fae mound? Fae were as dangerous as they were capricous."
        "Who knows if you'd even come back on the same day, or the same species."
    elif faekid == 3:
        "Bringing this faery kid home could be dangerous. While he wouldn't be dangerous alone, his family could be."
        "Hopefully they appreciated the gesture of protecting him."
        "Otherwise, your town might be reduced to nothing."
    elif faekid == 4:
        "You felt Caitlin would double back to find this child and help him in the end. Ultimately, it would be her choice."
        "But you had just felt something wrong about this kid. You couldn't let any of your people stay near him."
        "Something in his eyes, and the fact he was pure fae."
    "Something feels wrong about tonight to you."
    "Fae aren't normally this far out into the woods, and the air feels off. You aren't normally that attentive to signs, but the woods atmosphere is utterly different than normal."
    "Today feels like the sort of day in which something will change."
    "But you can't tell what."
    "Your eye is momentarily drawn to a pitch-black raven resting on a tree branch, watching you with interest. You are about to turn to inspect it in return, but are pulled away by a hand touching your shoulder."
    "Séan, your loyal friend, notices your unease, and lays a hand on your shoulder."
    show sean with dissolve
    sean "Once we get home, I think tonight will end find. This faery kid has just rattled us."
    "You nod, and soldier in with your friends in tow. The raven is gone from its perch, so you assume it must just be a bird that has yet to find its nest for the night."
    "Your mind turns inward again."
    "This geas you woke up to, your mind can't let it go."
    "Is it relating to just today, or some unknowable future event? You will learn by the end of the day, you suppose."
    sean "[heir], is that the huntsman Liam ahead?"
    "You squint at the coming crossroads and nod in affirmation."
    tan "Aye, though I'm not sure what he's looking at."
    show liam at right
    show nora at left
    with dissolve
    #If you lack Nora, you and she meet up at a fork, with liam
    #if Nora is with you, You meet Liam.
    if C_nora == False:
        ## She joins fiann at the end of this section. You offer to head for town with them.
        tan "Not just Liam, but [nora]. Good eye, Séan. Let's go see what they're up to."
        tan "Hail, Liam! [nora]!"
        "Nora is the only one who turns, only to gesture for you to be quiet. You're confused but comply and share the message with your group."
    else:
        nora "That is indeed my master. I wonder how he's gotten ahead of us."
        tan "Hail, Liam! What brings-"
        "Nora lays a hand on your arm as you raise it and your voice in greeting. Liam had gestured for quiet and beckoned you forward."
    "Puzzled, you move forward. The two are huddled around a deer with an arrow in its neck. But not of familiar make. The arrows are pure black like a raven's,"
    "Not a material used in your tuath. No ravens were killed lest it be the Morrígan, the Phantom Queen of Death."
    tan "What's this? Poachers?"
    liam "Must be. Or something else. They didn't take the carcass, save its antlers."
    "Indeed, the beast's skull had been smashed to lose what must have been antlers from this buck. What an odd thing."
    nora "And there's lacerations across the body. . ."
    sean "White Christ and Black Bird, it looks the work of a wolf, not a man, but that's the bite of iron, not ivory."
    "You grimace. Someone, potentially a hostile someone, is in the woods with you. You felt so since the initial encounter with the fae child. And here is the truth."

    if C_nora == False:
        tan "Nora, Liam. You're coming back with us. It's about time for us to return."
        "You leave out your worries over not being alone in the twilight woods, but Liam's gaze tells you what everything you need. He has the same thoughts."
        liam "We will. Come Nora, there's to be no delay."
        "She nods, and winks at you, before her face turns into a frown again and she stares at the corpse."
        show text "{b}{color=#FFFFFF}[nora] has joined your fiann, improving your finesse and seanchas!{/color}{/b}" at truecenter
        with dissolve

        $ Finesse += 2
        $ Seanchas += 1
        if renpy.in_rollback():
            $ C_nora = False
        else :
            $ C_nora = True

        pause 1.5
        hide text
        with dissolve
    else:
        tan "Liam, come with us back to the fort. There's something up in the woods tonight."
        liam "Astute. I will come. Evil stalks the woods."
        "Evil, not a word used lightly. You nod with respect at the older hunter."
        tan "Let's be on our way."
    liam "Wait."
    "He holds up a hand, summoning the quiet again as he sniffs around and peers through the dusk."
    liam "Someone is near."
    "[nora] glances around, sniffing at the air and frowning as well, as you strain your ears and eyes in the low light."
    #He's suspicious, says something seems to be up in the woods.
    #You try to look yourself, tough challenge of Finesse or seanchas

    $d20Roll = renpy.random.randint(1,20)
    $difficulty = 12
    if d20Roll+(Seanchas/3) >= difficulty or d20Roll+(Finesse/3) >= difficulty:
        play sound "sound/success.mp3"
        #Gasp, enemies. They aren't wearing any crest or insignia, who the hell are they? They seem mixed Norse and Gael and foreign too!
        #Liam gets you all into cover up in the top of the nearby hill
        "And there they were. Red and black war-paint through the trees in both stark runes and the lines of your ancestors. An odd mix of protection magic."
        "Animal and human teeth clatter on necklaces and antlers stand proud from their helmets. They moved in quiet, with purpose, towards your home."
        "They haven't noticed the cluster of people at the crossroads yet."
        liam "Quick, up the hill."
        "He ushers you out of the open and up a nearby hill with good visibility over the nearby forest."
        "Nora and [sean] bound after him, with you on their heels."
        if C_aoife == True:
            "Aoife grunts, ducking low as she follows along. She did cut an imposing and noticeable figure, after all."
        elif C_niall == True:
            "Niall sighs, mumbles about 'more running after a tiring day' but follows after as quick as the oak of a man can manage."
        jump noticedWarriors
    else:
        play sound "sound/fail.ogg"
        #Don't notice shit. You continue, only to be waylaid at the last hill before leaving the forest by mysterious warriors.
        "Minutes pass, and you see nothing. You frown. You are certain you had felt someone watching you too, but there's no one."
        "Are your instincts wrong on this one? Are Liam's?"
        "You sigh and give Liam a pat on the shoulder."
        tan "I don't see anything. We should get going home regardless. It's late."
        "He frowns, and nods, before standing up and stretching out his legs."
        liam "Must have just heard something. Lead the way."
        "You lead your group of companions onward, continuing towards Cnoc bhFianna and home."
        "The dark only grows as you continue, leading Séan to light a torch that he procured from somewhere, to light the path."
        jump ambushed

label ambushed:
    stop music fadeout 1.0
    play music "music/Fateful_Reunion.ogg" fadein 1.0
    scene bg latewoods
    show sean at left
    show liam at right
    with fade
    "A polearm flashes out of a nearby bush as you walk, and the ground comes rushing up to meet your face. You wheeze, winded on the ground."
    sean "Shit! ambush!"
    "He dashes for you, pulling you up and out of the way as the spear stabs down where you just were."
    "From the bushes, four rough-dressed men step out, one with spear and all cackling meanly."
    "Raider""Darn. Guess I missed. Won't miss again, meat."
    "He tosses the spear to a compatriot, eyeing you up eagerly. There's a hunger in those eyes that deeply unsettle you."
    "Now that you're on your feet, you appraise your attackers."
    "They wear red and black warpaint in both stark runes and the lines of your ancestors. An odd mix of protection magic."
    "Animal and human teeth clatter on necklaces and antlers stand proud from their helmets. They appear utterly savage, like something out of a long-forgotten past."
    liam "I don't recognize any tuath insignia on them."
    "Raider""Nope! We're freemen, through and through. And soon you'll be dead men!"
    "Your companions prepare their weapons. Apparently, the raiders weren't too plussed about this being a tough fight, or they could have killed you from hiding."
    hide sean
    hide liam
    with dissolve
    "The leader faces you, wild, red-rimmed eyes watching you with murderous intent."
    if faekid == 2 or faekid == 3:
        "Though, during the sudden confusion, you thankfully see the non-warrior [fp] slip off. You know she'll find her way fine in the woods, even with enemies."
        "You turn your attention on the bandit, as he spits in your direction."
    else:
        "You're glad [fp] had left earlier. She likely wasn't in a part of the forest afflicted with the ravenous blades."
        "She was no warrior, but among the golden canopy she'd never be found. It was true even for Liam."
    #Two tiers, first the initial one. if it succeeds, you have to keep trying, crit means instant win, fail means battle time.
    if injuryCount == 1: #He notices your wounds, brags how easy this will be
        "Raider""Oh, you're injured, huh? Poor baby."
        if request == 1: #hunt
            "Raider""See you got speared by something earlier, eh? This'll be easy."
        elif request == 2: #Wolves
            "Raider""Wolf teeth, I'm guessing? How about I add to that tally."
        elif request == 3: #community
            "Raider""Got smacked over the noggin, I see. How about I help end that pain, permanently."
    else:
        "You're still fresh, despite the busy day. You'll have no issue outlasting this raider."
        "You square off with him, weapon drawn and ready as he brandishes his shield and axe."
    $enemyInjuryMax = 2
    $enemyInjury = 0
    $difficulty = 10
    menu ambushstart:
        "Talk down with flowery promise of riches under your ruler. (Fili)":
            tan"C'mon now. You don't need to fight us. Y'all probably want wealth."
            tan"The tuath here is on a trade route between Armagh and Dylfinn, imagine the spoils of being on such a route!"
            tan "Join us, and you'll be much more comfortable."
            tan"At the very least, you could kill our enemies for wealth, rather than just take."
            #Yadda yadda Conn's gonna be better than your king or chief, join us Instead
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Fili/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                "The raider sniffs, and lets his axe fall into the dirt. He spits in his hand and holds it out for you."
                "Raider""Why not. I was gettin' bored of fighting with these shits anyway."
                "Raider""I'd be more than happy ta slice a few of their necks."
                "You grimace and shake his hand. At the very least, you could have this raider fight his brethren."
                jump ambushNegotiate
            elif d20Roll+(Fili/3) >= difficulty:
                play sound "sound/success.mp3"
                "He swings his axe around, sticking his tongue out as he seems to think for once in his life."
                "Raider" "Maybe, maybe. What's to say we don't just take the fort, shank you, and rule it ourselves?"
                jump ambushConvince
            else:
                play sound "sound/fail.ogg"
                "Raider""Really, you think we're that dumb?"
                "Raider""We're just gonna steal your shit anyway! Now get on your knees and die!"
                jump ambushBattle
        "Speak of Geas to get them to flee. (Seanchas)":
            tan"There're geas on the village. Only certain families can rule, or face death. To raid us is an exercise in futility."
            tan"You try to, and you'll die, and your family will be cursed."
            tan"And based off your garb, you must be the superstitious type, eh?"
            tan"No matter of protection magic can stop a geas."
            tan"You wanna risk being cursed for a quick payout? The gods don't take kindly to violating geas."
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Seanchas/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                "Raider""Y'know. . ."
                "Raider""If that's the case, why not join you, get the gods on our side too?"
                "He winks, spits in his hand and reaches out towards you. You grimace and accept the handshake."
                tan"True. At least you'll have their favor on our side."
                jump ambushNegotiate
            elif d20Roll+(Seanchas/3) >= difficulty:
                play sound "sound/success.mp3"
                "Raider"". . . Geas huh?"
                "Raider""Got any proof of it?"
                tan "Gods don't exactly write their pronouncements down on stone, do they?"
                jump ambushConvince
            else:
                play sound "sound/fail.ogg"
                "Raider""Geas, really? Pull the other one."
                "Raider""Now die, I wanna get to pillaging!"
                jump ambushBattle
        "Bring it. (Might/Finesse/Vitality)":
            tan"Oh fuck this, let's get 'em. No raiders are gonna wander my homeland."
            sean "That's more like it!"
            "You grunt, jumping back as the raider runs and swipes at your legs. He cackles madly and squares off with back between your companions and yourself."
            "His compatriots find their own dueling partner, and the clearing's sound is swallowed by clashing weapons."
            tan "Oi! Asshole!"
            jump ambushBattle

    menu ambushConvince:
        "Did I mention riches? I meant RICHES. (Fili)":
            tan"Hey, I can tell you like wealth. I can ensure we have hordes of it."
            tan"Why do you think we're wandering around in the woods in nice clothing?"
            tan "We aren't some backwoods tuath, no sir."
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Fili/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                "Raider""Fine, fine! Where do I sign up?"
                "The raider, though visually annoyed at your insistence, puts away his weapon."
                tan "Get us through this raid, I'll get you an audience with the king."
                "Raider" "Now we're talking."
                jump ambushNegotiate
            elif d20Roll+(Fili/3) >= difficulty:
                play sound "sound/success.mp3"
                "Raider" "Eh. Even if it's true, it isn't worth stealing if you have that much money."
                "Raider" "You probably have crazy good mercenaries hiding around!"
                "He whistles to his pack of raiders, who get the message when he jogs off towards the south, away from the Cnoc bhFianna."
                jump ambushFlee
            else:
                play sound "sound/fail.ogg"
                "Raider" "Dumbass, that's all the more reason to steal shit from here."
                "Raider" "Now die!"
                jump ambushBattle
        "Geas is not something to violate lightly, even for Norsemen. (Seanchas)":
            tan"C'mon, Geas is dangerous stuff. I was given one myself, and it's been stuck on my mind since."
            tan "Will you really just brush this aside?"
            tan"If you do, you're dumber than I thought you'd be."
            tan "Maybe you aren't Gaelic, but you must know the strength of gods. Defy them at your own risk."
            tan "You won't get another warning."
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Seanchas/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                "Raider" "True. But what if we join the side the geas helps?"
                tan "I suppose that's a solution. Help us kill the raiders, you get a place."
                "Raider" "Deal. Let's kill some bastards."
                "You have the feeling this could be an extremely poor idea."
                jump ambushNegotiate
            elif d20Roll+(Seanchas/3) >= difficulty:
                play sound "sound/success.mp3"
                "Raider" "I'm not much for superstition. . ."
                "His outfit tells you otherwise, full of arcane charms and ritualistic runes"
                "Raider" "Oh whatever, fuck this, it's not worth the chance."
                "He turns towards the others, cupping hands around his mouth."
                "Rader" "Clear out boys! Time to split from this army!"
                jump ambushFlee
            else:
                play sound "sound/fail.ogg"
                "Raider" "Dumbass. Idiot. Fuckhead."
                "Raider" "Who the hell believes Geas is anything more than social taboo? Time to fucking die."
                jump ambushBattle
        "Screw this, Let's fight. (Might/Finesse/Vitality)":
            tan"Oh fuck this, let's get 'em. No raiders are gonna wander my homeland."
            sean "That's more like it!"
            "You grunt, jumping back as the raider runs and swipes at your legs. He cackles madly and squares off with back between your companions and yourself."
            "His compatriots find their own dueling partner, and the clearing's sound is swallowed by clashing weapons."
            tan "Oi! Asshole!"
            jump ambushBattle

    label ambushBattle:
        stop music fadeout 1.0
        play music "music/Wolf_Blood.ogg" fadein 1.0
        #The combat starts, warriors squaring off. You take on the lead raider.
        menu combatAmbush:
            "You and the raider circle each other, readying attacks. He growls at you, snarling viciously."
            "Use Finesse and Vitality to strike true":
                $d20Roll = renpy.random.randint(1,20)
                if d20Roll+(Finesse/3)+(Vitality/3) >= difficulty+10 or d20Roll == 20:
                    play sound "sound/critSuccess.mp3"
                    #2 injuries dealt
                    $enemyInjury += 2
                    $Finesse += 3
                    $Vitality += 3
                    scene bg latewoods
                    with vpunch
                    play audio "sound/injury.ogg"
                    if enemyInjury >= enemyInjuryMax:
                        #they're down!
                        if weapon == 1:
                            #fists
                            "With one last blow to the windpipe against the raider, you hear a sickening crunch. The formerly cackling raider drops his weapons and reaches for his throat, falling onto his back."
                            "You don't leave him to suffer of course, a kick to the temple and he's out cold."
                        elif weapon == 2:
                            #spears
                            "With practiced grace you launch your spear for the raider. He, not expecting you to cast the polearm, is taken by surprise as the steel tip sails through his heart."
                            "It takes a few moments to retrieve the weapon from the now dead raider."
                        elif weapon == 3:
                            #swords
                            "Your sword glints in the low twilight and finds a critical weakness in the raider's armor. Your other hand hits the pommel, driving the blade deep into his heart."
                            "He collapses, dead before he hits the floor."
                        elif weapon == 4:
                            #Axes
                            "Your axe flies and squarely hits the bandit in the neck. A flash of realization flies over his face before it drains of color."
                            "You tug harshly, and his body slips, leaving you with a bloody axe."
                        elif weapon == 5:
                            #Claymore
                            "Your claymore flies through the air, catching him by the neck and severing it before he even can react. His body falls in two onto the forest floor."
                            "You sigh, resting the two-hander on the grass. No coming back from that."
                        elif weapon == 6:
                            #Bow
                            "Your arrow pierces his eye as he charges you. The momentum knocks him back where he lays, unmoving."
                            "A good shot, ultimately. It's just a shame you had to kill someone with it."
                        elif weapon == 7:
                            #Sling
                            "Your sling whirrs by your head, and flies towards your enemy as he charges for you. The stone hits square at his temple, knocking him down and out instantly."
                            "You sigh, watching the blood pooling around him. He might not survive that one, but at least it was just a raider."
                        jump ambushWin
                    else:
                        if weapon == 1:
                            #fists
                            "You feel a crunch of bone under your fists as you batter the raider, easily slipping past his defenses. You grin, winking at him before dodging out of the way of his counterattack."
                            "Not done quite yet, but it was a start!"
                        elif weapon == 2:
                            #spears
                            "Your spear's shaft slams into the side of his head, making the raider lose his balance. His flailing axe prevents you from capitalizing on the strike, sadly."
                            "But that was a solid hit, and you could tell. He'd be down soon."
                        elif weapon == 3:
                            #swords
                            "You stab forward with your sword, spearing into one of the raider's legs. You give a shout of triumph, twisting it a bit before he forces you back with his shield."
                            "You ready yourself, grinning a bit madly."
                        elif weapon == 4:
                            #Axes
                            "Your axe smashes hard into his shield, obviously shaking the raider's grip on it. He grimaces, pushing back against you to throw you off."
                            "Now that rattled him! Good, it shouldn't take much longer."
                        elif weapon == 5:
                            #Claymore
                            "Your blade just about cleaves his shield in twain with a single stroke. You let out a laugh as he staggers back to his feet."
                            tan"That'll teach you to take on the [heir] of this tuath!"
                        elif weapon == 6:
                            #Bow
                            "You roll out of the way of a hazardous slash of his weapon, loosing an arrow as you come to a stop. It impacts his side, making the raider his in pain."
                            "You wink, before prepping another arrow."
                        elif weapon == 7:
                            #Sling
                            "Your sling lets loose, the stone striking his chest and knocking the air out of him. Another quick one sets him wheezing, but a cough clears his airways."
                            "Darn, you thought you almost had him there."
                        jump combatAmbush
                elif d20Roll+(Finesse/3)+(Vitality/3) >= difficulty:
                    play sound "sound/success.mp3"
                    #1 injuries dealt
                    $enemyInjury += 1
                    $Finesse += 2
                    $Vitality += 2
                    scene bg latewoods
                    with vpunch
                    play audio "sound/injury.ogg"
                    if enemyInjury >= enemyInjuryMax:
                        #they're down!
                        if weapon == 1:
                            #fists
                            "You and the raider charge at each other, growling out insults. He swings high with his axe, you drop to the ground and simply kick upward towards his crotch."
                            "The sound that ensues probably shouldn't be repeated in polite company but reminded you of a time where a feral cat fell off into a pot. He topples over, soundly defeated."
                        elif weapon == 2:
                            #spears
                            "Your spear's haft practically bends as you slam it against the side of the raider's head. You manage to smash him down to the ground with the blow, leaving him open for a short jab to the neck."
                            "It won't take long for him to bleed out."
                        elif weapon == 3:
                            #swords
                            "Your sword smashes into his shield before you slide it past and straight into his jugular. You pull back, letting his lifeblood pour out over armor and shield."
                            "No recovering from that blow."
                        elif weapon == 4:
                            #Axes
                            "Your axe slams into his leg, knocking him over. A quick second blow against his chest and a bloody wheeze from the raider and the life goes out from his eyes."
                            "Quick, clean, just a bit brutal. How you liked it, honestly."
                        elif weapon == 5:
                            #Claymore
                            "Your blade sails in, smashing the raider's axe in half followed by catching him full in the side. He crumples, letting out dying wheezes."
                            "Bloody, and a bit messy. You deign to end it, stabbing downward with both hands into his chest."
                        elif weapon == 6:
                            #Bow
                            "Your bowstring sings as you fall back onto your knees to avoid a blow, the arrow sailing up and directly through the gap under his jaw."
                            "A kick, and you push him out of the way, so he doesn't fall on you, though you do know you'll have to deal with the bloodstains later. Hopefully it didn't break that arrow either."
                        elif weapon == 7:
                            #Sling
                            "A deft roll and you fire the stone backwards, smashing it into the back of his head. It proved just the thing to cause him to falter and the raider falls forward into his shield."
                            "He doesn't seem to be breathing when you check, so hopefully it was a quick death."
                        jump ambushWin
                    else:
                        #Continue
                        if weapon == 1:
                            #fists
                            "Dodging out of the way of the swing of his axe, you suckerpunch the raider in the stomach. He grunts and dodges away from a second attack."
                            "Well, at least you got a solid blow in."
                        elif weapon == 2:
                            #spears
                            "Your spear impacts the raider's shield, shaking him up and making him wince. He growls, swiping at the blade and trying to slice it in half."
                            "You jump out of the way to dodge, preserving yourself and your weapon."
                        elif weapon == 3:
                            #swords
                            "Your sword just about nicks his neck, but he stops it short with his shield."
                            "You take the chance to kick his stomach, forcing him back to give you a bit more breathing room again."
                        elif weapon == 4:
                            #Axes
                            "Your axe cuts into his shield, forcing him back a few paces before he throws you off."
                            "You take the opportunity to knee him in the side, digging it in as you ward off counteratack with your shield, before jumping away yourself."
                        elif weapon == 5:
                            #Claymore
                            "Your claymore swings, and gets stuck in the muck next to him, but not before forcing him off balance. You strike quickly and kick him hard in the side."
                            "He curses at you, but you pull your blade out and get away from retaliation."
                        elif weapon == 6:
                            #Bow
                            "You run around the clearing, staying clear of the constantly swearing, very angry raider. With a quick shot, you hit him in the thigh."
                            "He screams at you angrily, slicing off the arrow haft with his axe before resuming pursuit."
                        elif weapon == 7:
                            #Sling
                            "A quick rock smacks against his clavicle, the noise telling you it likely broke bone. You wink, smirking at him before dancing out of the way of his axe."
                            tan"Gonna have to try harder, bastard-born!"
                        jump combatAmbush
                else:
                    play sound "sound/fail.ogg"
                    #1 injuries gained
                    $injuryCount += 1
                    $Finesse += 1
                    $Vitality += 1
                    scene bg latewoods
                    with hpunch
                    show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    play audio "sound/injury.ogg"
                    if injuryCount >= injuryMax:
                        #You've lost!
                        if weapon == 1:
                            #fists
                            "You aim a kick at the raider's crotch. His shield comes down, smashing your leg out of the way."
                            "Your eyes go wide, before the shield smashes your face and knocks you onto your back."
                        elif weapon == 2:
                            #spears
                            "Your spear flashes forward only to be deflected with ease by your enemy."
                            "He laughs, and turns the shield deflecting your spear into smashing its rim into your chin and laying you out flat."
                        elif weapon == 3:
                            #swords
                            "Your sword slices through the air but is stopped dead by his shield. With a wicked glare, and a slight twist he disarms you."
                            "Before you can react, he headbutts you flat onto your back."
                        elif weapon == 4:
                            #Axes
                            "Matching a swing of his axe with your own, the hafts of your weapons vibrating hard as they impact."
                            "An extra smash of his shield and you lose both weapon and your footing."
                        elif weapon == 5:
                            #Claymore
                            "He dodges under a slow swing of your weapon, smacking your hands with his shield before following it up with a headbutt to your chest."
                            "You're on your back before your blade even sinks into the ground."
                        elif weapon == 6:
                            #Bow
                            "Dodging your final arrow, the raider barks out a laugh and brings his axe down on your weapon."
                            "It splits in half, and the shock of the impact knocks you flat onto your back."
                        elif weapon == 7:
                            #Sling
                            "He blocks your last stone, using the opening to dash up and smash your windpipe hard with his arm."
                            "He pulls you down to the ground hard enough to knock the wind utterly out of your chest."
                        jump ambushLoss
                    else:
                        #You continue, hurt
                        if weapon == 1:
                            #fists
                            "You attempt to pull his shield out of the way to strike at him, but he simply cackles and slams his head into yours."
                            "It rattles you, but you still can keep going."
                        elif weapon == 2:
                            #spears
                            "Your spear flashes, but he deftly lifts up a leg to step hard on the shaft and avoid the blow. He just about trips, but it's enough."
                            "He smacks his shield into your side before you can retrieve your spear from the ground, hacking up a bloody wad of spit."
                        elif weapon == 3:
                            #swords
                            "Your sword clashes against his shield, and his axe against yours. With a heavy kick, he pushes you away."
                            "The pull against your shoulder feels almost like a dislocation, but a quick roll of your arm tells you otherwise."
                        elif weapon == 4:
                            #Axes
                            "Your shield is rattled by his axe blow, your arm going a bit numb. You weren't sure how many more impacts it could take!"
                            "But you unentangle from each other and square off for another round."
                        elif weapon == 5:
                            #Claymore
                            "The heavy blade embeds itself in the crazed raider's shield, which he just uses as an opportinity to headbutt you hard."
                            tan "Oh no you don't!"
                            "You pull away, glaring at him with a bloody nose."
                        elif weapon == 6:
                            #Bow
                            "The raider closes the gap between you too fast for you to react and catches you with his axe in a surface blow."
                            "You hiss in pain, before dancing away to ready another arrow."
                        elif weapon == 7:
                            #Sling
                            "Your stone flies wide and strikes a tree. His axe flashes in your peripheral vision, and you just avoid it being buried in your side."
                            "Shit, he still drew blood, but you could keep going."
                        jump combatAmbush
            "Use Might and Vitality to deal great blows":
                $d20Roll = renpy.random.randint(1,20)
                if d20Roll+(Might/3)+(Vitality/3) >= difficulty+10 or d20Roll == 20:
                    play sound "sound/critSuccess.mp3"
                    #2 injuries dealt
                    $enemyInjury += 2
                    $Might += 3
                    $Vitality += 3
                    scene bg latewoods
                    with vpunch
                    play audio "sound/injury.ogg"
                    if enemyInjury >= enemyInjuryMax:
                        #they're down!
                        if weapon == 1:
                            #fists
                            "With one last blow to the windpipe against the raider, you hear a sickening crunch. The formerly cackling raider drops his weapons and reaches for his throat, falling onto his back."
                            "You don't leave him to suffer of course, a kick to the temple and he's out cold."
                        elif weapon == 2:
                            #spears
                            "With practiced grace you launch your spear for the raider. He, not expecting you to cast the polearm, is taken by surprise as the steel tip sails through his heart."
                            "It takes a few moments to retrieve the weapon from the now dead raider."
                        elif weapon == 3:
                            #swords
                            "Your sword glints in the low twilight and finds a critical weakness in the raider's armor. Your other hand hits the pommel, driving the blade deep into his heart."
                            "He collapses, dead before he hits the floor."
                        elif weapon == 4:
                            #Axes
                            "Your axe flies and squarely hits the bandit in the neck. A flash of realization flies over his face before it drains of color."
                            "You tug harshly, and his body slips, leaving you with a bloody axe."
                        elif weapon == 5:
                            #Claymore
                            "Your claymore flies through the air, catching him by the neck and severing it before he even can react. His body falls in two onto the forest floor."
                            "You sigh, resting the two-hander on the grass. No coming back from that."
                        elif weapon == 6:
                            #Bow
                            "Your arrow pierces his eye as he charges you. The momentum knocks him back where he lays, unmoving."
                            "A good shot, ultimately. It's just a shame you had to kill someone with it."
                        elif weapon == 7:
                            #Sling
                            "Your sling whirrs by your head, and flies towards your enemy as he charges for you. The stone hits square at his temple, knocking him down and out instantly."
                            "You sigh, watching the blood pooling around him. He might not survive that one, but at least it was just a raider."
                        jump ambushWin
                    else:
                        if weapon == 1:
                            #fists
                            "You feel a crunch of bone under your fists as you batter the raider, easily slipping past his defenses. You grin, winking at him before dodging out of the way of his counterattack."
                            "Not done quite yet, but it was a start!"
                        elif weapon == 2:
                            #spears
                            "Your spear's shaft slams into the side of his head, making the raider lose his balance. His flailing axe prevents you from capitalizing on the strike, sadly."
                            "But that was a solid hit, and you could tell. He'd be down soon."
                        elif weapon == 3:
                            #swords
                            "You stab forward with your sword, spearing into one of the raider's legs. You give a shout of triumph, twisting it a bit before he forces you back with his shield."
                            "You ready yourself, grinning a bit madly."
                        elif weapon == 4:
                            #Axes
                            "Your axe smashes hard into his shield, obviously shaking the raider's grip on it. He grimaces, pushing back against you to throw you off."
                            "Now that rattled him! Good, it shouldn't take much longer."
                        elif weapon == 5:
                            #Claymore
                            "Your blade just about cleaves his shield in twain with a single stroke. You let out a laugh as he staggers back to his feet."
                            tan"That'll teach you to take on the [heir] of this tuath!"
                        elif weapon == 6:
                            #Bow
                            "You roll out of the way of a hazardous slash of his weapon, loosing an arrow as you come to a stop. It impacts his side, making the raider his in pain."
                            "You wink, before prepping another arrow."
                        elif weapon == 7:
                            #Sling
                            "Your sling lets loose, the stone striking his chest and knocking the air out of him. Another quick one sets him wheezing, but a cough clears his airways."
                            "Darn, you thought you almost had him there."
                        jump combatAmbush
                elif d20Roll+(Might/3)+(Vitality/3) >= difficulty:
                    play sound "sound/success.mp3"
                    #1 injuries dealt
                    $enemyInjury += 1
                    $Might += 2
                    $Vitality += 2
                    scene bg latewoods
                    with vpunch
                    play audio "sound/injury.ogg"
                    if enemyInjury >= enemyInjuryMax:
                        #they're down!
                        if weapon == 1:
                            #fists
                            "You and the raider charge at each other, growling out insults. He swings high with his axe, you drop to the ground and simply kick upward towards his crotch."
                            "The sound that ensues probably shouldn't be repeated in polite company but reminded you of a time where a feral cat fell off into a pot. He topples over, soundly defeated."
                        elif weapon == 2:
                            #spears
                            "Your spear's haft practically bends as you slam it against the side of the raider's head. You manage to smash him down to the ground with the blow, leaving him open for a short jab to the neck."
                            "It won't take long for him to bleed out."
                        elif weapon == 3:
                            #swords
                            "Your sword smashes into his shield before you slide it past and straight into his jugular. You pull back, letting his lifeblood pour out over armor and shield."
                            "No recovering from that blow."
                        elif weapon == 4:
                            #Axes
                            "Your axe slams into his leg, knocking him over. A quick second blow against his chest and a bloody wheeze from the raider and the life goes out from his eyes."
                            "Quick, clean, just a bit brutal. How you liked it, honestly."
                        elif weapon == 5:
                            #Claymore
                            "Your blade sails in, smashing the raider's axe in half followed by catching him full in the side. He crumples, letting out dying wheezes."
                            "Bloody, and a bit messy. You deign to end it, stabbing downward with both hands into his chest."
                        elif weapon == 6:
                            #Bow
                            "Your bowstring sings as you fall back onto your knees to avoid a blow, the arrow sailing up and directly through the gap under his jaw."
                            "A kick, and you push him out of the way, so he doesn't fall on you, though you do know you'll have to deal with the bloodstains later. Hopefully it didn't break that arrow either."
                        elif weapon == 7:
                            #Sling
                            "A deft roll and you fire the stone backwards, smashing it into the back of his head. It proved just the thing to cause him to falter and the raider falls forward into his shield."
                            "He doesn't seem to be breathing when you check, so hopefully it was a quick death."
                        jump ambushWin
                    else:
                        #Continue
                        if weapon == 1:
                            #fists
                            "Dodging out of the way of the swing of his axe, you suckerpunch the raider in the stomach. He grunts and dodges away from a second attack."
                            "Well, at least you got a solid blow in."
                        elif weapon == 2:
                            #spears
                            "Your spear impacts the raider's shield, shaking him up and making him wince. He growls, swiping at the blade and trying to slice it in half."
                            "You jump out of the way to dodge, preserving yourself and your weapon."
                        elif weapon == 3:
                            #swords
                            "Your sword just about nicks his neck, but he stops it short with his shield."
                            "You take the chance to kick his stomach, forcing him back to give you a bit more breathing room again."
                        elif weapon == 4:
                            #Axes
                            "Your axe cuts into his shield, forcing him back a few paces before he throws you off."
                            "You take the opportunity to knee him in the side, digging it in as you ward off counteratack with your shield, before jumping away yourself."
                        elif weapon == 5:
                            #Claymore
                            "Your claymore swings, and gets stuck in the muck next to him, but not before forcing him off balance. You strike quickly and kick him hard in the side."
                            "He curses at you, but you pull your blade out and get away from retaliation."
                        elif weapon == 6:
                            #Bow
                            "You run around the clearing, staying clear of the constantly swearing, very angry raider. With a quick shot, you hit him in the thigh."
                            "He screams at you angrily, slicing off the arrow haft with his axe before resuming pursuit."
                        elif weapon == 7:
                            #Sling
                            "A quick rock smacks against his clavicle, the noise telling you it likely broke bone. You wink, smirking at him before dancing out of the way of his axe."
                            tan"Gonna have to try harder, bastard-born!"
                        jump combatAmbush
                else:
                    play sound "sound/fail.ogg"
                    #1 injuries gained
                    $injuryCount += 1
                    $Might += 1
                    $Vitality += 1
                    scene bg latewoods
                    with hpunch
                    show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    play audio "sound/injury.ogg"
                    if injuryCount >= injuryMax:
                        #You've lost!
                        if weapon == 1:
                            #fists
                            "You aim a kick at the raider's crotch. His shield comes down, smashing your leg out of the way."
                            "Your eyes go wide, before the shield smashes your face and knocks you onto your back."
                        elif weapon == 2:
                            #spears
                            "Your spear flashes forward only to be deflected with ease by your enemy."
                            "He laughs, and turns the shield deflecting your spear into smashing its rim into your chin and laying you out flat."
                        elif weapon == 3:
                            #swords
                            "Your sword slices through the air but is stopped dead by his shield. With a wicked glare, and a slight twist he disarms you."
                            "Before you can react, he headbutts you flat onto your back."
                        elif weapon == 4:
                            #Axes
                            "Matching a swing of his axe with your own, the hafts of your weapons vibrating hard as they impact."
                            "An extra smash of his shield and you lose both weapon and your footing."
                        elif weapon == 5:
                            #Claymore
                            "He dodges under a slow swing of your weapon, smacking your hands with his shield before following it up with a headbutt to your chest."
                            "You're on your back before your blade even sinks into the ground."
                        elif weapon == 6:
                            #Bow
                            "Dodging your final arrow, the raider barks out a laugh and brings his axe down on your weapon."
                            "It splits in half, and the shock of the impact knocks you flat onto your back."
                        elif weapon == 7:
                            #Sling
                            "He blocks your last stone, using the opening to dash up and smash your windpipe hard with his arm."
                            "He pulls you down to the ground hard enough to knock the wind utterly out of your chest."
                        jump ambushLoss
                    else:
                        #You continue, hurt
                        if weapon == 1:
                            #fists
                            "You attempt to pull his shield out of the way to strike at him, but he simply cackles and slams his head into yours."
                            "It rattles you, but you still can keep going."
                        elif weapon == 2:
                            #spears
                            "Your spear flashes, but he deftly lifts up a leg to step hard on the shaft and avoid the blow. He just about trips, but it's enough."
                            "He smacks his shield into your side before you can retrieve your spear from the ground, hacking up a bloody wad of spit."
                        elif weapon == 3:
                            #swords
                            "Your sword clashes against his shield, and his axe against yours. With a heavy kick, he pushes you away."
                            "The pull against your shoulder feels almost like a dislocation, but a quick roll of your arm tells you otherwise."
                        elif weapon == 4:
                            #Axes
                            "Your shield is rattled by his axe blow, your arm going a bit numb. You weren't sure how many more impacts it could take!"
                            "But you unentangle from each other and square off for another round."
                        elif weapon == 5:
                            #Claymore
                            "The heavy blade embeds itself in the crazed raider's shield, which he just uses as an opportinity to headbutt you hard."
                            tan "Oh no you don't!"
                            "You pull away, glaring at him with a bloody nose."
                        elif weapon == 6:
                            #Bow
                            "The raider closes the gap between you too fast for you to react and catches you with his axe in a surface blow."
                            "You hiss in pain, before dancing away to ready another arrow."
                        elif weapon == 7:
                            #Sling
                            "Your stone flies wide and strikes a tree. His axe flashes in your peripheral vision, and you just avoid it being buried in your side."
                            "Shit, he still drew blood, but you could keep going."
                        jump combatAmbush

    label ambushWin:
        $ ambushResult = 1
        $honor += 2
        stop music fadeout 1.0
        play music "music/Bua_no_Bas.ogg" fadein 1.0
        show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        "The final raider falls to the ground roughly, bloody and sightless eyes staring towards the sky."
        show liam at left
        show sean
        show nora at right
        with dissolve
        sean"Finally, I thought he'd never go down."
        nora "He could take a surprising ammount of arrows, indeed."
        tan "The man almost killed me, and you're compl-"
        liam "Quiet!"
        "Liam holds up a hand, hissing out his words through clenched teeth. Nora gets the hint and tries to pick out what Liam noticed through the dim light of the dying day."
        "Her eyes widen, and she slaps a hand over Séan's mouth, pointing down the hill."
        liam "They were just the start."
        jump noticedWarriors
    label ambushLoss:
        $ ambushResult = 3
        $honor -= 2
        show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        "You hiss in pain, attempting to pull yourself back up onto your feet, and the raider's boot smashes you across the nose."
        "With how much you're bleeding, and the flashes of pain, you feel yourself already passing out."
        "The raider boss laughs, his scarred visage leering down at you."
        "Raider" "What whimps. Leave 'em, they aren't worth shit. Let 'em bleed."
        "Raider" "Let's get to the town before our friends have all the fun looting and burning."
        jump lossAmbush
    label ambushNegotiate:
        # You manage to talk them down. Good job. You got new allies!
        $ raiderAllies += 1
        $ ambushResult = 4
        "A brief conversation later, and you've managed to get these raiders to stop trying to kill you."
        "Lucky you, you have a potentially murderous friend now."
        "Though, what he says next isn't exactly encouraging."
        "Raider" "Oh, yeah. We aren't the whole raider band, not by far."
        show liam
        with dissolve
        "Liam's eyes narrow as he stows his weapons."
        liam ". . . How many."
        "Raider" "Pfft. I don't even know."
        "He points over his shoulder, down the hill. Your eyes follow, and Liam lets out a grunt."
        liam "So you were just the start."
        "Raider" "Oh yes!"
        jump noticedWarriors
    label ambushFlee:
        #They aren't sure which side to take. They instead decide to just leave, look for greener pastures
        $ ambushResult = 2
        "With little fanfare, the raiders clear out of the little cleared hilltop they ambushed you in."
        show sean at left
        show liam at right
        with dissolve
        sean "Well, that was anticlimactic."
        tan"You're gonna argue on us surviving an attempted raid?"
        sean "Well no, but-"
        liam "Quiet!"
        "He holds up a hand, hissing out his words through clenched teeth. Nora gets the hint and tries to pick out what Liam noticed through the dim light of the dying day."
        "Her eyes widen, and she slaps a hand over Séan's mouth, pointing down the hill."
        liam "They were just the start."
        jump noticedWarriors

label noticedWarriors:
    show screen virt_comp_overlay
    stop music fadeout 1.0
    play music "music/Threat_From_The_North.ogg" fadein 1.0
    scene bg latewoods
    show sean
    show liam at left
    show nora at right
    with fade
    sean "By all the gods of the earth and sky. . ."
    "At the crest of the hill, you gain a proper scope of the threat. Dozens of warriors, more than a match for the [king]'s fiann."
    "All wore the black and red paint, all in similar, if rugged and rusted, armor, and all with antlers, fangs, teeth and other sorts of trophies adorning them."
    "They moved more like a wolf pack than an army, making them all the more unnerving."
    "Probably too many to handle safely. And the Tuath was likely unaware of this new threat."
    if (faekid == 2 or faekid == 3) and ambushResult == 0:
        "Seeing the deadly threat, [fp] informs you she'll be finding her own way back."
        "Though initially concerned, the fact she just outright disappears from sight for a few moments before emerging again with a blade to your chest convinces you in her safety."
        "You do decide to ask her how she did that later, though, as she again vanishes into the golden canopy."
    "Your companions grumble and talk amongst each other, trying to sight out the horde all around before [liam] speaks up."
    liam "There any banners? Can't spy any."
    nora "Cannot see any m'self. There's so many. Is this greater or worse than the last raid?"
    liam "Worse, I say, the last came during the day and openly, and it was simply an unlucky loss."
    liam "This seems an invasion."
    if faith == 1:
        tan"By the gods, this can't be good."
    elif faith == 2:
        tan"Highest lord protect us against these heathens."
    elif faith == 3:
        tan"Gods preserve us indeed, Séan."
    elif faith == 4:
        tan"We're absolutely fucked, aren't we?"
    elif faith == 5:
        tan"By the Thunderer, how could we stand against this?"
    if C_aoife == True:
        aoife "We must do something, or we risk the death of all we love."
    if C_niall == True:
        niall"I'm gonna need a bigger hammer."
    tan "Okay, let's think fast. How should we deal with this?"
    liam "I say we flee through the woods to warn the tuath."
    nora "It could be dangerous to do that. We don't know their numbers or how far towards the fort they are."
    liam "True, but the closer we are to home, the more we might be able to help."
    sean "I'm not entirely sure if we can do much other than hide and wait until it's blown over."
    nora "Séan don't be cowardly."
    sean "It's not! We bunker down and send our fastest, my or Liam, to warn them. The tuath bunkers down and lets them run through."
    nora "And if they're here to kill us all?"
    sean "Oh. Hrm. . ."
    if C_aoife == True:
        hide sean
        show aoife
        with dissolve
        aoife "We should stab towards their heart. Kill their champion and break their leadership."
        hide niall with dissolve
    elif C_niall == True:
        hide sean
        show niall
        with dissolve
        niall "Why don' we confront their champion? I'd love a chance to hammer the antlers off his smug head."
        hide niall with dissolve
    else:
        tan "We could fight the champion, deal with him and prevent them from having him as a banner."
    "The discussion continues as such, but the three ideas seemed to divide your companions."
    "Since they can't decide, you sigh and raise a hand."
    tan "Here's what I say we do, as [heir]"
    #You must decide what to do, you could single out what seems to be a champion to scare off the raiders, hide in the forest until it blows over, or sneak around to reach town first

    menu raidChoice:
        "We don't have the numbers, we should sneak around to Cnoc bhFianna.":
            $raidReact = 1
            tan"I'm not a fighter. We should run for town and make sure they get the gates closed."
            tan"And if we can make sure everyone's safe, all the better."
            liam"A lot of ground to cover."
            tan"We can definitely do it. Let's go."
            jump escape
        "We should challenge their champion.":
            $raidReact = 2
            tan"If he falls, the raiders are all the weaker. We must confront him and slay him."
            if C_niall == True:
                niall"I'm good with cracking a skull or two. I agree."
            if C_aoife == True:
                aoife"Tis noble to die in the name of your Tuath and home, so let's go kill that git."
            tan "Let's get going, we don't have much time."
            sean "Just promise we'll get home? I'd rather not die to weird antler hunters."
            tan "Same here, so I'll swear by the gods of our people. It'll be no trouble."
            jump confrontation
        "We should hide, the tuath will be safe.":
            $ raidReact = 3
            tan"We have walls, we have warriors. They'll be fine without us. We can watch our own skins."
            if C_niall == True:
                niall"I suppose. . . You are the [heir], and the smarter of us two."
            if C_aoife == True:
                aoife "Not very becoming of a leader to be cowardly. I'll be heading back myself then. I must return to my love."
                show text "{b}{color=#FFFFFF}[aoife] has left your fiann, reducing your might and fili!{/color}{/b}" at truecenter
                with dissolve

                $ Might -= 2
                $ Fili -= 1
                if renpy.in_rollback():
                    $ C_aoife = True
                else :
                    $ C_aoife = False

                pause 1.5
                hide text
                with dissolve
            "You nod. Liam grunts, and pulls his bow from his shoulder."
            liam "While you hide, I'll wander the woods and raid the raiders. I know this land well enough."
            tan "Good idea and good hunting, we'll be here."
            jump hideEffort

label confrontation:
    stop music fadeout 1.0
    play music "music/Fateful_Reunion.ogg" fadein 1.0
    "It proves surprisingly easy to find the curadh, the champion."
    "He forged a path through the woods like a fomorian giant."
    show champion at left
    with dissolve
    "Scarred, bald, but with beard larger than a mountain and the same color as one, he cut an intimidating figure."
    "Especially with the bearded daneaxe he used as a walking stick. The blade was wicked, huge. Just seeing the weapon through the trees made you shiver in your boots."
    "He seemed older, but not by much. You struggled to imagine just how a human could get so large."
    "Perhaps he was indeed part fomorian."
    "His armor was similar to his fellows' kit but decorated not just with the skulls of beasts but those of former enemies."
    "Even his axe wore a skull where the blade met the haft."
    "He must be a headhunter, given the runes, Nordic and Gaelic, carved into the bones."
    "You swallow your nerves. No matter how large and terrifying this beast was, you had to take him down."
    "You and your companions ambush him and his in a clearing, shouting at them as he emerges through breaking branches and shaking trees."
    sean "Oi, bastard son of a giant!"
    tan "You're the one leading this raid?"
    raidchamp "Nay, but I'll be your doom."
    "His grip on his axe shifts down, and he tosses it up ever so slightly to catch it with both hands. His fénnid prepare their own weapons, spreading around the field."
    "Before the champion finishes his thought, one of the raiders drops to the forest floor, [liam]'s arrow in his throat."
    $ raidchamp = Character("Auðvin Vestfirska", color="#7a7372")
    raidchamp "No one's beaten Auðvin Vestfirska."
    sean "Well shit, guess we won't get the chance to talk this fomorian down."
    nora "Was that ever an option?"
    sean "Well I'd hoped so."
    tan "Everyone, take care of his allies. I'll deal with this curadh myself."
    "They aren't sure about letting you do this, but you certainly have the warrior prowess for it."
    if injuryCount >= 1:
        "Despite your injuries, you decide you'll do your best. The raider champion chuckles though, eying you over. He can plainly see the dried blood on your armor and clothes, the wounds"
        raidchamp "You shall not withstand a single blow of mine axe."
        tan "We'll see about that."
    else:
        "You're still fresh, despite the busy day. You feel no issue in outlasting this raider."
        "You square off with him, weapon drawn and ready as he brandishes his daneaxe."
    $enemyInjuryMax = 5
    $enemyInjury = 0
    $difficulty == 12
    if raiderAllies == 1:
        $raiderAllies -= 1
        $ enemyInjury += 1
        "Oddly enough though, before you get your chance the raiders following in your tow decide to charge first."
        "It doesn't take long for the champion to dispatch them, but he's actually injured now. That'd certainly make it easier to face him."

    #Fighting him is tough. He's an expert. It's unlikely players will win unless they have focused exclusively on one skill.
    #It was a dumb idea to face him, but if you beat him its highly honorable and affects the Wolves in future chapters.
    stop music fadeout 1.0
    play music "music/Wolf_Blood.ogg" fadein 1.0
    menu combatConfront:
        "You and the raider circle each other, readying attacks. He glowers at you watching carefully. This man is much more calculating than his peers."
        "Use Finesse and Vitality to strike true":
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Finesse/3)+(Vitality/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                #2 injuries dealt
                $enemyInjury += 2
                $Finesse += 3
                $Vitality += 3
                scene bg latewoods
                show champion at left
                with vpunch
                play audio "sound/injury.ogg"
                if enemyInjury >= enemyInjuryMax:
                    #they're down!
                    if weapon == 1:
                        #fists
                        "With one last blow to the windpipe against the raider, you hear a sickening crunch. The grim giant drops his weapons and reaches for his throat, falling to his knees."
                        "You grunt, shaking out your hand. Damn, this man is solid. At least he was down now."
                    elif weapon == 2:
                        #spears
                        "With practiced grace you launch your spear for the raider."
                        "He, not expecting you to cast the polearm, is taken by surprise as the steel tip sails through his leg and pins him in a kneel."
                    elif weapon == 3:
                        #swords
                        "Your sword glints in the low twilight and finds a critical weakness in the raider's armor. Your other hand hits the pommel, driving the blade deep into his guts"
                        "He collapses to his knees, bleeding profusely. Without aid, he wouldn't survive the night."
                    elif weapon == 4:
                        #Axes
                        "Your axe flies and squarely hits the bandit in the clavicle. He roars, but the blow brings him to his knees."
                        "You tug harshly, and the weapon slips from his shoulder."
                    elif weapon == 5:
                        #Claymore
                        "Your claymore flies through the air, catching him by the side."
                        "He grunts, one knee hitting the ground as he yields from the mounting pain."
                    elif weapon == 6:
                        #Bow
                        "Your arrow pierces his knee as he charges you. He stumbles, only just managing to get himself to his knee."
                        "But the arrow had shredded the other, the momentum forcing it all the way through and snapping it."
                    elif weapon == 7:
                        #Sling
                        "Your sling whirrs by your head, and flies towards your enemy as he charges for you. The stone hits square at his temple."
                        "He tumbles, ending up on his back for a brief moment before he struggles to his knees."
                    jump confrontWin
                else:
                    if weapon == 1:
                        #fists
                        "You feel a crunch of bone under your fists as you batter the raider, easily slipping past his defenses. You grin, winking at him before dodging out of the way of his counterattack."
                        "Not done quite yet, but it was a start!"
                    elif weapon == 2:
                        #spears
                        "Your spear's shaft slams into the side of his head, making the raider lose his balance. His flailing axe prevents you from capitalizing on the strike, sadly."
                        "But that was a solid hit, and you could tell. He'd be down soon."
                    elif weapon == 3:
                        #swords
                        "You stab forward with your sword, spearing into one of the raider's legs. You give a shout of triumph, twisting it a bit before he forces you back with his polearm of an axe."
                        "You ready yourself, grinning a bit madly."
                    elif weapon == 4:
                        #Axes
                        "Your axe smashes hard into his armor, splintering it just a bit. He grimaces, pushing back against you to throw you off."
                        "Now that rattled him! Good, it shouldn't take much longer."
                    elif weapon == 5:
                        #Claymore
                        "Your blade sinks into the haft of his axe cleanly, rattling him. You let out a laugh as he staggers back to his feet."
                        tan"That'll teach you to take on the [heir] of this tuath!"
                    elif weapon == 6:
                        #Bow
                        "You roll out of the way of a hazardous slash of his weapon, loosing an arrow as you come to a stop. It impacts his side, making the raider his in pain."
                        "You wink, before prepping another arrow."
                    elif weapon == 7:
                        #Sling
                        "Your sling lets loose, the stone striking his chest and knocking the air out of him. Another quick one sets him wheezing, but a cough clears his airways."
                        "Darn, you thought you almost had him there."
                    jump combatConfront
            elif d20Roll+(Finesse/3)+(Vitality/3) >= difficulty:
                play sound "sound/success.mp3"
                #1 injuries dealt
                $enemyInjury += 1
                $Finesse += 2
                $Vitality += 2
                scene bg latewoods
                show champion at left
                with vpunch
                play audio "sound/injury.ogg"
                if enemyInjury >= enemyInjuryMax:
                    #they're down!
                    if weapon == 1:
                        #fists
                        "You and the raider charge at each other, growling out insults. He swings high with his axe, you drop to the ground and simply kick upward towards his crotch."
                        "The sound that ensues probably shouldn't be repeated in polite company but reminded you of a time where a feral cat fell off into a pot. He topples over, soundly defeated."
                    elif weapon == 2:
                        #spears
                        "Your spear's haft practically bends as you slam it against the side of the raider's head. You manage to smash him down to the ground with the blow."
                        "He staggers to his knees, glaring up at you."
                    elif weapon == 3:
                        #swords
                        "Your sword smashes into his shield before you slide it past and straight into his shoulder. You pull back, letting his lifeblood pour out over armor."
                        "He stumbles, the blow enough to force him to yield to his knees."
                    elif weapon == 4:
                        #Axes
                        "Your axe slams into his leg, knocking him over. A quick second blow against his chest and a bloody wheeze from the raider."
                        "Despite the brutality, he manages to stagger up and to his knees."
                    elif weapon == 5:
                        #Claymore
                        "Your blade sails in, smashing the raider's axe in half followed by catching him full in the side. He crumples into a kneeling position."
                        "Bloody, and a bit messy, but he glares up at you, still fully awake."
                    elif weapon == 6:
                        #Bow
                        "Your bowstring sings as you fall back onto your knees to avoid a blow, the arrow sailing up and directly into his stomach."
                        "A kick, and you push him out of the way, so he doesn't fall on you. He rights himself just enough to stay on his knees, arrows sticking out of his form."
                    elif weapon == 7:
                        #Sling
                        "A deft roll and you fire the stone backwards, smashing it into the back of his head. It proved just the thing to cause him to falter and the raider falls forward."
                        "He held himself up to his knees, though, telling you it wasn't quite his death."
                    jump confrontWin
                else:
                    #Continue
                    if weapon == 1:
                        #fists
                        "Dodging out of the way of the swing of his axe, you suckerpunch the raider in the stomach. He grunts and dodges away from a second attack."
                        "Well, at least you got a solid blow in."
                    elif weapon == 2:
                        #spears
                        "Your spear impacts the raider's armor in a glance, shaking him up and making him wince. He growls, swiping at the blade and trying to slice it in half."
                        "You jump out of the way to dodge, preserving yourself and your weapon."
                    elif weapon == 3:
                        #swords
                        "Your sword just about nicks his neck, but he stops it short with his arm alone."
                        "You take the chance to kick his stomach, forcing him back to give you a bit more breathing room again."
                    elif weapon == 4:
                        #Axes
                        "Your axe cuts into his side, forcing him back a few paces before he throws you off."
                        "You take the opportunity to knee him in the side, digging it in as you ward off counteratack with your shield, before jumping away yourself."
                    elif weapon == 5:
                        #Claymore
                        "Your claymore swings, and gets stuck in the muck next to him, but not before forcing him off balance. You strike quickly and kick him hard in the side."
                        "He curses at you, but you pull your blade out and get away from retaliation."
                    elif weapon == 6:
                        #Bow
                        "You run around the clearing, staying clear of the constantly swearing, very angry raider. With a quick shot, you hit him in the thigh."
                        "He screams at you angrily, slicing off the arrow haft with his axe before resuming pursuit."
                    elif weapon == 7:
                        #Sling
                        "A quick rock smacks against his clavicle, the noise telling you it likely broke bone. You wink, smirking at him before dancing out of the way of his axe."
                        tan"Gonna have to try harder, bastard-born!"
                    jump combatConfront
            else:
                play sound "sound/fail.ogg"
                #1 injuries gained
                $injuryCount += 1
                $Finesse += 1
                $Vitality += 1
                scene bg latewoods
                show champion at left
                with hpunch
                show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                with dissolve
                pause 1
                hide text
                with dissolve
                play audio "sound/injury.ogg"
                if injuryCount >= injuryMax:
                    #You've lost!
                    if weapon == 1:
                        #fists
                        "You aim a kick at the raider's crotch. The haft of his axe sweeps, smashing your leg out of the way."
                        "Your eyes go wide, before the haft returns and smashes your face and knocks you onto your back."
                    elif weapon == 2:
                        #spears
                        "Your spear flashes forward only to be deflected with ease by your enemy."
                        "He laughs, and his axe bites into your side, laying you out flat."
                    elif weapon == 3:
                        #swords
                        "Your sword slices through the air but is stopped dead by the armor on his side. With a severe grunt, and a slight twist he disarms you."
                        "Before you can react, he headbutts you flat onto your back."
                    elif weapon == 4:
                        #Axes
                        "Matching a swing of his axe with your own, the hafts of your weapons vibrating hard as they impact."
                        "An extra smash of his axe haft against yours and you lose both weapon and your footing."
                    elif weapon == 5:
                        #Claymore
                        "He dodges under a slow swing of your weapon, smacking your hands with his axe's haft before following it up with a headbutt to your chest."
                        "You're on your back before your blade even sinks into the ground."
                    elif weapon == 6:
                        #Bow
                        "Dodging your final arrow, the raider barks out a laugh and brings his axe down on your weapon."
                        "It splits in half, and the shock of the impact knocks you flat onto your back."
                    elif weapon == 7:
                        #Sling
                        "He blocks your last stone, using the opening to dash up and smash your windpipe hard with his arm as if a clothesline."
                        "He pulls you down to the ground hard enough to knock the wind utterly out of your chest."
                    jump confrontLoss
                else:
                    #You continue, hurt
                    if weapon == 1:
                        #fists
                        "You attempt to pull his blocking axe out of the way to strike at him, but he simply cackles and slams his head into yours."
                        "It rattles you, but you still can keep going."
                    elif weapon == 2:
                        #spears
                        "Your spear flashes, but he deftly lifts up a leg to step hard on the shaft and avoid the blow. He just about trips, but it's enough."
                        "He smacks the haft of his axe into your shoulder before you can retrieve your spear from the ground, hacking up a bloody wad of spit into your face."
                    elif weapon == 3:
                        #swords
                        "His axe smashes into your shield, getting lodged deep. With a heavy kick, he pushes you away."
                        "The pull against your shoulder feels almost like a dislocation, but a quick roll of your arm tells you otherwise. Your shield has had batter days, though."
                    elif weapon == 4:
                        #Axes
                        "Your shield is rattled by his axe blow, your arm going a bit numb. You weren't sure how many more impacts it could take!"
                        "But you unentangle from each other and square off for another round."
                    elif weapon == 5:
                        #Claymore
                        "The heavy blade embeds itself in the crazed raider's axe haft, which he just uses as an opportinity to headbutt you hard."
                        tan "Oh no you don't!"
                        "You pull away, glaring at him with a bloody nose."
                    elif weapon == 6:
                        #Bow
                        "The raider closes the gap between you too fast for you to react and catches you with his axe in a surface blow."
                        "You hiss in pain, before dancing away to ready another arrow."
                    elif weapon == 7:
                        #Sling
                        "Your stone flies wide and strikes a tree. His axe flashes in your peripheral vision, and you just avoid it being buried in your side."
                        "Shit, he still drew blood, but you could keep going."
                    jump combatConfront
        "Use Might and Vitality to deal great blows":
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Might/3)+(Vitality/3) >= difficulty+10 or d20Roll == 20:
                play sound "sound/critSuccess.mp3"
                #2 injuries dealt
                $enemyInjury += 2
                $Might += 3
                $Vitality += 3
                scene bg latewoods
                show champion at left
                with vpunch
                play audio "sound/injury.ogg"
                if enemyInjury >= enemyInjuryMax:
                    #they're down!
                    if weapon == 1:
                        #fists
                        "With one last blow to the windpipe against the raider, you hear a sickening crunch. The grim giant drops his weapons and reaches for his throat, falling to his knees."
                        "You grunt, shaking out your hand. Damn, this man is solid. At least he was down now."
                    elif weapon == 2:
                        #spears
                        "With practiced grace you launch your spear for the raider."
                        "He, not expecting you to cast the polearm, is taken by surprise as the steel tip sails through his leg and pins him in a kneel."
                    elif weapon == 3:
                        #swords
                        "Your sword glints in the low twilight and finds a critical weakness in the raider's armor. Your other hand hits the pommel, driving the blade deep into his guts"
                        "He collapses to his knees, bleeding profusely. Without aid, he wouldn't survive the night."
                    elif weapon == 4:
                        #Axes
                        "Your axe flies and squarely hits the bandit in the clavicle. He roars, but the blow brings him to his knees."
                        "You tug harshly, and the weapon slips from his shoulder."
                    elif weapon == 5:
                        #Claymore
                        "Your claymore flies through the air, catching him by the side."
                        "He grunts, one knee hitting the ground as he yields from the mounting pain."
                    elif weapon == 6:
                        #Bow
                        "Your arrow pierces his knee as he charges you. He stumbles, only just managing to get himself to his knee."
                        "But the arrow had shredded the other, the momentum forcing it all the way through and snapping it."
                    elif weapon == 7:
                        #Sling
                        "Your sling whirrs by your head, and flies towards your enemy as he charges for you. The stone hits square at his temple."
                        "He tumbles, ending up on his back for a brief moment before he struggles to his knees."
                    jump confrontWin
                else:
                    if weapon == 1:
                        #fists
                        "You feel a crunch of bone under your fists as you batter the raider, easily slipping past his defenses. You grin, winking at him before dodging out of the way of his counterattack."
                        "Not done quite yet, but it was a start!"
                    elif weapon == 2:
                        #spears
                        "Your spear's shaft slams into the side of his head, making the raider lose his balance. His flailing axe prevents you from capitalizing on the strike, sadly."
                        "But that was a solid hit, and you could tell. He'd be down soon."
                    elif weapon == 3:
                        #swords
                        "You stab forward with your sword, spearing into one of the raider's legs. You give a shout of triumph, twisting it a bit before he forces you back with his polearm of an axe."
                        "You ready yourself, grinning a bit madly."
                    elif weapon == 4:
                        #Axes
                        "Your axe smashes hard into his armor, splintering it just a bit. He grimaces, pushing back against you to throw you off."
                        "Now that rattled him! Good, it shouldn't take much longer."
                    elif weapon == 5:
                        #Claymore
                        "Your blade sinks into the haft of his axe cleanly, rattling him. You let out a laugh as he staggers back to his feet."
                        tan"That'll teach you to take on the [heir] of this tuath!"
                    elif weapon == 6:
                        #Bow
                        "You roll out of the way of a hazardous slash of his weapon, loosing an arrow as you come to a stop. It impacts his side, making the raider his in pain."
                        "You wink, before prepping another arrow."
                    elif weapon == 7:
                        #Sling
                        "Your sling lets loose, the stone striking his chest and knocking the air out of him. Another quick one sets him wheezing, but a cough clears his airways."
                        "Darn, you thought you almost had him there."
                    jump combatConfront
            elif d20Roll+(Might/3)+(Vitality/3) >= difficulty:
                play sound "sound/success.mp3"
                #1 injuries dealt
                $enemyInjury += 1
                $Might += 2
                $Vitality += 2
                scene bg latewoods
                show champion at left
                with vpunch
                play audio "sound/injury.ogg"
                if enemyInjury >= enemyInjuryMax:
                    #they're down!
                    if weapon == 1:
                        #fists
                        "You and the raider charge at each other, growling out insults. He swings high with his axe, you drop to the ground and simply kick upward towards his crotch."
                        "The sound that ensues probably shouldn't be repeated in polite company but reminded you of a time where a feral cat fell off into a pot. He topples over, soundly defeated."
                    elif weapon == 2:
                        #spears
                        "Your spear's haft practically bends as you slam it against the side of the raider's head. You manage to smash him down to the ground with the blow."
                        "He staggers to his knees, glaring up at you."
                    elif weapon == 3:
                        #swords
                        "Your sword smashes into his shield before you slide it past and straight into his shoulder. You pull back, letting his lifeblood pour out over armor."
                        "He stumbles, the blow enough to force him to yield to his knees."
                    elif weapon == 4:
                        #Axes
                        "Your axe slams into his leg, knocking him over. A quick second blow against his chest and a bloody wheeze from the raider."
                        "Despite the brutality, he manages to stagger up and to his knees."
                    elif weapon == 5:
                        #Claymore
                        "Your blade sails in, smashing the raider's axe in half followed by catching him full in the side. He crumples into a kneeling position."
                        "Bloody, and a bit messy, but he glares up at you, still fully awake."
                    elif weapon == 6:
                        #Bow
                        "Your bowstring sings as you fall back onto your knees to avoid a blow, the arrow sailing up and directly into his stomach."
                        "A kick, and you push him out of the way, so he doesn't fall on you. He rights himself just enough to stay on his knees, arrows sticking out of his form."
                    elif weapon == 7:
                        #Sling
                        "A deft roll and you fire the stone backwards, smashing it into the back of his head. It proved just the thing to cause him to falter and the raider falls forward."
                        "He held himself up to his knees, though, telling you it wasn't quite his death."
                    jump confrontWin
                else:
                    #Continue
                    if weapon == 1:
                        #fists
                        "Dodging out of the way of the swing of his axe, you suckerpunch the raider in the stomach. He grunts and dodges away from a second attack."
                        "Well, at least you got a solid blow in."
                    elif weapon == 2:
                        #spears
                        "Your spear impacts the raider's armor in a glance, shaking him up and making him wince. He growls, swiping at the blade and trying to slice it in half."
                        "You jump out of the way to dodge, preserving yourself and your weapon."
                    elif weapon == 3:
                        #swords
                        "Your sword just about nicks his neck, but he stops it short with his arm alone."
                        "You take the chance to kick his stomach, forcing him back to give you a bit more breathing room again."
                    elif weapon == 4:
                        #Axes
                        "Your axe cuts into his side, forcing him back a few paces before he throws you off."
                        "You take the opportunity to knee him in the side, digging it in as you ward off counteratack with your shield, before jumping away yourself."
                    elif weapon == 5:
                        #Claymore
                        "Your claymore swings, and gets stuck in the muck next to him, but not before forcing him off balance. You strike quickly and kick him hard in the side."
                        "He curses at you, but you pull your blade out and get away from retaliation."
                    elif weapon == 6:
                        #Bow
                        "You run around the clearing, staying clear of the constantly swearing, very angry raider. With a quick shot, you hit him in the thigh."
                        "He screams at you angrily, slicing off the arrow haft with his axe before resuming pursuit."
                    elif weapon == 7:
                        #Sling
                        "A quick rock smacks against his clavicle, the noise telling you it likely broke bone. You wink, smirking at him before dancing out of the way of his axe."
                        tan"Gonna have to try harder, bastard-born!"
                    jump combatConfront
            else:
                play sound "sound/fail.ogg"
                #1 injuries gained
                $injuryCount += 1
                $Might += 1
                $Vitality += 1
                scene bg latewoods
                show champion at left
                with hpunch
                show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                with dissolve
                pause 1
                hide text
                with dissolve
                play audio "sound/injury.ogg"
                if injuryCount >= injuryMax:
                    #You've lost!
                    if weapon == 1:
                        #fists
                        "You aim a kick at the raider's crotch. The haft of his axe sweeps, smashing your leg out of the way."
                        "Your eyes go wide, before the haft returns and smashes your face and knocks you onto your back."
                    elif weapon == 2:
                        #spears
                        "Your spear flashes forward only to be deflected with ease by your enemy."
                        "He laughs, and his axe bites into your side, laying you out flat."
                    elif weapon == 3:
                        #swords
                        "Your sword slices through the air but is stopped dead by the armor on his side. With a severe grunt, and a slight twist he disarms you."
                        "Before you can react, he headbutts you flat onto your back."
                    elif weapon == 4:
                        #Axes
                        "Matching a swing of his axe with your own, the hafts of your weapons vibrating hard as they impact."
                        "An extra smash of his axe haft against yours and you lose both weapon and your footing."
                    elif weapon == 5:
                        #Claymore
                        "He dodges under a slow swing of your weapon, smacking your hands with his axe's haft before following it up with a headbutt to your chest."
                        "You're on your back before your blade even sinks into the ground."
                    elif weapon == 6:
                        #Bow
                        "Dodging your final arrow, the raider barks out a laugh and brings his axe down on your weapon."
                        "It splits in half, and the shock of the impact knocks you flat onto your back."
                    elif weapon == 7:
                        #Sling
                        "He blocks your last stone, using the opening to dash up and smash your windpipe hard with his arm as if a clothesline."
                        "He pulls you down to the ground hard enough to knock the wind utterly out of your chest."
                    jump confrontLoss
                else:
                    #You continue, hurt
                    if weapon == 1:
                        #fists
                        "You attempt to pull his blocking axe out of the way to strike at him, but he simply cackles and slams his head into yours."
                        "It rattles you, but you still can keep going."
                    elif weapon == 2:
                        #spears
                        "Your spear flashes, but he deftly lifts up a leg to step hard on the shaft and avoid the blow. He just about trips, but it's enough."
                        "He smacks the haft of his axe into your shoulder before you can retrieve your spear from the ground, hacking up a bloody wad of spit into your face."
                    elif weapon == 3:
                        #swords
                        "His axe smashes into your shield, getting lodged deep. With a heavy kick, he pushes you away."
                        "The pull against your shoulder feels almost like a dislocation, but a quick roll of your arm tells you otherwise. Your shield has had batter days, though."
                    elif weapon == 4:
                        #Axes
                        "Your shield is rattled by his axe blow, your arm going a bit numb. You weren't sure how many more impacts it could take!"
                        "But you unentangle from each other and square off for another round."
                    elif weapon == 5:
                        #Claymore
                        "The heavy blade embeds itself in the crazed raider's axe haft, which he just uses as an opportinity to headbutt you hard."
                        tan "Oh no you don't!"
                        "You pull away, glaring at him with a bloody nose."
                    elif weapon == 6:
                        #Bow
                        "The raider closes the gap between you too fast for you to react and catches you with his axe in a surface blow."
                        "You hiss in pain, before dancing away to ready another arrow."
                    elif weapon == 7:
                        #Sling
                        "Your stone flies wide and strikes a tree. His axe flashes in your peripheral vision, and you just avoid it being buried in your side."
                        "Shit, he still drew blood, but you could keep going."
                    jump combatConfront

    label confrontWin:
        stop music fadeout 1.0
        play music "music/Bua_no_Bas.ogg" fadein 1.0
        show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        $Honor += 3
        "The raider remains on his knees in front of you, bloodied and panting."
        raidchamp "Finish me, then."
        "You growl, taking up his discarded weapon, holding the heavy thing in both hands."
        "How had he even used this effectively in battle?"
        "It comes to your mind that the future of this man is still as unwritten as your own."
        "Perhaps you could even show mercy."
        "But then again, he had been just about to take your head should you have lost. . ."
        menu banditChoice:
            "Spare him, without shame.":
                $ confrontResult = 4
                tan "Leave. Never return."
                "The raider stares at you in confusion, not processing the words."
                tan"I leverage a prohibition on your presence in my people's lands. A geas, if you will."
                tan"Should you return, I will not be as merciful."
                "He grumbles, but nods. The few remaining fénnid of his gather to help the giant of a man off the field."
                hide champion with moveoutleft
                "You turn to Liam, who's sitting on a stump to regain his breath as your allies check each other's wounds."
                tan "Should you see him returning, you have my permission to give him no courtesy, put an arrow in his skull."
            "Spare him, offer him a place in the tuath.":
                $ confrontResult = 5
                tan "You're strong."
                "He watches you warily, confused as you place the axe on the ground between you two."
                tan "My home could use strong warriors like you. In fact, we'd be lucky to have you."
                tan "Flee for now. But if you would wish to serve honorably, in a proper kingship, return."
                tan "But if you return as a raider, I will take your head as a decoration of my own."
                "He nods, still wary. He slowly reaches for the axe, but you do not stop him."
                "With the aid of his few remaining fènnid, he limps off the field and away from the tuath."
                hide champion with moveoutleft
                sean "You sure about that offer? He was pretty savage."
                tan "He could be useful, regardless."
            "Slay him quickly.":
                $ confrontResult = 3
                "You toss the axe to the side and draw your knife."
                "It only takes one quick stab to the neck, then heart, to kill the champion."
                "With one final push you leave him dead and bloody in the leaves and grass, the rest of his fénnid fleeing in terror."
                hide champion with dissolve
                "You start wiping blood from yourself and your blades, before sighing."
                tan "Glad we dealt with him before he faced the tuath proper."
                tan "Though I wonder why they were so far out here, and where the leader of the raiders is."
                sean "No idea. Maybe he's raiding a different part and left the town to the champion?"
                tan "Perhaps."
                liam "He's dealt with. We have the rest of the raiders."
                tan "Right."
            "Slay him, take his head.":
                $ confrontResult = 2
                "A twisted smile graces your face, your eyes passing between the axe in your hands and this champion's neck."
                "With a single swing, you sever his head from his body."
                "Both of them fall to the earth with a powerful thud."
                "You retrieve the head by the head by his beard, peering into the glassy eyes of the dead champion."
                hide champion with moveoutleft
                tan "The rest of you better run. Your best's soul is now mine."
                "The fénnid run in a panic, scattering to the four winds. You chuckle darkly and toss the blooded axe to the ground."
                tan "Guess I have a new trophy. First head, though."
                sean "Morbid, but effective."
                tan "It would seem so."

        tan "Let's get back to the tuath. We're still under attack."
        jump townDefense

    label confrontLoss:
        $ confrontResult = 1
        show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        $Honor -= 1
        raidchamp "Tch. No challenge indeed."
        "He hefts his axe skyward, lining it up with your neck. . ."
        "Then an arrow embeds in his shoulder and he grunts, with narrowed eyes. The axe's blade lays in the dirt next to him as his baleful gaze turns to the source."
        "Your head weakly turns in the direction to see Liam, the last of your allies still standing."
        "The old hunter is wounded, but still standing strong."
        liam "Come at me, fomorian."
        raidchamp "I'll take your head then."
        liam "I'd like to see you try!"
        "Another arrow, and a few more felling the remaining fénnid of the raider champion, and [raidchamp] roars at Liam."
        "The last you see of the two is of them chasing into the woods, towards the tuath."
        "Axe blade flashes in the twlight and arrows soar in the sky, but neither able to get a solid hit yet."
        "Your head rolls back to stare at the sky. You know Liam will be fine, he'd faced tougher enemies."
        "Before another thought goes through your head, you feel like you're melting into the turf of the forest as consciousness flees you."
        jump lossConfront

label escape:
    stop music fadeout 1.0
    play music "music/Foreboding_Forest.ogg" fadein 1.0
    scene bg latewoods
    show sean
    with fade
    "You decide to exercise the greater part of caution."
    "Slipping from the safety of the hilltop with your companions, you run a long circuit around the bulk of the raiders."
    "At least, the ones you had seen before you started on the trek."
    "Antlered raiders stalk through the forest on all sides soon enough."
    "[sean] mumbles something about this being a bad idea, but you just ignore him and press onward."
    "So far, the plan had just been to make a run for it, but its rapidly becoming obvious that won't be possible."
    "You pull everyone to a stop once the raiders grow thicker. With so many ahead, you need to make a quick decision of how to proceed the final stretch."

    #if fail, go to confrontation, if win, go to town defense

    $difficulty = 12
    menu escapeTest:
        "Use natural shape of the land to hide progress. (Seanchas)":
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Seanchas/3) >= difficulty+10 or d20Roll == 20:
                $ Seanchas += 3
                "You're in luck, and quickly spot an easy way to run to town."
                "An old, unused deer trail abandoned as the game moved further north in the woods as human traffic expanded."
                "You usher everyone down the trail. Shortly later, you emerge out of the woods to witness the battle in the field around the tuath fort."
                jump townDefense
            elif d20Roll+(Seanchas/3) >= difficulty:
                $ Seanchas += 2
                "It takes a bit of maneuvering, but you manage to make it all the way to the field around tuath fort."
                "There's a few close calls on the way, handled with throws of dirt or quick smacks with a weapon, but the sneaking otherwise goes well."
                "However, the battle was already joined around the fort. It'll take a bit more doing to force your way through."
                jump townDefense
            else:
                $ Seanchas += 1
                "You keep trying your best to find a decent path through, but each attempt is headed off by more emerging raiders."
                "And even then, your attempts are to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation
        "Be quick, rather than sneaky. (Finesse)":
            if d20Roll+(Finesse/3) >= difficulty+10 or d20Roll == 20:
                $ Finesse += 3
                "With a jump and a call to action, you lead your friends on a mad dash through the woods. Through utter chance, not a single raider sees you."
                "Ducking under bough and jumping over stones, you power through the woods without impediment."
                "When you emerge on the other side, out into the field surrounding the tuath fort, you get an eyeful of the pitched battle engulfing the fort. Time for action, apparently."
                "You decide it might be better to just, gods be damned, break into a sprint."
                "Despite the fact you hear numerous shouts of alarm behind you, it turns out surprisingly easy to just bumrush for the fort."
                "Unfortunately, battle has already been joined on the outskirts, and you're running right into it."
                jump townDefense
            elif d20Roll+(Finesse/3) >= difficulty:
                $ Finesse += 2
                "You decide it might be better to just, gods be damned, break into a sprint."
                "Despite the fact you hear numerous shouts of alarm behind you, it turns out surprisingly easy to just rush for the fort."
                "Unfortunately, battle has already been joined on the outskirts, and you're running right into it."
                jump townDefense
            else:
                $ Finesse += 1
                "You keep trying your best to find a decent path through, but each attempt is headed off by more emerging raiders."
                "And even then, your attemps are to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation
        "If you get caught, bullshit your way through. (FIli)":
            if d20Roll+(Fili/3) >= difficulty+10 or d20Roll == 20:
                $ Fili += 3
                "You encounter at least half a dozen raiders, threatening and questioning you. While intimidating, you hold firm."
                "Every time, you and [sean] bamboozle them with words until they're too confused to put up a chase. His aggressive strumming of a fiddle especially helps confuse them."
                "Soon enough you arrive at the edge of the woods, a string of confused and turned around raiders behind you. But there were plenty more ahead."
                jump townDefense
            elif d20Roll+(Fili/3) >= difficulty:
                $ Fili += 2
                "Though you stumble a few times in explanations, it proves plenty to confuse the raiders you are running amidst."
                "Some of them even think they're going in the wrong way and turn around!"
                "Not as luckily, you find Cnoc bhFianna surrounded by enemies and the battle joined with its defenders."
                jump townDefense
            else:
                $ Fili += 1
                "You keep trying your best to find a decent path through, but each attempt is headed off by more emerging raiders."
                "And even then, your attempts are to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation

label hideEffort:
    stop music fadeout 1.0
    play music "music/Foreboding_Forest.ogg" fadein 1.0
    scene bg latewoods
    show sean
    with fade
    "With your mind set on hiding for the night, you quickly try to throw together some plan or another to properly prevent being found."
    "You click your tongue, thinking about what you have on hand. A shelter would probably be the best choice, one of cloaks and twigs."
    "But how to disguise it?"
    "Mud, dirt, and grime could hide it as a piece of the ground."
    "Clever use of redirecting magic thanks to [sean] and yourself could accomplish much of the same."
    "You could also keep a keen watch and strike down any who get near but stay put over the night."
    "Either way, with the raiders wandering the woods, it'll be tough to stay safe."

    $difficulty = 12
    menu hideTest:
        "Hide the shelter's presence and hunker down. (Seanchas)":
            $d20Roll = renpy.random.randint(1,20)
            if d20Roll+(Seanchas/3) >= difficulty+10 or d20Roll == 20:
                $ Seanchas += 3
                "With some clever uses of mud and twigs and dead leaves, you get the shelter to appear exactly like a pile of leaves on a slight swell in the ground."
                "You beckon your friends inside and hunker down for the night."
                "It'll be a long one, but you'll be safe in here."
                jump nextMorningHid
            elif d20Roll+(Seanchas/3) >= difficulty:
                $ Seanchas += 2
                "It's a bit scruffy and will likely not stand up to scrutiny in the daylight... but it certainly would do the job while you wait overnight."
                "You sigh, slumping yourself down on the inside against a stump, and watch your friends get comfortable."
                "Was this the right choice, you wonder. You won't know until tomorrow."
                jump nextMorningHid
            else:
                $ Seanchas += 1
                "While you spend the better part of an hour trying to put together a shelter and hide it, it only seems extremely shoddy work by the end."
                "And even then, it's to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation
        "Keep a watch through the night. (Finesse)":
            if d20Roll+(Finesse/3) >= difficulty+10 or d20Roll == 20:
                $ Finesse += 3
                "You keep a keen eye out on the hilltop ready to strike against any who come. Around midnight, a lone raider walks up, animalistically sniffing around."
                "The moment he sets eyes on your shelter, they sprout arrows and he witnesses no more."
                "A few others wander up through the night, but it otherwise passes slowly. The morning dawns, and you can relax."
                jump nextMorningHid
            elif d20Roll+(Finesse/3) >= difficulty:
                $ Finesse += 2
                "You set up the shelter with [sean]'s bow aiming out the entrance You are the best for this job, and more rested than other companions."
                "No one shows up over the night, but you do slay a rabbit. Perhaps it'll make a good breakfast."
                "But the night goes slowly, and the sun rises with you safe and the woods quiet."
                jump nextMorningHid
            else:
                $ Finesse += 1
                "While you spend the better part of an hour trying to put together a shelter and hide it, it only seems extremely shoddy work by the end."
                "And even then, it's to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation
        "Set up magical redirects to make the shelter unnoticable. (FIli)":
            if d20Roll+(Fili/3) >= difficulty+10 or d20Roll == 20:
                $ Fili += 3
                "With gentle strumming of the fiddle, runic lines, and spoken magic, and even you find difficulty keeping your eyes on the shelter."
                "It in reality sticks out like a thumb, but this enchantment should prevent any unwanted attention."
                "You wink at [sean] with a proud smirk and beckon your friends inside."
                "The night, while not truly restful, is quiet. You even hear a group of raiders stomping past, yet utterly missing the shelter."
                jump nextMorningHid
            elif d20Roll+(Fili/3) >= difficulty:
                $ Fili += 2
                "With magic weaved through music, [sean] sets up some basic sight wards. Whenever you set eyes on the shelter, a mild headache makes you wish you to look away."
                "It should suffice, though with knowledge of magic, it would be easy to tell something was there."
                "But you and friends bunker down for the night, hoping this was the right choice for the raiders."
                jump nextMorningHid
            else:
                $ Fili += 1
                "While you spend the better part of an hour trying to put together a shelter and hide it, it only seems extremely shoddy work by the end."
                "And even then, its to utterly no avail."
                "The crunch of leaves behind you heralds someone approaching, you and [sean] whirling around to face them."
                jump confrontation

label townDefense:
    stop music fadeout 1.0
    play music "music/Wolf_Blood.ogg" fadein 1.0
    play sound "sound/medium_fire.wav" fadein 1.0 loop
    play looper "sound/medievalcombatloop.ogg" fadein 1.0 loop
    scene bg battlefield
    show liam at left
    show sean
    show nora at right
    with fade
    $difficulty = 12
    "At the edge of the forest, the meadow of battle rolls out in front of you. The din of clashing steel, dying warriors, and multi-lingual shouts fill the air."
    "You frown, trying to discern the fastest way to rally warriors and aid in repulsing the antlered raiders."
    "The situation seems dire, but perhaps not unsalvageable... "

    "Your companions joining the fray and getting the fiann gathered around you would help draw them together in heart and deed."
    "But the battle was spread, and the occasional raider was slipping into town already."
    "It might be better to try to rally them back to the gate and shut it. The raiders had weapons, but no fortress-fighting equipment."
    "You could always say damn it to the battle and seek out Conn. Your geas weighs heavily, like a cattle mark on your very soul."
    sean "[tan], my [heir], what're we doing. We cannot just sit, my battle tune thrums in my heart."
    nora "Indeed, my bow itches, and Liam's as well."
    "The ranger simply nods, but without waiting for any other word, runs into the field and begins his hail of death upon the antlered men."
    "Your fate won't be his, it seems."
    hide liam with moveoutright
    if C_aoife == True:
        show aoife at right with dissolve
        aoife"We must rally my fellow fénnid. They are leaderless without me."
    else:
        hide sean
        show sean at right with dissolve
        "You sight [aoife] fighting valiantly in the field, surrounded on all sides."
        "Her shieldarm remains strong, and you assume the blood mingling with her warpaint is that of others. But she may need help."
    if C_niall == True:
        show aoife at right with dissolve
        niall "I could do with some smashing myself. The gate needs defended, though. Too many warriors going for glory in the field."
    else:
        hide sean
        show sean at right with dissolve
        "You cannot spot Niall out in the melee and assume he must be in the town. He would likely be defending the marketplace with all the might he had."
    if raiderAllies == 1:
        $raiderAllies -= 1
        $difficulty -= 2
        "Your newfound allies give a whoop and charge in full tilt into the melee. Luckily, they seem to keep their word and chop away at the enemy."
        "Might be a bit easier a challenge for their aid, or they could just be causing more confusion."

    menu fieldChoice:
        "Make a break for the gate and defend it. (Might + Vitality)":
            $ fieldHelp == 1
            tan "We must hold the gate, and prevent any more from slipping in. This seems the only one open at the moment. We hold it, Cnoc bhFianna is safe."
            tan "Let's hurry. We don't have much time."
            hide sean
            hide nora
            with moveoutright
            if C_niall == True:
                hide niall with moveoutright
            if C_aoife == True:
                hide aoife with moveoutright
            jump gateDefense
        "Rally the Fiann and slay the raiders. (Fili + Finesse)":
            $ fieldHelp == 2
            tan "The warriors need aid. We help them hold the field."
            tan "To arms, comrades!"
            hide sean
            hide nora
            with moveoutright
            if C_niall == True:
                hide niall with moveoutright
            if C_aoife == True:
                hide aoife with moveoutright
            jump fieldDefense
        "Run for the inner fort and [bro]. (Finesse + Seanchas)":
            $ fieldHelp == 3
            tan "My priority is the [king] and his health. We drive a path into and through the city."
            tan "Make haste!"
            hide sean
            hide nora
            with moveoutright
            if C_niall == True:
                hide niall with moveoutright
            if C_aoife == True:
                hide aoife with moveoutright
            jump marketDefense

    label gateDefense:
        #You hold the gate, rallying the remaining fennid to regroup in the walls as you hold off the enemy. Run as a skill test. (Vitality, Might, Finesse)
        #if you win, the gate is held and you retreat beyond it. You collapse from exhaustion shortly after.
        #Same loss condition as fieldDefense
        "You shout for aid as you charge across the field, cutting down raiders with your companions at your side."
        tan"Fiann of the Ó Durcáin! Rally at the gates! We must hold them!"
        show aoife
        show sean at right
        show nora at left
        with dissolve
        "The friendly warrior rally at your words, bolstered by Aoife's own echoing your command."
        "You bash through a raider about to stab through her back, using his own shield to smash his skull."
        tan "Hurry! The more time we waste allowing them to slip past us the worse this will be!"
        "You, [aoife], and [sean] lead the charge through the chaotic field and help everyone form up at the gates."
        "[sean], true to form, takes the back lines and begins to play his fiddle, shouting a battle song."
        "You, meanwhile, pick up a lost spear and shield and lock it with Aoife, standing in a forming double line of spears filling the gap in the gate."
        tan"[sean]! Play until they're dead or you are! We'll hold here!"
        "The warriors without a spot to stand in the line take up range from behind, or filter into the town to deal with those within."
        "Nora guides them to targets, calling them out as Liam stays out in the field, kiting the stragglers in wide circles until he moves out of site with the mob chasing him."

        $d20Roll = renpy.random.randint(1,20)
        if d20Roll+(Might/3)+(Vitality/3) >= difficulty:
            play sound "sound/success.mp3"
            $Might += 2
            $Vitality += 2
            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor += 2
            $ townResult = 1

            "With eager viciousness, the antlered raiders fall upon the line of spears."
            "Dozens of them fall within the first few moments, bodies pierced to the core by spear and pike"
            "You growl, pushing against the wave of raiders, holding firm and strong."
            "Blood slicks the grass and dirt, turning the ground beneath to a macabre swamp of red-stained mud."
            "But you hold, and so does the line. It becomes starkly obvious that with you and Aoife at the core, the remaining fénnid will never break."
            "The raiders begin to panic, and break."
            tan "We've done it!"
            "The last of the antlered men vanish into the woods as you shout, and you let your weapons drop into the mud, arms beyond sore."

            "At the very edge of the field you faintly see a gaunt, tall man in similar gear to the raiders, yet with some sort of crown upon his head."
            "You can't make out any features, any details, He's just too far."
            "But you do see his piercing blue eyes, staring directly at you."
            "You feel faint. A moment later, you're face down in the bloody mud with head smashing into a shield and luckily keeping you from inhaling the muck."
            "You hear Séan shout, but the words are distant, muddled. Then, nothing."
            jump nextMorningWon
        else:
            play sound "sound/fail.ogg"
            $Might += 1
            $Vitality += 1
            $ townResult = 2

            "While you do your best to hold the line, the antler men start their assault before its properly ready."
            "Aoife does her best, but a club knocks her out of the line, opening it up just enough for the raiders to surge in."
            "The line is cut in half, your back pinned to a wall as you continue to fight."
            "You growl,and stab a raider through the chest."
            tan "Keep fighting! They can't break us!"
            "But they do, and soon the fiann around you shatters and runs back into the town to continue the defense elsewhere."
            "You get stuck out in the field, fighting, fighting, fighting."
            "A whistle is heard, and you get distracted, eyes pulled towards the forest."

            "At the very edge of the field you faintly see a gaunt, tall man in similar gear to the raiders, yet with some sort of crown upon his head."
            "You can't make out any features, any details, He's just too far."
            "But you do see his piercing blue eyes, staring directly at you."
            "You feel faint, weird, not quite connected to your body."
            "A moment later, you're face down in the bloody mud with head smashing into a shield and luckily keeping you from inhaling the muck."
            "You hear Séan shout, but the words are distant, muddled. Then, nothing."
            jump lossTown

    label fieldDefense:
        #You take the fight to the field, forming a core around you and aoife and killing any who arrive. Run as a skill test. (Vitality, Might, Finesse)
        #if you win, they're driven off. The gate is barred and raiders inside are dealt with. You collapse from exhaustion shortly after.
        #If the champion is still standing, you see him and the leader but they don't confront you. they instead direct a retreat.
        #if you lose, the fiann is overwhelmed and you wake up among survivors inside the walls.
        "You shout for aid as you charge across the field, cutting down raiders with your companions at your side."
        tan"Fiann of the Ó Durcáin! Fight on! Your [heir] calls for it! Battle is in our blood, we can prevail!"
        show aoife
        show sean at right
        show nora at left
        with dissolve
        "The friendly warrior rally at your words, bolstered by Aoife's own echoing your command."
        "You bash through a raider about to stab through her back, using his own shield to smash his skull."
        tan "Any who beg mercy, let flee! Slay the rest, leave none standing!"
        "The battle in the field commences with speed and violence."
        "It becomes a running battle, you trade weapons whenever yours are no longer usable. A spear, then a bow, then a mace. You have enough experience for any."
        "But, for each you kill, there only seems to be more and more. [sean] does his best at keeping spirits high, but it might not be enough."

        $d20Roll = renpy.random.randint(1,20)
        if d20Roll+(Might/3)+(Vitality/3) >= difficulty:
            play sound "sound/success.mp3"
            $Finesse += 2
            $Fili += 2
            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor += 2
            $ townResult = 1
            "You stop and shout hard for all the warriors to hear."
            tan "Fight on! I swear by the gods of the sky, of the ground, and of the waves, we will triumph!"
            tan "We defend our homes, we defend our loved ones! They merely fight for gain!"
            "You are interrupted by an attempt to spear you through the side, but a swift dodge and a vicious headbutt to the perpetrator ends that."
            tan "We are the warriors of the Ó Durcáin! Fight on!"
            "You growl, and feel an arrow pierce your leg. Shit, that burns, but adrenaline keeps you moving."
            "Quickly, you snap the arrow shaft just enough to keep it from inhibiting movement."
            "You dive back into the battle, and within a short time, it seems to be won. The antlered ones flee, and you can get a breath."
            "Your words did just enough. Before you're about to shout out victory, your head wrenches towards the forest."

            "At the very edge of the field you faintly see a gaunt, tall man in similar gear to the raiders, yet with some sort of crown upon his head."
            "You can't make out any features, any details, He's just too far."
            "But you do see his piercing blue eyes, staring directly at you."
            "You feel faint. A moment later, you're face down in the bloody mud with head smashing into a shield and luckily keeping you from inhaling the muck."
            "You hear Séan shout, but the words are distant, muddled. Then, nothing."
            jump nextMorningWon
        else:
            play sound "sound/fail.ogg"
            $Finesse += 1
            $Fili += 1
            $ townResult = 2
            "The fighting is brutal, and quick. Strength wanes as it goes on, and even your endurance is quickly spent trying to fight so many foes."
            "The fénnid around you is close to running, the exhaustion and losses starting to mount."
            "You growl, and stab a raider through the chest."
            tan "Keep fighting! They can't break us!"
            "But they do, and soon the fiann around you shatters and runs back into the town to continue the defense elsewhere."
            "You get stuck out in the field, fighting, fighting, fighting."
            "Your shield breaks, and you fight with just a weapon you pulled from a corpse."
            "You hear a high, shrill whisle from the woods. Distracted, your eyes pull towards the forest."

            "At the very edge of the field you faintly see a gaunt, tall man in similar gear to the raiders, yet with some sort of crown upon his head."
            "You can't make out any features, any details, He's just too far."
            "But you do see his piercing blue eyes, staring directly at you."
            "You feel faint. A moment later, you're face down in the bloody mud with head smashing into a shield and luckily keeping you from inhaling the muck."
            "You hear Séan shout, but the words are distant, muddled. Then, nothing."
            jump lossTown

    label marketDefense:
        #While running to conn, you get bogged down in aiding Niall. Run as combat, due to lower numbers.
        #If you win, some crumbling building collapses as you head for the keep again, knocking you unconcious.
        #if you lose, the raiders knock you out and you wake up sore, but alive.

        "Your companions and you make the charge, cutting down any enemies as you do."
        "The field, with battles spread out across its vastness, is easy enough to traverse."
        if C_aoife == True:
            "Aoife breaks off to fight with the fiann, shouting for you to find Conn."
            "You nod solemnly, your feet carrying you faster towards the burning town."
        else:
            "Aoife continues to fight, grunting as you pass and shouting for you to find Conn in the town."
            "He was supposed to be out here by now, something must be wrong in the city."
        "Before you enter Cnoc bhFianna, you feel the impuse to turn back, to take one last glance over the field."
        "At the very edge of the field you faintly see a gaunt, tall man in similar gear to the raiders, yet with some sort of crown upon his head."
        "You can't make out any features, any details, He's just too far."
        "But you do see his piercing blue eyes, staring directly at you."
        "You turn in, past the gate, breaking eye contact. You have a mission."
        "As you run, you try to aid warriors as you see the, and cut down what raiders you can."
        show sean at right
        show nora at left
        with dissolve
        "Sean and Nora keep to your side, warding off enemies from flanking you."
        "With the town is burning, it becomes treacherous to navigate. Debris in narrow streets, burning beams of collapsed structures. Nothing that can't be rebuilt, but it's the people who suffer most."
        "Most people seem to have fled to strongholds in the kingfort and town around, leaving just the defending warriors and looting raiders."
        "As much as you wish you could help stop the blaze that isn't something you can deal with on such short notice."
        "You grimace and make your way to the market. From there, you could easily run to the inner fort."
        show niall with dissolve
        if C_niall == False:
            "In the market, you see [tb] and [niall] fighting for their lives, defending the church."
            "There's likely non-warriors inside, and the two hold each other back to back. Niall sights you and shouts."
            niall"[tan]! Hurry!"
        else:
            "In the market, you see [tb] fighting for his life, defending the church."
            "There's likely non-warriors inside. Niall grimaces, and immediately runs to join his master's side. He shouts back to you."
            niall"[tan]! We must help!"
        "You nod, and immediately run into the fray."

        $d20Roll = renpy.random.randint(1,20)
        if d20Roll+(Finesse/3)+(Seanchas/3) >= difficulty:
            play sound "sound/success.mp3"
            $Finesse += 2
            $Seanchas += 2
            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor += 2
            $ townResult = 1
            "Steel meets wood and steel in the market as you fight against the raiders harassing the blacksmith."
            "Niall fights akin to a man possessed, hammer cracking skulls and breaking bone, and not just the ones your enemy is wearing."
            "You find a sword, you can't even tell if its tuath-made or foreign, but it does the job in the close quarters you find yourself in."
            "Shields break and swords cut, but your companions overwhelm those strangers who think they have the right to kill and maim for wealth with impunity."
            "And soon, the field is quiet, save the exhausted panting of your friends and Conchobar."
            tb "Thanks."
            "You nod in acknowledgement to the laconic blacksmith, letting the sword fall from your hand."
            "Time to get up to the inner fort an-"

            "That odd feeling, the one when you locked eyes with the strange man watching the battle unfold, returns."
            "Your eyes dart around, but you can't find anything."
            sean "[tan]. . .?"
            "He starts speaking, but you only hear the sound of stone grind against stone. You whip your head around, looking for the source."
            "Then your eyes rest on the church. The steeple is collapsing as flame licks at it."
            "You shout, warning everyone, but a stray stone falls out and directly into the head."
            "You're out before you hit the ground, and the world melts away."
            jump nextMorningWon
        else:
            play sound "sound/fail.ogg"
            $Finesse += 1
            $Seanchas += 1
            $ townResult = 2
            "As you charge into battle, that odd feeling, the one when you locked eyes with the strange man watching the battle unfold, returns."
            "You do your best to shake it, but it persists. You simply fight through it."
            "You find a sword, you can't even tell if its tuath-made or foreign, but it does the job in the close quarters you find yourself in."
            "Shields break and swords cut, but your companions overwhelm those strangers who think they have the right to kill and maim for wealth with impunity."
            "But your motions feel sluggish."
            "Your muscles tired."
            "At first, you put it on the long day, and long battle, but you notice something."
            "The rest of your companions seem affected by it too."
            "Before you can shout out about it, a spear swings at you, the haft knocking you back into the market."
            "Your head smashes into a box of apples, sending them flying into the gravel of the market square."
            sean "[tan]!"
            "You see stars for a moment, before the world melts away and you lose consciousness."
            jump lossTown

label nextMorning:
    label nextMorningHid:
        #If you chose to run away and hide like a coward
        scene black
        with fade
        $raidResult = 1
        show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        $Honor -= 5
        play music "music/Foreboding_Town.ogg" fadein 1.0
        play sound "sound/Small_fire_loop.ogg" fadein 1.0 loop
        $ renpy.fix_rollback()
        "The night is long, and full of nasty noises. Even in this remote part of the woods, you can hear the occasional scream of pain."
        "You convince yourself it's just the raiders being fought off."
        "You don't see Liam again, once he wanders off to fight the raiders. You and your companions hope he'll be okay, but these men seem particularly nasty."
        "Nora keeps to herself, watching out of your makeshift shelter and into the darkness around for any movement."
        "It's an anxious night, but it passes the same as any other with the warm light of the dawning sun."
        "Eventually, the morning breaks. Reds and yellows bleed through the cloak and branches hiding you and your companions."
        sean "Guess it's time to go back. I don't feel right that we sought our own health over the rest, though."
        tan "It'll be fine, I swear by the gods my people swear by."
        "You don't believe yourself, but you lead them out of the shelter and into the early morning light."
        jump ruinField

    label nextMorningWon:
        scene black
        with fade
        $raidResult = 2
        show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
        with dissolve
        pause 1
        hide text
        with dissolve
        $Honor += 5
        stop music fadeout 1.0
        play music "music/Bua_no_Bas.ogg" fadein 1.0
        $ renpy.fix_rollback()

        "You awake with a gasp the next morning, in a very familiar environment."
        "Comfortable bedding under you, your weapons and armor draped over nearby furniture."
        "You're home."

        scene bg home
        with fade

        "Your wounds have been dressed, and you were set gently into bed. You touch your head and wince."
        "Nasty welt, right behind your right ear, made everything just a bit foggy."
        tan"Shit."
        "You pull yourself out of bed, wincing as you get dressed and try to get a semblance of comfort."
        "Pain wracks your body every so often, but it's all pain you know will fade with time. Doesn't stop you from cursing every so often."
        "Almost as if summoned by your vulgarity, [sean] steps in."
        show sean at right with moveinleft
        sean "Oh, you're awake. Glad you got some good sleep, it's still early in the day, though."
        tan "How's the tuath look?"
        sean "Great, actually. With your aid the warriors were able to rally and drive off the raiders enough to head out to the rest of the tuath and secure it too."
        tan "Good. Our losses?"
        sean "Oh. . . Well. . . Not too bad, but,"
        "Nora pushed [sean] in at this point, with her speaking up."
        show nora at left with moveinleft
        nora "We lost [liam]."
        "You pause in your dressing."
        tan "But wasn't he. . ."
        "Last you saw him, he'd been running out to fight valiantly, even as the rest of the fiann was retreating to regroup."
        nora "They cornered him out in the forest."
        if confrontResult == 0:
            nora "Their champion slew him, eventually. A daneaxe to the spine. Bastard stole Liam's head."
        else:
            nora "I think it was their leader who killed him. An arrow to the kneecap, then lopped off his head with a broadsword. Then left with it."
        tan "We need to retrieve his head, then."
        nora "My thought's exactly, [tan]."
        "Niall took that moment to call out from outside."
        niall "Friends, Aoife called us from the hall."
        if C_aoife == True:
            niall "No one's heard from [king] [bro] since last night. She only just woke up too, so has been heading there to check."
        else:
            niall "She's been up there since last night, and refused to let anyone in. Got me worried."
        "You smile, glad to hear the smith's voice. Once you step outside, you appraise him. He didn't look too hurt, you must have just gotten the worst of it."
        if C_niall == False:
            "You regret not bringing him with you yesterday, he would have been stuck in the tuath as raiders arrived. Hopefully he'd kept everyone safe."
            tan "Glad to hear you, Niall. Let's get on it. Coming with?"
            niall "Certainly."
            show text "{b}{color=#FFFFFF}[niall] has joined your fiann, improving your vitality and might!{/color}{/b}" at truecenter
            with dissolve

            $ Vitality += 2
            $Might += 1
            if renpy.in_rollback():
                $ C_niall = False
            else:
                $ C_niall = True

            pause 1.5
            hide text
            with dissolve
        else:
            "You're glad Niall had come with yesterday."
            "If he hadn't, you couldn't imagine how he'd fare. He was a blacksmith, not as much of a warrior."
        "With your clothing situated, and friends helping you, you head outside."
        scene bg village
        with dissolve
        "The town, though with some buildings in poorer state than yesterday, seems mostly intact. Your people scurry about, fixing up what they can and noting what they can't."
        "The walk is uneventful, and peaceful, but the raid hangs over the town, with all the losses you've seen."
        "A good number of familiar faces are missing."
        "Hopefully, you won't hear of anyone else you knew well, other than Liam."
        "At the very least, he died honorably."
        "Once you reach the inner fort and hall, you can easily tell at least some raiders made it this far. A few bodies lay, being shuffled off one at a time."
        show aoife with dissolve
        if C_aoife == False:
            "The king's hall sits, cold and quiet without a single light lit, waiting for your entry."
            "Aoife must already be inside."
        else:
            "Aoife greets you at the inner wall gate and rushes you towards the entrance."
            "She's worried, but can't face the empty-looking, cold hall alone, so you step in first."
        jump connDead

    label nextMorningLoss: #If you lost, with variants depending on when you lost.
        label lossAmbush:
            scene black
            with fade
            $raidResult = 3
            show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor -= 2
            play music "music/Foreboding_Town.ogg" fadein 1.0
            play sound "sound/Small_fire_loop.ogg" fadein 1.0 loop
            $ renpy.fix_rollback()
            "You wake up to [sean] shaking you awake in the early day sun filtering through the trees."
            "You aren't dead, but a heavy cough and blood splatters your friend's cloak."
            sean "Christ-in-heaven, [tan], aim that differently!"
            tan"Got it, got it... What'd I miss."
            sean"I woke up a few hours ago. Apparently when the battle got bad, you were the first out. Dunno what happened to Liam, not here when I woke."
            sean"But, we all got hurt bad, no one killed, surprisingly."
            nora"We should hurry back."
            "Her voice is a bit shaky, shivering from the cold of the autumn night and blood loss."
            "You pull yourself to your feet and shake your head in a no."
            tan"First, tend to everyone's wounds properly, then we head out."
            nora "Fine, but we gotta find Liam."
            jump ruinField

        label lossTown:
            scene black
            with fade
            $raidResult = 3
            show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor -= 2
            play music "music/Foreboding_Town.ogg" fadein 1.0
            play sound "sound/Small_fire_loop.ogg" fadein 1.0 loop
            $ renpy.fix_rollback()
            "You awake bleary eyed the next day, your eyes greeted by canvas skies. You're in a tent, alongside numerous other wounded warriors from the day before."
            "With a grunt, you roll over onto your side slightly before working yourself to sitting."
            "Your companions, save [sean], are nowhere to be seen. The bard is resting nearby, sitting on a stump stool."
            "You jostle his leg with the back of your hand, rousing him from tired half-sleep"
            sean "Mrrph...? Oh... Oh, you're up!"
            show sean with dissolve
            "His eyes are red, he must have been awake while you slept unconscious."
            tan "Indeed. Last I remember, I was being fed a serving of bootleather."
            tan"What's happened?"
            sean "The battle went south from there, of course. Aoife tried to keep the warriors rallied, but it just didn't work."
            sean "They were just too shaken by the numbers. We managed to pull many into the walls while we retreated and barred the gate."
            sean "Hasn't been a full tally of dead yet, but it's not good. The rest of the tuath can't be faring well either."
            tan "Damned raiders."
            "[sean] aids you to your feet and you stagger yourself outside. Your wounds have been bandaged, and luckily you can move, but it's painful with each step and strain."
            scene bg village
            show nora at right
            show sean at left
            with fade
            if C_niall == True:
                show niall with dissolve
            if C_aoife == True:
                show aoife with dissolve
            "The rest of your companions are waiting outside, but you cannot see Liam."
            "Nora's downcast expression tells you plenty, though."
            tan"How'd he die, Nora?"
            nora "Fighting like a demon. Slew dozens himself. Held them off while we rescued those we could. He was a hero."
            if confrontResult == 0:
                nora "Their champion slew him, eventually. A daneaxe to the spine. Bastard stole Liam's head."
            else:
                nora "I think it was their leader who killed him. An arrow to the kneecap, then lopped off his head with a broadsword. Then left with it."
            "She looks at you intently."
            nora"I will get it back, one way or another."
            tan"We will. But first, I need to see the town and Conn."
            jump ruinTown

        label lossConfront:
            scene bg latewoods
            with fade
            $raidResult = 3
            show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            $Honor -= 2
            play music "music/Foreboding_Town.ogg" fadein 1.0
            play sound "sound/Small_fire_loop.ogg" fadein 1.0 loop
            $ renpy.fix_rollback()
            "You're the first of your companions awake. While hurt, no one seems to have slain you or any of them in their sleep."
            "The only one missing is Liam. Had he not come back for you. . .?"
            "One by one, you wake up the others. [sean] takes the longest and sports a nasty welt on his temple."
            show sean with dissolve
            sean "Christ-in-heaven, why'd we fight that brute."
            show nora at left with dissolve
            nora "For the glory, for the tuath. We lost, sadly. Hopefully we ain't lose too much."
            tan "I hope so too. But we must hurry."
            if C_aoife == True:
                show aoife at right with dissolve
                aoife "We must see Conn. Perhaps they got the gates closed in time."
            if C_niall == True:
                show niall at right with dissolve
                niall "Gotta check up on the smithy and my Da. How's [sean]' wounds?"
            "You help the bard up and set to work on his wounds. Aside from the welt, he seems to not be too badly hurt."
            tan "Be careful resting the next day, [sean]. You may not wake."
            sean "Shit. That bad?"
            tan "A scrambled brain, potentially, from the impact site. You're lucky you aren't a corpse."
            sean "Shiiiit."
            nora "Make haste, we don't have much time."
            jump ruinField

        label ruinField:
            scene bg woods
            with fade
            "Nora leads your companions through and out of the forest. It's a slow trek, but you pick up hints of what happened the night before on the way."
            "While the occasional dead raider is found, you mostly find dead you recognize. Not many, but enough to be concerning."
            "Often hacked to pieces and torn like with claws, you get the sense of bodies mutilated by wolves, rather than blades."
            "Maybe it was a term to call these monstrous raiders, Wolves."
            "The raiders certainly fought like wolves from the carnage they left in their wake."
            "On the edge of the plain surrounding Cnoc bhFianna, you and your companions find something that rips at your soul."
            "Nora spotted the same sight first and fell deathly silent. She walked forward, eyes affixed to a mass of dead."
            "Most in the area wore antlers and had sprouted arrows and piercing wounds in vital areas."
            "But that's not what Nora is staring at."
            "At the head of a pack of dead raiders, still and utterly unmoving, lay Liam."
            "He was dead, body filled with enough steel and iron to build an entire wall. And his head had been stolen, like a few other warriors of the tuath."
            "They wouldn't know true rest until heads were given the same burial."
            "Nora kneeled, mumbling some unheard words, perhaps a prayer. You weren't sure of her religious inclination, but she gently wept yet with body shaking in anger."
            show nora at right with dissolve
            nora"So, that answers that question."
            nora"I must get his head back."
            tan"Indeed. I wish you luck."
            show sean with dissolve
            "[sean] rests a hand on her shoulder, head gesturing for the tuath's gate, worryingly lying open."
            sean"We need to check on the others. Do you need time with him?"
            nora "Please."
            "Both you and [sean] nod and bid her farewell. You know she'll meet up with you again within the day. She just needed time with her mentor."
            jump ruinTown

        label ruinTown:
            scene bg ruinedvillage
            with fade
            "You and your companions pick through the ruined remains of the gate, and wander towards the town's center."
            "The sound of still burning buildings echoes over the hillfort, and eyes watch you with confusion."
            "The people wandering the streets obviously wonder where you were, but your wounds tells them you must have been involved at least somehow."
            "But it was too late to change that fact."
            "Dead littered the streets, but less than in the fields outside. The bulk of combat must have been out before the gates."
            "Most of the dead inside are locals, unlike outside. It sets your bones cold as you wonder who might be dead due to your loss."
            "And inside, it seems as if the more well adorned buildings, such as clan holdfasts and the church, were hardest hit. Luckily enough for you, your home was in the part of town untouched."
            "You feel responsible for the devastation, but they're already trying to pick up the pieces."
            "This isn't the first raid they lived through, they were a truth of Ireland, always had been."
            show niall at left with dissolve
            if C_niall == False:
                "Near the smithy and town center, you spot your friend Niall sitting on a stump stool."
                "He mumbles softly, trying to parse the destruction around him."
                "By the bandage on his head, you assume he didn't get far into the battle before being rendered unconcious."
                "You thank your lucky stars that he's still alive. Concobhar, too, as the stocky blacksmith has already resumed working in his forge."
                show sean with dissolve
                sean "You big lug of a smith, how's your head?"
                "[sean] squats himself down gently next to the blacksmith apprentice. The bard starts humming a tune you recognize slightly as a tune of rest and health."
                niall "Decent. Could be better. You heading up to the king's hall?"
                tan "Suppose so."
                niall "No one's been up there yet, I think. The destruction trails up there though so..."
                "You nod, holding out a hand for Niall."
                tan "Come with. Conn will be waiting for us, I'm sure."
                niall "Sure. Let me get my hammer."

                show text "{b}{color=#FFFFFF}[niall] has joined your fiann, improving your vitality and might!{/color}{/b}" at truecenter
                with dissolve

                $ Vitality += 2
                $Might += 1
                if renpy.in_rollback():
                    $ C_niall = False
                else:
                    $ C_niall = True

                pause 1.5
                hide text
                with dissolve
            else:
                "Niall ran for the smithy as you approached it, wanting to check in on Concobhar."
                "With relief, he emerges a short time later. The smith had taken a nasty smack to the head but was resting and recovering."
                "No dead near here save the Wolves."
                "Its unsurprising, though. Concobhar was quite the warrior when he got his mind to it."
                "You sit down on a stump stool, getting a look over the market square. Unsurprisingly, it was ransacked."
                "On the other side, the humble church lay smoldering with some of its riches splayed over the grass in front of it."
                "The cross formerly mounted on its front was embedded in a wolf raider who felt like trying his chances with removing it."
                "Apparently, the Highest's sense of retribution could be highly ironic."
                niall "Master says he's unsure the state of the inner fort. No one's been up there yet."
                tan"We better go check then. I'm certain Conn will be waiting for us."
                show sean with dissolve
                sean "Lead the way, [tan]."
                "You nod, and stand again after the brief rest, striding forward with companions in tow."
            "Now, only the King's hall and inner fort remained for you to check. You and your companions walk up the hill slope towards it, dread slowly growing in your throat."
            jump connDead

label connDead:
    stop music fadeout 1.0
    play sound "sound/Small_fire_loop.ogg" fadein 1.0 loop
    scene bg kinghall
    with fade
    "You and your friends step into the King's Hall. The doors are rendered into splintered wood and buckled iron, broken the rush of bodies and Norse axes."
    "The interior is dark, quiet, in the early morning. While the sound of licking flames can be heard, it isn't from the hearth, but rather from the parts of the inner fort still burning from the attack."
    "Your companions pick around, checking the dead fénnid around the room. [sean] gently mumbles prayers for them to find their afterlife safely."
    show aoife with dissolve
    if C_aoife == False:
        "In the center of the hall you find Aoife, stone faced staring at the dead fire."
        "She bore the telltale signs of battle and conflict. But her face was gaunt, blank."
        "Rivulets of tears streak her freckled countenance, leaving you to wonder what-"
    else:
        "Aoife strides forward once she's inside, looking around in a panic."
        "She must be looking for Conn and her child. They would have been here during such a battle."
        "But then her face blanches, jaw going slack for a moment, before setting hard. You walk forward and around her to see just what has her so-"
    "Your blood runs cold."
    "You saw what had Aoife so twisted."
    "Red stained floorboards, familiar bodies, the scents of violence, in front of the throne."
    "You had hoped to never see this sight."
    "But there's Conn. Your brother. Dead."
    "His body lays broken by blade and blow at the foot of his throne, curling around a small bundle. His lifeblood is drying all around, mingling with the viscera from the bundle."
    "It must be Aengus. He died as the raiders slew the king. While the king protected his only child."
    "Such indignity. . . You can scarcely think of these monsters as humans anymore."
    "And [fmb]'s words ring in your ears. He had warned you about this. The gods had given you a warning. A geas."
    "But you ran away to deal with the tuath's business, and spent the day advancing your own glory."
    "You must be cursed."
    "You can do naught but the first thing coming to your mind."
    menu deathReact:
        "Run":
            $deathchoice = 1
            "You turn on your heels. The world around you is a blur as you shove aside anyone in your path. Your companions are left in the dust."
            if faith == 1:
                "You're found in the nemeton the next day, mumbling the old stories alongside [td]. She holds her head to yours. Calling upon her magic to help bless you against any godly curse of geas."
                "[sean] convinces you to return. The tuath does need their new king."
                "You agree, your heart full of the ancient wisdom and stories of your people."
            elif faith == 2:
                "You're found in the Culdee monastery the next day and lead back to Cnoc bhFianna. Your knees are raw from the stone floor where you spent the day praying."
                "You hope The Lord has heard your calls."
                "But for now, you must deal with this world's hardship."
            elif faith == 3:
                "The next day, you return to the tuath, sore from the night spent outside and clothing ruined."
                "You spend time praying to every god you know for the safety of your dead family's souls."
                "Perhaps they'll be safer once the Highest or the [tdd] receive them."
            elif faith == 4:
                "The next day, you stumble back into the tuath, eyes red but face stony. You brush aside concerns for your health and return home for a change of clothes."
                "You immediately head for where Conn's body is, and you do not leave his side until he's put to rest."
                "Despite your lack of faith, you respect his wishes to be laid out like his ancestors and immolated."
            elif faith == 5:
                "The next day, they find you on the edge of the forest, carving runes into a stone painstakingly. They speak of Conn."
                "Of his short life, his triumphs, and of your love for him. Of your family and line. Of little Aengus."
                "Your companions aid you, letting your red-raw and bleeding hands rest."
            "You can't run forever, though, and soon enough you must return to the tuath as its new leader."
        "Weep":
            $deathchoice = 2
            "You drop to your knees and tears begin to well up."
            "Your body shakes, and it's all you can do to remain perpendicular to the ground with knuckles whitened against your knees as you hold onto them."
            "Was this failure on you? You had tried so hard to make it back here, yet Conn and others still perished. Aengus was slain so brutally."
            "Perhaps it is your fault. But you're the king now. This is written into the laws, so it is."
            "You have plenty of time over the next few days to ruminate on this, as preparations for a new coronation commence."
            "But you cannot help but feel if you had been faster, gone home sooner, you would have saved them. History was written, and not in a way you wanted it to be."
        "Anger":
            $deathchoice = 3
            "The world around you becomes fogged in a red haze. How dare anyone murder your family."
            "You grip the side of the throne, hard, knuckles white. You glare down at the bodies, muscles tensing and eye twitching."
            "Your companions try in vain to calm you. You fume, curse, and rave against the gods themselves."
            "Your rage only grows. You uselessly shout at the sky and stab the dead raiders and deface whatever you can reach."
            "Aoife and Niall manage to tie you down with extreme effort, and simply knock you out when even that isn't enough."
            "By the next day, the rage has left you. Your heart feels torn and bitter, but with direction."
        "Hollow":
            $deathchoice = 4
            "You slump to your knees and stare at the bodies."
            "You just feel cold. Empty. You don't know how to feel."
            "When your mother died, it wasn't like this. It wasn't like your soul had been torn in two and left half-dead in a beating heart. This is a new hurt."
            "It felt shitty. There was no other way to describe this pain of loss of someone you trusted and loved so unconditionally."
            "There is simply nothing to say."
            "The feeling doesn't leave, but you eventually get back to your life."
            "You have a job to do. After all: You're the king."
    jump Coronation

#Ch 1 part 5
label Coronation:
    stop sound fadeout 1.0
    play music "music/Legacy.ogg" fadein 1.0
    scene bg kinghall
    show text "A few days later. . ." at truecenter
    with fade
    pause 2
    hide text
    with dissolve
    $injuryCount = 0
    show text "{b}{color=#FFFFFF}Injuries Lost{/color}{/b}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    "Once Conn and Aengus have been laid to rest, cremated and the wind allowed to whisk their souls and bodies across the world, the preparations for your coronation can begin."
    "A feast, not as grand as the one Conn had been planning, is put together. You make it more of a wake honoring the dead than a proper coronation feast, but the people and your friends appreciate that."
    "The festivities are somber at first, people sharing the memories of those lost and those still alive. Like most Gaelic celebrations, it continues into the wee hours of the morning."
    "A success, by all reckoning."
    "All that was left is the rites of kingship up in the old passage tomb on the day of the next new moon."
    "Until then, you are left to run the tuath. It mostly ran itself, with you occasionally solving disputes, but after the raid everyone seem much more sedate and pulled together."
    "No one wants to start shit that would hurt the tuath as a whole."
    "So, you have plenty of time to think, and to talk. Luckily, the new moon is only a few days distant following the death of Conn."
    "You and your companions, no, your fiann spend more time in the King's Hall, conversations of the future passing between the group."
    "The five of your core fiann, Niall, Séan, Nora, Aoife, and yourself, regularly sit at the large table for these conversations."
    "Occasionally, other important people from the tuath arrive to join discussions, but never permenantly."
    "Today, you came together to talk again, about the coronation tomorrow and what may come after it. You were expected to give a speech about the raid and retribution for it."
    "You look around the table at the hard-set expressions of your friends and allies and think about the events of the last few days."
    show aoife
    with dissolve
    if C_aoife == True:
        "Aoife is torn apart by this. She dearly loved Conn, and since Aengus had been slain too, she had sunk into unending rage."
        "You just hope her intelligent, witty, and strong self shall properly re-emerge from this fog of death and despair."
    else:
        "Aoife, being rígfénnid for the tuath, is now considered your hand. She officially joins your rule, and while torn by events of recent days is eager to join you."
        "You just hope her intelligent, witty, and strong self shall properly re-emerge from this fog of death and despair."
        show text "{b}{color=#FFFFFF}[aoife] has joined your fiann, improving your might and fili!{/color}{/b}" at truecenter
        with dissolve

        $ Might += 2
        $ Fili += 1
        if renpy.in_rollback():
            $ C_aoife = False
        else :
            $C_aoife = True

        pause 1.5
        hide text
        with dissolve
        hide aoife
        "She now wore her dead beloved's ring on her shield-hand, a small memento of what she'd lost and who she was fighting to avenge."
    #Nora
    show nora at left with dissolve
    "Nora is shaken by Liam's death defending the woods. Much like Conn, his body had already been sent into the air and ground with fire."
    "But she knew this would happen someday. She had just wished it later, not sooner. She would have to live without her foster father from now on. And certainly not with the dishonor he was given."
    if wolftarget == 3 and wolfwin == 0:
        "With Adh perishing as well, she had no living remains of Liam. But she held onto his bow, carved in ornate lines and markings honoring the gods of Eire."
    else:
        "She at the very least has Adh. The silly dog sits next to her, oblivious of the mood of the room but loyal as ever."
        "She has also held onto Liam's bow. A strong weapon, carved in ornate lines and markings honoring the gods of Eire, and a memento of her loss"
    #Niall
    show niall at right with dissolve
    "Niall had always been one of the more serious of your group, but there's a grimmer face to him now."
    "Last raid, he hadn't lost much. This time, [tb]'s smithy was torched, and Brigit been cut down. Niall always loved spending time with her. She half raised him with Concobhar, after all."
    "His days have been taken by planning proper wakes for those lost, which would be held once the coronation was through. You admire his willingness to celebrate in such hard times."
    #Sean
    hide aoife
    show sean with dissolve
    "[sean], being Séan, continues playing his fiddle, albeit in a more somber tone. It is rare his music isn't hopeful, but ever since the raid he's learned to appreciate the songs of hardship."
    "But, of you all he is still the most upbeat. He turns you to focus on the positive sides of life."
    "After every storm came a dawn, and every loss is only temporary. You will see them again someday, so you better make some damn good stories for that meeting."
    "It is surprisingly uplifting."

    #Deaths from the tuath - Liam, Brigit, the farmer patriarch and several clergy

    scene bg kinghall
    with dissolve
    "But of course, the deaths of many in the tuath is still on your mind."
    "Dozens of villagers, members of every clan and peasant family, and people you care for lost for good."
    "The loss of Liam is keenly felt by many in the tuath. He had been a foster father to many in the tuath, and a teacher to many more. Nora has offered to take his place as chief hunter, which you accepted."
    "And Old Brigit too. In the morning she'd been found in her bakery, surrounded by at least six dead raiders. The old baker had been hacked to pieces, yet before that defeated so many enemies."
    "You are glad that she was given a hero's burial like Liam and Conn and honored the same. You personally carved her name into the menhir in town center honoring the heroic dead of the tuath."
    "One of the wolf raider targets, aside from the wealth squirreled away in the fort itself and the clan halls, was the church it turned out."
    "The day after the raid, a few of the clergymen from the monastery made their way to town. While [tp] had survived, many of the clergymen had been cut down defending the church from raiders."
    "And the local farm patriarch was found beheaded and dead with a good portion of his family. Being one of the older rustic families, you weren't sure who the farming families would organize around."
    "The Wolves, as the tuath has taken to calling them, weren't just stealing whatever they could but striving to cause as much damage as humanly possible."
    "And it leaves you fuming."
    show sean with dissolve
    sean "Uh, [tan], I mean, [king]?"
    if tan == Character("Tánaiste", color="#006400", image="player"):
        "Right, your title wasn't [heir], anymore. Perhaps you should go by that."
        "Or, perhaps a new epithet?"
        menu nickChoice1:
            "Go by [king], now.":
                $tan = Character("Rí", color="#006400", image="player")
                "Perhaps it is time to grow up."
                tan "Yes, [king] should work now, call me as such."
            "Choose a different one.":
                "It might be time to reinvent myself."
                jump nickReChoice
    else:
        "Sean tries to get your attention, but it brings up the fact of your byname to your mind."
        "Perhaps you should your newly gained title, rather than the epithets and titles of yesterday?"
        menu nickChoice2:
            "Go by [king], now.":
                $tan = Character("Rí", color="#006400", image="player")
                "Perhaps it is time to grow up."
                tan "Yes, [king] should work now, call me as such."
            "Use the same epithet":
                "No. no need to change what has always been the case."
                tan "Just call me [tan], Séan. You're my friend."
            "Choose a different one.":
                "It might be time to reinvent myself."
                jump nickReChoice
    label afternick:
        "Yeah, that's a good choice."
        tan"I will go by [tan], now. A new name for a new epoch of my life."
    "[sean] nods then sets his fiddle aside."
    sean "So, [tan]. We were discussing the coronation when you got that distant look again."
    tan "Right. It's planned for tomorrow, yes? We have everything in hand?"
    show aoife at right with dissolve
    aoife "The township's been happy to contribute. They need something uniting, especially after such a short time between new kings."
    aoife "The wake feast helped, but you need something a bit more."
    tan "Understandable. I need to show them I care just as much about the losses. I'll be giving a speech during the proceedings, at the coronation hill."
    aoife"Smart idea. What are you going to focus on?"
    tan "I'm not quite sure yet. Something like this, it needs to flow from the heart. I have a few ideas, such as the unity of our clans, "
    sean "Right on that, [tan]."
    show nora at right with dissolve
    nora "You'll need to address the Wolves, too."
    "Niall nods, but is otherwise staying silent. Must not have anything to add."
    tan "I plan to. Let's just take this one day at a time."
    "Your companions agree, and the rest of the day passes without much to note, organizing relief for families who had lost someone, touring to see damage, and preparing for the somber festivities of the morrow."
    scene black
    show text "Coronation\nKing's Hill" at truecenter
    with fade
    pause 2
    hide text
    with dissolve
    scene bg kinghill
    with fade
    play sound "sound/rainloop.ogg" fadein 1.0 loop
    "The King's Hill is a hilltop with an old passage tomb of earlier men of Ireland, before even the Gaels."
    "Your clan wasn't sure who the tomb belonged to, but you always thought it was perhaps the tomb of the Hound of Ulster himself."
    "The images inside are too faded to tell, anyway, but it certainly was grandiose enough. Perhaps you just want a connection to that legendary hero."
    "For your tuath, it is a place to sit in the presence of the ancients, those who had ruled this land long before your family."
    "Often, relics of your family are left here to leave a mark, but the bones interred were never disturbed."
    "Today, you sit in silence and wait. Wait for what, you aren't entirely sure."
    "Dressed in golden and silver ancient gear of royals, including a long out-of-style torc, a short, heavy yet soft cape of reddish-purple material, and a stately silver coronet of much more recent make."
    "You can see why, the band of jeweled gold was heavy as the hells on your neck. You let the cape fall back as well. Sovereignty may be in the material possessions, but these were not yours."
    "As you wait, nothing continues to happen, save the gentle drone of rain outside. At the very least, it was a calm, warm rain."
    "The ceremony has gone well, so far. All the religious leaders of the tuath have been happy enough to help anoint the new rightful [king]."
    "But still, you're nervous, uncertain."
    "You have to give a speech once you set foot outside, something you aren't sure you're ready for yet."
    "So, instead, you pull out the sword Niall prepared for Conn the day he was killed."
    "The blade had been snapped in half during his struggle, the jagged iron a more wicked edge than any human could craft."
    "You had taken it from the scene, and now laid it, with cloth from both Aengus and Conn tied to its hilt, in one of the reliquaries of your family."
    "A silent prayer, and you turn around to leave the tomb. You were only to spend an hour in here anyway."
    play music "music/Come_Little_Children.ogg" fadein 1.0
    show morrigan at right
    show macha at left
    with dissolve
    "But as your eyes alight on the stone bench you'd been sitting on, two strange women are resting there, watching you."
    "One of straight, raven hair streaked with grey, with pale skin whiter than any snow you'd ever seen, and eyes as cold as the winter sun."
    "She wore similarly dark cloaks, no instrument or pack evident on her person."
    "She seemed the older of the two, but not without vitality."
    "The other, fiery red curls and amused expression, her skin pale but sun-kissed, with freckles spattered across her nose and cheeks."
    "She, on the other hand was dressed for battle. An old-looking sword was at her hip."
    tan". . . Are you two visitors? You don't seem familiar to me."
    "The red warrior answers first."
    macha "Interestin' indeed. Weren' we expectin' this one's brother?"
    morrigan "Certainly. He was the older. But, and I doubt you noticed, he has passed on to be in the otherworld."
    tan "News travels fast, it seems."
    morrigan "In my circle, yes. My cousin's not so much."
    macha "Oi, just 'cause you fly 'round the land, doesn' mean I don' keep up."
    macha "This happened within the week, we just got here."
    morrigan "And I of course, arrived early. Not quite early enough."
    "Your eyes narrow and flit between the two. Something is weird here. The weight of their words is off. Those eyes of theirs. . ."
    tan"You aren't human, are you? Was Conn gonna meet up with the local fae to bless his reign?"
    morrigan "Something akin. But I was always coming to meet you, [tan]."
    tan "You. . ."
    "She cuts you off with a wave of a hand. Your mouth shuts of its own accord."
    morrigan "Yes, I know your name. I believe you saw me as you were returning to Cnoc bhFianna?"
    "It hits you, and you resist the instant urge to kneel. Your skin crawls, and her thin lips curl into a knowing, birdlike smirk."
    tan "The Morrígan."
    $morrigan = Character("The Morrígan", color="#000000")
    "She nods, and her companion stands up from the bench laughing a belly laugh fit for a giant."
    macha "Are yuh people so confused you don' recognize royals of the Goddess at first sight? Ya silly child."
    "The boisterousness, and energy. Red hair..."
    tan "Macha?"
    $macha = Character("Macha", color="#bb0a1e")
    macha "Aye. And that lass behind you is Ériu."
    tan "Behind. . ."
    show eiru with dissolve
    "You turn, and indeed, a woman of golden hair, with matronly looks and a loving gaze is watching you. And same as the other two, her eyes are the same oddity of the awakened Tuath Dé Dannan."
    "She smiles and rests a hand on your shoulder. Where did she even arrived from?"
    "Three goddesses of sovereignty. Attending your coronation. What kind of sign could that be interpreted as?"
    "Perhaps ill, due to the warlike nature of Macha and the presence of the psychopomp [morrigan]."
    tan "My reign is not going to be an easy one, is it?"
    macha "Would t' be a fun one if it wasn't?"
    morrigan "No, in short. The world is changing, as [fmb] told you. He asked us to attend here and confirm your geas."
    tan ". . . My geas? The one I already broke?"
    morrigan "No. You did help him. Even if he perished, you did your utmost to aid in his final days and sent his soul to the otherworlds."
    tan "So, I'm not cursed."
    eiru "Not necessarily. Many mortals are cursed, and even we can miss the magic of other divines."
    tan "Worrying."
    morrigan "You will not die for a long time, unless from your own stupidity. Mortals are funny like that."
    morrigan "But first, the geas. Your reign will be long and prosperous, but should you be idle and wasteful, the fortunes of your family shall be undone."
    eiru "You shall have a great influence over the course of soon-to-be events in my land, yet the role is yet to be determined. Ruin shall follow you regardless."
    macha "Y'warrior heart is unparalleled, n' ya shall spill much blood to defend yuh home. But not without personal loss n' strife."
    morrigan "Death shall be your companion in life. To take on another shall invite her wrath."
    tan "Okay that one seems strangely specific."
    morrigan "Prophecies can be such. Fintan has only given us those. You may find others."
    morrigan "But we must leave. Reign well, child of the night."

    scene bg kinghill
    with flash
    stop music fadeout 1.0
    "And the room is filled with a violent flash of light, any questions you had for them wiped far away."
    "All that is left is a single feather of black and red resting where the Morrigan sat."
    play music "music/Legend.ogg" fadein 1.0
    "As many times in your life, you are left without proper answer."
    "Perhaps you will find one, someday, but for now, you hear a familiar voice calling."
    sean "[king]! It's been a while, you didn't crack your head, did you? You don't even have a [heir] yet!"
    tan "I. . ."
    "Your voice cracks, and your eyes look around the room."
    "They pull out the shape of a triumphant warrior on one of the walls, before you finish your sentence."
    tan"I'm on the way. Do not worry."
    "Gently, you stow the raven feather away in your cloak. You re-don the cloak and step out towards the light and your friends."
    "You feel a new fire within you, even with your brother gone and your world changed, for the first time since then you feel like you're grounded."
    "Perhaps the gods had granted you some strength of theirs. Perhaps you've found your own. Either way, it's time to face your people."
    "Gathered around the hill, the tuath's people stand waiting for you. Some mill about and chat, but most simply waited."
    "A few thousand, a small but respectable tuath in all. When you step out onto the platform carved into the hillside, they quiet, and await your words."
    "You clear your throat, set a hand at the ceremonial dagger at your waist, and push thoughts of gods and ghosts from your mind."
    tan"We're here to celebrate my coronation."
    tan"I think we should celebrate many things, myself the least of them."
    tan "But, I cannot forget the events of the last few days. They fill my thoughts, almost to despair."
    menu speech1:
        "We've suffered much.":
            $speech1choice = 1
            tan"The last few years have been hellish, there is no doubt. First, the loss of the Old [king], then the raids and warfare that lead to the loss of my own mother."
            tan"Now We've lost my wonderful brother Conn. He deserved a long, loving and peaceful reign."
            tan"But those aren't the times we live in anymore, it seems. Ireland has always had raiders, but this has become something new."
            tan"The raiding styles of the Norse, to tear and destroy and despoil, have arrived again."
            tan"It may be Gaels this time, but it has the same outcome. I and my warriors will be here to protect you as actively as we can. I will not let any of you suffer like this again."
        "We're still strong.":
            $speech1choice = 2
            tan"We've lost many. Liam, Conn, Brigit, so many more. All members of our tuath who kept us strong and united."
            tan"We'll have to step up to cover for the losses in short term, but I think we can recover. We're still alive, and still strong."
            tan"Strength is important. It's one of the few things that keeps us all safe."
            tan"As nice as it would be to be peaceful, that isn't the world we live in."
            tan"We are still strong, despite the grievous losses recently. We will recover."
        "We have each other.":
            $speech1choice = 3
            tan "So much has happened and so much has been lost. We need to find our center again, and come together as a clan, as a family."
            tan"We only have each other. We can rely on each other and grow together. Liam, Brigit, both were key figures in the family of our tuath."
            tan"We should honor their willingness to aid the tuath and its people."
            tan"We should be more like them, I think."
            tan"It is the very least we can do to honor them."
        "Our spirit isn't broken.":
            $speech1choice = 4
            tan"We are a defiant, strong tuath. We may not be mighty as the Ui Niell, or the kings of Dyflinn, but we are mighty in spirit and will."
            tan"Even the great losses we have experienced won't change any of that."
            tan"I know us, I have watched our tuath live and grow and prosper. We refuse to bow or be broken by hardship, but double down and persevere."
            tan"We have wills of steel, wills of oak, and wills of the untamed oceans. Nothing can break us."
            tan "We will continue to grow and be strong, defiant, and outlast our enemies. This I will swear, lest the earth swallow me and the sea wash away my works."
        "We can defeat our enemies.":
            $speech1choice = 5
            tan "We have suffered one indignity too many now. We must strike back like a cornered wildcat."
            tan "We can't continue to be tame kine, unwilling to retaliate to an abusive cowherd."
            tan "These raiders, these wolves of men, is the last straw. We have been pushed around by all our neighbors for generations."
            tan"Why shouldn't we be the ones to push them? To rule them? We have just as much right to soverienghty as anyone."
            tan "And by my rule, I swear we shall pursue it."
        "Only the future will matter.":
            $speech1choice = 6
            tan "We must look forward."
            tan "Buoyed by the grievances of the past to strive for great accomplishments."
            tan "As much as we will miss our loved ones, those we have lost, they will not come back."
            tan "The best way to honor them is to strive and grow."
            tan "We can be mighty, but not by holding onto a lost past."

    tan"About those raiders, the Wolves? I only have a few things to say about those scum."
    menu speech2:
        "The Wolves must be put down.":
            $speech2choice = 1
            tan"They are animals. Terrible and awesome, the wolves will destroy our way of life if they're left to it."
            tan "They must be killed. They are a threat not only to us, but the rest of Ireland."
            tan"So they should be put down like the wolves they are."
            tan"I swear by the gods my people swear by that I will hunt them down, avenge our people, and kill their leaders. The monsters will be slain."
        "We shall watch for them, but not seek them.":
            $speech2choice = 2
            tan"They are a threat but should not be our first priority. Seeking them out could invite destruction upon us again."
            tan"We will be vigilant. The dear departed headman of the farming village had warned Conn about raiders, and we took it lightly."
            tan"We should not do so again. The fiann will be more responsive to such threats."
            tan"Any note of antlered raiders will be watched carefully."
        "We must be better than them.":
            $speech2choice = 3
            tan"They are monsters, yes. But monsters are just that, and nothing more."
            tan"We should not lose ourselves seeking out retribution for the dead. A blood feud may be satisfying in short term, but we'll loose more than we gain."
            tan"We will be better. Our ancestors knew it was best to create, not destroy, when we gave up raiding to settle here."
            tan"So we shall continue to be better than raiders, but never complacent."
        "They are just raiders like any other.":
            $speech2choice = 4
            tan"These wolves will ultimately die. The life of a perennial raider is a meaningless one!"
            tan"So, they are ultimately nothing special. Nothing but men who think they can abuse and steal for a living without adding to the body of society."
            tan"I'm honestly sad for them. They will not be remembered, while what we build here shall be remembered."
            tan"They're a sad, sad group, playing at importance and doomed to the ash heap of history."
        "Our future will not be held back by them.":
            $speech2choice = 5
            tan"We have already survived their attempts on our lives."
            tan"We won't be caught unprepared again. We have experience of their tactics and what to look for."
            tan"Our future as a tuath will not be held back by raiders who think themselves powerful for adorning their trophies."
            tan"Ultimately, we will be the triumphant ones, looking forward into the glorious future."

    tan"But I think. . . For my reign, this first part at the very least, I shall swear at least one thing."
    menu speech3:
        "Vengence.":
            $speech3choice = 1
            tan"The Wolves, Mugdorna, the others, they've wronged us. It is about time we get even for the harm."
            tan"We will not rest until the world knows to cross our tuath is to invite death."
            tan"This I swear to you, my people."
        "Justice.":
            $speech3choice = 2
            tan"We have suffered grave injustices, not only at the hands of the Wolves, but at our neighbors."
            tan"We must call down the might of law against our enemies. Make them responsible for the damage they have done."
            tan"We are justified, and we shall have justice."
        "Strength.":
            $speech3choice = 3
            tan"Strength of will and arms is ultimately what matters in this world. We need more of both."
            tan"The raids and vulnerability of previous reigns must end."
            tan"Our fiann is our might, and I think we should start to flex it, to train it. I'll make us conquerors again."
        "Honor.":
            $speech3choice = 4
            tan"Honor is what matters to a king. I will do my duty to the best of my ability."
            tan"Trust me to be honorable, even if I may not have always been so in the past."
            tan"If you do, I swear by the gods of earth, sky, and wave that I will do right by you all."
        "Prosperity.":
            $speech3choice = 5
            tan"Trade. Prosperity, and happiness. Our home is a crossroads of nations, we should take advantage of this."
            tan"We may not have the numbers, but position and resources are just as important."
            tan"If we grow our trade network we can grow just as strong as Dyflinn."
        "Unity.":
            $speech3choice = 6
            tan"The tragedies of the recent days and what I've seen in recent seasons within our tuath tells me we are increasingly divided."
            tan"We are blood, siblings, family. It's inexcusable to be so divided! We can do better."
            tan "I can do better. I've been victim of this same sectarian tension. I have plans on how to solve this, and I'll do my best to."
        "Faith." if faith != 4:
            $speech3choice = 7
            if faith == 1:
                #gaelic
                tan "I know our path forward, and it should be in our ancestor's steps. Ireland is Gaelic land. It should stay such."
                tan "The Fae can be our allies, the druids our advisors. We should heed them both."
                tan "Join me in this path, and we shall honor our ancestors."
            elif faith == 2:
                #christian
                tan"The Highest can protect us. He is strong, mighty, and loving. The god of the Christian monks can aid our tuath greatly."
                tan "The monks even have many allies across Ireland and beyond. A network of faithful."
                tan"Join me, and the tuath will be more united than ever, in faith and blood."
            elif faith == 3:
                #Syncretic
                tan"Unity in faith will keep our home strong. We have people following every creed of this island, yet I see arguments almost every day."
                tan"That needs to change. There is a place for every god, every faith, in this tuath."
                tan "It just needs to take us sitting down and talking, rather than immediate defensive reaction to some unknown offense."
            elif faith == 5:
                #norse
                tan"Perhaps the new gods will be stronger than our native ones. I've found strength falling back upon my Norse heritage."
                tan"Plenty of you do have said heritage too."
                tan"Even if the other gods dislike it, I hope to find strength in the ones of my father, strength enough to defeat our enemies."
                tan"For our home needs aid, and my father's gods could provide."
    tan"I shall provide and aid you all. Your troubles are my troubles. Your gods are my gods. I will be your [king], your parent, your confidant."
    tan "Trust me to rule, keep me to rule right, and the tuath shall grow and prosper again."
    tan "And our dead will smile on us and bless us."
    "The crowd initially, is quiet, as if waiting for a bit more. You grow nervous, wondering if you said something wrong."
    "But they cheer, a roar growing and nearly making you stumble backwards. The desperation evident in many of them, they'd have cheered anyone willing to step up as king, you think."
    "Séan rests his hand on your shoulder."
    sean "Good job, though I say I'd give a bit of a better speech myself."
    aoife "Shove off, bard, you know you wouldn't."
    sean "Fiiine. Great job, [tan]."
    "You smile, and nod. At least now, all that remained for the day was a feast."
    "And a feast would be a good time to relax from the hardship and strangeness of the last few days."
    "You turn back to the crowd and raise both hands."
    tan "And now, it's time for the feast! Last one to arrive gets the gristle!"
    "You wink, and grin widely, trying to show you won't be all seriousness."
    "Hopefully, you'll have plenty of more chances to show your worth to these people."
    scene black
    with fade
    show text "End of Act One" at truecenter
    with fade
    pause 2
    hide text
    with dissolve
jump work_in_progress

menu nickReChoice:
    "My byname will be..."
    "From my heritage.":
            if heritage == 1:
                "Because I aided my father in the fields, I started being called a sheepdog. My nickname is Caorach."
                $tan = Character("Caorach", color="#006400", image="player")
            if heritage == 2:
                "While dad taught me some of his hunting skills, I was more distracted with picking up sticks than the bow. He started calling me Twig."
                $tan = Character("Twig", color="#006400", image="player")
            if heritage == 3:
                "I inherited the pale hair more common of the Norse, so I was given the byname Fionn, pale-haired."
                $tan = Character("Fionn", color="#006400", image="player")
            if heritage == 4:
                "My father had plenty of manuscripts and books for me to read through. I started being called a Leamhan! A Moth!"
                $tan = Character("Leamhan", color="#006400", image="player")
            if heritage == 5:
                "I inherited Dad's energy and drive, and he couldn't help but compare me to his favored instrument, a fiddle. So I became Fidil."
                $tan =Character("Fidil", color="#006400", image="player")
    "From my childhood.":
            if childhood == 1:
                "The Ri saw something special when he trained me. Before he died, he started calling me Fáil, Destiny. I wonder what he saw."
                $tan = Character("Fáil", color="#006400", image="player")
            if childhood == 2:
                "[td] often lamented my independent streak by calling me a wildflower. I took the name as my own."
                $tan = Character("Wildflower", color="#006400", image="player")
            if childhood == 3:
                "[tb] was a straightforward man. He simply called me Iron, because he saw me as dependable."
                $tan = Character("Iron", color="#006400", image="player")
            if childhood == 4:
                "Liam couldn't help but compare me to a deer, fia, when he saw my long loping run to chase down animals. It seems apropriate to honor him by using it."
                $tan = Character("Fia", color="#006400", image="player")
            if childhood == 5:
                "I wouldn't, even for a moment, stop asking [fp] about the Fae and Gods. She started calling me Sí Cara, fairy-friend, within the week."
                $tan = Character("Sí Cara", color="#006400", image="player")
    "From my training.":
            if training == 1:
                "My fellows in the fiann knew me for my wit as well as my skill with a blade. They called me Witty, Scéalta."
                $tan = Character("Scéalta", color="#006400", image="player")
            if training == 2:
                "While working with the circle, I was known for my wisdom despite my age. They began calling me salmon, bradán, after the fish of knowledge."
                $tan = Character("Bradán", color="#006400", image="player")
            if training == 3:
                "Rianaigh is the name I earned while training as a ranger. I was a quick study at tracking and wayfinding, so they honored me for it."
                $tan = Character("Rianaigh", color="#006400", image="player")
            if training == 4:
                "My training in forges and pottery and other strenuous fields made me strong, so folk began calling me strong-arm, géagláidir."
                $tan = Character("Géagláidir", color="#006400", image="player")
            if training == 5:
                "Ironically, the name I got learning to be a poet wasn't very creative! They started calling me the Young Poet, An Fhéile Óg."
                $tan = Character("An Fhéile Óg", color="#006400", image="player")
    "From my rite of passage.":
            if rite == 1:
                "For my struggles in our arena, I began to be called a champion, a Curadh! I quite like the name."
                $tan = Character("An Curadh", color="#006400", image="player")
            if rite == 2:
                "With my contact with the Gods, I have a new reputation as one who follows them, a Godseeker."
                $tan = Character("Godseeker", color="#006400", image="player")
            if rite == 3:
                "Even though I failed by task, they began calling me a hunter, sealgair, and the title stuck."
                $tan = Character("Sealgair", color="#006400", image="player")
            if rite == 4:
                "I built a storehouse, people started calling me The Builder, An Tógálaí. Pretty simple."
                $tan = Character("An Tógálaí", color="#006400", image="player")
            if rite == 5:
                "The people called me Storyweaver once the new tale settled. I must have impressed them enough!"
                $tan = Character("Fíochán Scéal", color="#006400", image="player")
    "Something Unique":
            "The name I'll go by won't be something tied to my past, but dedicated new future."
            python:
                tan = renpy.input("Enter your nickname:")
                tan = Character(tan.strip(), color="#006400", image="player")
                if not tan:
                    tan = Character("Iora", color="#006400", image="player")
jump afternick
