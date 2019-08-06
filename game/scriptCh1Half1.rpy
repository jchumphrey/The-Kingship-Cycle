label chapter_one_half_one:
    show text "Act One: Coronation\nÓ Durcáin Tuath, 974 AD\nMorning" at truecenter
    with dissolve
    pause 2
    hide text
    with dissolve

    stop music fadeout 1.0

    play music "music/The_First_Steps.ogg" fadein 1.0

    label ch1_part1:
        show screen virt_comp_overlay
        label home:
            "The firepit and [fmb] fade from view, along with the sense of peace and comfort it had brought you."
            "Your eyes take a moment to adjust to the light filtering in."

            scene bg home
            with fade

            "The familiar wood and stone of your home dyed warm by the sunrise greets you. While small, it was cozy enough for your unmarried and unproven status, with possessions arranged just how you enjoy."
            "Well-made wooden furniture dot the rectangular home's one room:"
            "Your straw bed made more comfortable by heavy quilt and pillows,"
            "A few chairs, one pointed to the slit window facing outward from the hillfort that let you see out past the village,"
            "A set of drawers for clothing and affects, completing the -"
            ". . . . . ."
            tan"[sean] what in the name of the tuath god are you doing in my house?"

            show sean
            with dissolve

            "[sean], the Rose of the Ó Durcáin. A friend from childhood, claimed to be a distant cousin. Always a prankster, mischievous, and a bard like his father."
            "His hair was a messy shock of blond half-tied back into a ponytail, his eyes as emerald as Ireland. He usually wore some of the flashiest outfits you'd seen in Eire. All color and style and soft fabrics."
            "Honestly, you had no idea where he got the money for it, but you did have to admit he always looked good wearing them."
            "For some reason he was staring at your wall, that just happened to mean he was standing on top of your best chair."
            sean"Why, I swear I felt a draft while I was fetching you for the [king]."
            tan"A... a draft? Wait, you're burying the lead, what does Conn need with me?"
            sean"Oh, I can't quite remember. He told me to fetch you last night, but then there was that drinking-contest-turned-hunt-turned-"
            "He suddenly cuts off, eyes looking off into nothingness above your head. Then laughs and taps his head like he just had a realization."
            sean "There it is!"
            "The bard takes a bit of wood from... somewhere (Why did he have that in his pockets?) and a hammer with a few nails. [sean] begins patching your wall like he wasn't just in the middle of a conversation."
            tan "Séan!"
            sean "Hmm? Wrrt dough you mead?"
            "He mumbles through two nails held in his mouth."
            tan "Conn needed me... last night? And you're only getting here now?"
            "Séan removes the nails, hammering in the last one into the wall. His work is very sloppy, and its actually a bit aggravating. You decide to fix it yourself later, if there even was a problem."
            sean "Well no, I fell asleep here last night."
            tan ". . . . What."
            sean "Well, you looked like you were having an important dream, so I didn't bother you. Why do you think I noticed the draft?"
            tan "Because you're a bit daft and distractible?"
            sean "I think you mean brilliant and perceptive!"
            "You sigh slowly but drop the topic for something more relevant."
            tan "Okay, so was my brother's task time pressured?"
            "His posture shifted, a bit more serious now. His dagger slipped from his belt, and he twirled it on his fingers. The man could never stand still for more than a moment."
            sean "Just preparations for the ceremony, friend. I get you to him, and I'll tag along to help, make up for the intrusion, good?"
            tan "Acceptable."
            "You grumble and he beams. The bard claps a hand to your back as you stand up out of bed."
            sean "Excellent. Now let's get going!"
            "He waves for you to catch up, already on his way out the door."
            tan "Séan! I don't even have my britches on yet!"
            sean "Excuses, excuses!"
            "[sean] strides out, immediately getting locked in conversation with a passing farmer from the border region with Armagh. The farmer's uncertain at first, but Séan's charm seems to win over his interest soon enough."
            "Sometimes, you wonder why you're still his friend when he stumbles from trouble to trouble. He'd probably lose his head without you, though."

            show text "{b}{color=#FFFFFF}[sean] has joined your fiann, improving your Fili and finesse!{/color}{/b}" at truecenter
            with dissolve

            $ Fili += 2
            $ Finesse += 1
            if renpy.in_rollback():
                $ C_sean = False
            else:
                $C_sean = True

            pause 1.5
            hide text
            with dissolve

            scene bg village
            with fade
            "Once you manage to pull Sean away from the farmer, the two of you set off on the way to the King's Hall."
            "The morning is quiet. The occasional birdsong carries on the cool autumn breeze that rustles the green grasses and leaves of trees around you."
            "Your home on the edge of the walled part of the village hillfort means you'll be walking for a good while to get to the King's Hall on the hilltop. Another wall separated it and the squat keep from the rest of the town."
            "The inner circle was usually restricted to the [king]'s closest family and their fianna unless it had been officially opened for feasts."
            "Of course, petitioners were given access, but the fénnid at the gates ensured their lack of weapons."
            "In the next few days, however, the quiet little village would become bustling and busy."
            "With the ceremony and celebration tomorrow people have been focusing on preparation over normal business."
            "While most of the food and trappings will come from the [king]'s coffers, as was tradition, but the nobles and people would provide as well."
            "The whole tuath comes together for feasts and celebrations. While nothing compared to the great feasts of Tara, the tuath's thousand or so residents would still be in and out of the [king]'s village over the next three days."
            "So, you knew to appreciate the quiet of the few hundred people that lived inside the village walls."
            "You knew it wouldn't last long."
            "You let out a long sigh as you lead the way, [sean] raising an eyebrow but not questioning it."
            hide sean
            with fade

        label medb_padraig_feud: #A feud between religious leaders.
            stop music fadeout 1.0
            play music "music/Village_Fair.ogg" fadein 1.0

            "As you and Séan approach the town market, the sound of shouts from the small chapel flanking the market draws your attention."
            "A few people watch as the wise head of the local Druids, [td], verbally spars with [tp], a priest sent from the Christian center of Ireland due to the Tuath's proximity."
            "The two never had gotten along. Theology and personality made them clash, and it often annoyed many in the Tuath."
            "Faith in the old ways and faith in the Lord of Christianity weren't seen as exclusive by many in Ireland, but for [td] and [tp] compromise was hard to accept."
            td "Your god, as I have said before, is naught but an over-righteous deity of a people not native to these isles."
            tp "The almighty knows his power, and your 'gods' are but devils whose power will be revealed as pale compared to the Lord's."
            show sean
            with dissolve
            "Séan sighs heavily, obviously annoyed."
            sean "Must they fight? I see no reason why they cannot find common standing."
            "Medb overhears Séan, and gives a wide, frustrated gesture."
            td "If this zealot admitted his god is not superior to ours, he could perhaps find better luck in convincing me of his good intentions."
            td "All I see is a man who forsakes the ancestral ways for the glamour of some distant dead man's god."
            tp "Christ was God incarnate, he was more than just a man. Rome's oppression of our faith has only hardened our resolve, and we have indeed outlived them in the holy land."
            tp "And your ancestral wisdom is not something certainly true itself. My fellow scholars of the Armagh school have found dozens, if not hundreds of variants of the same stories across Ireland."
            td "And does your own faith not have its disagreements?"
            tp "The Word of God is preserved in text passed directly from His lips to mortal minds. Any discrepancy is purely mortal misunderstanding of God's Will."
            td "Truly you claim inspiration of the divine mysteries? What a load of shit."
            "They continue to argue, the initial crowd it drew peters out. While a shouting match often drew a crowd, the lack of an ensuing brawl convinced the villagers to simply go back to business."
            "Eventually, Medb and Padraig pose you a question:"
            td "As [heir], you must have your own opinion on the matter."
            if rite == 2:
                td "You had experience with the gods themselves, not even a few months ago. Surely you understand the importance of our heritage."
            elif heritage == 4:
                tp "Their father must have raised them Christian, as any priest would have."
            elif training == 2 or childhood == 2:
                td "I did educate you on the Ways of the Elders, child. You must see their importance."
            tp "Please, you have attended rituals at the nemeton and chapel, which did you find more alluring?"
            sean "I've made my position clear, but I'm curious about your take myself, [tan]."

            menu religious_choice:
                tan "Well, for me..."
                "I prefer the Ways of the Elders.":
                    tan "Our ancestors have pacts and agreements with the Tuath Dé Danann. We should honor them and keep to the Elder's faith and druid's teachings."
                    "Medb gives a look of superiority to the priest, who mumbles something annoyedly."
                    td "I'm glad you have a good head on your shoulders."
                    $faith = 1
                "I prefer faith in the Highest.":
                    tan "I have faith in the Highest, and seen miracles worked by His priests in Armagh."
                    tan "Ireland should follow His Word to find salvation."
                    tp "The future of Ireland is in its children, and if they are His children they will prosper!"
                    "The priest announces, throwing hands into the air reverently."
                    $faith = 2
                "There's a place for both in Ireland.":
                    tan "I agree with Séan. The people of Ireland have always been mixed, why can't our faith support the traditions of both?"
                    "The two give mildly disappointed looks, but don't raise much of a fuss. It isn't like you took an unpopular position in Ireland."
                    $faith = 3
                "I don't put much stock in gods, period.":
                    tan "They have never helped me, so I see no reason to help them. Making my own path is the way of a true Irishman anyway."
                    "Both have a look of distaste. An agnostic approach to life, spurning the domain of any gods, was obviously not a choice they appreciate."
                    tp "Heathen."
                    td "May you never confront them with such an attitude."
                    $ Honor -= 1
                    show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $faith = 4
                "My father's gods are strong, so I follow them." if heritage == 3:
                    tan "Odin's host and the traditions of the Norse have served them well in their campaigns across the Northern Sea and Europe."
                    tan "Why should they not serve me well in Ireland?"
                    "Medh seems a bit more accepting of this, given the Norse proved more amenable to Irish traditions and working with locals."
                    "Padraig, however, is aghast."
                    tp "Those {i}barbarians{/i} nearly destroyed Armagh and have ravaged monasteries throughout Europe! God will smite them, and you, soon enough, I swear to you."
                    $ Honor -= 1
                    show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $faith = 5

            if faith == 3:
                sean "Glad you agree, [tan]!"
                sean "Ireland shouldn't be stuck in the mud seeking out a single theology or way of life."
            else:
                sean "I can respect that, myself. I have no issue in differing opinion, unlike some."
                "He gives a look in the direction of the feuding religious figures."
            "You sigh and turn to start leaving now that that business is concluded. The two holy people turn attention away from you now that you have answered."
            tp "If the manuscripts were not scattered by the Norse, I assure you Armagh would have converted the whole of Ireland by now."
            td "Wishful thinking. Perhaps those manuscripts and the collated stories of Ireland would have convinced them in the power of the Tuatha Dé?"
            tp "A righteous Christian would not be swayed to heresy, Matron."
            td "A wise person would be open to the truth, regardless of its confirmation or denial of their worldview."
            "You take your leave, continuing your trip towards the King's Hall. With the market behind you, the central walls were visible down the road."

        label to_hall_1: #a little scene between the church and Smithy

            scene bg village
            with fade
            "With [td] and [tp] continuing their debate behind you (as if they would ever finish, the two only bickered more as they aged.) you continue towards the King's Hall."
            "The pleasant, clear sky, the sounds of a busy town around you and of the birds in the sky."
            "The rhythm of life in the Tuath flows around you while on the way to the King's Hall."
            "It's almost relaxing."
            "But of course, your friend always finds ways to put his own spin on the morning."
            show sean with dissolve
            "[sean], following along behind you, begins whistling a jaunty tune. The bard just about pulls his fiddle from his bag before you stop him. No time for distractions."
            sean "Quite the buzzkill this morning, aren't ya?"
            tan "Would you be if you woke up with a friend telling you you're late to meeting the [king] among other revelations?"
            sean "Perhaps, but it's also hospitable to help your friends if they're too drunk to make it to their own home!"
            tan "I can still be annoyed at not being given the choice to give hospitality. I couldn't even make you dinner, nor ensure you a proper bed to sleep on!"
            sean "See, you do care!"
            "You concede with an eyeroll. Of course you care, he's a good friend."
            tan "Doesn't mean you aren't an asshole at times, Séan."
            sean "I'm still the most popular bard in town!"
            tan "You and the old timers, not much competition."
            sean "Well, you'd be decent would you apply yourself."
            "Oh, not this again. Must he bring this up every week? Maybe he was under geas to sell his profession."
            if rite == 5:
                sean "By the gods of our people your rendition of the Wasting was quite a piece. I especially loved the music you put to it."
                sean "Why haven't you made more like it?"
                tan "Time, needing to learn rulership, any number of things. Maybe I'll pick up verse again someday, though."
            elif training == 5:
                sean "You even went through all that training under the old guard. Will you just waste it, [tan]?"
                tan "I doubt it. We noble-blooded should be well-rounded anyway."
                sean "I expect the occasional poem, at the least!"
                tan "Someday, [sean], someday."
            elif childhood == 5:
                sean "What about growing up under [fp]'s guidance? Didn't you learn anything from her?"
                tan "A lot of recipes for how to prepare food, the occasional revelation from the Gods, and astronomy."
                sean "The poet didn't teach you poetry?"
                tan "Insults set to rhyme, mostly."
                sean "Odd."
            elif heritage == 5:
                sean "Did [dad] teach you nothing while raising you?"
                tan "No, father was often too busy seeking out new folk to hear his songs to put finer details into raising us."
                tan "Maybe a bit, but I was but a kid."
                sean "Some might be jealous of such a hands-off childhood. Me, not so much."
            else:
                tan "As adept as a fish who attempts to swim through earth, [sean]."
                sean "Poetic and proving my point."
                sean "Shan't need training to become a creative, my friend."
                tan "You do need the drive, however."
            "You and Séan idly spoke as you continued. Not about anything specific, but at least it was friendly."

        label smithy_morning: #Meeting Niall, deciding preferred weapon.
            "It wouldn't be long before you passed by the home of [tb], the town's blacksmith and mentor to another friend of yours, [niall]."
            "Niall, his byname evoking his use of hammers in combat, had apprenticed at the smithy since he was a child."
            "Niall had been an orphan, so Conchobhar had raised him."
            "He was decent looking, not quite as dashing as [sean], but he was built sturdy and strong, enough for anyone in the tuath."
            show sean at left
            with dissolve

            "Before you can stop him, [sean] already bounded his way to the wide door where smoke and heat belched into the surrounding village."
            "The furnace room and metallurgic workshop sat open to the public, but most steered clear of the acrid cloud unless they had business."
            sean "[niall], you big brute, put your namesake down and let's catch up!"
            niall "Christ-in-heaven, [sean], do you have no sense of timing."

            show niall at right
            with dissolve

            "The brown-haired smith glowers at the shorter bard as you turn into the open doors of the furnace room. Niall was built like a stone wall and could probably rend one to pieces by himself anyway."
            "Turns out, Niall and his master had been having a bit of a conversation about the best weapons to use in battle."
            "Naturally, Niall was of the mind that the bigger the better. His warhammer a great example of such excessive force."
            "Conchobhar believed in fitting the weapon to the battle. You wouldn't fight a Norseman without something to crack armor, nor a man of Pictavia without a spear to match his own."
            tb"Spears for me. Hitting your target is more important than great strength."
            "While they'd continued working, Séan's arrival had thrown a branch through the cart's spokes. Niall was distracted"
            niall "What was I- Right. [tb]! If you bring a big enough weapon, you never need to worry about figuring out which to use."
            niall "Viking armor cracks under hammer blows the same as it was made under them, and snapping the haft or blade means they can't retaliate."
            tb "So crude. You leave yourself open, rushing in with heavy hammer. A short jab through the side and you bleed the same as any stuck cattle."
            sean "Grim image, Conchobhar. I like it."
            "Niall grimaced. Despite his strength, he had never been one for combat. His weaker stomach for innards sees to that."
            niall "What about you, [tan]? What do you prefer? I can never tell given your training with so many."

            if Finesse > Might:
                $dexFighter = 1
            elif Finesse == Might:
                $dexFighter = 2
            menu weapon_choice:
                tan "My favored weapon definitely is..."
                "My own fists":
                    $weapon = 1
                    tan "Nothing more reliable than your own limbs, I say. No special training needed and save limb removal you always have a weapon handy."
                "Spears":
                    $weapon = 2
                    tan "I like having the choice of distance or ranged attacks. A spear paired with a shield, I feel unstoppable."
                "Swords":
                    $weapon = 3
                    tan"Swords are just a classic weapon. Simple enough, precise enough, deadly enough. Complete with a shield, and I'll cut down and army."
                "Axes" if dexFighter == 0 or dexFighter == 2:
                    $weapon = 4
                    tan"It may be unconventional, but I prefer axes. They prove useful against the heavier armor of the Norse, and smaller ones let me have a bit of range too."
                "Claymores" if dexFighter == 0 or dexFighter == 2:
                    $weapon = 5
                    tan"I love myself a big sword. Who needs defensive gear like shields when you can slice your enemy's own defenses in twain with but a few strikes?"
                "Bows" if dexFighter == 1 or dexFighter == 2:
                    $weapon = 6
                    tan"I like to fancy myself a bit of an archer. Nothing like striking down game from across a plain, without ever being seen."
                "Slings" if dexFighter == 1 or dexFighter == 2:
                    $weapon = 7
                    tan"I go more traditional, my preference lies in slings, like Cù Chulainn. I'll also never run low on ammo, unlike a bow."

            niall "Hrmph. Not my choice, but okay."
            sean "Niall, you carry a blacksmith's hammer into battle, you have {i}no{/i} room to talk about weird weapon choice, friend."
            niall "Says you, bard-who-uses-knives."
            sean "Daggers! A knife slices bread, a dagger slices flesh."
            "The blacksmith's apprentice smirks. By now, the blacksmith gave up participating in the conversation and set back hammering out a new sword blade."
            niall "Oh, so you've taken up cooking for the tuath? I didn't know Old Brigit accepted apprentices as old as you."
            hide niall
            hide sean
            with dissolve
            "You sigh, a hand holding your forehead and massaging. Sean shouts back, drawing one of his blades and feeling the need to twirl and toss it to show his skill."
            "The two argue, and you step away towards where [tb] had resumed his work. He doesn't even seem to notice the bickering."
            tan "How's life, Conchobhar?"
            "You hazard a question, to pass time as the two argue."
            tb "Busy."
            tan ". . ."
            "No dice. Conchobhar was legendary for his laconic nature, the argument with Niall was the most you'd ever seen him speak at once!"
            tan "Work?"
            tb "Busy."
            "You glance over at your friends. Still bickering, now about... what the hell, how did they get to cheese?"
            tan "Right... The kids?"
            tb "Grown, not my business to pry."
            "You give up. You bid farewell to Conchobhar. He grunts. You sigh."
            "A moment later you're back with Niall and [sean]. The topic has shifted to something more sedate, preferred way to prepare rabbit."
            show sean at left
            show niall at right with dissolve
            sean "No no no, Niall. You have to cook the rabbit {i}before{/i} the stew, that's how you get the most of its flavors with the vegetables."
            niall "But then you'll overcook it."
            sean "I promise, you will not."
            tan "Doesn't Niall need to get back to work? You've been arguing for a half hour."
            niall "I do have to finish repairing the [king]'s blade..."
            "He mumbles a bit, thinking before turning back to his station, starting to kick the whetstone wheel back into gear."
            tan "We have our own errand for my brother, so we should get going too."
            sean "But, [tan], when was the last time we did anything with Niall?"
            "You pause. When was that... Samhain? No, maybe Beltane, a whole season ago? Gods, it had been."
            tan "Niall?"
            "You call out for him, pulling him away from his work once more."
            niall "Aye?"
            tan "Hey, if we go hunting later, we'll come grab you. I don't know what job my brother has for me, but if its something you'd enjoy...?"
            "Niall nodded his assent."
            niall "A plan it is, then. Now, I need to finish this blade, the [king]'d be lost without it."
            "You give Niall a firm embrace before taking your leave of the smithy."

            hide niall
            with dissolve

            "After the distraction at the smithy, you realize you've dawdled enough. No more distractions before the King's Hall."
            "You keep Séan moving, almost half dragging him behind you! But it was his fault you were late to begin with, so you felt just a bit less guilty about the rough treatment."

        label hall_debate: #introducing the politics for later.
            stop music fadeout 1.0

            play music "music/Hail_to_the_King.ogg" fadein 1.0

            "It isn't hard to convince the guards of the inner wall to let you through. Though the high wall is intimidating as ever, the two guards on duty are less so. Activity and shouts come from inside, but nothing out of the ordinary."
            "Both are young, people you grew up with. Hell, one of them is three quarters of your height, without facial hair, and looking like he hadn't finished puberty."
            "He clears this throat, and speaks in an authoritative tone, as much as he could muster."
            "Guard" "Weren't you meant to be here last night, [tan]?"
            tan "Long story involving [sean]."
            "Guard" "Right. Get going."
            "You and [sean] walk through the courtyard. The largely open field is the same as it has been since your childhood."
            "The 'keep' being a glorified stone house with a heavy door, extra floors and places for archers. Impressive enough, but the fortifications of Dyflinn spoiled you."
            "The rest of the space is taken up by training yard, practice range, and two main buildings."
            "First in importance is the King's Hall, a long, well-built, and ornate building housing the [king]'s residence alongside the tuath's main feast hall."
            "The other building is a barracks for the Fénnid, the warriors of the royal Fiann. Better than your dwelling, but certainly more rugged than a noble's home."
            "The sound of people training and playing sports through the inner fields become much easier to hear without a wall in the way."
            "You make your way up the path to the Hall at the crest of the hill without delay."

            scene bg kinghall
            with fade

            "The first thing you notice after your entrance is your brother, [king] [bro], and your father, [dad], are discussing some of the rumors and news from outside of the Tuath."
            "Aside from the discussion, the mood in the hall is relaxed. A few fénnid watch the central fire and keep it lit."
            "They idly chat about nothing, make boasts they may or may not follow through with. His 'job' done, [sean] joins them with enthusiasm."

            show aoife
            with dissolve

            "[aoife], the leader of the king's fiann and wife of your brother, is tending to their child off to one side, gently rocking him in his cradle. With her free hand and legs, she works to polish her shield."
            "When she notices you, she gives a small nod but says nothing."

            hide aoife
            show brother at right
            show father at left
            with dissolve

            bro "With this news of the Uí Néill [highking]'s murder, the situation between the Uí Néill of Ulster and the Uí Ímair of Dyflinn has become dire."
            "You'd heard of the murder yourself, but it seemed too outlandish to have been more than rumor. But Conn was [king] so must have heard from other courts."
            "A dishonorable scene, the High King slain during this year's Samhain festival by a pair of drunken Norsemen, in the [king]'s own hall."
            "To add insult to injury, the Norsemen refused to pay the price of his death claiming it extortionate. The Norse king himself had even stated the [highking] must have been a poor ruler and warrior for two drunks to kill him."
            "Not only had the Uí Néill family been insulted and denied restitution, they took revenge by slaying the Norsemen when no silver was paid and declared a feud with the Uí Ímair dynasts ruling Dyflinn."
            bro "We're stuck between their domains, and war seems inevitable at this point."
            dad "We need to do something, at the very least ready defenses if we don't take a side."
            bro "Father, we cannot take a side so soon into the crisis. It'll be the death of us it goes poorly."
            bro "The last time we had a large-scale battle it killed the Old [king] and many of our old warriors."
            dad "I know, Conn, but..."
            "He pauses for a moment, collecting his thoughts with a hand on his forehead."

            if heritage == 1: #Traditionalist
                dad "We must keep to the old ways, Conn."
                dad "Letting the bastard Dubhgaill hold our lands, especially so close to Tara, is inviting trouble from the gods."
                dad "We side with the Uí Néill and prepare for war against Dyflinn. We don't take a move without word from our [overking] or the Uí Néill [provincialking]."
                dad "Preparation first, then siding with our natural allies."
            elif heritage == 2: #Warmonger
                dad "Take the example of Lugh, son. The Norse king proved himself a poor ruler by letting his subjects commit such a crime without reproach."
                dad "Take up the spear and smite the Norsemen, seize their cattle and lands."
                dad "We could make our Tuath a great one in the fortune of war, and the gods would be on our side."
            elif heritage == 3: #Work as a bridge, town is full of mixed heritage
                dad "You yourself are half-Norse, half-Gael. Why not serve to solve this crisis equitably?"
                dad "The Norse bring in trade from across the world. The Gael know this land."
                dad "If they work together, we could create a great kingship here in our homeland."
            elif heritage == 4: #Convert the pagans, increase ties with Armagh
                dad "Son, I give the same advice I gave your mother in life: Put your faith in the Lord."
                dad "If you accept baptism, we can increase ties with Armagh and the Culdees of Dál Riata."
                dad "Certainly that should help our position in Ireland."
            elif heritage == 5: #Peace first
                dad "I hate to see Ireland tearing itself apart over such pettiness. We need unity, and war won't bring that."
                dad "I propose we keep our hat out of the ring for as long as we could. If we don't, I dread what'll happen to our small kingship."

            bro "I'm not sure, [dad]. While your path could work, I do not know if it will."
            bro "As [king], my first thoughts need to be of the prosperity of my people, not some grand ambitions of my own."
            bro "If I rush into this, it could leave many dead without any gain."
            dad "It is a troubling issue, Conn."
            "There's a break in conversation. Neither has noticed you yet. Troubling topics for a pleasant morning before his official crowning."
            "Perhaps you could speak up, and give your own views? As the [heir], you do have a bit of a say in tuath politics such as this."

            menu speak_out:
                "Speak out.":
                    jump hall_opinion
                "Stay silent.":
                    jump conn_worries

        label hall_opinion:
            "You clear your throat, drawing [bro]'s and [dad]'s attention to yourself. [sean] raises an eyebrow, uncertain of what you might say next."
            menu politic_opinon: #Warmonger, Develop tuath, religion, diplomacy
                tan"Brother, here's what I think..."
                "The Tuath should go to war.":
                    $opinion = 1
                    tan "We need to assert ourselves during this time of strife."
                    tan "It may be hard, but if we don't establish our tuath's strength early, we'll be overwhelmed if the warfare continues to escalate."
                "Let's focus on our own people.":
                    $opinon = 2
                    tan"We pay our tributes and let the rest war while we build. We have no stake in this fight."
                    tan"Build defenses, train troops, whatever we need. It's not our fight at the end of the day."
                "The teachings of the druids hold many secrets." if faith == 1:
                    $opinion = 3
                    tan"If we follow the paths of our ancestors, Ireland itself will aid us."
                    tan "An alliance with our local Sidhe could even tip the balance in our favor and ward off any attacks from outsiders."
                "I believe the Lord holds the future of Ireland" if faith == 2:
                    $opinon = 4
                    tan "His power shall give us triumph over the pagans around, and salvation."
                    tan "Armagh is strong, and its connections with the Celi Dé church mean we have trade partners even if the rest of Ireland goes to war."
                "Father's gods hold great strength. We should align with the Norse kings." if faith == 5:
                    $opinon = 5
                    tan"Such a strong people must be the future of Ireland."
                    tan "Submission to the King of Dyflinn could mean an early balance shift wards the Norse."
                    tan "We may even be given our own Overkingdom or Province should he wish to establish more loyalists."
                "We can be a bridge, perhaps even stop this war before it worsens.":
                    $opinon = 6
                    tan"I cannot stand the suffering abroad, so maybe our words can help soothe their angry hearts."
                    tan"I even offer my life and talents towards this cause, brother."

        label conn_worries:
            ## Conn describes his worries for the tuath and his own future
            "Conn sighs. He shakes his head, as if dismissing ill thoughts."
            bro "We cannot make a statement yet, no matter how good ideas may seem."
            bro "The Tuath simply lacks the manpower to be involved, or the influence to make our voice heard."
            bro "Even within the Confederation our words are worth little. The rest of Airgíalla dismisses us at the gatherings. I don't see this changing."
            bro "Our relations with Armagh have suffered too, as the druids' and the clergy's feuds continue to escalate."
            bro"I believe you both remember hearing that the druids pushed the people of Sligo to sack and burn their local monastery?"
            bro "To open ourselves to external politics is to invite the death of the tuath and our clann. And that means doing nothing. Keeping our loyalties and tribute and keeping our people at home."
            "He looks between you two. Aoife glances up from her tending of the baby with concern on her brow."
            bro "I personally don't understand why the clann preferred my inheritance to yours, or one of our cousins... No, not you [sean] I see that face."
            "Séan had ever so slowly lifted himself up from the firepit, pointing to himself at the mention of 'cousins'. He deflated, and immediately sat back down."
            bro "I am no leader. I just wish to raise my kid, eventually children, in peace and see our family and tuath continue to grow."
            bro "The last few decades have been hard for Ireland, for our tuath in particular. The Norsemen raids were devastating to Armagh, and our trade with them has suffered."
            bro "We once were their primary provider for food, fur and lumber given the short distance and bountiful land we hold."
            bro "But our neighbors chipped away at the border families, stole our trade routes, and dead priests can't keep promises."
            "He sighed heavily, head in hands for a few moments. You look at [dad], sharing a worried look. You're about to speak up when [bro] resumes."
            bro "What if I hurt the tuath. I finally break our foundation of generations and the tuath is scattered, claimed by rivals and neighbors."
            bro "So much can be lost, and I haven't the knowledge to control it."
            bro "The most I can do is keep people happy with traditions like this feast!"
            bro "Even then, so many small things end up falling through. I'm no administrator nor a regent. I trained a potter and hunter, not a king."
            bro "We were certain the cousin branches would want our family out with how short mother's reign was, and the raids that ended the Old [king]'s."
            bro "But they chose, of the two of us no less, me."
            bro "I am not a good choice."
            bro "Our clann was wrong for choosing me."
            "His head falls into his hands, elbows on his thighs as he slips into a pit of despair fraught with anxieties."
            "Aoife frowns heavily, calling one of the fénnid over to watch her child as she steps over to whisper something to Conn."
            "Whatever it is, it doesn't seem to help."
            "Maybe... you could help?"

            menu reassure_approach:
                "Explain why he was a good choice for [king], using your words.(Fili)":
                    $ Honor += 1
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $ reassureAttempt = 1
                    $difficulty = 8
                    $d20Roll = renpy.random.randint(1,20)
                    $renpy.log(d20Roll)
                    if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                        $Fili +=3
                        play sound "sound/critSuccess.mp3"
                        jump conn_Crit_reassure
                    elif d20Roll+(Fili/3) >= (difficulty):
                        $Fili +=2
                        play sound "sound/success.mp3"
                        jump conn_charisma_reassure
                    else:
                        $Fili +=1
                        play sound "sound/fail.ogg"
                        jump conn_reassure_failure
                "Explain he was the accepted choice, following the laws (Seanchas)":
                    $ Honor += 1
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $ reassureAttempt = 1
                    $difficulty = 8
                    $d20Roll = renpy.random.randint(1,20)
                    $renpy.log(d20Roll)
                    if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                        $Seanchas +=3
                        play sound "sound/critSuccess.mp3"
                        jump conn_Crit_reassure
                    elif d20Roll+(Seanchas/3) >= (difficulty):
                        $Seanchas +=2
                        play sound "sound/success.mp3"
                        jump conn_Seanchas_reassure
                    else:
                        $Seanchas +=1
                        play sound "sound/fail.ogg"
                        jump conn_reassure_failure
                "Do not reassure him. It is shameful he is showing such weakness.":
                    $ Honor -= 1
                    show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $ reassureAttempt = 0
                    jump conn_dismissive

        label conn_reacts:
            label conn_Crit_reassure:
                #you not only reassure him, but instill him with fresh confidence with your words.
                "You walk up to his throne and take your brother's hand in a firm grip between both of yours giving a hearty squeeze and his face a firm look. "
                tan"Brother. You have to know that's just not true."
                tan"You were not only chosen by our family for your kindness and sense of justice, but because of how you aided people during the raid."
                tan"During one of the tuath's lowest moments, you were there aiding the villagers and craftsmen and smallfolk."
                tan"You risked your life to protect the tuath's people. You are exactly what we need in times like this."
                tan"You aren't a warrior like some of our previous kings, no. But you do not need to be."
                "He looks a bit confused, but a bit of the brightness has returned."
                tan"You need to be you, you need to be kind. You need to be a guiding influence and mentor for our Tuath to rebuild under."
                tan"I can see your influence bringing us to a thriving future. You can become a father to the tuath, just as you are now a father to Aengus."
                "Your hands release his own, and you grasp his shoulders to help straighten his back."
                tan "I know my words cannot solve what ails you. I can do my best, but my Fili just isn't that strong."
                tan "But I will always be here to help. Not only as [heir]. But as your younger sibling and your dear friend."
                "It's now that you notice Conn has teared up, the occasional streak on his face. It seems your words hit something deep!"
                bro "Thank you, [tan]. Thank you dearly."
                bro "I don't say enough how much I appreciate your aid so far in my rule."
                bro "I know I can depend on you."
                "He sniffles and wipes the tears from his eyes. Aoife smiles warmly, and after a firm squeeze to Conn's shoulder, she returns to Aengus."
                bro "Had you heard Old Brigit threw dough at me yesterday? I had to tell her about the youth troop being behind the mischief in her bakery, and she flew into a rage!"
                tan "No, I did not!"
                jump reassure_end

            label conn_charisma_reassure:
                ##kind words and friendly temperment soothe his crisis
                tan "Conn. C'mon, let's look on the positives."
                bro ". . . Positives?"
                tan "Of course, the bright side is always a better place to be."
                tan "The clann wouldn't have kept you as [heir] if they didn't trust you. The villagers would have grumbled too."
                tan "Has a single person said anything?"
                bro "Old Brigit wasn't exactly happy when I had to tell her that her bakery had been broken into by the Youth Troop."
                tan "How. . . In any way is that your fault?"
                bro "She threw dough at me."
                "He looks rather pathetic for a moment. But you can't help but snicker at the image of Conn with a big blob of dough on his head."
                tan "Brother, you must lighten up. You don't see the humor in that?"
                jump reassure_end

            label conn_Seanchas_reassure:
                ##you leverage law to soothe his heart, to reassure him of his place in society
                tan "Now that's just ridiculous, Conn. Brehon law is very clear on succession, and you were the [heir]."
                tan "And with mother passing, that made you the king. The laws are very clear on this."
                tan "There can be no qualm with the legality of your rule. And if our family believed you the best choice, you must be, eh?"
                "He thinks for a moment, before nodding softly with a gentle smile."
                bro "Yeah, I suppose that makes sense."
                bro "Though, speaking of brehon law and seanchas. . ."
                "He ruminates for a few moments, before continuing."
                bro "Well, the Fili can make and unmake kings. I worry about an incident yesterday, which is partially what set off this train of thought."
                tan "What was it?"
                bro "Old Brigit threw dough at me yesterday? I had to tell her about the youth troop being behind the mischief in her bakery, and she flew into a rage!"
                jump reassure_end

            label reassure_end:
                bro "I suppose it was rather funny of a scene. [fp] couldn't stop laughing. She ended up writing a limerick on the spot about it."
                tan "Oh, I have to hear this."
                "[bro] clears his throat, before reciting two lines in a lilting rhythm."
                bro "\"Ho there, mighty King of Ó Durcáin!\n
                    You seem to have dough on the brain.\n"
                bro "\"At first blush,\n
                    This strange rush,\n
                    Seems quite the way to start a reign.\""
                bro "Not too flattering, eh?"
                "You can't help but laugh loud enough that the fénnids at the fire have their interest piqued by the exchange."
                tan "A joking poem, even from our resident poet, isn't a portent."
                tan "If anything, this tells me the people are supportive of you so far, and comfortable with your rule."
                tan "Let's keep it that way."
                "[dad] lets out a soft chuckle, giving a shake of his head in fatherly pride."
                jump conn_requests

            label conn_reassure_failure:
                "No matter what you try, your words fall flat."
                "You spend an hour attempting, but nothing seems to properly work. [bro] dismisses your words and gestures, preferring to wallow in misery."
                bro "You just don't get the weight of this role, not yet."
                "That's just about all he's willing to offer in response."
                "Aoife and you manage to get him to focus though, and do your best to comfort him even if he denies it."
                tan "Conn, I'm sure you'll feel better once you get busy. Morning blues is all."
                bro "Maybe."
                "Your father coughs into his closed fist, drawing the attention of the rousing King and yourself."
                jump conn_requests

            label conn_dismissive:
                ##you snub him, and get down to business.
                "You sigh and shake your head. Father raised us better than to show this sort of weakness."
                tan "Pull it together, [king]. You are on your throne, in your court. It's lucky no smallfolk were around to see."
                "Aoife's eyes narrowed a bit, and she gave a squeeze to Conn's shoulder."
                "The King looks hurt for a few moments, before he swallows, straightens his back, and dusts off his clothing."
                "He'll likely remember this callousness."
                bro "Right."
                "He waves to dismiss Aoife, who leaves with some trepidation. Your father grunts with a frown to pull your and Conn's attention."
                "Conn's gaze turns towards your father, but he certainly has looked happier before."
                jump conn_requests

        label conn_requests:
            $ d20Roll = 0
            $ difficulty = 0
            $ renpy.fix_rollback()
            ##Conn, after talking with the player, has a job for you.
            dad "I need to get going. Think on what we talked about Conn, okay?"
            bro "Certainly."
            "The two embrace, and Father whistles while striding for the exit. You feel you should check in with him later, just to catch up."
            "He had been quiet since Mom had died, so it wouldn't hurt."

            hide father with fade

            "Conn clears his throat and sits back in his throne."
            bro "Anyway... You came for the job, yes?"
            tan "Indeed. [sean] told me you needed help this morning."
            bro "I had just thought it too late to get your help yesterday, he only arrived this morning? What in Lugh's name did he spend the evening doing?"
            tan "Partying. Then crashing at my house when he lives within walking distance."
            "Conn tries to stifle a laugh, before erupting into raucous guffaws. It takes a good few minutes for his laughter to subside."
            bro "Classic! That is such a thing Séan would do. Luckily, I had told him this was a job for today, not last night."
            tan "Could have told me, too."
            "You give a pointed glare to Séan. He grins back, perhaps obliviously. Conn's laughter resumes, causing him to cough from lack of air."
            bro "Christ, Séan could you have messed up more?"
            sean "Coulda just forgotten."
            bro "True."
            "He clears his throat, focusing again."
            bro"Anyway, I have three tasks. Two out in the forest, and one here in the village. Well, the latter will likely involve more travel, but..."
            "He pauses for a moment to collect his thoughts. As he does, you idly remember your dream, and the mention of a geas to aid Conn. You couldn't refuse his words now if you wanted or risk a divine curse."
            "Not that he needed to know that, of course. He did always worry about your health."
            bro"I'll just cover that later."
            bro "First, We need more game for the feast tomorrow. Some rats got into our stores and ruined some of our best catches of the last week."
            bro "I'd say either a good number of small game animals could cover it, or a few larger beasts. Try to get quality ones, not just whatever you can find."
            bro "Liam has some sites marked out as good hunting grounds. Stick to them, you should have no trouble."
            bro "Next. Liam needs some aid driving wolves out of the forests between here and Armagh. They've been harassing nearby farms and pastures and been a nuisance to travelers."
            bro "Pretty straightforward here, get out to Liam's cottage and help him however you can. [nora] offered to help already, so she should be there too."
            bro "Finally, help Aoife on her duties as [fiannaleader]. Her normal aides are sick, weren't able to get into the village today."
            bro "Just help her in what she needs, around the village and in our territories."
            bro "It shouldn't be too strenuous, if you don't feel like hunting today."

            menu conn_request:
                bro"So, which job do you want?"
                "Hunt for game in the forest":
                    $request = 1
                    bro"Fun choice!"
                    bro"Still be careful though, don't want to stumble into those wolves."
                    tan"If I do, it'll be no trouble."
                    "Conn has to stifle a chuckle through his grin."
                    bro"Overconfident, much? Get us some small game, hares and the like, or a deer or two. No need to go for dangerous prey for my coronation, I'd rather not have a dead sibling on my mind."
                    "He stands from his throne, walking over to give you a clap on the back and a push towards the door."
                    bro"Anyway, get going. I don't have anything else for you."
                    "You nod in response."
                    tan "I'll be sure to not return empty handed, I swear on our gods."
                    "You and [sean] leave the King's Hall once you extract Séan from his gossip with the king's fianna members present."
                    "He whines about not being able to finish his half-romanticized story of an encounter he had with some bard or another."

                    scene bg village
                    show niall
                    with fade

                    "On the way to the northern gates, you stop by to recruit [niall] from his work at the smithy."
                    "You convince him to help, citing trios as a safer hunting group than a duo. Also, because, as he put it:"
                    niall "[sean] would likely end up too distracted writing a poem about nature to properly hunt it."
                    "Friends in tow, and eager to bring back some valuable game to the tuath's celebrations, you leave the village without delay."
                    show text "{b}{color=#FFFFFF}[niall] has joined your fiann, improving your vitality and might!{/color}{/b}" at truecenter
                    with dissolve

                    $ Vitality += 2
                    $ Might += 1
                    if renpy.in_rollback():
                        $ C_niall = False
                    else:
                        $ C_niall = True

                    pause 1.5
                    hide text
                    with dissolve
                    hide niall

                    scene black
                    with dissolve


                    jump hunt
                "Drive out the Wolves":
                    $request = 2
                    bro"Brave, I'll send word ahead to Liam... Ho, Fénnid!"
                    "[bro] calls up one of his fiann, who had been sharpening a spear in the center of the hall around the firepit. Brecc, if memory serves you, a young man with firey hair and freckled face."
                    "Brecc" "Liege?"
                    bro "Go tell Liam the [heir] is going to be aiding his work today, alongside Nóra. Be quick, he should still be somewhere in town."
                    "Brecc" "Aye, I'll be there faster than a hawk."
                    bro "See you are."
                    "[bro] turns towards you again."
                    bro"He'll be expecting you at his cottage, so I wouldn't delay."
                    if weapon == 1:
                        "You crack your knuckles, wondering if you'll get to punch a wolf in the face by the end of the day. Certainly would be a feat, and a tale."
                    elif weapon == 2:
                        "You tap the butt of your spear against the ground. You wonder if it'd be easier to run up and gut a wolf, or skewer it from a distance."
                    elif weapon == 3 or weapon == 5:
                        "You give a slight nod, patting blade at your side. Your weapon was as decent as any to bring to battle wolves, though not as fitting as, say, a spear or bow. You'll get the job done though."
                    elif weapon == 4:
                        "You flip the latch holding your handaxe in place and draw it to feel the weight of the iron and wood. A clean chop to the head, a wolf for your wall."
                    elif weapon == 6:
                        "A shrug, and your bow slips off your shoulder and into your hand. The perfect weapon for hunting, especially such a dangerous creature."
                    elif weapon == 7:
                        "The cord of leather and fiber wrapped around your hand itches. Itches for the chance to be tested against a real sort of challenge."
                    tan "You can count on me, brother. Those wolves are good as dead."
                    "Conn smirks a bit, Aoife chuckles in her own seat. Your father has a proud look on his face."
                    bro "See that you get back safely. You haven't hunted wolves with Liam before, or at all. They aren't like a deer or hare, a wolf that thinks it can take you will turn to attack, or flank around."
                    bro "Even a boar isn't that crafty."
                    "You can't help but swallow a bit."
                    tan "I'll be fine, I swear by our gods."
                    bro "Good. Now get going, you have a long day ahead."
                    "A handshake and half hug with your sibling later, you and [sean] leave to join Liam on this quest against the wolves of the wood."

                    scene black
                    with dissolve

                    jump wolves
                "Help the Fianna":
                    $request = 3
                    bro"Aoife! You've got some help collecting for the feast, my turn to care for little Aengus!"
                    show aoife at left
                    with dissolve
                    "[aoife] looked up from the child playing in her lap, her content smile turning to a more serious look as she looks over you and [sean]."
                    aoife"Are you sure? The job we have here ain't that interesting. Collecting the King's tribute...{nw}"
                    bro"Well of course they are. They're the ones that chose it! Now bring me my boy and get going, I want you back before dark!"
                    "Aoife rolled her eyes. Conn always loved to watch his son, even if he was supposed to be running the tuath, villagers would often come to talk to him and find Aengus on his lap as well."
                    "He had always been a good father, even for the scant year Aengus had been alive."
                    aoife "Let's get going then. We have several dozen households in town to visit, and some outlying clans."
                    "Aoife grabs your shirt briefly, turning you around on your heels and pushing you forward."
                    aoife "You lead, I'll direct you."
                    "She doesn't even give you time to properly respond or question what you got yourself into. Firm pushes against your back and Aoife's stern tone get you marching like a trained soldier."
                    "And with that, you leave the king's presence. Conn waves after you, gleefully holding his child in one arm."
                    "Dad'll probably end up joining the doting soon enough, once his businessfor the day is done, but for now you're pulled outside to join Aoife on her duties."

                    show text "{b}{color=#FFFFFF}[aoife] has joined your fiann, improving your might and fili!{/color}{/b}" at truecenter
                    with dissolve

                    $ Might += 2
                    $ Fili += 1
                    if renpy.in_rollback():
                        $ C_aoife = False
                    else:
                        $ C_aoife = True

                    pause 1.5
                    hide text
                    with dissolve

                    scene black
                    with dissolve

                    jump community

    label ch1_part2:
        ##You set off on your job.
        label hunt:
            scene bg woods
            with dissolve
            stop music fadeout 1.0
            play music "music/Surreal_Forest.ogg" fadein 1.0

            "The tuath had historically been split into a few distinct partitions of its land. It'd been so as far back as when the great Cú Chulainn roamed the fields of Ulster, before the Confederation."
            "To the north, the woods and border with the the monastery lands of Armagh. The closest Otherworld Mound was located somewhere deep in those woods but was always tricky to find."
            "To the west was the tuath's main town, Cnoc bhFianna, your home and the seat of the King."
            "The center held farmland, and a satellite monastery of Armagh nestled in the crook of a stream. the Woods extended south from the northern section, spearing between the farmland and Cnoc bhFianna."
            "The south and east was hilly, rocky pastureland, and often used as a hideout for bandits. The King's fiann often patrolled the area and ensured safe trade down south to Dyflinn."
            "Today, you travel north with [niall] and [sean] to seek out less used hunting grounds in the tuath lands."
            play sound "sound/forestWalk.ogg"
            "The trip is uneventful, with the three of you jesting as you traveled. The paths towards the woods were well-trod enough to be clear and easy to follow."
            "With the midday sun beating down, the greenery of the Tuath shone. It didn't take long for the rolling hills around Cnoc bhFianna to give way to hilly forests."
            "The forests of Ireland were vast, though over time more had been cleared to aid in the growth of human settlement. Old contracts with the Sí and Tuath preserved tracts of forests, however, such as the woodland between Armagh and the Tuath."
            "While hunting was generally allowed within the Sí forests, mortals had to be careful to not run too far astray of the paths and clearings."
            "Magic beasts and immortal things lived in those woods, according the tuath legends."
            if rite == 3:
                "It was something you knew all too well. The strange animals of the Mounds and the forests around them."
            else:
                "Though you've never had any experience with the stranger things of the woods, you trust the old wisdom."
            "Your friends and you arrive at a clearing, set up with the winter lodge. The building was squat, utilitarian, rather than the homely quality of homes back in the village."
            "Log and thatch and stone had been used to build the square-ish lodge, with open windows on every side to watch for approaching beasts or dangerous mauraders."
            "Liam had his own, more permanent structure deeper in the woods, but clearings like this one were enough for most tuath hunters."
            "Without much ceremony, the three of you begin preparations for a hunt: retrieving the sledge from the lodge to prepare it for carcases, fetching and checking arrows, a bit of sharpening of blades even thanks to Niall."
            "Séan is the first to start speaking, snapping the comfortable working silence of companions."
            show sean at left
            show niall at right
            with dissolve
            sean "Hmm, I swore the lodge was bigger."
            niall "It has been years. Maybe you grew?"
            sean "Mayhaps I have. Mayhaps it's simply run down."
            tan "A possibility, yes. Let's get a plan for this hunt together, how about."
            sean "Not a bad idea. How about I start, as the best looking of us three."
            "Niall grumbled something but continued to slide his whetstone along his sword. You never could tell why he kept the blade, given he always defaulted to grabbing the hammer next to it."
            sean "The way I see it, we have three ways of going about this hunt:"
            sean "First, we go for quantity with small game. While they can be flighty, traps and arrows and spears can deal with them easy enough."
            sean "Second, we go for bigger, and track down a herd of deer. We take down a stag or two, or some doe, get some nice trophies. Deer are a bit trickier, though, with their speed."
            sean "We could also go for broke and, I like this idea the most, hunt down a boar. While we might not get the quantity, a boar makes for good eating and its hunt for a good song."
            niall "Weren't we told to avoid the dangerous game?"
            sean "But where's the fun in the easy way? I say we go for the boar."
            niall "Deer or small-game."
            sean "Must you be so responsible?"
            sean "[tan], what say you to our noble quest for food? Which should we go with?"

            menu hunt_choice:
                "Small Game": #hunt for things like squirrels and hares( requires speed and endurance or cleverness)
                    $hunttarget = 1
                    tan"I agree with Niall. Small game would be safest and the easiest, so we should go for that."
                    tan"Might not be as glamorous..."
                    "You shoot a look towards [sean]."
                    tan"But it's more of a guarantee of us bringing back some food. That is why we're out here, after all."
                    jump hunt_small_game
                "Deer": #hunt for deer (tougher, more skilled = more honor)
                    $hunttarget = 2
                    tan"Deer must be a good compromise for you both. Challenging enough, aye?"
                    "The two give each other glances before nodding in agreement."
                    tan"Good. Let's get to planning, we only have today after all. The coronation will not wait for the whims of three hunters."
                    jump hunt_deer
                "Boar": #hunt for boar (dangerous, failure can cause injury, high honor reward)
                    $hunttarget = 3
                    tan"Boar."
                    niall"You sure? We could very well get injured on this. It'd be no fun to miss the coronation due to boar-based death."
                    tan"Why not. A good story seems like just the thing to get us noticed in the Tuath, maybe even into one of the Fianna properly."
                    sean "I didn't even think of that! Clever, [tan], clever."
                    jump hunt_boar

            label hunt_small_game:
                $ difficulty = 8
                scene bg rabbit
                show sean at left
                show niall at right
                with dissolve
                sean "So, rabbits it is?"
                "The bard looks between the two of you with an excited look. Niall finished with his blade, sliding it back into his sheath before responding."
                niall "Aye."
                if weapon == 2:
                    "You wring your hands against the haft of your spear. Might be overkill, but it certainly would slay anything small enough within range of your throwing arm."
                elif weapon == 4:
                    "You flip your axe in the air, catching it by the handle. You briefly wonder how tough it would be to hit a rabbit with an axe from afar. You'd never tried, but you feel you could."
                elif weapon == 6:
                    "The bow on your shoulder is obvious enough. Should you wish to stalk prey, you figure you'll have no trouble slaying any beast of the bush."
                elif weapon == 7:
                    "A sling, and rocks. You'll never run out of ammo in the Forest, and the sling is faster on the draw than a bow, even if slightly."
                else:
                    "A hunt was always the chance to try new skills. You figure your weapon will be just as good as any in killing small game."
                tan "So, how do we wanna go about this. Niall, you're the avid hunter among us."
                niall "We have a few ways to go about this, I'd say."
                niall "We could just chase them down using speed and weapons. No real subtlety, lots of action. With my size I'd likely startle enough small creatures to make our rampage easy enough."
                niall "But, again, no subtlety. We could just scare them off and not hit anything."
                sean "It isn't much my style to go running through the woods like Buile Suibhne. I'm not a madman living in a tree, nay."
                tan "I'm sure you'd make quite a good madman, Séan."
                "He harumphs and gestures for Niall, who patiently had been kicking at the golden, reddish, and orange leaves laying across the ground below, to continue."
                niall "Anyway. We could also just stake out some warrens, dens, such places, place traps and be a bit more subtle than a raging bull."
                tan "Sensible."
                niall "It would be no trouble. Traps will mean even if we catch little today, we can always return in the morning for our prize."
                #a simple challenge, easy to pass. DC 8
                menu small_game_skill:
                    "We shall..."
                    "Use quickness and chase down prey (Finesse)":
                        tan"We should try to be fast about this. I've always wanted to try grabbing a rabbit by the ears."
                        "The other two nod in agreement and set about preparations for the day. You'll know if this was a good plan soon enough."
                        "You, [sean], and [niall] all split up, with the goal to herd beasts back towards the clearing to make the work of returning with the carcasses easier."
                        "You head for the east. Niall goes north. Séan for the west. You wish the other two luck, before heading into the dense underbrush of the woods around the lodge."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Finesse/3) >= (difficulty + 10) or d20Roll == 20:
                            $Finesse +=3
                            $huntwin = 2
                            play sound "sound/critSuccess.mp3"
                            "Despite the appearance of madness as three warriors chase rodents and lapines through the brush of the forest, the three of you corral a significant amount into the clearing."
                            "The three of you whoop in triumph, letting loose with bows and weapons and laying the small animals low."
                            "After the carnage, with [sean] backtracking to pick up the beasts slain on the paths, you and Niall begin the work of cleaning weapons and piling up the meat on the sledge."
                            tan "Quite the bounty. You feel like Mad Sweeny yet, [sean]?"
                            sean "Oh yes. I'll turn into a bird at any moment!"
                            "You guffaw and your friends join in the laughter moments later, likely scaring off any remaing animals in the area. No matter, you had plenty of game to bring home today."
                        elif d20Roll+(Finesse/3) >= (difficulty):
                            $huntwin = 1
                            $Finesse +=2
                            play sound "sound/success.mp3"
                            "The daft plan ends up working well enough, with your swiftness on the trail proving enough to slay a number of beasts. Niall and [sean] have similar luck, thankfully."
                            tan"I cannot believe this plan actually worked. I thought it only worked against larger game!"
                            sean"I cannot believe you went with this plan over actual traps."
                            niall"Worked, so I can't complain. Needed the run anyway."
                            "The three of you set off for home soon enough, after cleaning up the clearing and collecting your haul for the return journey."
                        else:
                            $Finesse +=1
                            play sound "sound/fail.ogg"
                            "Perhaps the encroaching winter scared enough of the game underground by now. Maybe you just weren't lucky enough today. Either way, you only managed to catch a few beasts."
                            "The mood is distinctly somber as you return to the clearing."
                            sean "I regret we set up no traps, now. We don't even have that security. Maybe we'll find something on the way home."
                            tan "It'll still hurt to return empty handed."
                            niall "Aye."
                    "Use knowledge of warrens and traps (Seanchas)":
                        tan"Let's not be silly about this. Traps would be the best way to go about this."
                        "The blacksmith apprentice Niall nods, and steps into the lodge to collect the hunting traps left there. Séan nods his approval."
                        sean "We'd have just been silly, running our way through the forest like madmen."
                        "Within the hour, you've set off as a group to find some good places to set traps. Spirits are high, you're with friends, and the weather is pleasant. You couldn't have made a better day to hunt."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $huntwin = 2
                            $Seanchas +=3
                            play sound "sound/critSuccess.mp3"
                            "Within a short walk from the lodge, [sean] spots the telltale signs of rabbits and other small animals. He hauls himself up into a tree, and whispers back down at you and Niall."
                            sean "Looks like an active warren. If we set up traps near here... Quite the haul, I'd guess."
                            niall "Wonderful. I'll get to work."
                            "Sean keeps lookout for anything more dangerous, but shortly enough a host of traps and bait have been laid. It's only a matter of time until some beast trips one or another."
                            "By the end of the day, you must have two dozen rabbits at the very least, along with the occasional creature you and your compatriots laid low while waiting for traps."
                            "A veritable bounty!"
                            "You can't help but feel pride at this accomplishment. Hopefully this helps ease Conn's worries, even just a little."
                            "With the surplus, you decide to roast some rabbit before continuing home. It certainly wouldn't hurt."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $huntwin = 1
                            $Seanchas +=2
                            play sound "sound/success.mp3"
                            "The day is long, but ultimately you get more than enough game. At least this should tide over for the feast."
                            "You and Niall load up the sledge to leave once you get back to the clearing. Enough to fill it, but not enough to weigh it down."
                            niall "A productive day."
                            "Those are the only words traded, given the tiredness setting into your bones after a long day out in the woods."
                            "But the three of you are content in this success."
                        else:
                            $Seanchas +=1
                            play sound "sound/fail.ogg"
                            "Perhaps the encroaching winter scared enough of the game underground by now. Maybe you just weren't lucky enough today. Either way, you only managed to catch a few beasts."
                            "The mood is distinctly somber as you return to the clearing."
                            sean "Maybe the rest of the traps will catch something by tomorrow? I'll make sure to come check with Liam, howabout?"
                            tan "It'll still hurt to return empty handed."
                            niall "Aye."
                    "Try a different task":
                        tan"We should try hunting something else, actually."
                        jump hunt_choice
                jump after_hunt
            label hunt_deer:
                $ difficulty = 10
                scene bg deer
                show sean at left
                show niall at right
                with dissolve
                niall "Deer is a good challenge, but it shouldn't hurt us should we fail. It should be no trouble to find a good haul, our tuath is known for deer hunting, is it not?"
                niall "It'll take a bit of tracking, but we can find the trails deer often use and strike from concealment."
                niall "With a few good shots from arrows, spears, slings, we have some dead deer for us to take back home."
                sean "Tricky, and reliant on them not noticing us. If the wind shifts, they'll smell us and we'll have nothing to show for it."
                tan "True. Couldn't we also try to negate that with your music, Sean?"
                if Fili >= 6:
                        tan"I could even lend my own voice to aid you, the magic of music and voice could pull in the deer for Niall to catch."
                else:
                    tan"Niall and I can set a trap, as your music pulls them in we can strike them down."
                niall"Not entirely orthodox, but deer do seem to respond well to the music of the fair folk, why not our music too?"
                tan "Exactly, my friend."
                "[sean]' eyes sparkle at the thought, obviously favoring this second plan. But as usual, they'll rely on your decision for which might be the best path."
                niall "Of course, should we wish for volume over quality of meat, we can go for small game. Venison always makes a good centerpiece for feasts, though..."
                sean "Let's try out my magic!"
                niall "Friend, I doubt your music could pull anything other than a mangy hound."
                "Séan immediately, but playfully, smacked Niall's shoulder, who let out a laugh."
                menu deer_skill:
                    "Lie in wait near deer trails and strike quickly (Finesse)":
                        tan"I believe waiting for the deer to come through will be the better choice for us. I'm better when it comes to my weapons than with magic."
                        niall "True, I'd rather not rely on Séan's music. It's staler than biscuits by the end of winter."
                        sean "You better watch your mouth, I only take so many insults!"
                        "Sean's tone was joking, especially with the aggressive fiddle playing that followed. You and your companions prepare for your deer hunt."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Finesse/3) >= (difficulty + 10) or d20Roll == 20:
                            $huntwin = 2
                            $Finesse +=3
                            play sound "sound/critSuccess.mp3"
                            "The rest of the day goes with utter aplomb. Niall tracked down a trail quickly, and the three of you lie in wait. along a dense turn in the trail."
                            if weapon == 2:
                                "You cast your spear into the first stag you see, impacting him square through the chest. Niall and [sean] unleash arrows and slingstones and fell another few."
                                "You charge forward yourself, using your knife to end the lives of the deer already on the ground. No point in them suffering."
                            if weapon == 6:
                                "With a drawn bow, you wait. Deer trot along in a group, ignorant of your presence. The stag falls before he even hears the arrow zipping towards his eye."
                                "Your Companions loose their own arrows into the herd. More fall, and the three of you close in to end those who are injured yet still live."
                            else:
                                "You use a borrowed bow to strike true, before running in to catch the startled animals before they could run. The stag falls, and your companions' own strikes hit their marks."
                            "After a good early haul, its easy to realize you are unlikely to find more deer on this trail. The blood will attract predators and ward away more deer."
                            "You, Niall and Séan collect the deer and leave an offering to the gods. Connal Cernach. A great hunter, and protector of horned beasts."
                            "A deer's heart is nailed to a tree and the blood's used to draw a snake below and a pair of antlers above. An ancient rite to thank for a successful hunt."
                            "Upon returning, the three of you happily relax and prepare a bit of meat for the road. With a host of deer caught, you can return with honor."
                        elif d20Roll+(Finesse/3) >= (difficulty):
                            $huntwin = 1
                            $Finesse +=2
                            play sound "sound/success.mp3"
                            "While Niall found a good trail to lie in wait, the day crawls by. It isn't until the afternoon that anything crosses your path. A trio of deer led by a stag."
                            "For a brief moment, you think the stag notices you."
                            "You lock eyes, before signaling the others to strike with your own attack."
                            if weapon == 2:
                                "You cast your spear into the stag, impacting him square through the chest. Niall and [sean] unleash arrows and sling-stones and fell the other two without difficulty."
                                "You charge forward yourself, using your knife to end the lives of the deer already on the ground. No point in them suffering."
                            if weapon == 6:
                                "The stag falls before he even hears the arrow zipping towards his eye."
                                "Your Companions loose their own arrows into the trio. More fall, and the three of you close in to end those who are injured yet still live."
                            else:
                                "You use a borrowed bow to strike true, before running in to catch the startled animals before they could run. The stag falls, and your companions' own strikes hit their marks."
                            "It's over in a few moments. A successful hunt, but nothing out of the ordinary for the forest."
                            "It's easy to realize you are unlikely to find more deer on this trail. The blood will attract predators and ward away more deer."
                            "You, Niall and Séan collect the deer, one each, and leave an offering to the gods. Connal Cernach. A great hunter, and protector of horned beasts."
                            "A deer's heart is nailed to a tree and the blood's used to draw a snake below and a pair of antlers above. An ancient rite to thank for a successful hunt."
                            "Upon returning, the three of you happily relax and prepare a bit of meat for the road. With a host of deer caught, you can return with honor."
                        else:
                            $Finesse +=1
                            play sound "sound/fail.ogg"
                            "Unfortunately, nothing arrived after the entire day's hunt. The trail Niall found must have been old and no longer used."
                            "He grumbles, kicking at sticks and rocks as the three of you return to the clearing."
                            niall "I swear that trail was a fresh one..."
                            "The mood is more somber than you'd like, but at the very least you slay a few rabbits while on your way back. Scrawny ones, but the half-dozen animals will be good stews."
                            "You won't return with nothing today, but what you will bring won't what you intended."
                    "Use magic and song to call for the deer (Fili)":
                        tan"I do like my music, and I've never lured a deer with my voice. Let's try that, fellows."
                        sean"Excellent! I have just the song for them."
                        niall"We're serenading deer now? Wonderful. At least let's ensure we get something by the end of the day."
                        tan "I promise, Niall."
                        "The three of you head out from the clearing as a group, with [sean] slowly humming to find his notes. Niall grumbles a bit, but follows along with sling in hand."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                            $huntwin = 2
                            $Fili +=3
                            play sound "sound/critSuccess.mp3"
                            "Séan set to work at playing his song, using what he knows of the old magics to weave together a lure for the beasts of the forests."
                            "Séan's fiddle plays out a haunting melody that even you struggle to resist. Niall prepares his sling and hammer for anything that might emerge towards you three."
                            "But the animals that arrive even moments later are docile. The rabbit's almost twitch twitch their noses in time with the music."
                            if Fili >= 6:
                                "You add your voice to the music, singing a lullaby. The animals lull themselves to sleep. Four rabbits, a whole herd of deer, and a few other beasts."
                                "With a hand you gesture to Niall to select a few for bring home for the feast."
                                "You and Niall, while Séan continues the song on his fiddle, kill a few of the pacified creatures."
                            else:
                                "You and Niall, not being as musical as Séan was, take to the task of selecting which ones to kill and which ones to let loose. A bit of a morbid task, when you aren't hunting them."
                                "The serene look of the animals even as you cut their throats was just unnerving."
                            "Thanks to Séan's skill you manage to preserve the hides and meat much more than if you killed them violently."
                            "Once you get the carcasses back onto the sledge in the clearing, you can tell the haul was significantly more than expected. Not even just deer, but a variety of game covered the transport."
                            "The tuath would eat well tomorrow!"
                        elif d20Roll+(Fili/3) >= (difficulty):
                            $huntwin = 1
                            $Fili +=2
                            play sound "sound/success.mp3"
                            "Séan set to work at playing his song, using what he knows of the old magics to weave together a lure for the beasts of the forests."
                            "And luckily, every so often a deer or two wandered into the clearing seeking out the song. They were spellbound, but not totally unaware."
                            "Once they noticed the humans they often would begin to bolt!"
                            "You and Niall  strike as soon as you could, with bow and sling and both of your preferred weapons."
                            "By the end of the day, you three had slain at least twice as many deer as your own number."
                            "The three of you happily set on the road with the sledge once it's been loaded up, but not before leaving an offering for the gods for the animals slain. It was only proper to do so."
                        else:
                            $Fili +=1
                            play sound "sound/fail.ogg"
                            "You spend the whole day trying to lure animals in with song, yet nothing."
                            "It's unfortunate, and [sean] looks positively downtrodden, mumbling about his skill with the instrument maybe not being all he thought it was. Niall does his best to comfort him."
                            "The mood is more somber than you'd like, but at the very least you slay a few rabbits while on your way back. Scrawny ones, but the half-dozen animals will be good stews."
                            "You won't return with nothing today, but what you will bring won't what you intended."
                    "Try a different task":
                        tan"We should try hunting something else, actually."
                        jump hunt_choice

                jump after_hunt
            label hunt_boar:
                $ difficulty = 12
                scene bg boar
                show sean at left
                show niall at right
                with dissolve
                sean "So, a boar, how do we go about hunting that?"
                niall "Carefully."
                sean "[tb] is really rubbing off on you, isn't he? I swear you used to talk more."
                "Niall raised an eyebrow, shrugging, no verbal response. Maybe he has started taking after Conchobhar."
                tan "I've discussed hunting boar with the rígfénnid before. Aoife's always mentioned two main ways of hunting boar."
                tan "You either standoff with it and kill it before it can kill you or avoid its tusks and tire it out."
                tan "For the former, you'd need to be quick or strong, and use a spear or something able to catch the boar before it hits you. Letting it too close is a good way to end up dead."
                tan "With tiring it, wrestling skills or outrunning it will be the way to keep a boar from killing you. Once its too tired, you double back and slice its neck."
                "Both of your friends look at you with worry on their faces."
                sean "Are you sure we can do that? Both seems dangerous."
                niall"I could help hold it down for the latter, but all three of us will mean it might be easier to slay the beast."
                tan "Certainly, especially if we get one that's all by itself."
                tan "We want it for the meat, rather than the challenge specifically, so we should make it easier rather than go for the difficult methods."
                menu boar_skill:
                    tan "I think we should..."
                    "Head for a boar's den and challenge it (Might)":
                        tan"We might as well take advantage of having these weapons against the boar's tusks."
                        tan"We have range, so getting the good boar spear from the lodge to compliment it I think we'd be able to kill the boar without much trouble."
                        niall "I'll take the spear, being a blacksmith does mean I'm probably stronger than the both of you."
                        if dexfighter == 1:
                            tan"Well, true, I do prefer finesse to brute force."
                        elif dexfighter == 2:
                            tan"No preference myself, but I'll let you take it."
                        else:
                            tan"Maybe just by a bit, my friend! I've done plenty of feats of strength myself!"
                        "The boar spear was a hefty thing once you pulled it out of its storage. A broad bladed head with solid wings to prevent a boar from thrashing its way to the wielder."
                        "In the firm grip of a strong hunter, no boar could beat it unless possessed with the fury of the gods."
                        "You and your companions stalk through the forest. The Fianna's hunters had spotted a boar's den within the last month and left it for anyone who wished to try their luck."
                        "And now you were on your way to said den to take them up on the challenge."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Might/3) >= (difficulty + 10) or d20Roll == 20:
                            $huntwin = 2
                            $Might +=3
                            play sound "sound/critSuccess.mp3"
                            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            $Honor += 2
                            "Niall held tight to the boar spear as you approached the den. Séan was tense too, his knuckles white from gripping onto his bow."
                            "With it being winter the beasts likely wouldn't be as riled up as during mating season in spring, but they could get riled up should hunters get too close."
                            sean "Two, ahead!"
                            "Séan points with his bow, but the boar's already charging with its mate. Niall curses, and sets the boar spear in its path and into the ground just in time."
                            "The large male squeals as he impales himself on the spear, rage making him attempt to reach Niall. The blacksmith holds firm, grunting with effort."
                            "Meanwhile, you and Séan have to deal with the second. The bard looses his arrows, trying to slow the now dying male's mate down before she reaches you two."
                            if weapon == 2:
                                "You grip your spear much like Niall with his boar spear, and hope it works just as well."
                                "Séan's bow sings as the second boar spears itself on yours. The blade to the heart, along with arrow to the eye quiets it as Niall finally manages to wrestle the other down."
                            elif weapon == 3 or weapon == 4:
                                "With quick reflexes, you bring your shield to bear right as the boar thuds into it. The shock knocks you onto your back and the wind out of you."
                                "Séan dashes up with a dagger and half-tackles it to the ground to slice its throat. Niall throws his boar to the ground a moment later, shouting in triumph"
                            elif weapon == 5:
                                "Your two-hand sword slips from its sheath and cuts into the boar as you side step its charge. With the speed of the charge and your swing, you take its head off in one strike."
                                "Niall roars, pulling out his hammer to strike a blow to the temple of his boar, forcing it to give up the ghost."
                            elif weapon == 7:
                                "Your sling accompanies Séan's bow, creating a ranged symphony of death to the boar. One of your stones strikes the boar's temple, and it stumbles into the dirt."
                                "Séan steps in to end the boar, as Niall does the same with his as the struggle dies from his boar."
                            else:
                                "Your bow sings alongside of Séan's. You thank the tuath's hunters for stocking the lodge with so many arrows, as the boar falls just short of you two."
                                "Niall manages to defeat the boar on his spear shortly after, panting with exhaustion."
                            sean "That went amazingly! Bravo, both of you!"
                            niall "Yeah, yeah. You owe me a few drinks when we get home."
                            tan "Let's get these bodies back to the clearing, first."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $huntwin = 1
                            $Might +=2
                            play sound "sound/success.mp3"
                            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            $Honor += 1
                            "The three of you are tense as you approach the den. But lucky enough it seems as if the den is mostly empty. A single boar, male from the looks of it, rooting around for food."
                            "Once Niall gets himself set up, shield in one hand and spear in another, braced against the ground and angled towards the beast, you shout out towards the boar."
                            tan "Lily-livered boar! Come get some!"
                            "It takes the bait, snorting and angry as it charges for you."
                            "With more insults and aggressive actions flung at the boar you goad him to charge, before you and your bard friend both dive behind Niall. Success is in his hands now!"
                            "A second of angry bellows and squeals pass, before you hear the sickening sound of metal piercing flesh, and a thud against the shield."
                            "Thrashing, angry sounds continue, and Niall obviously struggles with holding the spear in place."
                            niall". . . Got 'im!"
                            sean "Thank the gods! Great job, Niall."
                            tan "That'll be good for the hunt today, le's get back."
                            sean "Drinks are on me!"
                        else:                                          #injury
                            $Might += 1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "Upon arrival at the boar's den, everything just seems to go wrong right away."
                            "Niall immediately is noticed and charged at by an angry boar. He manages to dodge and roll out of the way but loses his spear in the process."
                            sean "Shit! Get the spear!"
                            "Both you and the bard scramble for it, only for the boar to redirect and charge at you right as you grab it. The beast is vicious, and you're no match for the blow."
                            play sound "sound/injury.ogg"
                            "You're knocked off your feet, and you only just manage to spear the boar in the side, instead of head on."
                            sean"Get bloody away from them!"
                            "The last thing you hear before you pass out from the pain is Séan shouting, and Niall tackling the boar off of you before it could do more damage."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            "You wake up a few hours later to find Séan has tended to the wound, but a sharp pain remains in your side. That'll be a nasty scar later."
                            "[sean] and [niall] managed to take down the boar after you lost consciousness but look just as worse for the wear as you do. At the very least no one perished."
                            "It won't be as glorious for you as it could have been, but at the very least you completed your task."
                            tan "Remind me to never go boar hunting again, [sean]."
                    "Exhaust the boar by baiting and dodging it. (Vitality)":
                        tan"We humans are built for stamina. I haven't ever seen a boar able to turn the same way as a human, either. We should be able to weave around their charge, bait them, safely enough."
                        niall"I suppose. You won't catch me running around the woods like a madman, however. You tire them, I'll slay them."
                        sean"Now that's clever thinking! Meanwhile, I'm fast and tricky too, I'll run around and keep them distracted along with you. [tan]."
                        "You nod, before stretching your legs a bit. You'll need every bit of help to get yourself ready for this run. Niall, meanwhile, goes to grab the boar spear. A regular one just wouldn't cut it."
                        "The boar spear was a hefty thing once you pulled it out of its storage. A broad bladed head with solid wings to prevent a boar from thrashing its way to the wielder."
                        "In the firm grip of a strong hunter, no boar could beat it unless possessed with the fury of the gods."
                        "You and your companions stalk through the forest. The Fianna's hunters had spotted a boar's den within the last month and left it for anyone who wished to try their luck."
                        "And now you were on your way to said den to take them up on the challenge."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Vitality/3) >= (difficulty + 10) or d20Roll == 20:
                            $huntwin = 2
                            $Vitality +=3
                            play sound "sound/critSuccess.mp3"
                            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            $Honor += 2
                            "Niall is quick to point out a pair of boars, what seem to be twin females, rooting around the den the three of you chose."
                            niall"If we can pull both of them separate, it should be easy to-"
                            "He's cut off as they snort. One turns to look at the three humans intruding in their small clearing. Beady eyes focus on the humans armed with hunting gear and looking caught out like they walked into a feast hall naked."
                            "The wind shifted, they could pick up the scent of predators now. One starts to charge, with the other in tow soon after, heading right for the three of you."
                            sean"Well, that's not good."
                            "He immediately breaks into a sprint, scooping up a branch from the ground to whap one of the boars before peeling into the underbrush. It trails after, turning on a dime with a furious squeal."
                            sean "Get the other!"
                            "You nod, before running towards the other, skidding just out of reach to send dirt, leaves, and twigs at the charging boar before you turn into the brush."
                            "Clever running and dodging keeps you just out of the boar's reach, and it only takes a short time, maybe an hour, until the boar is absolutely exhausted."
                            "You don't even feel winded, yet, and the boar's knees buckle as it hits the limit of its stamina. A quick blade to its throat and its spirit passes."
                            "A quiet prayer, a wait for blood to drain and you hoist the exsanguinated boar over your shoulders."
                            "Séan had, in the meantime, lead the other boar back and Niall helped slay it. With two in hand, you happily head back to the hunting lodge to load up the boars and head back to the village."
                        elif d20Roll+(Vitality/3) >= (difficulty):
                            $huntwin = 1
                            $Vitality +=2
                            play sound "sound/success.mp3"
                            show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            $Honor += 1
                            #A single boar chase, drops and killed.
                            "Upon approaching the boar's den, you managed to pull its attention right away. Throwing rocks at a boar tends to do that!"
                            "You and Séan take off at a slow pace to see who the boar follows, as Niall will bunker down and wait for you to string the boar in a wide circle back to the den."
                            "He ends up going after you, perhaps due to you being just a bit slower than Séan was. Or maybe it was the fact you managed to hit it hard with a rock first?"
                            "Either way, you take off into the underbrush with a charging boar on your heels."
                            "Dodging around fallen trees and brush and stone, you manage to continue baiting the boar on your tail with the occasional rock or shout, along with mimicking sounds of injury."
                            "By the time you pull him back around towards his den again, the boar seems to be wheezing and slowing down."
                            "A quick dodge around Niall's hiding space and he emerges, casting a spear towards the boar and catching him hard enough to knock the rest of the fight out of your quarry."
                            "Séan moves in to finish the boar off with his dagger, whispering a thanks for the chase and to the gods."
                            tan "By our ancestors, I am tired!"
                            sean "You did just run a circuit worthy of a hound, [tan]"
                            tan "T'was nothing. Let us get ourselves back to the clearing and get this beast back to the village for the night."
                        else:                                           #injury
                            $Vitality +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "Upon arrival at the boar's den, everything just seems to go wrong right away."
                            "Niall immediately is noticed and charged at by an angry boar. He manages to dodge and roll out of the way but loses his spear in the process."
                            sean "Shit! Get the spear!"
                            "Both you and the bard scramble for it, only for the boar to redirect and charge at you right as you grab it. The beast is vicious, and you're no match for the blow."
                            "You're knocked off your feet, and you only just manage to spear the boar in the side, instead of head on."
                            sean"Get bloody away from them!"
                            "The last thing you hear before you pass out from the pain is Séan shouting, and Niall tackling the boar off of you before it could do more damage."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            "You wake up a few hours later to find  Séan has tended to the wound, but a sharp pain remains in your side. That'll be a nasty scar later."
                            "[sean] and [niall] managed to take down the boar after you lost consciousness but look just as worse for the wear as you do. At the very least no one perished."
                            "It won't be as glorious for you as it could have been, but at the very least you completed your task."
                            tan "Remind me to never go boar hunting again, [sean]."
                    "Try a different task":
                        tan"We should try hunting something else, actually."
                        jump hunt_choice
                jump after_hunt

            label after_hunt:
                $ d20Roll = 0
                $ difficulty = 0
                scene bg woods
                show sean at right
                show niall at left
                with dissolve
                play music "music/Return_Forest.ogg" fadein 1.0
                play sound "sound/forestWalk.ogg"
                if huntwin == 2:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 2
                if huntwin == 1:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 1
                sean "Ugh, I need a wash."
                "Séan sniffs at his clothes, tugging at the woolen outfit. His words come after the three of you are about halfway home, with the tuath town visible on the horizon."
                sean "I'm surprised, though. I thought the woods would have more than this. Maybe the tuath needs to change hunting grounds?"
                niall "Would not be surprised. Even with the raids, our population grows."
                tan "Perhaps. We may just be a bit late in the season for seeing animals out and about."
                sean "Yeah, that's a bit more likely."
                "Sean began to play his instrument, getting the first notes of a melody out, before his attention is torn to the side. He keeps walking for a moment, before stopping."
                "Niall and yourself outpace him without noticing for a few seconds longer."
                tan "Wait... [sean]? What's going on back there?"
                "Séan takes a moment to respond, still a bit spellbound."
                sean "Something... I think I saw a rabbit with the antlers of a deer. Or maybe just a deer? I could not tell."
                niall "Odd. . ."
                tan "Should we go after it?"
                sean "It couldn't hurt."
                "You pause for a moment, looking at the sledge holding your catch before you look back at [sean]."
                if huntwin == 2:
                    "With such a haul... You decide it would definitely be for the best to hide the sledge until you return. No reason to let all that meat go to waste."
                if huntwin == 1:
                    "Quality meat and a decent haul. You decide you might as well obscure the sledge from casual view."
                else:
                    "Despite the lack of any substantial result on this hunt, the sledge itself is still valuable. Better hide it."
                tan "Tuck the sledge behind a bush, Niall. Leave a sign that Liam can pick up, he returns along this road. We're going to figure out what Séan saw out there."
                "He grunts, manhandling the transport off the road before joining you and Séan in pacing out into the woods once more."
                jump LostChild

        label community:
            scene bg village
            with fade
            stop music fadeout 1.0
            play music "music/Village_Fair.ogg" fadein 1.0
            show aoife at left
            show sean at right
            with moveinleft


            aoife "Okay, [heir]. I'm surprised this is the first time you've come with me on this duty. You are second-in-command in the tuath after all."
            aoife "It is almost silly for you to not be involved in ensuring Conn's will is enforced."
            tan "It shouldn't be too difficult, should it?"
            "Séan sucked in his breath through his teeth, before dawdling just a bit behind you two as you walk."
            aoife"Difficulty is subjective. It may not be a hunt, but clansmen can be more stubborn than a bull in rut. I've had many times of having to smack someone to make them toe the line."
            aoife "Leaders must know when force should be used, and when obligation to the tuath, and when flowery words."
            aoife "When they don't, it is how you end up with rebellion and civil war in a tuath. People can only be pushed so far before it becomes intolerable."
            "As she speaks, it reminds you just how intelligent Aoife is, and how fit to rule she herself is."
            "In another life, or family, she could have become the [king] of a tuath. But her family was only recently made noble, and not related enough to your own."
            "You also couldn't have asked for a better match for the gentle Conn. Aoife was strong and firm, and knew how to make herself heard among even the most obstinate [chief]s."
            aoife "Anyway. Today our job is threefold."
            aoife"We must get tribute from the local villagers. This will mostly take the form of contributions for tomorrow's feast."
            aoife"Next, we must ensure the tuath is in order, without pressing needs."
            aoife"Finally, we check up on the fianna's readiness."
            sean "That last one seems a bit out of place, doesn't it?"
            aoife "Not at all. The [fiannaleader] must ensure our best warriors are sated. They can be both our largest boon and greatest danger. A disloyal fianna can spell the end of a tuath's independence."
            "You frown. It seems infeasible for the warriors to dislike Conn. He had been raised among them, and always been such a kind person."
            "But who knew what secrets were held in people's hearts."
            "As you walk, you notice Aoife's path leads past Conchobur's smithy. You excuse yourself for a moment and lean into the open door to shout for Niall."
            tan "Niall! The job wasn't for hunting, we'll do some tomorrow!"
            niall "I'll hold you to that promise."
            tan "You do that!"
            "You rejoin Aoife, who looks at you with a raised eyebrow."
            aoife "Did you not have the choice to hunt?"
            tan "I felt I should help around the tuath today, more than seek personal glory. Hunting can always wait."
            "She rolled her eyes but lead the three of you to the clan dwellings in town. "
            "The squat houses lay in the north of the walled section, where the clan [chief]s when called by the [king] resided. The members of their families who were part of the Fianna resided there when they did not."
            "With the feast coming, most of the [chief]s are in town, making it a good time to pull their tribute for tomorrow."
            "Something which they also know and are likely prepared for."
            "The next few hours are full of talking with various clan leaders. There were only about five clans under the Ó Durcáin, being a small Tuath."
            "The hunters of the Uí Diarmada, the Christian Mac Síomóin, the traditionalist Mac Thóm, the traders of Uí Donnchú, and the forgettable Ó Flannagáin."
            "All of them were happy to contribute in their own ways, the Uí Diarmada for instance had heard of the shortage of game the tuath had found itself in, so had brought extra from its stores."
            "You weren't quite sure how to read the Mac Síomóin or Mac Thóm. Neither of their [chief] would meet with you directly. Aoife and [sean] weren't sure either, but since they did give tribute, it was shrugged off for now."
            "There was also a branch of the Ó Durcáin, who managed the largest portion of the pasturelands of the tuath and watched the western border. Of all the clans, they were the most conspicuously absent during feast preparations."
            "Old Brigit, an older member of that branch who had always been friendlier with your half of the family than her own, for as long as you knew, proved happy enough to explain why."
            "Old Brigit" "Oh, my kin? They'm been busy with somethin' on the borderland with the neighboring Tuath."
            tan "Which, ma'am?"
            "Old Brigit thought, kneading out dough as you sit around her bakery. Aoife stretches in place as she listens in. So far, she's been letting you take the lead, probably testing your iron."
            "Old Brigit" "Must be the Mugdorna. My kin do watch the largest border with them."
            "You sniff back your disbelief, leaning back in your chair and shooting a glance at Aoife and [sean]. The Mugdorna had been hostile to your home tuath for generations. They considered the Ó Durcáin rightfully subservient to their [king]."
            "If the border clan sided with them, though..."
            aoife "Thank you, Brigit. Good luck getting your work done for tomorrow."
            "Old Brigit" "Oh you better wish me more than luck, young'un. I got another dozen loaf to get in before I even can get my own midday meal!"
            "And there was her temper! But at least this was good natured. You doge a small clump of dough."
            tan "Not gonna get me as easily as you did [king] [bro]!"
            "You stick your tongue out and dodge out the door. A passing fénnid takes the dough for you, as [sean] ducks out behind you. Aoife rolls her eyes, and bids Old Brigit goodbye."
            stop music fadeout 1.0
            play music "music/Fable.ogg" fadein 1.0
            "Once you've gotten out of range of the old lady's balls of dough and outside the tuath village walls, Aoife stops both you and Séan."
            aoife "Okay. We have a choice to make on where to go now. I'm worried about the Ó Durcáin-Teorainn clan, after what we heard from Brigit."
            aoife "But we still have our job to do. The farms and nearby monastery still need to give their tributes for the season."
            aoife "Banditry has made the farms nervous, so they need reassuring. The Culdee monks have always been reluctant to give their fair share. The Culdee have the most wealth, but the Farms have the most to give for the feast."
            aoife "The talks with the visiting [chief]s soaked up more time than I expected. We only have the time to visit one of the three."
            sean "The farm would definitely be the easiest. It's odd they're late in delivery. They are usually good on tribute."
            tan "There is also the fact the Christians may dislike us pressuring the monastery. Many of them have taken offense to such before."
            aoife "Both true. As the [heir] you make the call, [tan]. You outrank me. Not an easy choice, mind you, but a taste of what your brother has to do daily."

            menu tribute_choice:
                "The farm seems the best for a large haul.":
                    $tributetarget = 1
                    tan"We need to prepare for tomorrow. The herders can wait, and we don't want to offend the church so early into Conn's reign."
                    aoife "Sounds good. I want to check in with them about these tales of bandits, too. Might have a few rebellious kids on our hands."
                    sean "Or something bigger."
                    aoife "It's near enough to our southern border that it could be Norsemen, but I doubt we have that much to worry."
                    jump tributeFarm
                "The Ó Durcáin-Teorainn herders' rebelliousness should be checked.":
                    $tributetarget = 2
                    tan"Conn is the rightful ruler. Their branch isn't a valid choice under our laws anymore. They need to accept that."
                    sean "Let's be careful, however. We might run into more than we can handle should they turn violent."
                    aoife"I don't see that. Their patriarch is old, he wouldn't risk dying to younger folk like us before he gets the chance to pull something for his family."
                    tan"Perhaps, but [sean] is right, we should go about this carefully."
                    jump tributeHerder
                "The Culdee should pull their weight, too.":
                    $tributetarget = 3
                    tan "Why should the church not help us?"
                    tan "They are subject to the same laws as all Gaels, which means they pull their weight in the tuath."
                    sean "Just avoid pissing them off too. We can't afford to lose their support with Armagh so close."
                    jump tributeChurch

            label tributeFarm:
                menu tributeFarmCheck:
                    aoife"Are you sure about pressuring them for tribute? We cannot go back to another location once we commit to one of the three."
                    "Yes, they're the ones.":
                        "With the decision made, Aoife leads you and [sean] to collect an ox and wagon from the stables. A short time later, you're trundling down the road towards your destination."
                    "No, let me rethink this...":
                        jump tribute_choice

                scene bg farm
                with dissolve

                "The tuath had historically been split into a few distinct partitions of its land. It'd been so as far back as when the great Cú Chulainn roamed the fields of Ulster, before the Confederation."
                "To the north, the woods and border with the monastery lands of Armagh. The closest Otherworld Mound was located somewhere deep in those woods but was always tricky to find."
                "To the west was the tuath's main town, Cnoc bhFianna, your home and the seat of the King."
                "The center held farmland, and a satellite monastery of Armagh nestled in the crook of a stream. the Woods extended south from the northern section, spearing between the farmland and Cnoc bhFianna."
                "The south and east was hilly, rocky pastureland, and often used as a hideout for bandits. The King's fiann often patrolled the area and ensured safe trade down south to Dyflinn."
                "Today, you journeyed for the center, to visit the farmlands surrounding the monastery."
                play sound "sound/roadWalk.ogg"
                "Even this late in the year, the farms are always pleasant to visit. The clansmen and freemen who lived out here were humble and hospitable and being in a valley the weather became quite predictable."
                "The last of the summer's harvests lay awaiting collection in the common-held fields radiating from small roundhouse hamlets."
                "These villages cluster along the streams that fed back into the Chaisleán Dhún Dealgan river and eventually the middle sea between Ireland and Sasana."
                "You have certainly seen the mood of its largest town, and common place for the fianna to collect tribute for the [king], be much brighter around this time of year."
                "[sean] had run ahead to fetch their [chief] and patriarch, Frassach Mac Conmara."
                "Aoife and you rode on the wagon, which you tie up to their humble stables. [sean] waves you over, he and Frassach waiting for you near a fallen Menhir."
                "The carvings on which tell you it was a monolith dedicated to Bres and Donn Cuailnge. A common enough dedication for a farm, though you must wonder what toppled it. It must have weighed a ton!"
                "Frassach Mac Conmara" "Pleasant to see you, [heir]. You come to address these bandits?"
                tan "Certainly, it'll be no trouble to. Tell me what's been going on."
                "Frassach Mac Conmara" "Ever since midsummer, we've had supplies, food, tools, you name it, disappearing. We've never caught anyone in the act, but since this theft's been happening from across the farm hamlets, we got no idea who it may be."
                aoife "And you only just reported this?"
                "Frassach Mac Conmara" "We told some fénnid months ago. Nothing got done."
                "Aoife shakes her head dismissively."
                aoife "Must have been Domhnall. He's a lazy shit. I need to either whip him into shape or kick him out."
                "Frassach Mac Conmara" "Yes, truly. What's prompeted us to send more word though was the desecration of this Menhir. If you wouldn't mind..."
                "He gestures for your help, placing hands on the part of the Menhir sticking up. {i}So that's why its on its side.{/i} You think, gesturing for [aoife] and [sean]."
                if Might >= 8:
                    "With the aid of your fianna and a few of the local farm-boys, Frassach and yourself manage to right the menhir. He nods appreciatively towards you."
                    "Frassach sets to work removing mud and dirt caked to its side, while continuing to talk to you."
                else:
                    "But to no avail, as the menhir remains embedded."
                    aoife"I can get my warriors out here after the feast to fix the stone. It should not lay in indignity like this."
                    "Frassach Mac Conmara" "Appreciate it, Aoife."
                "Frassach Mac Conmara" "Anyway, within the last week this Menhir and a few others were disturbed in the night. It was deep enough that none of us woke, even from the torchlight of the raiders."
                aoife "They obviously wish to turn the gods against us, or to prove the [king] has no power over his own domain. We'll prove otherwise."
                "Frassach Mac Conmara" "We need assurance that our trust in the [king] and his people are not misplaced."
                "Frassach Mac Conmara" "We haven't had much reason to trust in Conn Óg Ó Durcáin. He's green, young. He needs to prove why he deserves our loyalty as much as his great uncle and mother did."
                "Frassach Mac Conmara" "You can stand in as a surrogate, [heir]."
                $difficulty = 8
                menu tributefarmskill: #simple, not a tough task as they're compliant
                    "Frassach Mac Conmara" "What do you say, [heir]?"
                    "I'll ask [king] [bro] to provide you with some warriors.(Fili)":
                        tan"You must understand the Ó Durcáin fianna will be here to protect from raiders. It is their duty."
                        tan"We've heard troubling things from other parts of the tuath too."
                        tan"I was planning on aiding Aoife in dealing with these troubles within the month. Your farm shall be a priority of ours. What is a kingdom without its farms and freemen?"
                        "Frassach watches you carefully for a few moments. . ."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                            $Fili +=3
                            $tributewin = 2
                            play sound "sound/critSuccess.mp3"
                            "And then he burst out in an exuberant grin, embracing you heartily and easily."
                            "Frassach Mac Conmara" "Wonderful! Let us enjoy tomorrow with full hearts and end the day with full stomachs."
                            "Frassach Mac Conmara" "Boys! Help the [heir] load up their cart. Get our good supplies too, for we shall be going to a feast tomorrow!"
                        elif d20Roll+(Fili/3) >= (difficulty):
                            $Fili +=2
                            $tributewin = 1
                            play sound "sound/success.mp3"
                            "Frassach grunts, and nods."
                            "Frassach Mac Conmara" "I see the honesty of your words. We shall attend your feast and bless [king] [bro]'s reign."
                            "Frassach Mac Conmara" "But, I expect to have plenty of good food and good spirits, along with your aid in the coming weeks."
                        else:
                            $Fili +=1
                            play sound "sound/fail.ogg"
                            "And he shakes his head no, holding up a hand towards you in refusal."
                            "Frassach Mac Conmara" "Leave, [heir]. I do not trust your claims or loyalty. We shall meet with the [king] directly to solve this."
                            "Frassach Mac Conmara" "You shall get no tribute, nor shall we bless his reign, until we are satisfied that he cares for his people."
                    "You should listen, the King's Fiann can be as nasty as those bandits. (Might)":
                        "Your words are threatening, laden with the promise of violence should they not tow the line. Frassach grimaces, but Aoife supports your words with her own glower upon him."
                        tan "The contract of our people doesn't have to be a pleasant one. Refusal to provide tribute or siding with an enemy would make you our enemy."
                        tan "And enemies are easier to deal with than friends, in some ways."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Might/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Seanchas +=3
                            play sound "sound/critSuccess.mp3"
                            "Frassach takes to a single knee and bows in the dirt."
                            "Frassach Mac Conmara" "We will continue our submission to the righteousness of your clan. We only wish for your aid in dealing with threats to both your power and our prosperity."
                            tan "Of course we will help. It is our place in society to deal with these militant threats."
                            "Frassach Mac Conmara" "With Lugh's blessing, they shall be dealt with swiftly and justly at your blade."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $tributewin = 1
                            $Might +=2
                            play sound "sound/success.mp3"
                            "Frassach acquiesces to your tone, and nods."
                            "Frassach Mac Conmara" "The reality of our situation is evident. Get your tribute, [heir]."
                            "Frassach Mac Conmara" "Hopefully your warriors can turn your wrath upon the bandits, for we are of the same kindred as you."
                            tan "You have our word, Frassach Mac Conmara."
                        else:
                            $Might +=1
                            play sound "sound/fail.ogg"
                            "Frassach's eyes narrow, and fury grows on his face. It seems just about all he can do to not insult you."
                            "Frassach Mac Conmara" "Out."
                            "Frassach Mac conmara" "You shall get no tribute, nor shall we bless his reign, until we are satisfied that he cares for his people."
                    "The Brehon Laws and Seanchas make our actions clear. You, as subject to the [king], must pay tribute. (Seanchas)":
                        tan "Society is a hierarchy as it makes it easier. It helps when each class knows their place."
                        tan "We, as the nobility and warriors, protect our clan and tuath with blade and words. You, as freemen farmers, provide for the clans and tuath with plow and fortitude."
                        tan "As it is meant to be, so it is. We will tolerate no disruption of this order from banditry, so our warriors shall deal with this threat accordingly."
                        tan "You have nothing to fear, Frassach. Forgive our idleness, the chaos of last year lingers still within the clans, it seems."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Seanchas +=3
                            play sound "sound/critSuccess.mp3"
                            "Frassach nods, understanding your intentions. He bows, with fist to his chest."
                            "Frassach Mac Conmara" "Then I apologize for my impertinence, [heir]. We shall endeavor to find where these bandits are hosted and deliver them to your blades."
                            "Frassach Mac Conmara" "No enemies of the tuath's farmers will be tolerated by you, I see now. Thank you."
                            "Frassach Mac Conmara" "Let's enjoy this feast, first. With the hardship of this last year, we all could use a celebration."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $tributewin = 1
                            $Seanchas +=2
                            play sound "sound/success.mp3"
                            "Frassach Mac Conmara""I understand. Once this feast is done, you promise to follow through with your obligation as warriors and defenders of the tuath?"
                            tan "Most certainly. It will be no trouble."
                            "Frassach Mac Conmara" "Then with a clear conscious I can attend and bless the king's reign. I do expect more members of the Fiann here within the week to aid us in tracking these bandits, however."
                            aoife "It shall be done, Frassach. I've been itching for a fight, anyway."
                        else:
                            $Seanchas +=1
                            play sound "sound/fail.ogg"
                            "Frassach is dismissive of your words, waving a hand in the air like he was casting a spell."
                            "Frassach Mac Conmara" "You quote laws and tradition, but do not live it. Leave us."
                            "Frassach Mac Conmara" "You shall get no tribute, nor shall we bless his reign, until we are satisfied that he cares for his people."

                if tributewin == 2:
                    "Thankfully, with the solid loyalty of Frassach ensured and a hearty supply of food stacking up in the wagon, you feel excited."
                    "One of your first true jobs as [heir], and it went spectacularly. Hopefully this trend only continues!"
                    "Tomorrow's feast should go well."
                elif tributewin == 1:
                    "Frassach summoned his farmhands and aid from the nearby villages. [sean] strikes up a hearty tune to entertain the children as the farmhand, Aoife, and yourself work to load up the wagon."
                    "The celebrations tomorrow look just a bit brighter, with the hospitality of the farmlands not in question."
                else:
                    "Without the tribute, and the refusal of the farmers to provide support to Conn, it is time to return to Cnoc bhFianna."
                    "Aoife retrieves the wagon, and while some of the outlying farms are willing to provide something, the news of Frassach rebuking the [heir] travels fast."
                    "It may not bode well for tomorrow's celebrations, or Conn's rule in general."

                jump after_tribute

            label tributeHerder:

                menu tributeHerdCheck:
                    aoife"Are you sure about pressuring them for tribute?"
                    "Yes, they're the ones.":
                        "With the decision made, Aoife leads you and [sean] to collect an ox and wagon from the stables. A short time later, you're trundling down the road towards your destination."
                    "No, let me rethink this...":
                        jump tribute_choice

                scene bg herd
                with fade
                "The tuath had historically been split into a few distinct partitions of its land. It'd been so as far back as when the great Cú Chulainn roamed the fields of Ulster, before the Confederation."
                "To the north, the woods and border with the monastery lands of Armagh. The closest Otherworld Mound was located somewhere deep in those woods but was always tricky to find."
                "To the west was the tuath's main town, Cnoc bhFianna, your home and the seat of the King."
                "The center held farmland, and a satellite monastery of Armagh nestled in the crook of a stream. the Woods extended south from the northern section, spearing between the farmland and Cnoc bhFianna."
                "The south and east was hilly, rocky pastureland, and often used as a hideout for bandits. The King's fiann often patrolled the area and ensured safe trade down south to Dyflinn."
                "Today, you go to the edge of Tuath lands to visit the Ó Durcáin-Teorainn, the branch of your family who both herd and keep watch of the border."
                play sound "sound/roadWalk.ogg"
                "Or specifically, towards their winter village on top of some of the hills overlooking Cnoc bhFianna."
                "Like many Irish pastoralists, they often moved from place to place during the year to follow herds between common-held rundale plots."
                "The herders would share grazing land among the entire group, moving between seasonal villages to prevent over-use."
                "It worked well and ensured no one's animals ran out of food during either summer or winter, even in the harsher lands. Luckily for the herders of your tuath, the land was plentiful enough to never have been a concern."
                "The Ó Durcáin had historically been herders in Cualinge, but centuries ago your family moved north along with a few allies to carve out some land separate from the overlordships of Meath and Ulaidh."
                "They seized lands on the border of Ulaidh and Airgíalla and petitioned to join the latter of the two confederations. The confederates accepted, happy to take in vital warriors and healthy land from rivals."
                "But as always, time split clans, and new rivalries formed. Nothing remained static in the world of mortal men."
                "The current patriarch of Clan Ó Durcáin-Teorainn, Domhnall Mac Domhnall, was an old man, a warrior, who during a skirmish with the Mugdorna years ago had lost his arm roughly halfway down the upper forearm."
                "While still patriarch of the clan, Domhnall had been ineligible for any further positions in the tuath. That had never stopped him from pushing for his sons and grandsons."
                "He'd also never liked you, for reasons you never understood."
                "The village's position at the top of a hill with a winding stone-laid path meant Domhnall knew you were coming as you, [aoife], and [sean] trundled up the hill in the loaned wagon."
                "Domhnall" "[heir]. We weren't expecting you today. Why'd you come."
                "It wasn't a question, more of a demand of intent."
                "His expression was unapproachable and unreadable. Especially with the grey, bushy beard obscuring half of his face, trimmed off to form a long-goatee. You'd never seen him quite this hostile."
                "Aoife spoke up before you."
                aoife"We're here for-"
                "Domhnall" "No. I asked the [heir]. Well?"
                tan"Tribute, is what Aoife was saying. If you forgot, we have a feast day tomorrow. All of the clanns are supposed to be there."
                "Domhnall" "Aye. The Clanns. Not us. The Ó Durcáin are a clann. We are not a full clann."
                sean "Now wait-"
                "Domhall held up his hand, stopping [sean]."
                "Domhnall" "We have no reason to attend. Nor to give tribute. We provide in labor and in warriors."
                "He turned towards you again, a scowl on his face."
                "Domhnall" "Of course... should we come to an agreement over who the true [heir] should actually be, perhaps this could be negotiated. Wouldn't Cillian make a good future [king]?"
                "You shoot out a hand to hold in front of Aoife, who had almost launched herself at the patriarch. [sean] himself wasn't fairing much better. Such blatant power grabs were unheard of."
                "And you certainly could not give up your position as easily as that. It just... wasn't done."

                $difficulty = 12
                menu tributeherdskill: #tougher, not as willing to work with the player.
                    "But how to rebuke his claims. . .?"
                    "Brehon law and tradition states your family is too far distant to inherit.(Seanchas)":
                        tan "However, that does not mean your word should not be respected. You are able to declare a new clan and gain more prestige in the tuath as a result."
                        tan "Drop the idea of inheriting power. It is unbecoming to be as jealous as you are, and there is no legal recourse."
                        tan "The other clanns would never support you. If you break our traditions, especially."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $Seanchas +=3
                            $tributewin = 2
                            play sound "sound/critSuccess.mp3"
                            "He snorted, looking up towards the sky with the sun up high. His features softened slowly, before he nodded."
                            "Domhnall""Fine. You know what? That makes sense. We shall get you some tribute, and let you be on your way in peace."
                            "Domhnall""Its been silly for me to be so hostile because of your birth, [tan]. Perhaps this plan of yours, to form a new clann, yes? Would be a better way to improve the lot of my family."
                            "Domhnall""It is all I've wanted. Politics are by nature aggressive. Do forgive me."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $Seanchas +=2
                            $tributewin = 1
                            play sound "sound/success.mp3"
                            "He grunts, and waves theatrically through the air with his one hand."
                            "Domhnall" "You'll get your tribute for now, but this plan of us becoming our own clann I am not sure of. It seems a strange one, and just as unorthodox."
                            "Domhnall" "No trouble, mutually, but we must discuss with Conn and the [chief]s."
                        else:
                            $Seanchas +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "Domhnall outright growls, and like lightning grips you by the shoulder and throws you back against the wagon."
                            play sound "sound/injury.ogg"
                            "Domhnall" "You do not speak like that to your betters! My family are the rightful rulers of this tuath, indeed this confederation!"
                            "Domhnall" "It was stupid for our ancestors to settle. We are warriors, not farmers."
                            "Aoife rushes to you, pulling out her shield as Domhnall storms away shouting for aid. She and [sean] pull you onto the cart without delay and turn the ox to hurry down the hill."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                    "-Refuse to budge, stare him down-. (Vitality)":
                        "A strong, vital man, even in his old age would only respect toughness in kind. You set your stance, and stare at him once this indignity hangs in this air."
                        "You'll not moving. Your hand is at your weapon, and you simply wait. The discomfort will do the convincing for you."
                        "But with him, perhaps this'll lead to further hostility."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Vitality/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Vitality +=3
                            play sound "sound/critSuccess.mp3"
                            "He stares back, hand on his own blade, as he waits. No one moves, the village scarcely breathes."
                            "But finally, Domhnall relents, kneeling before you with hand on his knee."
                            "Domhnall" "That was impertinent, I apologize. We shall provide food and furs like we are supposed to."
                            tan"I appreciate that, Domhnall. Remember, you are welcome at the tuath. You're family. Perhaps we've let this feud fester too much. I'll talk with Conn about it when we return."
                            "He nodded, before pulling himself back to his feet and gesturing to his family to begin loading up your wagon."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $tributewin = 1
                            $Vitality +=2
                            play sound "sound/success.mp3"
                            "The angry patriarch points at you as you glower, before grunting and shaking his head."
                            "Domhnall" "Fine, I get your point. You won't be intimidated. But neither shall I. You leave in my graces, but do not mistake that for my friendship."
                            "Domhnall" "We shall give tribute, but we need to talk once this feast is concluded, as equals."
                        else:
                            $Vitality +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "With a roar that sounds like something of a fomorian monster, Domhnall grabs you by your throat and simply throws you hard enough for you to land, badly, in the wagon's open back."
                            "You see stars and feel hot wetness trailing against your eye."
                            play sound "sound/injury.ogg"
                            "Aoife and [sean] shout, muddled as you are you cannot discern the words. But they pull the wagon out and onto the roa, and get on the path back to Cnoc bhFianna."
                            "Seems your intimidation idea didn't work very well."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                    "C'mon, Cousin, trust me. If you help contribute, I'll get Conn's ear to have you on the [king]'s council. (Fili)":
                        tan"Tradition. It's a bit overrated. You've been a good supporter for decades, and both our Uncle and mother never properly recognized it."
                        tan "Under my brother and myself, I promise that will be different. You will no longer simply be another branch of the family but elevated to a clann in your own right."
                        tan "How does that sound? With changing times, we need to adapt."
                        tan "Your family deserves just as much respect as every clann in the tuath."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Fili +=3
                            play sound "sound/critSuccess.mp3"
                            "Domhnall thinks, before nodding. His unpleasant expression melts into a confident, but more friendly than previously."
                            "Domhnall" "That. . . That is actually a decent idea. It would increase the prestige of my close kin and solidify that we act as separate clanns in our own right."
                            "Domhnall" "Stewards of the Tuath could make for a fine title of my clann, do you think?"
                            "There's a twinkle in his eyes, and he winks before summoning his kin to properly load up your wagon."
                            "You worry about his reaction. It was much too cheery. Had you created a monster?"
                        elif d20Roll+(Fili/3) >= (difficulty):
                            $tributewin = 1
                            $Fili +=2
                            play sound "sound/success.mp3"
                            "Domhnall scoffs, shaking his head, but gestures for his kin to load on the wagon."
                            "Domhnall" "A stupider man would interpret that as you no longer considering us kin. However, I see the intention behind your words is good."
                            "Domhnall" "This warrants discussion with the [king], soon. I would appreciate the position, but let us focus on this feast and winter, first."
                        else:
                            $Fili +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "Domhnall glowers and grabs you by the neck before you even can react. His face seems huge, monstrous as he pulls you close."
                            "Domhnall" "So you no longer see us as family. Fine then."
                            "With his grip, he throws you back, leading your head to smack hard against the side of the wagon. Your knees buckle, and you just about catch yourself on the same blood-spattered wood."
                            play sound "sound/injury.ogg"
                            "Aoife and [sean] jump in the way of further assault, but make to retreat, pulling you into the wagon and setting on the road without more than angry shouts and enemies behind you."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                if tributewin == 2:
                    "Once the rest of his family had gotten the trophies, furs, meat, and wool laid out in the wagon. Don and you have caught up a bit, and now he has an actual pleasant smile on his face."
                    tan "We are family, Dom. You helped raise my mother. I would love to see you and your kin around Cnoc bhFianna more. Brigit's missed her brother, and the split has affected the whole of the tuath."
                    "He smiled, and nodded, before laying a strong hand on your shoulder and squeezing."
                    "Domhnall" "Don't tell Conn, but I feel you'll be an even better leader than he. You do have a way with words."
                    "Domhnall" "See you tomorrow."
                elif tributewin == 1:
                    "Domhnall" "This isn't the end of our discussions, but still, go in peace."
                    tan "Thank you. Hopefully this is the start of a renewal of our relationship as family."
                    "While the scene is still tense, Domhnall's kin still helps load up the wagon with the basics of the tribute. The meat will certainly be welcome for the feast tomorrow, and furs for the winter."
                    "You say goodbye with a bit of worry, hoping he keeps his word to not stir trouble."
                else:
                    "The wagon clatters down the trail, missiles fired after and embedding in the wood by the offended herders and warriors."
                    "With this failure, it could be a weakness revealed or a weakness created. All Aoife can tell you is you need to alert Conn as soon as humanly possible."
                    "Aoife tends to your wounded head in the back of the cart as [sean] drives you onward. Once you regain your senses, you take the reins back as the other two watch the trail for anyone following. No one was, luckily enough."
                    "Cnoc bhFianna and Conn awaited."
                jump after_tribute

            label tributeChurch:
                menu tributeChurchCheck:
                    aoife"Are you sure about pressuring them for tribute?"
                    "Yes, they're the ones.":
                        "With the decision made, Aoife leads you and [sean] to collect an ox and wagon from the stables. A short time later, you're trundling down the road towards your destination."
                    "No, let me rethink this...":
                        jump tribute_choice

                scene bg church
                with fade
                stop music fadeout 1.0
                play music "music/Ancient_Irish_Chant.ogg" fadein 1.0
                "The tuath had historically been split into a few distinct partitions of its land. It'd been so as far back as when the great Cú Chulainn roamed the fields of Ulster, before the Confederation."
                "To the north, the woods and border with the monastery lands of Armagh. The closest Otherworld Mound was located somewhere deep in those woods but was always tricky to find."
                "To the west was the tuath's main town, Cnoc na bhFianna, your home and the seat of the King."
                "The center held farmland, and a satellite monastery of Armagh nestled in the crook of a stream. the Woods extended south from the northern section, spearing between the farmland and Cnoc na bhFianna."
                "The south and east was hilly, rocky pastureland, and often used as a hideout for bandits. The King's fiann often patrolled the area and ensured safe trade down south to Dyflinn."
                "Today, your work brings you to the center of the tuath, to the small monastic village within the tuath's lands."
                play sound "sound/roadWalk.ogg"
                "The monastery was where the Christian faithful of the tuath and beyond gathered. Not everyone could hazard a trip to a center like Armagh, so the local abbots and monks were always happy to host sermons for the freefolk and nobles of the book."
                "It was a simple affair on the exterior, a small stone complex with a bell tower that rung out the hours loud enough for everyone in the farmland to hear, along with the daily calls to service."
                "Culdee, or more properly, the Céilí Dé, were monks known for their piety and missionary activity throughout the Isles and beyond. "
                "A Céilí Dé monk was known to have singlehandedly converted the Kingdom of Mercia a century ago, and despite their mission being unfinished still were highly prestigious."
                "While traditionally ascetic, the ones in Ireland had grown a propensity for material wealth much like their noble counterparts in the fort-towns."
                "But the rural folk had just as easy access to holy sites for the Elder's ways, and the druid often were more willing to get out of the chapel to wander the countryside."
                "When Padraig wasn't busy arguing with [td] in Cnoc bhFianna, he often spent plenty of time out here in the monastery or Armagh."
                "Today, though, he seemed to solely have business within the tuath village, as his normal place proselytizing on the monastery's patio was empty."
                "Given you had seen him not even an hour ago still arguing with Medbh, he likely would be staying in Cnoc bhFianna until at least the end of the feast."
                "But the church itself was likely one of the newest and prettiest buildings in the tuath which was treat enough for you visiting it on a difficult task."
                "The nicely dressed interior made the smallish stone rooms feel airy and pleasant, with wooden pews and golden ornamentation."
                "The wealth of the church is plainly on display, in a way you hadn't even seen king's revel in."
                "Sconces of metal, painstakingly bound and illuminated texts, soft cushions in the monk's quarters, luxurious curtains of a material you struggled to even name, and goods that bore marks of every province of Ireland and beyond."
                "And the large cross, set with gems and wrought from gold and iron in rounded, knot-like patterns. That was almost a show-stopping piece alone."
                if heritage == 3 or faith == 5:
                    "You briefly fantasize about your Norseman brethren raiding such monasteries, wondering if riches like these were what convinced them to attack rather than trade."
                    "Dad did always have the most interesting stories of Christian riches. . ."
                elif heritage == 4 or faith == 2:
                    "It is hard to not be purely humbled by this house of God. Its splendor only surpassed by the divine light of heaven itself."
                    "Aoife nudges your side, an amused look on your face from your hanging jaw and reverent stare at the chapel's cross."
                else:
                    "The opulence was almost blinding. You could scarcely imagine how the priests justified not paying any tribute when their house of worship looked as such. Even the druids contributed."
                "An elder priest approaches you as you idle at the entryway taking in the decor. He must be a new arrival from Armagh, given your utter inability to place his face or name."
                "Priest""You... You must be the [heir], yes?"
                "You give him a simple nod in return, his stance rather nervous and closed off as he eyed you, [sean] and Aoife over. Was he uncomfortable from your weapons? How strange."
                "Priest""Have you come to be baptized? Or to attend a service? The next one isn't until an hour before sundown."
                if faith == 2:
                    tan "I have already been baptized, Father. We're here for the tuath's tribute. The monastery hasn't given any this season."
                elif faith == 5 or faith == 4:
                    tan "Tribute, old man. The church hasn't paid up to the [king]. No one is exempt."
                else:
                    tan "Not today. We're going around collecting tribute before the feast tomorrow."
                "The priest huffed indignantly clutching at the collar of his robes with one parchment-skinned hand, his crucifix in another."
                "Priest""The holy church of Armagh is above tithes to local lords. We pay only to the Church itself and to God's graces."
                aoife "And who is the one who protects you from raiders and, as you call them, heathens?"
                "Priest" "God and prayer!"
                sean "I've never seen a miracle save a church from raiders, and according to locals, they've become an issue, eh?"
                "Priest" "They have never touched a single stone of this church. I promise you, He above is the truest way to protect yourself from eternal damnation."
                "His indignance was only growing at the insistence of your companions to keep arguing. No matter what the others say, it just leads back into the spiel of how faith will aid them, they weren't subjects, etc."
                "You figure it's time to stop this, once you get the time to think through of how to convince this obstinate  priest."
                "You clear your throat to get his attention back, before speaking your case."
                "But right when you are about to, you hear a gentle cough from behind you. The actual abbot of the monastery, Padraig, apparently has returned from town. He gives a nod to all three of you."
                tp "My young ones, the Church of the Holy Christ have privilege from taxation in most nations of this age. At least those who are properly Christian."
                tp "We return the tithes and money given to the locals in the form of service and education, as opposed to the nobility's strong-arming and wars."
                "You sigh and lay your hand on Padraig's shoulder. He raises an eyebrow but waits for your words."

                $difficulty = 10
                if faith == 2:
                    $difficulty -= 2
                elif faith == 5:
                    $difficulty += 2
                menu tributechurchskill: #moderate, just due to unwillingness to part with wealth or food.
                    "Druids pay tribute to the [king]. Why shouldn't abbots? (Seanchas)":
                        tan"The order of society is kept through wealth circulating and being bequeathed by the [king]. It does not stay with him."
                        tan"If the church was willing to open its doors to the Fianna, I'm certain we could find something we could take as tribute without resorting to relics."
                        tan"It would be a shame to sell unique relics and ways to draw more pilgrims to the tuath. More trade and visitors will help everyone here."
                        tan "So what say you about tribute? Will you follow our traditions or stay apart and refuse to adapt to how Gaels rule? We can be just as stubborn in our beliefs as you, Abbot."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $Seanchas +=3
                            $tributewin = 2
                            play sound "sound/critSuccess.mp3"
                            "Padraig sighs, and shakes his head in disbelief. But he soon embraces you and lets out such a hearty laugh you for a moment forget his age."
                            tp"The young child I remember trying to make silly pranks on my person and all religious figures certainly has grown up, haven't they? You seem to be right on this."
                            tp"I should speak with Armagh. Perhaps this assimilation should be two ways, and more equitable. Let us look for something for you to bring back as tribute."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $Seanchas +=2
                            $tributewin = 1
                            play sound "sound/success.mp3"
                            "He pulls away, face deep in thought as he paces towards the altar. Looking over, he grabs finely bound book and leaves through it."
                            "His finger pokes at a passage. He reads aloud in Latin, before translating into Gaeilige."
                            tp"The book of Matthew states: \"Thou shalt love the Lord thy God without limit from your heart, your soul, your mind. The greatest commandment is that.\""
                            tp "\" Second comes alike: Thou shalt love thy neighbor as thyself. On these two commandments hang all laws and prophets.\" "
                            tp "The church shall open its coffers to the local tuath as equals. Not as a tribute, but as a gift of goodwill."
                        else:
                            $Seanchas +=1
                            play sound "sound/fail.ogg"
                            tp"I see you have never read the scriptures or forgot their lessons. A christian does not compromise with the heathen, for they are the misguided future flock."
                            tp"For Ireland to be saved, it must be Christian. For it to be Christian, we need wealth."
                            tp"So no, leave us and be without tribute from here forevermore."
                    "-You help yourself some expensive looking ornament- And why should I not just take it? (Might)":
                        tan"I'm certain the Norse could have had the right idea. It may be a bit distasteful, but I wonder how well this would sell in the Dyflinn markets? Plenty of silver for food this summer, or whatever I fancy buying."
                        "You notice you grabbed a crucifix, though you just as quickly place it back. Padraig and the priest both visibly relax, where a moment before they were wound up tighter than a cat whose tail had been trod on."
                        "Hopefully this was enough. You had no desire to actually steal from the church. Conn would give you no end to hearing of it."
                        tan "Well? Which will you choose? Tribute by force, or through willing participation?"
                        if faith == 5:
                            $difficulty -= 4
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Vitality/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Vitality +=3
                            play sound "sound/critSuccess.mp3"
                            "Padraig grimaces, but nods. He refuses to speak as he orders his monks to begin collecting food stores and silver for the wagon. But before you leave the church, he speaks."
                            tp"Perhaps in the future we shall be able to come to an understanding with words, rather than just force and intimidation. It is very un-Christian to do so."
                            tp "Primitive, almost."
                            tan"But certainly effective."
                            tp "Indeed . . ."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $tributewin = 1
                            $Vitality +=2
                            play sound "sound/success.mp3"
                            tp"Very well. We have food that would be appropriate for tomorrow's feast. I expect you to be on better behavior than today, however. A continued intimidation no longer holds the same effect, if no downside comes of it."
                            "You wince, and suck in air through your teeth. Was the intimidation that see-through? But they still agreed so. . ."
                            tan"There will be, I promise. Tribute is a regular thing, Padraig, not a 'when we feel like it' thing."
                        else:
                            $Vitality +=1
                            play sound "sound/fail.ogg"
                            tp"Get out, or I shall call my monks to arms."
                            "It was as simple as that. The intimidation had crossed a line many Christians were sensitive to."
                            "Threaten their relics and shiny things and they got just as defensive as a Norseman who found a badass axe in a bog."
                            "The monks very gently but firmly escorted you out, and slammed the door behind you."
                    "Helping the [king] is helping the people. Why not promote good-will between crown and mission? (Fili)":
                        tan"Isn't Christ all about good will among men, aiding your fellow human, and providing whatever you can to your neighbors? Even the most cursory knowledge of the Bible tells that."
                        tan "And wouldn't it be helping your fellow man to donate wealth and food to the [king]? It is the role of a [king] to provide for all who live in a tuath, just as a priest provides for the spirituality of their flock."
                        tan "Have a heart, Padraig. If you help us, we can help you in the future."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                            $tributewin = 2
                            $Fili +=3
                            play sound "sound/critSuccess.mp3"
                            tp"{i}Quid pro Quo{/i}, then?"
                            "The monastic thinks for a moment, before nodding enthusiastically. A strange twinkle enters his eyes as he looks between the three of you. You feel just a bit uncomfortable as he does. What is he planning?"
                            tp"An alliance seems prudent. The Culdee and Church of Ireland has never looked gift horses in the mouth. Well, unless of course they held treacherous Greeks."
                            tan"Why would Greeks be inside of a horse?"
                            tp"It is a long story. How about for now, we focus on getting you loaded up for the feast, tomorrow?"
                        elif d20Roll+(Fili/3) >= (difficulty):
                            $tributewin = 1
                            $Fili +=2
                            play sound "sound/success.mp3"
                            "Padraig sighs, pinching the bridge of his nose. He seems almost annoyed, but that washes away to a friendly appearing smile. Was it something you said that had annoyed him?"
                            tp"We can provide some tribute for now, but this has simply made me realize I must discuss the state of our relationship, the crown and the church, into better focus with [king] [bro]."
                            tp"You must be just a bit daft to try leveraging the holy scripture against a priest, but you do seem to know what you speak of, even just a bit."
                        else:
                            $Fili +=1
                            play sound "sound/fail.ogg"
                            "Padraig, very simply, couldn't stop laughing at your words."
                            "Between the guffaws, cackles, and laughter, you manage to discern a few phrases such as 'Have you ever read the book?', 'The devil must be running out of tricks', among other discouraging statements."
                            "He manages to calm down soon enough, a bemused smile on his face."
                            tp"No, we will not be giving you tribute. How silly of you to even try to get a righteous man such as myself to sin and accept the words of an uneducated noble."
                            tp"I have not laughed that hard in very long. Good show, [tan]. Now, get going."
                            "He brushed you off, literally, gesturing with a few fingers to tell you to leave in a sweeping motion."

                if tributewin == 2:
                    $Wealth += 10
                    "Padraig catches you as the last of the trinkets and food from the monastery is loaded up on the wagon. He leans in, whispering to you."
                    tp"I hope our newfound understanding shan't be wasted on trifles such as feasts and tribal raiding. Trade should be your focus. The Norse are ripe for conversion, the same as the Gaels. With the right hand,"
                    "He looks at you significantly, before continuing."
                    tp "Ireland can become a Christian nation, even if it is not politically unified. Change is in the air this winter. Not everything will be the same this time next year in Ireland."
                elif tributewin == 1:
                    $Wealth += 5
                    "You load up the last of the tribute onto the back of the wagon and Padraig pulls you aside. He glances towards [sean] and Aoife, before looking at you intently."
                    tp"You need make no promises today, but we Culdee monks have long memories. If you side with us over the druid, I am certain the Church of Ireland shall be a great ally. A Christian [king] here could promote many things."
                    tp"Remember my generosity today. I certainly will."
                    "He rushes away before you can properly respond, leaving you with questions of his goals and intentions for the Tuath."
                else:
                    "Despite leaving not on the best terms with the monks, they remained polite enough to offer food for the road and preparations for your oxen."
                    "You feel almost embarrassed for it. They remain polite even after telling you off for attempting to pressure them into giving you wealth and supplies."
                    "You pass the time talking idly with [sean], even with the oddly cheery monks going about their work."
                    "Once the ox was watered and ready, you leave the village and church to head back to Cnoc bhFianna."
                jump after_tribute

            label after_tribute:
                $ d20Roll = 0
                $ difficulty = 0
                $ renpy.fix_rollback()
                scene bg woods
                with fade
                play music "music/Return_Forest.ogg" fadein 1.0
                play sound "sound/roadWalk.ogg"
                if tributewin == 2:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 2
                    "With wagon in tow, laden with tributes from the distant parts of the tuath, the three of you begin on your trip through the forest towards the tuath village."
                    "After such a good job done enforcing the [king]'s will, you certainly would have plenty for the feast tomorrow, along with improving your own prestige."
                    if tributetarget == 1:
                        "The farm had made good on its promises, with the barrels of food in the back of your wagon, tomorrow's feast would be a stellar one."
                    elif tributetarget == 2:
                        "Game, wool, and trophies lay in the back of the wagon as you drive it forward, promising a safe winter for the whole of the tuath with its bounty."
                    else:
                        "The wealth and goods of the Culdee monastery would help promote trade over this winter and ensure prosperity for the next few seasons."
                if tributewin == 1:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 1
                    "The wagon bounces along, pulled by oxen, as you, Aoife, and [sean] pass through the forest on the way back to Cnoc bhFianna."
                    "With your success, it should ensure the feast tomorrow goes off without a hitch."
                    if tributetarget == 1:
                        "While the wagon is lighter than you might have liked, the food would help keep people fed during winter even if it wasn't as suited for feasting tomorrow."
                    elif tributetarget == 2:
                        "The herders had refused to give a full tribute, only giving a token of game, wool, and furs. Hopefully you can convince them to be more amenable after the feast, or after."
                    else:
                        "With the Culdee agreeing to start properly pay tribute again, you are certain their goods will aid trade to Armagh and Dyflinn. Good news for the future of the Tuath."
                else:
                    "Going back, the mood is much more somber."
                    "Without a the whole tuath pitching in, the feast tomorrow may not go over well. Hopefully your attempts haven't soured relations with the people of the tuath."
                    if tributetarget == 1:
                        "The farmers couldn't even promise showing up tomorrow, with their insistence of watching their stocks so bandits didn't doom them for this winter."
                    elif tributetarget == 2:
                        "You feel you barely escaped the border clan with your skin intact. With that jump to violence, you feel Brigit's story of them conspiring is all the more validated. It may be time to warn Conn."
                    else:
                        "Being told off at the Culdee monastery stung, but at the very least it was limited to that. Perhaps you can speak with their abbot again later to smooth things over."
                show sean at right with dissolve
                "[sean], who had been walking alongside the wagon as it went, gestured for you to stop. You heel the oxen and raise an eyebrow at your friend."
                tan "What's going on?"
                sean "I saw a rabbit."
                show aoife at left with moveinleft
                aoife "A. . . rabbit?"
                sean "It looked like a magic one. I swear it had antlers."
                aoife "Antlers."
                sean "I swear upon the tuath gods that I am not lying."
                "You and Aoife glance at each other, and you dismount the wagon."
                tan "We have a bit of time before nightfall, might as well see if there's any trace of this antlered rabbit. Aoife. Get the wagon off the road while we go look. This shouldn't take long."
                aoife "Certainly."
                hide sean with moveoutright
                "[sean] waited anxiously, eyes at the forest. Once Aoife had safely stowed the wagon and oxen, he immediately dashed off into the woods. You jump after to follow, with Aoife taking up the rear."
                hide aoife with moveoutright
                "What was he getting you into this time. . ."
                jump LostChild

        label wolves:
            scene bg woods
            with fade
            stop music fadeout 1.0
            play music "music/Surreal_Forest.ogg" fadein 1.0
            "The tuath had historically been split into a few distinct partitions of its land. It'd been so as far back as when the great Cú Chulainn roamed the fields of Ulster, before the Confederation."
            "To the north, the woods and border with the the monastery lands of Armagh. The closest Otherworld Mound was located somewhere deep in those woods but was always tricky to find."
            "To the west was the tuath's main town, Cnoc na bhFianna, your home and the seat of the King."
            "The center held farmland, and a satellite monastery of Armagh nestled in the crook of a stream. the Woods extended south from the northern section, spearing between the farmland and Cnoc na bhFianna."
            "The south and east was hilly, rocky pastureland, and often used as a hideout for bandits. The King's fiann often patrolled the area and ensured safe trade down south to Dyflinn."
            "Today, you and [sean] are heading out to join [liam] and [nora] in dealing with the wolf den to the northwest of the tuath."
        label soundtest:
            show sean at right with moveinleft
            play sound "sound/forestWalk.ogg"
            "The woods have a chill to them, blowing in from Armagh to the north, as you walk towards the meeting point with Liam and [nora]."
            "You look up, watching the sky disappear as the forest swallows it a pine-needle at a time."
            "It's always a strange thing, to go from the brightness of an open plain or hill to the constant twilight of the forest. Was it no wonder that the Fae and Tuath Dé preferred it to the increasing open skies of Ireland?"
            "They drew power from the land and woods, in the same way they taught the druids. So to stray too far away from the forest was to invite challenge from humans to test their magic."
            "It always interested you how the Christians formed magic seemingly without source, and the Norse from the seas and air, with similar ease."
            if Seanchas >= 12:
                "Though no druidic expert, you know much of magic appears to have the same nature regardless of source, so perhaps the traditions were all just ways to access this energy."
            elif Seanchas >= 6:
                "While you have theories, you figured you'd need to do more research and delve into lore to properly understand the magic behind it."
            else:
                "But, being a noble rather than a druid, even with the little education in the mysteries you received, the intricacies of magic are still deep and mysterious."
            if Finesse >= 8:
                "You hear a twig snap beyond the trees, attention being drawn from your thoughts. Something was out there, was it?"
                "Your eyes scan the treeline, and you stick out a hand to stop [sean]. The two of you had been traveling in silence up until now."
                if Finesse >= 10:
                    "And there, you spot her. [nora]. She must have gone ahead to find you. You smirk, and wave her towards you."
                    tan"Nora! I see you out there, you deer-chaser!"
                    "A childhood tease created among your little group. Nora always bragged about chasing down deer as a child, a boast she never proved until adulthood."
                    nora"Did you... How did you see me? I swear I've gotten sneakier!"
                    tan"Not enough for my eyes."
                    "She groans, stepping forward and down towards the path with you and [sean], who was highly amused by all of this."
                else:
                    "But you cannot pick anything out. You shrug, and gesture for [sean] to continue. Along the path."
                    "Within about ten minutes you feel a tap on your shoulder."
                    "Freezing up, you spin around and grab the hand. They grip back, like arm wrestling."
                    "But. . . "
                    "Its [nora], all smiles and looking rather smug. She embraces you using the grip she already has, and laughs heartily."
                    nora"I cannot believe I snuck up on you after that blunder of mine. I was certain you'd notice me!"
                    nora "Anyway. . ."
            else:
                "You and [sean] begin chatting, trying to pass the time as you follow the trail. You swear Liam's cabin should have been just around the last bend."
                "But it wasn't, or the next five."
                "About a half-hour later, you feel a tap on your shoulder."
                "Freezing up, you spin around and grab the hand. They grip back, like arm wrestling."
                "But. . . "
                "Its [nora], all smiles and looking rather smug. She embraces you using the grip she already has on your shoulder to pull you in and laughs heartily."
                nora"I cannot believe I snuck up on you after that blunder of mine. I was certain you'd notice me!"
                nora "Anyway. . ."

            show nora at left
            with dissolve
            "Nora grinned. Another friend from childhood, like [sean] and [niall]. Blond and willowy like Liam, but with blue tattoos much like Aoife."
            "She'd always been mischievous, but never malicious. A good person, in your eyes, and you always cared about her dearly."
            nora "'m here to lead you towards Liam's cabin. You two got off track at least a half-hour back."
            sean ". . . How? There was only one forest trail."
            nora "Yup. One that leads two Armagh. Liam built his place off the main track a good way distant."
            "You shrug as [sean] looks at you incredulously. You honestly forgot exactly where it was, anyway. Liam liked moving around, so he had a good number of small homes dotted around the forest."
            tan "Well, lead on then, friend."
            "She gives a thumbs up, and spins on her heels to lead you towards Liam's cabin."
            nora "Let's get a move on, we only have today to deal with this. If we can't get the roads to Armagh clear, trade'll slowly die. Not to mention the cost in livestock."

            show text "{b}{color=#FFFFFF}[nora] has joined your fiann, improving your finesse and seanchas!{/color}{/b}" at truecenter
            with dissolve

            $ Finesse += 2
            $ Seanchas += 1
            if renpy.in_rollback():
                $ C_niall = False
            else:
                $ C_niall = True

            pause 1.5
            hide text
            with dissolve

            scene bg liamcottage
            show nora at left
            show sean at right
            with fade

            "The cabin sat ahead in a pleasant glade. A solid construction of logs and thatch, you can't imagine how much work he had done to make more than one. But there he sat on a log, fletching some arrows in preparation for the wolf hunt."
            "He gives you a nod but continues working. The hunter had been a fixture in the tuath for practically generations now. He'd been an aid of the previous three kings, and the chief hunter of the [king]'s fianna."
            "He was a freeman, diligent but solitary and free-spirited. Not a very humorous person, but people could rely on him."
            "He stood tall with grey-blond hair and willowy frame honed by years hunting in the forest and hills."
            "Nora had always admired him, as well. From a young age she had tagged along on his hunts, to the point he actually enjoys her presence out in his solitude in the forest."
            "He'd never liked being bothered, but she was a daughter to him. You always thought it rather sweet, personally."
            if training == 3 or childhood == 4:
                "He thought much the same about you, after your childhood and training with him. He rarely showed it, but you knew."
            nora"Okay, I'm glad y'all are here to help out. It'd be one thing if it was a wolf or two, but Liam's said it's a full pack. Not gonna be as easy to deal with."
            sean"What's the trouble in a few pups?"
            nora "It's the mothers that's the trouble. Vicious fuckers when cornered, but a mother cornered will kids will die twice before they stop."
            nora"Plus, they get even more territorial towards humans as you get closer to the den."
            "You nod, striding across the glade towards Liam."
            tan"Hey there, hunter! How goes the hunting this season?"
            show liam with dissolve
            liam"Slow. The lingering cold through spring meant animals were sparse. Its picking up now, but I can feel this late warmth won't last."
            tan"It might be a rough winter. Hopefully trade'll help, and hunting."
            liam"Time will tell."
            "He shrugs and finishes his work with the arrows. With a stretch, he sets his now filled quiver aside to stand."
            liam"Only you two?"
            tan"Conn thought we would be enough. A few good hunters can take down a pack. Don't you have Ádh too?"
            "With the mention of her name, the wolfhound perked up and started panting, practically charging from her post on the far side of the clearing. Liam gave a soft smile, and pet behind her ears as she came to a stop near him."
            liam"Certainly. She has always been a boon."
            liam"Anyway. I have two plans we could use when it comes to wolves. Let me know what you think."
            liam"If they think their den is no longer safe, they'll relocate. If we scare them, or lure them off, we can ensure they don't come back if we destroy the den."
            liam"Or, we kill the hunters. Just reduce their number and prevent them from overpopulation."
            liam"Such a thing will be a bit tougher, but catching a few wolves is easier than the final option."
            "[sean] pipes up, making Liam raise an eyebrow. The bard never had been much of a hunter."
            sean "Why don't we just kill them all, if we must rid ourselves of them. It'd solve the problem, certainly."
            liam "It would be dangerous, [sean]. If we try to kill them all they'd get even more defensive."
            sean "But they'd still be dead."
            "Liam shakes his head, and sighs."
            liam"I myself would prefer to lure them away. With our numbers it'll be both easy and safe. I don't want to put us in danger if it isn't necessary."
            nora"Killing a few's my take. A good middle ground. Liam's the expert, but we don't wanna throw off the cycle of the woods."
            liam"An impasse then. [heir]?"

            menu wolf_choice:
                "We should lead them away. No need to kill them if we can part peaceably.":
                    $wolftarget = 1
                    show screen virt_comp_overlay
                    tan"Liam is right. There's no need to be any sort of violent if we have the intelligence and numbers to lure them or scare them."
                    tan"It'll be better to be clever, than put ourselves in undue danger."
                    jump wolflead
                "If we can kill the pack's hunters, the rest should seek safer areas.":
                    $wolftarget = 2
                    tan"Nora's right on this one."
                    tan"The hunters are the threat, if we kill or wound them, we'll accomplish the task more certainly than if we simply scare them and killing is too dangerous."
                    jump wolfscare
                "Better to solve the problem now: Let's go after the den.":
                    $wolftarget = 3
                    tan"If we kill them, they're dead. [sean] is right on this. We don't want to scare or kill a few only for this to become an issue down the road."
                    tan"To hell with the danger, we're all strong and able enough."
                    jump wolfkill

            label wolflead:
                menu wolfLeadCheck:
                    liam"Are you sure about that plan?"
                    "Yes, it should work.":
                        tan"Its the best option, at the very least."
                        liam "Then let us get going."
                    "No, let me rethink this...":
                        jump wolf_choice

                stop music fadeout 1.0
                play music "music/Part_of_the_Pack.ogg" fadein 1.0
                scene bg wolfden
                show liam
                with dissolve
                "The den was in a remote part of the woods, sheltered under a cliff. It made for a tough thing to approach."
                "With the only visible entrance having one way to approach, it meant the wolves would see, hear, or smell you long before you entered the area."
                "Liam had tried to get close before, to get a count of the wolves, but they drove him off, even with the help of his hound."
                "Hopefully as group, you stand a better chance of defeating the defenses of the den."
                "Liam lead the way to a shelter he set up to hide scents just out of the range of the wolves but close enough to the den."
                "When he arrived, he sat the three of you down and drew out the general shape of the den on the ground."
                liam"So. They have a good number. about ten."
                sean"Ten?!"
                nora"Indeed. The situation this summer aided them in proliferating, and a good number of them are young adults who haven't broken away yet."
                nora"Two competing large packs would be disastrous for herds and farmers. We gotta deal with 'em now."
                liam"Indeed. Not a fun situation, but we'll handle it. Either today, or within the month."
                "Liam's tone is serious, and he watches both you and [sean] for reactions. Séan, for his credit, is only shaking a bit. Wolves had always scared him, so to face ten? Terrifying."
                "You lay a hand on his shoulders, and squeeze. It's a wonder he's the one that suggested to exterminate them!"
                "Must have been from that fear."
                tan"I'm certain you have plans for us?"
                liam"Of course."
                "He first looks at Séan and gives a soft smile."
                liam "First plan. Use Séan."
                sean "Oh no. . ."
                liam "Use your music, silly child. I'm certain you've hunted using the magic of song before, I know you. The same principle holds for wolves. Enchant them away."
                sean "I see a few differences. . ."
                liam "Next. Mimic animal calls to lure them away or scare them. It'd work for obvious reasons. I'd prefer this, it's in my purview the most."
                liam"Finally, run along like rabbits to chase away the hunters, then scare away the mother and kids."
                nora"That seems like it might have the most potential, teacher."
                liam "Perhaps. We'll see."
                liam "We've voiced our opinions. [heir]? Tiebreaker again, it seems."
                #plans on how to lead them off.
                    #Wild animal calls to frighten them
                    #Stay just out of reach, goad them after
                    #use music and voice to pull them along
                $difficulty = 8
                menu wolflead_skill: #simple but time consuming
                    "Mimic calls of wild animals to lure or scare them away. (Seanchas)":
                        tan"I've practiced a bit, but I feel Liam should lead on this. He's spent his whole life hearing the sounds of the wild, after all."
                        liam"Indeed. Strange noises will more likely scare them off though, so I think we should do that."
                        nora "Wouldn't it be better to sound like a wolf pack?"
                        liam "No. They may instead challenge, as we don't have enough voices to make a large enough sound."
                        nora "Makes sense on that."
                        liam"Well, let's get started."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $Seanchas +=3
                            $wolfwin = 2
                            play sound "sound/critSuccess.mp3"
                            "Who knew making rediculous, aggressive sounds on the forest could be both useful and incredibly fun?"
                            "You make howls and growls, Liam makes hoots and hollers, Nora let out snorts and screeches, and Séan whoops and roars."
                            "A cacophonous mess of sound, that undoubtedly frightened every gods-damned wolf throughout the forest."
                            "As a group, they seemed to work! As you approached the den, the occasional sound of scuffling could be heard, and whining whimpers."
                            "By the time the four of you arrived, there was nothing in the den."
                            liam"I'm not quite sure if that's enough. . ."
                            "He snorted, glanced around, and immediately set to work again with the noises. The rest of you follow suit and spread out to properly chase off the wolves."
                            "Hours later, you reconvened at his shack to find a beaming Liam."
                            liam "Perfect."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $Seanchas +=2
                            $wolfwin = 1
                            play sound "sound/success.mp3"
                            "Turned out, making animal noise was a skill you were halfway decent at. You even had a bit of fun doing it!"
                            "The noises you made were often a bit ridiculous, and it took a good bit of work to convince the wolves to actually start worrying."
                            "The four of you made sure to stick on the edge of their lands to prevent them sniffing you out, Keeping in shadows and out of sight."
                            "Wolves weren't stupid, if they saw a bunch of humans, they'd likely get defensive."
                            "The nebulous threat of dangerous animals seemed to be working, but you still spend almost all of the day out and making noises."
                            "Gods be damned, you felt your voice would become sore by the end of the day."
                            "But luckily enough, Liam came by shortly before dusk, stealthily tapping your shoulder."
                            liam"I think we got them. I checked the den, and I can scarcely see a pup."
                            liam "Let's get back."
                            "You nod, and grin."
                            tan "Told you it'd be no trouble."
                        else:
                            $Seanchas +=1
                            play sound "sound/fail.ogg"
                            "While at first, making crazy sounds in the forest was kind of fun, it turned dangerous fast."
                            "When the sounds first start, the wolves proved to be intrigued, rather than frightened. You think it could be that they thought the sounds must be some new prey."
                            "When sought out the sounds, Liam got worried."
                            "He began ushering you towards the others, his own animal calls cutting off."
                            liam "Of course they're confident. . . "
                            sean "Liam, what do you mean?"
                            liam "Pack's too big, they've gotten bold. We'll need to come back with more people."
                            "You let out a curse, spitting towards where the wolves are visible over the hill. As you do, the leader turns to stare towards you, hackles raised."
                            "He barks out, and the wolves, five in all, start running."
                            sean "Shit!"
                            "It takes the rest of the day to dodge the wolves and make it back to the cabin. While no one was caught, it proved to be incredibly annoying."
                    "Run along just out of reach, with some of us goading along behind. (Vitality)":
                        tan"Let's be just a bit daring. I could use the run as it is, too."
                        nora"Sounds fun!"
                        liam "This is meant to be work, not fun."
                        nora "Can't it be both?"
                        liam "Perhaps, let's get to work, though."
                        "You nod, and Liam ducks out of the shack to lead the way."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Vitality/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Vitality +=3
                            play sound "sound/critSuccess.mp3"
                            "All in all, the plan works nicely. The wolves take the bait almost instantly, with each of you, Liam excluded, running past the den in turn."
                            "You go first and get the largest number behind you. The leader almost catches you at one point, chomping at your heels, but a clever jump and dodge keeps you out of reach."
                            "Séan immediately begins panicking as he runs, but you can't blame him. Nora runs after, pulling the rest of the hunters."
                            "Or at least, you guess. Your view of the den disappears as you run off towards the east in a winding path."
                            "Liam was supposed to run in after, scaring out the mother and pups with aggression. Once they were gone and running, hopefully the hunters would start scattering."
                            "An hour of running later, the wolves at your back are dropping off, scattered and flagging from exhaustion. No beast could match humans in sheer vitality!"
                            "So, you circle around, and make your way back towards the cabin, once even the leader collapses."
                            "Liam calls out at your arrival. Séan lays, half-exhausted and panting, on the ground between him and Nora."
                            liam "The den's clear, and I collapsed the entrance. It should stay clear for good."
                        elif d20Roll+(Vitality/3) >= (difficulty):
                            $wolfwin = 1
                            $Vitality +=2
                            play sound "sound/success.mp3"
                            "The plan is simple. Except Liam, everyone takes turns chasing out and tiring wolves. He'd come in after to scare out the kids."
                            "Once the first is beyond sight, send another. Keep close enough and run in cirlces."
                            "It seems a good plan, in your head."
                            "You dash through the den's clearing, almost tripping up on a twig. It takes a few passes as the wolves first get defensive, but soon enough you get a few of the beasts chasing you."
                            "Hopefully, the others have better luck. You scramble and sprint through the woods, ducking under or over fallen trees. The trio chasing gain with each movement."
                            "But a wolf is only fast, not enduring like a human. Nothing in the forest could outlast you."
                            "They soon fall behind, or collapse. Wolves exhausted fast, much like dogs, and they didn't have the mobile cleverness a human did."
                            "You shout in triumph, giving a victory lap of the forest before you turn towards the cabin."
                            liam"Oh, there you are!"
                            "He shouts as you approach. Séan looked a bit scruffy, his clothes torn by brambles."
                            liam"He got himself tripped up shortly after we started. Lucky for me, it happened to be near where I was hiding. A few good smacks and a wolf runs for the hills."
                            liam "Good job everyone."
                        else:
                            $Vitality +=1
                            play sound "sound/fail.ogg"
                            "The plan is simple. Except Liam, everyone takes turns chasing out and tiring wolves. Once the first is beyond sight, send another. Keep close enough and run in circles."
                            "It seems a good plan, in your head."
                            "It does not go to plan in the slightest."
                            "Séan tripped into brambles and got a bit bit before Liam could scare them off."
                            "Neither you or Nora could pull a single wolf out of the den, either. They were indeed annoyed but only chased you for a short distance before returning."
                            "The stubborn bastards make you waste the whole day running without getting tired themselves. They simply refuse to give into the taunts."
                            "Liam is frustrated fast. He mumbles something about annoying canines as he returns to his cabin with the three of you in tow."
                            liam "Well, that was a way to spend a day."
                            tan "I'll get Conn to send more fianna to help. Guess we just weren't enough."
                            liam "Yeah. Do that."
                    "Play a tune to lead the entire pack along peaceably. (Fili)":
                        tan"Séan can definitely do that, let's give it a try. Worst that happens, we just give a bunch of wolves a song."
                        sean"Worst, I get eaten by wolves."
                        tan "I'm certain you'll be fine! Right Liam?"
                        liam "Oh, most likely. Unless of course he plays certain songs."
                        "Séan is just about to shout in protest, before Liam simply winks and steps out of the small shack."
                        liam "Let's get going."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Fili/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Fili +=3
                            play sound "sound/critSuccess.mp3"
                            "The sound of music and song fills the forest as Séan and yourself work. You add your voice to his fiddle's tune, calling the wolves in the language of druids."
                            "They respond well, as docile as the gentlest hound, and one by one start padding out of the den."
                            "Séan gets nervous just as fast as they arrive."
                            sean"This... this is working, right?"
                            "Liam just shrugs. He cleared his throat, before barking out orders for the wolves. By literally barking. You never knew he could speak to animals."
                            "The leader tilts their head, before nudging the matron. They appear to converse some with Liam, before nodding. The pair walk off, the rest of the wolves in a group behind."
                            "In all, you count almost a dozen wolves. You're glad now you didn't try to fight them."
                            "Once the wolves are gone, Séan and yourself slowly wind down the performance. As a group, you return to Liam's cabin."
                            sean"That... was Scary."
                        elif d20Roll+(Fili/3) >= (difficulty):
                            $wolfwin = 1
                            $Fili +=2
                            play sound "sound/success.mp3"
                            "[sean] sets to work with a calming sound, his fiddle working and voice carrying the call to peace. You feel at ease, an unforced smile coming to your face."
                            "Nora and Liam wait anxiously. The wolves over the ridge are simply confused at first, maybe it wasn't working?"
                            "But one by one, the wolves make their way up and out of the den and towards the group. Liam takes the time to bark and talk with each."
                            "You had no idea he knew the languages of beasts."
                            "Once the leader and matron arrive with pups in tow, it seems like the pack is happy and compliant."
                            tan"Hey, get going. You'll find better pastures in the west, friends."
                            "Liam conveys your words, and after some grumbling, the wolves seem to acquiesce."
                            "An hour later, Séan winds down the song. He breathes out heavily, face covered in sweat."
                            "I wanted to be sure... They're gone right?"
                            liam "Should be, I can check the den, get back to the cabin"
                        else:
                            $Fili +=1
                            play sound "sound/fail.ogg"
                            "Séan began playing once you found a good spot to lure the wolves too. A quiet glade a bit away from their den."
                            "It'll be the best place of any to try."
                            "So, you sit down with Nora to wait, both anxiously watching the woods around."
                            "Even with hours of playing, the wolves ignore Séan's call. You think it's some of his best work as a bard, but apparently the wolves didn't agree."
                            sean"Mutts couldn't appreciate good music if I smacked them with my fiddle."
                            liam"Something about the instrument, I'm betting. It's a bit too shrill for the ears of hounds."
                            sean"I'll give them shrill..."
                            "Sean grumbled dissatisfied, but packs up his instrument all the same."
                            liam "Let's just head back to the cabin."
                jump after_wolf

            label wolfscare: #tougher, but not deadly.
                menu wolfScareCheck:
                    "Are you sure about that plan?"
                    "Yes, it should work.":
                        tan"Its the best option, at the very least."
                        liam "Then let us get going."
                    "No, let me rethink this...":
                        jump wolf_choice

                stop music fadeout 1.0
                play music "music/Part_of_the_Pack.ogg" fadein 1.0
                scene bg wolfden
                show liam
                with dissolve
                "The den was in a remote part of the woods, sheltered under a cliff. It made for a tough thing to approach."
                "With the only visible entrance having one way to approach, it meant the wolves would see, hear, or smell you long before you entered the area."
                "Liam had tried to get close before, to get a count of the wolves, but they drove him off, even with the help of his hound."
                "Hopefully as group, you stand a better chance of defeating the defenses of the den."
                "Liam lead the way to a shelter he set up to hide scents just out of the range of the wolves but close enough to the den."
                "When he arrived, he sat the three of you down and drew out the general shape of the den on the ground."
                liam"So. They have a good number. about ten."
                sean"Ten?!"
                nora"Indeed. The situation this summer aided them in proliferating, and a good number of them are young adults who haven't broken away yet."
                nora"Two competing large packs would be disastrous for herds and farmers. We gotta deal with 'em now."
                liam"Indeed. Not a fun situation, but we'll handle it. Either today, or within the month."
                "Liam's tone is serious, and he watches both you and [sean] for reactions. Séan, for his credit, is only shaking a bit. Wolves had always scared him, so to face ten? Terrifying."
                "You lay a hand on his shoulders, and squeeze. It's a wonder he's the one that suggested to exterminate them!"
                "Must have been from that fear."
                tan"I'm certain you have plans for us?"
                liam"How about Nora leads this one? It was her preferred idea."
                nora "Certainly."
                nora "Pretty simple. First, we could lay some bait. Something fresh dead or near dead. Kill the hunters who show up, not tough."
                nora"We could also track a few more proactively, chase and slay them."
                nora"Finally, we make one of ourselves a target and fight more openly."
                sean "What's the difference between the first and last?"
                nora "Danger to ourselves. The first one is much more clever, as opposed to basically challenging the hunters to a sparring match."
                liam "The tracking seems most my speed, but I'll be good with any."
                sean "But which are we doing?"
                #plans on how deal with the wolf hunters.
                    #Lay easy bait and trap them too.
                    #Track them, chase them down
                    #Make yourself a target and strike back.
                $difficulty = 10
                menu wolfscare_skill: #tougher, riskier
                    "Bait a known hunting ground and draw them out (Seanchas)":
                        tan"No need for undue risk if we can accomplish the same with some traps."
                        tan"We are only seeking to kill a few, after all."
                        sean"Hey, if we set up a good trap, they won't even need to be killed by us, directly."
                        liam"Lets get to work then. A wolf doesn't catch itself."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Seanchas/3) >= (difficulty + 10) or d20Roll == 20:
                            $Seanchas +=3
                            $wolfwin = 2
                            play sound "sound/critSuccess.mp3"
                            "The trap setup goes well. Liam tracks down a deer, hamstrings it, and ties it in a clearing. The hunters make blood trails leading out towards the den, while Séan watches the glade."
                            "Nothing is sprung early by freak mistake and you're able to lay the trail quickly. Liam watches the den from a distance as you, Nora, and Séan wait."
                            sean "How long might this take, you think?"
                            nora"Not long, the wolves are bold."
                            tan"Quiet, Liam's on the way."
                            "He joins the three of you on the ledge, crouching and laying an arrow on his bow."
                            liam"A few follow the trail, the leader even. A good result, if we kill him."
                            "Ten minutes later, a troupe of five wolves passes into the forest clearing. You bite your lip, before following Liam's lead."
                            liam"One at a time. Back one first, end with the leader."
                            "Bows strum in time, as four arrows in tandem sinks into one, two, three, four, then five wolves."
                            "They all fall, and the trap is done. A merciful arrow ends the deer and provides Liam with lunch. You collect the corpses and head back for the cabin."
                        elif d20Roll+(Seanchas/3) >= (difficulty):
                            $Seanchas +=2
                            $wolfwin = 1
                            play sound "sound/success.mp3"
                            "The trap setup goes well. Liam tracks down a deer, hamstrings it, and ties it in a clearing. The hunters make blood trails leading out towards the den, while Séan watches the glade."
                            "Séan has a fright, firing off an arrow wild at a falling leaf and almost hitting the rope holding the deer down."
                            tan"Careful."
                            "You warn him upon return. Liam runs back in, eyes wide. Shit, the wolves were coming, weren't they?"
                            liam "Places, fire on my mark!"
                            "The group scrambles into their locations, just in time for three wolves to stride into the clearing and sniff around the suspicious deer."
                            "Leader wolf is missing, but some of the older and more vital ones in the pack are present. A decent result, even if you would have preferred more. It'd be a start, you figure."
                            "Arrows fly, and the wolves die one at a time. It was a bit bit messy, for one almost got away, but the job was done."
                            "You and the other hunters head back for Liam's cabin, wolf corpses in tow. No point to waste the furs."
                        else:
                            $Seanchas +=1
                            play sound "sound/fail.ogg"
                            "While at first the trap setup goes well, it falls apart pretty quick after. The deer, initially stunned, startles and runs into the woods."
                            "Liam manages to catch it again and hamstring it properly, but the noise and disturbance must have spooked any hunters."
                            "No matter how long you wait, nothing comes for the deer. Not a single curious wolf."
                            "Liam ranges between the den and the clearing, but always reports negative on any curious wolves."
                            "As the sun starts to go down, Liam calls it a day and kills the deer. At least he'd have food."
                            liam"I'll just have to try again next time, eh? The idea was sound, just unlucky today."
                    "Track them down and slay them. (Finesse)":
                        tan"Liam, you're great at ranging in the woods, so let's use those skills."
                        liam"Running in the woods with wolves can be dangerous. Let's keep it to just a few of those beasts."
                        liam"And avoid the leader of the bunch. He'd cause more trouble than we need."
                        tan"Right. Let's get to work, aye?"
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Finesse/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Finesse +=3
                            play sound "sound/critSuccess.mp3"
                            "You and the others spread out from the shack, creeping through the brush with bows in hand. Liam takes the lead, for obvious reasons of experience."
                            "With Liam's prowess, nothing can hide from you and the other hunters. Especially not a group of aggressive wolves."
                            "Following tracks and disturbed flora, it takes only a few hours to find an isolated group of wolves on the hunt."
                            "Liam keeps the four of you downwind, watching the wolves ahead."
                            liam"Five wolves. The leader is here, unfortunate, but we can even the odds fast."
                            "They are idling about, likely to find a new scent to follow on the hunt. They're utterly unaware of the humans but a short distance away with knocked bows."
                            liam"Loose."
                            "The four of you let arrows fly in tandem, arrows felling one wolf at a time. Soon, only the leader is left."
                            "He's startled, unable to find the source of what was killing his pack."
                            "But he'd soon join them on the ground, dead."
                            "Liam steps out into the clearing to take stock, the rest of you splitting off back to the cabin at his command."
                        elif d20Roll+(Finesse/3) >= (difficulty):
                            $wolfwin = 1
                            $Finesse +=2
                            play sound "sound/success.mp3"
                            "With practiced calm and order, the four of you stalk into the forest. Rather than stick to one group, the four of you spread out to take down single wolves."
                            "If you kill enough out in the woods, it'll be much easier for Liam in the future to maintain the pack size."
                            "While each of you stay within earshot of at least one of the others, it becomes a solitary endeavor."
                            "It's a long day, but you have plenty of experience hunting. It isn't be too tedious."
                            "Shortly after you start, you and a wolf just about stumble into each other."
                            tan "Oh. Shit."
                            "The young male is alone, and equally as startled. His hackles raise and he starts to growl."
                            "He charges, paws kicking up dirt and leaves. But your bow is faster, and he skids to a stop in front of you with an arrow in his neck."
                            "You see no other wolves over the day, but the others have more luck."
                            "You meet them back at Liam's cabin to regroup and rest before returning to the tuath village."
                        else:
                            $Finesse +=1
                            play sound "sound/fail.ogg"
                            "The hunt goes bad almost pretty quickly."
                            "Séan disturbs an entire bush and scatters the first group of wolves you find, making the entire pack defensive."
                            "Despite spending most of the day trying to find at least one caught out alone, none move alone or in numbers you and the others can safely confront."
                            "It's frustrating, but Liam calls the day as the sun goes down."
                            "No wolves slain, but at least no one was hurt."
                    "Make yourself a target. Draw them into a clearing for a fight. (Might)":
                        tan"You know, it's always been a dream of mine to wrestle a wolf."
                        nora"Since when, [tan]?"
                        tan"Since I realized it became something I could realistically fit into my day."
                        sean"So, a minute ago?"
                        liam"Wrestle all the wolves you like, we just need to cull the pack."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Might/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Might +=3
                            play sound "sound/critSuccess.mp3"
                            "You stake out a clearing, wide and open, with plenty of space to catch out wolves before they could reach you."
                            "Your friends stalk the woods around, watching and funneling wolves to approach you only from the front."
                            tan"Come get some meat, wolves! I'm strong enough to take on your whole pack!"
                            "You shout, howl, and make noise, trying to make yourself as obnoxious as possible to the wolves."
                            "This had to be one of the silliest things you ever have done, but you knew it would be glorious in execution."
                            "It doesn't take long for the first wolf to arrive."
                            "It comes growling and snarling, stoked into a furor by your noise."
                            tan"I got this! You get any others that arrive, friends!"
                            "You shout, charging across the field as it charges in return."
                            "You narrowly avoid its snapping jaws, slipping a cord out of your pocket to wrap around those vicious bites and tie shut the slavering maw."
                            "And you proceed to pin the thing to the ground bodily. Its jaws strain against the hempen cord as you pull out a knife."
                            "Holding it down and in place, you cut its throat."
                            "While you were struggling with the wolf, a further four had arrived to the scene, including the leader of the pack."
                            "Liam personally handled the leader in a similar, but more finessed manner to your own, while Nora and Séan fought off the rest."
                            "The four of you return to the cabin with stories to brag about at tomorrow's feast."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $wolfwin = 1
                            $Might +=2
                            play sound "sound/success.mp3"
                            "The clearing you found for challenging the wolves was wide and clear with plenty of places for your friends to hide out and aid you."
                            liam"Be safe, don't actually try to wrestle a wolf, you won't win!"
                            tan"Certainly. I'm still going to try."
                            "You get your chance soon enough. First, you start shouting out insults to the pack and its members, trying to incite them to violent deeds."
                            "It works, within about ten minutes the first wolf arrives. It charges for you and immediately you lunge back with a spear."
                            "You miss, the spear being lodged in the ground next to the wolf."
                            "Its counter knocks you onto your back, its jaws an inch from your face and held back by your struggling arms. Those wicked teeth snap and snarl, trying to bite off your nose!"
                            "Then an arrow buries itself in the wolf's eye, and Liam steps into the clearing looking unimpressed."
                            liam"So, like I said?"
                            tan"Of course, master hunter. I'll do better next time."
                            liam"See that you do."
                            "He smirks, and winks."
                            "Once the wolves catch onto the plot, they stop coming. But with a few dead wolves in the clearing you have plenty of progress made."
                            "You and the others head back to Liam's cabin to regroup before you'll head back to the tuath."
                        else:
                            $Might +=1
                            play sound "sound/fail.ogg"
                            "You stake out a clearing and shout challenges, Adh happily helping you in making as much noise as possible."
                            "It should certainly draw a wolf to you, right? They hate noise!"
                            "Your allies take up spots to wait in ambush around the clearing, with bows and spears ready."
                            "But, regardless of the type and amount of noise you and Liam's hound make, nothing comes."
                            "It's surprisingly discouraging."
                            tan"What, am I that unappealing of a challenge, you bastard wolves?!"
                            sean"Well, apparently. What a funny way to spend a day though, watching you try to challenge wolves to a wrestling match."
                            liam"Let's just get back. I'll deal with the wolves after the feast."

                jump after_wolf

            label wolfkill:
                menu wolfKillCheck:
                    liam"Are you sure about that plan?"
                    "Yes, it should work.":
                        tan"Its the best option, at the very least."
                        liam "Then let us get going."
                    "No, let me rethink this...":
                        jump wolf_choice

                stop music fadeout 1.0
                play music "music/Part_of_the_Pack.ogg" fadein 1.0
                scene bg wolfden
                show liam
                with dissolve
                "The den was in a remote part of the woods, sheltered under a cliff. It made for a tough thing to approach."
                "With the only visible entrance having one way to approach, it meant the wolves would see, hear, or smell you long before you entered the area."
                "Liam had tried to get close before, to get a count of the wolves, but they drove him off, even with the help of his hound."
                "Hopefully as group, you stand a better chance of defeating the defenses of the den."
                "Liam lead the way to a shelter he set up to hide scents just out of the range of the wolves but close enough to the den."
                "When he arrived, he sat the three of you down and drew out the general shape of the den on the ground."
                liam"So. They have a good number. about ten."
                sean"Ten?!"
                nora"Indeed. The situation this summer aided them in proliferating, and a good number of them are young adults who haven't broken away yet."
                nora"Two competing large packs would be disastrous for herds and farmers. We gotta deal with 'em now."
                liam"Indeed. Not a fun situation, but we'll handle it. Either today, or within the month."
                "Liam's tone is serious, and he watches both you and [sean] for reactions. Séan, for his credit, is only shaking a bit. Wolves had always scared him, so to face ten? Terrifying."
                "You lay a hand on his shoulders, and squeeze. It's a wonder he's the one that suggested to exterminate them!"
                "Must have been from that fear."
                tan"I'm certain you have plans for us?"
                liam"Actually no, I thought [sean] could enlighten us to what he thinks could work. I'll comment."
                sean"Oh. Very well."
                "He clears his throat, glancing around the small shack."
                sean"I'm no hunter, but well, here's what comes to mind. We deal with them a few at a time. Lure them, kill them, keep going until only the, uh, pups are left."
                liam "Blunt but effective."
                sean"Right."
                nora"Why not confront the strongest, and work our way down the chain?"
                liam"Bold."
                tan"Potentially dangerous, but it might work."
                tan "On the same vein, couldn't we simply surround the exits and kill them as they try to leave for food?"
                liam"More time consuming, we'd need to goad them out as well."
                liam"But rather than being further afield, if we're close it'll run a higher risk of dragging in the whole pack. But we can also strike faster."
                sean"I don't quite like the thought of killing young, that'll be on you Liam."
                liam "So, lure a few and kill them quick, wait them out and kill any that wander out, or march in and fight the strongest."
                sean "I'm regretting this idea already."
                sean"But okay, which'll we be doing?"
                #plans on how to kill them
                    #Draw them off a few at a time
                    #Confront the strongest first
                    #Surround the den and kill any that try leaving
                    #benefit if hunter background?
                $difficulty = 12
                menu wolfkill_skill: #potentially dangerous!
                    "Lure out a few, kill them quickly. (Finesse)":
                        tan "Brutal, but fast. If we kill them before they can call for help, we can cull down the pack to a more manageable size."
                        liam "A good plan. Do we ambush them from above or from shelter like this shack?"
                        tan "I think if we have a little cliff, we can have you and Nora stand on top of it and fill them with arrows as I and [sean] keep them at bay with spears."
                        liam "Even better! Let's get to it."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Finesse/3) >= (difficulty + 10) or d20Roll == 20:
                            $Finesse +=3
                            $wolfwin = 2
                            play sound "sound/critSuccess.mp3"
                            "With the ambush point set, you and Séan set to work in luring the wolves. Adh aiding with mournful howls, but music and song slowly spreading across the forest."
                            "The song appears to work, with wolves appearing in first small groups of two or three. While the first seem hypnotised, the arrows soon end that."
                            "Howls cut short, yipes of pain, and the smell of dead wolves. The forest is permeated by all three."
                            "But more wolves keep coming, called in by curiosity or otherwise trying to help injured brethren."
                            "After an hour, the trickle stops."
                            liam "Well, I'm surprised how well that went. Though, we were only supposed to kill a few before moving in, this must be most of the pack."
                            sean"All the better, eh? We can leave these beasts out here."
                            "You nod, Thank the gods it proved nice and simple."
                            tan"Liam, could you deal with any stragglers at the den itself?"
                            liam "It would be no problem. Wait for met at the Cabin."
                        elif d20Roll+(Finesse/3) >= (difficulty):
                            $Finesse +=2
                            $wolfwin = 1
                            play sound "sound/success.mp3"
                            sean"Hey canine bastards! Get over here!"
                            "Séan immediately started shouting, drawing your ire and shushing. You hadn't told them to start yet!"
                            "But of course, there just so happened to be a wolf nearby. Adh intercepts it before it can sink its teeth into Séan, but the goofy bard passed out of fright from those sharp fangs."
                            "You personally finished off the wolf, heaving out an annoyed sigh."
                            tan "Get him up there, Nora. I'll keep them at bay."
                            "She nods, vaulting down and slinging the bard over her shoulder. He was always a light one."
                            nora "He's not hurt, is he?"
                            tan"Just a fright. He'll be fine."
                            "The rest of the hunt goes much better after that, with every wolf killed who you lured to the glade."
                            "Eventually, Liam and Adh leave to deal with the Den themselves. You and Nora carry Séan back to the cabin, happy to be done with that bloody work."
                        else:
                            $Finesse +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "As safe as this plan initially seemed to be, your little staging point was quickly overwhelmed. The first group that emerges from the woods is the leader himself with some of the toughest wolves."
                            sean"Shit."
                            "The only word passed between the four of you and the dog before the mayhem started. You initially hold ground against the large wolves, but it proves futile."
                            "Liam shouts to run. [sean] happily responds. Your flank is left open, and the leader gets his jaws in your calf."
                            play sound "sound/injury.ogg"
                            "You howl in abject pain, stars flashing across the day sky obscured by the old trees."
                            "Liam, the practiced hunter, responds and spears the beast through his skull and forces the release of your leg. You collapse backward, bleeding badly as Nora grabs under your shoulders and starts dragging."
                            "The hunter covers your tracks, spear jabbing at any wolf trying to get close. One jumps for Liam and almost slips past, but Adh springs into action and intercepts."
                            "The hound fights off the three remaining wolves, growling and backed into a corner as Liam shouts for her to run."
                            "The pain buzzes until the world turns black around you and melts away."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            scene bg liamcottage with fade
                            "When you wake, you're back at Liam's own cottage. Liam is tending your wounds, face set hard. [sean] does his best to aid the hunter and Nora watches the exterior of the small dwelling."
                            "Adh is nowhere to be seen."
                    "Surround the den. Wait them out. Kill any who leave. (Vitality)":
                        nora"So, the long haul."
                        tan"Indeed. I figure it'll be the least dangerous and most thorough."
                        liam"It'll also take advantage of the natural bottleneck of the den."
                        sean"Can we just get this over with?"
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Vitality/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Vitality +=3
                            play sound "sound/critSuccess.mp3"
                            "It doesn't take long for the wolves to sniff out something is wrong. The first wolf that wanders out of the vale gains an arrow to the eye and collapses."
                            "Curious, another few investigates. Another few fall to arrows. Séan pulls away the bodies, keeping quiet and hiding his scent with wolf blood."
                            "Nora knocks another arrow and lets it sail into the clearing to strike at a smaller wolf. It goes down. So far, you're all at a kill each."
                            liam"Going well, hold steady."
                            "The pack starts to worry at this point. Arrows from nowhere, missing members, and dead ones don't make for happy wolves."
                            "But they aren't aware of where its coming from in the slightest."
                            "The leader emerges from the den, and you nudge Nora."
                            tan"If we can get him down soon, the rest will start panicking and flee."
                            "She and Liam nod, as Séan readies his spear. The three of you launch a volley through the brush. Each arrow strikes its mark and the leader is nearly knocked off his feet."
                            "He staggers a few steps, before one last arrow plunges through the meat of his throat and he collapses."
                            "By the end of the day, the pack lies dead and slain and no longer a threat. The hound couldn't even sink its teeth in, with how well the rest of you handled your task."
                            "You and the others return to Liam's cabin while he and his hound checks for any stragglers. The hound remains, as it can keep pace with any wolf."
                        elif d20Roll+(Vitality/3) >= (difficulty):
                            $wolfwin = 1
                            $Vitality +=2
                            play sound "sound/success.mp3"
                            "While the work seems like it could take forever, you and the other three hunters start with a happy heart. Adh's behavior becomes that of a hunter, the hound no longer exuberant as you approach the den."
                            "The four of you take up positions, then Liam lets out a whistle. Adh starts to bark sounding like a lost puppy."
                            "You raise an eyebrow and Liam winks in return."
                            "The first of the beasts trot up. Nora takes him down with a well-placed arrow. A few more are in his wake, and the hillside suddenly gets active."
                            "While it isn't as bloodless as you'd prefer, the flying arrows and iron spears and flashing teeth bloody the hillside with the blood of wolves. Only the occasional drop of human blood is spilt."
                            "Your spear strikes true time and time again. Soon, the wolves have become reluctant to leave the area of the den. Half of their number slain, it's no wonder! "
                            "Finally, the leader emerges. He's flanked by a few of the other older females, and the four charge up the hill."
                            "The final charge is in vain, however, and a barrage of arrows and spear strikes brings down all four."
                            "You leave Liam and Nora the remainder, the young of the wolves. You and [sean] both lacked the stomach for it."
                        else:
                            $Vitality +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "At first it seems to be going to plan. One of the wolves wanders out and you slay him quickly."
                            "But of course, things rapidly degenerate from there."
                            "When the leader emerges, Nora misses her mark and sends him into a fury. He charges up for your position, bloodlust in his eyes and snarl."
                            "You just barely push Nora out of the way with a jumping tackle, leaving only your leg in range of his jaws."
                            play sound "sound/injury.ogg"
                            "A sickening sound fills the vale as you howl in pain and those powerful jaws bite into your limb."
                            "But the jaw goes slack as Liam sends a spear through it, and up into the beast's skull."
                            "You're thankful, but the scene starts fading as the pain gets to you. Last you see is Adh doing her damnedest to fight back three wolves at the mouth of the incline towards the den."
                            "Then the world disappears."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            scene bg liamcottage with fade
                            "When you wake, you're back at Liam's own cottage. Liam is tending your wounds, face set hard. [sean] does his best to aid the hunter and Nora watches the exterior of the small dwelling."
                            "Adh is nowhere to be seen."
                    "Go for the leaders and strongest and work your way down. (Might)":
                        tan"If we deal with the strongest, the rest may panic and flee."
                        liam"So, try to kill them all but leave them open to flight? Not quite extermination, but it works."
                        sean"Maybe it'll be better?"
                        liam"It would help keep a balance more."
                        tan"Good. Let's go."
                        $d20Roll = renpy.random.randint(1,20)
                        if d20Roll+(Might/3) >= (difficulty + 10) or d20Roll == 20:
                            $wolfwin = 2
                            $Might +=3
                            play sound "sound/critSuccess.mp3"
                            "You take the lead, shouting out a challenge with spear in hand at the top of the hill. Of course, the wolves can't understand your words, but the posture is enough."
                            "With a howl, the leader bounds up the slope for you and your allies with lieutenants in tow."
                            "You grunt and heave your spear down the cliff towards him. A perfect strike renders him dead in an instant, spear keeping him standing as it goes from head to bowels then into the ground."
                            "[sean] shouts a battle cry and lets his own spear sail. Liam and Nora keep themselves much more collected, thankfully, and start raining a deadly hail of arrows into the vale and den."
                            "You have to pull another spear from the supply you brought, but any wolves on the slope soon meet their end from you and your bard friend."
                            sean"Maybe wolves aren't so sc-"
                            "He shrieks as Liam slays a wolf that was just about to bite off his shins."
                            sean"Oh definitely nevermind, fuck these things."
                            "You laugh, and grin. Even the hound Adh gets in on the fun, ripping wolves asunder alongside you and Séan."
                        elif d20Roll+(Might/3) >= (difficulty):
                            $wolfwin = 1
                            $Might +=2
                            play sound "sound/success.mp3"
                            "All it takes to lure a wolf is walk around in its territory without hiding your scent or presence. They'll find you soon enough."
                            "With a howl, you and the party of hunters are just about ambushed by wolves. The leader himself had caught wind of you. Good."
                            "You and Séan grit your teeth and level spears towards wolf-height and make a tandem charge. Nora and Liam meanwhile pepper the wolf lieutenants."
                            "Adh the hound barks and chases after you. Of course, she wants in on the fun of slaying wolves!"
                            "You bark as well, as you and [sean] manage to corner the leader, bleeding and woudned, between a rock and tree. With his seconds dead, only one more stroke of your spear ends him as well."
                            liam "No time to waste, onto the den."
                            "The group of you storm the hill like fomorians, all battle cries and anger. Spears clash against teeth, and more than a little blood gets spilled, scratches and surface wounds only on your side."
                            "It almost feels like a true battle, getting your blood pumping with rage and excitement."
                            "But it ends all too soon, leaving you all a panting mess."
                            liam"Get back to the cabin. Me and Adh will check for any survivors."
                        else:
                            $Might +=1
                            $injuryCount+=1
                            play sound "sound/fail.ogg"
                            "You later decide this plan ended up being one of the worst ideas you ever came up with. Not only for the sharp teeth of the leader, but their sheer numbers."
                            "They refuse to come out one on one. Instead, the pack hunters charge as a unit, and overwhelm the basic position you and the other hunters set up."
                            "While the others escape unscathed, you aren't quite as lucky. The lead wolf dodges the thrust of your spear and goes right for your throat."
                            "The only thing that saves you is the timely intervention of Adh and Liam."
                            play sound "sound/injury.ogg"
                            "The blade of Liam's spear jammed the wolf's side so his teeth only sink into your leg, and not deeply. You are able to wrench his jaws open and stagger away, only for another wolf to attempt at your life."
                            "This one doesn't get quite as close, but the pain of the previous attack makes you falter and fall to your knees in the mud of the forest."
                            "In the middle of the glade you see Liam's hound fighting for its life and holding back the pack as Liam finishes off the leader."
                            "Liam half picks you up, arms wrapped under your shoulders and dragging you out of the glade."
                            "And then everything turns black."
                            scene black
                            with dissolve
                            show text "{b}{color=#FFFFFF}Injury Gained{/color}{/b}" at truecenter
                            with dissolve
                            pause 1
                            hide text
                            with dissolve
                            scene bg liamcottage with fade
                            "When you wake, you're back at Liam's own cottage. Liam is tending your wounds, face set hard. [sean] does his best to aid the hunter and Nora watches the exterior of the small dwelling."
                            "Adh is nowhere to be seen."

                jump after_wolf

            label after_wolf:
                $ d20Roll = 0
                $ difficulty = 0
                $ renpy.fix_rollback()
                scene bg woods
                show liam
                with dissolve
                play music "music/Return_Forest.ogg" fadein 1.0
                play sound "sound/forestWalk.ogg"
                if wolfwin == 2:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 2
                    if wolftarget == 1:
                        "Liam informs you that luring the pack had gone well. When he checks their den, he finds no wolves anywhere near. Apparently, he and his hound even made doubly sure they wouldn't return by pissing on the entryway to the den."
                    elif wolftarget == 2:
                        "The pack is worse off with the main breeding male dead. Another is likely to replace him, but it will be a while. Liam can keep them maintained, without them becoming a danger."
                    else:
                        "The pack is definitively dead. Liam's hound proves quite an aid in preventing any from escaping, and you and the other hunters do the rest."
                    "With the pack being so thoroughly dealt with, they would never trouble the tuath. Liam was all smiles, a rarity for the serious man, and had already offered to tell Conn just how well you, Nora, and [sean] worked together."
                    "Hopefully, there wouldn't be more wolves causing problems in the tuath for a good long while with such a success."
                elif wolfwin == 1:
                    show text "{b}{color=#FFFFFF}Honor Gained{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor += 1
                    "You feel the tuath will sleep safer now that the wolves were gone. Hopefully they'd stay gone, and you hadn't missed any of the wolves."
                    "It was a tricky job you took on, after all. Wolves were one of the most dangerous animals in Ireland."
                    if wolftarget == 1:
                        "Since the luring had gone so well, Liam assured you they would stay gone, likely moved on to neighboring land such as that of the Mugdorna. Let them deal with it, was his opinion."
                    elif wolftarget == 2:
                        "A good number of the hunters of the pack slain, they wouldn't be as bold for a while. It would also help Liam maintain the pack without needing to exterminate it."
                    else:
                        "With most, if not all, of the wolves dead, you know there would be no chance of them becoming a recurring threat. A single wolf was easy enough for Liam to deal with."
                else:
                    "The cabin is somber and quiet. The four of you scarcely talk."
                    "The wolves will continue to plague the tuath's countryside without being properly dealt with. While the encoutner may buy more time, they obviously won't be gone anytime soon."
                    if wolftarget == 1:
                        "Your attempts to lure them away failed, ultimately. Liam promised he'd keep trying before he left, but failure was always bitter."
                    elif wolftarget == 2:
                        "Without any bites to your attempts to lure or catch out wolves, the pack remained together and strong. Liam will just have to try again some other day."
                    else:
                        "You can still feel the sting of teeth and claws. Especially in your leg. It'll heal, but without the wolves dealt with it'll be a bitter scar to stomach."
                "Liam bids goodbye, directing you back towards the tuath and wishing you luck on the remainder of feast preparations. [nora] would join you on the return trip. Her home was next to yours, after all."
                hide liam
                show sean at right
                show nora at left
                with dissolve
                sean"A day running in the woods, hunting wolves. Not how I saw my day going this morning."
                nora "Well, you probably thought yourself shacking up with the fiann or in the feast hall, drunkard."
                tan "True, he did wake up in my home after a binge."
                nora "Did he now? That makes it what, the twentieth time this season?"
                tan "More or less"
                "Séan gave you a tut, before playing an eager, aggressive tune on his fiddle to drown out both of your continued conversation."
                "However, you and Nora continue to joke and tease, along with catching up of stories of the last week. You hadn't spent as much time with her this last season, but you're happy to have it now."
                "It takes you a moment to notice as [sean]'s tune dyes down behind you two. You shout back at him, and he turns towards you with a mystified look on his face."
                tan "What's going on?"
                sean "I saw a rabbit."
                nora "A. . . rabbit?"
                sean "It looked like a magic one. I swear it had antlers."
                nora "Antlers."
                sean "I swear upon the tuath gods that I am not lying."
                nora "Lead on then. Lead us to this 'magic rabbit'"
                tan "You sure? We do have to return."
                nora "It'll be no trouble, I'd say. Not more than an hour to check, and it'll still be light then."
                "She glances around, though, looking a bit confused."
                nora "I think, this part of the woods seems a bit different than I expected. Maybe we got off track while we were ribbing [sean]."
                tan "Perhaps, I don't recognize this part of the woods either."
                nora "Either way, let's seek out this rabbit."
                "You nod your assent, before gesturing for [sean] to lead you on into the forest. He slips his fiddle onto his back again, before striding off."
                hide nora
                hide sean
                with moveoutright
                jump LostChild

    label ch1_part3:
        label LostChild:
            $ renpy.fix_rollback()
            stop music fadeout 1.0
            show sean
            with moveinleft
            play sound "sound/forestWalk.ogg"
            "Your companions get a bit ahead of you as you navigate through the underbrush. Séan continues to lead, the group becoming increasingly strung out across a forest."
            "You can't help but feel lost already. This area seems unfamiliar, despite having wandered the woods plenty in your youth. Perhaps you just always missed this area."
            "You do your best to hold your bearing as you go further into the forest."
            "But Séan stops and suddenly points off into the brush, before shouting."
            sean "There it is!"
            "He immediately dashes off into the woods before either you or anyone else could speak out. He keeps shouting back \"This way, this way!\" to make sure you know where he's going."
            hide sean
            with moveoutright
            if C_aoife == True:
                show aoife at left
                with moveinleft
                ##Aoife calls after him, trying to get him to stay around. You're too stunned by the quickness to say anything.
                aoife"Kid's gonna get himself killed like this. [sean]! Get back here!"
                "You blink as she too jumps into the brush, shouting for him to get back to the road. Her too? Wasn't she supposed to be the responsible one among you?"
            if C_niall == True:
                show niall at left
                with moveinleft
                # Niall runs after Sean, eager to help in the hunt.
                niall"Hahahaha! Time for a chase!"
                "The large blacksmith strides forward, pushing aside the brush then breaking into a sprint to keep up with [sean]."
                niall "You're mine, strange rabbit!"
                "You sigh, of course Niall was already this pumped."
            if C_nora == True:
                show nora at left
                with moveinleft
                ## Nora brings up stories of strange animals in the woods of late, getting close to travelers late at night
                nora"Now that I think about it..."
                "She turns towards you for a moment, then back to the Séan shaped hole in the brush."
                nora"There has been rumors of more strange animals in the woods, but none of our tuath have tried approaching them. They felt the presence of Sídhe-dwellers and scrammed."
                "She doesn't give you the chance to respond to this revelation, instead dashing after [sean] before he gets too far out. You reach out after, but no words come."

            "Your hesitation lasts a moment or two longer. Something about this situation feels wrong, dangerous, but you can't pin a word to why."
            "But you realize you can't stay here and wait, they'll be lost in the Forest of the Mounds!"
            "You will your legs into action, vaulting over the tree they crossed. Your boots crush the leaves on the ground as you follow the shouting of Séan."
            "But then his voice cuts off, and the forest is quiet save the sound of people running through the forest."
            "{i}What in blazes is going on now?{/i} You think, growing increasingly worried."
            "You stumble just a bit stepping into the glade where you last heard Séan. When you recover, you finally get a proper view of the scene in the clearing."
            stop music fadeout 1.0
            play music "music/Come_Little_Children.ogg" fadein 1.0
            show sean at right
            with dissolve
            "Séan stands, transfixed, staring at a strange child as if beholding the true face of the Highest. Séan had never been a very devout person, yet here he was with a face like he'd seen a miracle."
            "A subtle music hangs in the air, the sound of chimes. Your other companion seems just as spellbound, yet you don't feel compelled to do... well anything."
            "Had you missed something important? How was a six-year-old boy this entrancing? And no one was talking, at all."
            tan "Hey! What's going on? Snap the fuck out of whatever this is!"
            "You shout, hand at your weapon, the forceful sound seeming to shake them out of it. The kid, previously silent, starts tearing up. He must not be used to aggressive posturing."
            "Séan looked confused, glancing back at you, then the sobbing child. He kneels, resting a hand on the kid's shoulder. He seems a bit calmed by this, at the very least."
            sean "I have. . ."
            sean "I have no idea. I just- I was- I was chasing the rabbit. I finally saw it through the brush. It dashed to this clearing but when I got here this kid was scared and I just froze."
            sean "Where did he even come from? Is he from the village, the farms, the herders, the monastery? A neighboring Tuath?"
            if C_aoife == True:
                "Aoife, by that point, gathered her wits once more."
                "She looks annoyed, but the rígfénnid simply grumbles and sets her shield on the ground. She approaches the kid, offering more comfort and support for the child in the form of a firm hug and quiet calming whispers."
                aoife"He does not look to be of us. His eyes are too... bright. Hair is too flaxen. Perhaps he is from the Norse towns to the south, and he wandered north?"
                tan"Wouldn't the traders and herders have caught him? There is a lot between here and Dyflinner territory."
                aoife "And beyond that, the lakes and rivers between here and Dyflinn are dangerous for such a young one alone."
                tan"True."
                "She pauses, before gently lifting the child's chin to look over him a bit closer."
                "There is something indeed odd about this child. He seems to have iris's just a bit too big. His dimples were set with color, purple, but perhaps that was just some sort of tuath marking."
                "His clothing, though a bit tattered by running through the woods, were fancy and of high quality."
                aoife "Child, where are you from?"
            elif C_niall == True:
                "Niall snorted, coughed, and spit."
                niall "Hellfire, I thought I was gonna choke on snot while I was frozen. What the hell is with this kid?"
                sean "Not sure. He's an odd one."
                tan "Has he said anything yet?"
                sean "I... think? But I couldn't understand."
                niall "Has that music of yours destroyed your ears, finally?"
                "You shush them, kneeling to get a closer look at this kid. His hair is flaxen, eyes a vibrant blue... Is he Norse?"
                tan "He looks Norse to me, almost. But... I'm not sure. Could a Norse child get this far north without a family?"
                niall "They are tough as nails. Maybe their kids are too."
                sean "It must be something else, I think. This kid's odd."
                "There is something indeed odd about this child. He seems to have iris's just a bit too big. His dimples were set with color, purple, but perhaps that was just some sort of tuath marking."
                "His clothing, though a bit tattered by running through the woods, were fancy and of high quality."
                niall "Hey kid, you from around here?"
            elif C_nora == True:
                "Nóra shivers and shakes out her limbs."
                nora "Okay, that's enough magic for me for the month."
                tan "Magic?"
                nora"Sorcery, whatever, that was definitely strong fae magic from this kid. I'm going out on a limb, but he's not human, I feel it."
                "You frown and kneel down to get a proper look at the kid. Nóra is right, he isn't quite right looking."
                "He seems to have iris's just a bit too big. His dimples were set with color, purple, but perhaps that was just some sort of tuath marking."
                "His clothing, though a bit tattered by running through the woods, were fancy and of high quality."
                "With flaxen hair and blue eyes as well, he certainly isn't a native Gael, at the very least."
                sean "Well, he must be lost, then. If he's something else, should we even help?"
                tan "He's probably just Norse. We should ask him."
                "You turn, and nod to the kid, who looked between all of you with confusion on his face."
                tan "So, kid, where are you from? Can we help you?"

            "All of you are confused by the jumble of words that come forth. It seems... Gaelic, but also not. A few snippets of words, forest, faery, legends... A few you can hear, but not much."
            if Seanchas >= 10 or Fili >= 10 or rite == 2:
                "But then it clicks in your mind. You recognize this tongue. It is the tongue of the gods and their servants."
                "It has been long since you heard any of it, but you focus, and his words start to parse in your mind."
                sc "Well... I got lost in your forest after I wandered out of the otherworld into yours. My people are called faery in your legends. I'm sorry I transfixed you, I didn't mean to, I promise."
                "You clear your throat and respond in the same tongue."
                tan"Child of the Fae, you're lost?"
                "Your companions look even more confused, eyes darting between the two of you. The kid nods innocently, with big eyes looking up into your own as you properly approach him now."
                tan "Oh, great, we have to deal with fae."
            tan"Whatever are we going to do with this kid..."
            "You mumble, mostly to yourself. A twig snap from the woods prompts your eyes towards the sound. Someone approaching? Your hand goes for your weapon, before you relax."
            "Your eyes catch a raucous mismatch of colors through the brush. Oh, perfect. The gods had a sense of humor, eh? It was [fp], the local fili, who was often known for her associations with the occult and strange of the Tuath."
            tan "Hail, Cait. How goes it?"
            fp "Pleasantly. You met a faery child, I see?"
            "Of course, her keen eyes picked up the strange child in your midst right away. She did have a knack for picking out what others might not."
            tan "So he's fae then?"
            fp "What else would he be, a turnip?"
            "She gently prods you to the side as she enters the glade and approaches the child. A few whispers in the ear, and the child nodded, reaching up towards her. With grace, the red- and scatter-haired mystic gently picked up the child."
            "You blink, and the child is now a rabbit. With small antlers. You aren't sure if that explains anything, or just raises more questions. Séan, meanwhile, nods with oblivious understanding."
            sean "So, that's where the kid, er, the rabbit, the kid? That's where the-"
            "Your other companion shushes him, and he clams up."
            fp "We need to help this child. It isn't safe in these woods, even for his people. Especially today."
            tan "What's wrong with today?"
            "Cait simply shakes her head, lips drawn into a closed line."
            fp "I can bring him to the mound he's from. I was to visit there today anyway."
            fp"This child is of the kin of Connal Cernach, so he must have just felt the pull of our wilds. It would be no trouble to leave him to me."
            "You aren't sure if you should trust her. The poet had always been a bit of an outsider to the rest of the Tuath, some even claimed half-fae herself."
            "Her foreboding words about today, on top of memories of last night's dream, make it hard to trust her intentions."
            sean "Maybe... Maybe we should help too. Escort you there."
            fp "The forest is friendly to me, that would not be necessary."
            if C_aoife == True:
                aoife "He should return with us, I say. Let the [king] negotiate with these fae. This is above us."
            elif C_niall == True:
                niall "Why not bring him home? We could feed him and repair his clothes, return him on the morn with a gift."
            elif C_nora == True:
                nora "I don't know about going tonight. It is late, we can always go tomorrow, bring him to safety today."
            fp "Taking him to the village could be a poor decision, with today's fortunes and the capriciousness of the supernatural."
            "{i}Or maybe,{/i} you think to yourself, {i}Maybe it would be better if we left him out here. If he was a child of the forest, he would be safe, wouldn't he?{/i}"
            menu childChoice:
                "Get to the Mound quickly, [fp]":
                    $faekid = 1
                    tan"You've said yourself, things are strange tonight, even if not with those words. I'd not want to lose you. Get on the way to the mound, now."
                    tan "We'll send a message to Liam to make sure you get home safely."
                    "The mystic smiles, and nods. She gently pets the rabbit as she turns, and promptly walks out into the forest. Within moments, you can no longer see her eclectic clothing."
                    "You wonder if that's just due to the growing dark, or because of some fae trickery."
                    "You may never know."
                "We'll escort you there.":
                    $faekid = 2
                    "Despite her protests but moments before, the mystic smiles at this, giving as much of a bow as she can while carrying a rabbit."
                    fp"I thank you, my [heir]. This is more than a poet like myself could expect."
                    tan "Think nothing of it. I will be glad to help you."
                    "[sean] swallows, looking increasingly nervous."
                    sean "Okay, time to visit a Sídhe, then."
                "Take him home with us, we can return him tomorrow.":
                    $faekid = 3
                    "The Mystic's face darkens slightly, but she does not look too torn by this."
                    fp "I suppose. Let us be on our way?"
                    "You give her a nod, and gesture for all of back the way you came along the wild chase."
                    sean"This'll make for a good song, I suppose. Not had a Sí child at our tuath... ever, I think!"
                "Leave him, he can make his own way.":
                    $faekid = 4
                    "You shake your head, frowning."
                    tan"He is not our problem. We can't afford to deal the fae misinterpreting our actions. I'm sure his parents will be along shortly to recover him."
                    show text "{b}{color=#FFFFFF}Honor Lost{/color}{/b}" at truecenter
                    with dissolve
                    pause 1
                    hide text
                    with dissolve
                    $Honor -= 1
                    "The rest of the group has a hard look on their face. All but Cait nod in what you assume is understanding a moment later."
                    if C_aoife == True:
                        aoife "This... This is probably for the best."
                    elif C_niall == True:
                        "Niall simply grunts and turns to begin walking for the path you left a short time ago."
                    elif C_nora == True:
                        nora "Hrmph. I suppose. Not a fan of leaving a kid behind in the forest at night, though."
                    "The mystic looks mortified. She harmuphs and quickly whispers something into the rabbit's ears. It's ears twitch before it bounds out of her hands and into the woods."
                    fp "I gave him directions. It was the least I can do. I cannot defy my [heir]."
                    fp "But I will be making my own way home, tonight."
                    "You give her a nod, and she melts into the forest, off to some unknown location."

            sean "Let's get going. I'm suddenly worried about getting home as soon as we can. There's something odd on the air tonight, magic children aside."
            tan "Good idea. Lead the way, friend."
            #Choice regardless leads to the forest sneak and discovery of the raiders.
            jump WoodlandTrek
