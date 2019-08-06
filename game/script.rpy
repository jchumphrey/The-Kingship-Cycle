#Character definitions
#Protagonist
#define tan = Character("Tánaiste", color="#006400")
define tan = Character("Tánaiste", color="#006400") #remove
image side player = ConditionSwitch(
    "PCportrait == 0", "portraitbase.png",
    "PCportrait == 1", "portrait1.png",
    "PCportrait == 2", "portrait2.png",
    "PCportrait == 3", "portrait3.png",
    "PCportrait == 4", "portrait4.png",
    "PCportrait == 5", "portrait5.png",
    "PCportrait == 6", "portrait6.png")
define PCportrait = 0

#images
#main screen images
image brother = "brother.png"
image fintan = "fintan.png"
image sean = "sean.png"
image niall = "niall.png"
image nora = "nora.png"
image aoife = "aoife.png"
image liam = "liam.png"
image dad = "father.png"
image morrigan = "morrigan.png"
image macha = "macha.png"
image eiru = "eiru.png"


#side images
image side sean = "sean icon.png"
image side niall = "niall icon.png"
image side nora = "nora icon.png"
image side aoife = "aoife icon.png"
image side liam = "liam icon.png"
image side conn = "brother icon.png"
image side fintan = "fintan icon.png"
image side dad = "father icon.png"

#titles
define heir = Character("Tánaiste")
define chief = Character("Taoiseach")
define king = Character("Rí")
define overking = Character("Ruirí")
define provincialking = Character("Rí ruirech")
define highking = Character("Ard-Rí")
define fiannaleader = Character("Rígfénnid")

#NPCs
#Legendary
define fmb = Character("Fintan mac Bóchra", color="#191970", image="fintan") #Immortal historian/lorekeeper
define morrigan = Character("Raven-woman")
define macha = Character ("Red Warrior")
define eiru = Character ("Ériu", color="#758b72")
define tdd = Character("Tuath Dé") #Since this may come up often
define ost = Character("An Old Storyteller")

#Potential Fiann members.
define niall = Character("Niall Casúr", color="996633", image="niall")     #Curadh Vitality/Might #The Hammer
define nora = Character("Nora Uí Diarmada", color="1c8352", image="nora")   #Ranger Finesse/Seanchas
define sean = Character("Séan Rós", color="C02E4C", image="sean")           #Bard   Fili/Finesse "Rose"
define aoife = Character("Aoife Sciath", color="42cef4", image="aoife") #Conn's wife, current rígfénnid. Might/Fili
                        #Aoife Shield
#Tuath
define bro = Character("Conn Óg", color="FA8072", image="conn")     #Your brother "The Young"
define liam = Character("Liam of the Wood", color="4e5746", image="liam")   #relaxed, expert archer, hunter, and woodsman
define tb = Character("Conchobhar the Smith") #Gruff weaponsmith and metalworker
define td = Character("Medb Ciallmhar")  #local druid leader "The Wise"
define tp = Character("Padraig of Armagh")  #Priest from Armagh
define fp = Character("Caitlín the Mystic")  #Faetouched Poet
define dad = Character("Father", color="6633FF")

#Royals
define kod = Character("Rí Amlaíb")         #King of Dublin
define kot = Character("Uí Néill Ard-Rí")       #King of Tara

#Fae
define sc = Character("Lost Child")

#Enemies
define raidchamp = Character("Raider Curadh", color="#7a7372")

#reset after playtest
#Mechanics definitions
#Virtues
define Might = 1
define Finesse = 1
define Seanchas = 1
define Fili = 1
define Vitality = 1

define injuryCount = 0
define injuryMax = 3

define d20Roll = 0
define difficulty = 0
#When rolling use: $d20Roll = renpy.random.randint(1,20)
define enemyInjury = 0
define enemyInjuryMax = 3

#Resources
define Honor = 5     #What the people think of you

#Flag Definitions 0 either is default or not set
#Background flags
define heritage = 0  #1-Connachtman, 2-Ulsterman, 3-Norse, 4-Christian, 5-Bard
define childhood = 0    #1-Old Ri, 2-Druid Matron, 3-Weaponsmith, 4-Hunter/Ranger, 5-Faetouched Poet.
define training = 0    #1-Fiann training, 2-Druid circle, 3-Ranger/huntsman, 4-artisan/builder, 5-artist/poet/bard
define rite = 0       #1-challenged warriors,2- communed with the gods,3- expedition into the Sidhe Woods,4- Built a storehouse,5- Wrote old story

define dexFighter = 0 #0-Might, 1-Dex, 2-equal

##Act 1 flags
define faith = 0 #1-Gaelic, 2-Christian, 3-Syncretic, 4-Agnostic, 5-Norse
define weapon = 0 #1-fists,2-Spears,3-Swords,4-Axes,5-Claymores,6-Bows,7-Slings
define reassureAttempt = 0 #0-no attempt, 1-attempted
define request = 0 #1-hunt,2-wolves,3-community

define hunttarget = 0 #1-small game, 2- deer, 3- boar
define huntwin = 0 # 0-fail, 1-succeed, 2-great succeed

define tributetarget = 0 #1-farm, 2- herders, 3- church
define tributewin = 0 # 0-fail, 1-succeed, 2-great succeed

define wolftarget = 0 #1- drive away, 2- scare off 3- exterminate
define wolfwin = 0  # 0-fail, 1-succeed, 2-great succeed

define faekid = 1 # 1-Cait goes alone to the mound, 3-Escort to the mound, 4-take him home, 4- leave him.

define raiderAllies = 0
define raidReact = 0 #0-no choice 1-sneak 2-confront 3-hide
define ambushResult = 0 #0-not amubushed, 1-ambushed, killed enemies, 2- amubushed, enemies fled, 3-ambushed, lost. 4-ambushed, enemies joined
define confrontResult = 0 #0-Did not confront, 1-lost, 2-killed, took head, 3-killed, 4-spared, 5-spared, asked to join tuath
define fieldHelp = 0 #0-didn't help in field, 1- gate. 2-fiann 3-market
define townResult = 0 #1-win 2- loss

define raidResult = 0 #1-Hid overnight, 2- Win. 3- Loss
define deathchoice = 0 #1-run 2-weep 3- anger 4- cold
define speech1choice = 0 #1-suffer, 2-strong, 3-together, 4-defiant, 5-die enemies, 6-future
define speech2choice = 0 #1- put down, 2- watchful, 3-be better, 4-meaningless raiders, 5-Not held back
define speech3choice = 0 #1-Vengence 2-Justice 3-Strength 4- Honor 5- Prosperity 6- Unity 7-Faith

#Companion Flags
define C_sean = False
define C_nora = False
define C_aoife = False
define C_niall = False

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#Playtest variables to remove later
define primary = 0
define secondary = 0

#Python
init python: # Code snippet to put sounds for page advancement. By Divonna and found at: https://lemmasoft.renai.us/forums/viewtopic.php?p=465398#p465398
    def dismiss_callback():
        renpy.play("sound/pageTurn.wav")
        return True
    config.say_allow_dismiss = dismiss_callback

# The game starts here.

label start:
    #Test spot
label IrelandStory:
    ost "On the edge of the world lies a green jewel of an island, desired by all who have set foot on her."
    ost "She has been fought over since the world was young. Monsters, demons, gods, and humans have all tried to take this land for their own."
    ost "Nourished by rains from the Western Sea, this land is impeccably green, thriving, alive. Ancient woods and fertile fields stand next to the deepest of bogs and rocky pastureland."
    ost "The land has always been a boon for the people blessed to live on it, and inspired envy in others to seize its verdant shores."
    ost"Six invaders have trod upon this land's shores."
    ost"Cessair, Partholon, Nemed, the Fir Bolg, the Tuath Dé Danann, and finally the Gaels."
    ost"They have all staked their claim on this bountiful island. The first three failed in their attempts, but Nemed's people would return."
    ost"The first part would come as the Fir Bolg. The Men of the Bags, named after the bags of soil they brought to settle the salt-scoured, hostile western lands and shape them to be like the rest of the island."
    ost"Their later brethren, the godly Tuath Dé Danann, the Tribe of the Goddess Danu, had fled north where the Fir Bolg had fled south."
    ost"The Tuath Dé would meet the World's creator, Danu, in the far north of the world and would learn the secrets of civilization and magic at her side."
    ost"While living in four cities along Danu's River, the Tuath Dé created wondrous artifacts and magical weapons that ensured the might of their warriors, the health of their people, and righteousness of their king."

    show artifact fourtreasures
    with dissolve

    ost"In Goirias the spear of Lugh was fashioned. Lugh, the hero of the Tuath Dé, named the spear the Red Javelin. It became known as Slaughterer for no one who went against it could survive."
    ost"In Findias the sword of the King of the Tuath Dé, Nuada, was forged. When the sun-bright blade was drawn from the sheath, no one could escape it, nor resist it."
    ost"In Muirias, the Dagda, the druidic Good God, crafted the Cauldron of Plenty from which any number of people could be satisfied."
    ost"The final item was created in Falias. It was the Lia Fáil, the Stone of Destiny, which would shout with joy when a true King strode upon it."
    ost"When the Tuatha Dé returned to the Island of Cessair, they gave it a new name after this stone: Inis Fáil, Island of Destiny."

    hide artifact
    with dissolve

    ost"But the Emerald Island was still held by their cousins, the Fir Bolg, who had brought new fertility to the most remote islands and reaches."
    ost"The Gods and the Fir Bolg went to war when no compromise could be met. The battle was honorable and fair, and continued for many days and nights. In the end, the Tuath Dé won."
    ost"However, during the great battle, the Fir Bolg King had severed Nuada's arm. The [tdd] King had to step down. He was no longer perfect in body and by ancient custom a king must be whole to rule."

    show nuada silverhand
    with dissolve

    ost"The Great Physician Dian Cecht crafted Nuada an arm as good and as able as his original. The arm was wrought from silver and sinew, earning him the name Nuada Airgetlam, Nuada Silver-hand."
    ost"But he still was not whole as he once was."

    hide nuada
    with dissolve

    ost"So the Tuath Dé, after granting the honorable Fir Bolg parts of the western of Connacht, had to choose a new king. Of their number, the half-fomorian Bres the Beautiful was crowned."
    ost"But his reign would prove tyrannical. For he took after his fomorian, monstrous heritage rather than the noble heritage of the gods."
    ost"He forced the Gods to toil apart from their skills, extracted heavy tributes back to his fomorian brothers, and mistreated all in his court with his wanton cruelty."

    show lugh
    with dissolve

    ost"The Tuath Dé would rise up, led by Lugh Lámfada, Lugh of Long Arm, and force Bres to flee. Nuada was crowned once more as his arm was once again replaced with one of flesh and blood by Dian Cecht's children."
    ost"But Bres convinced his monstrous family to invade Ireland in turn. After a harsh battle that ended Nuada's life by way of the Fomorian King Balor's baleful eye, the Tuatha were dominant. They crowned Lugh their new King."
    ost"Much later, your people, the Gaels, would invade from Hispania and Gaul. During this invasion, the island gained new names: Fodla, Banba, and most importantly Ériu, after the three goddesses of the land."
    ost"The Tuath Dé would agree to share Eire with the Gaels. You were granted the Overworld, while they retreated to the plentiful Otherworld."

    hide lugh
    with dissolve

    ost"How do I know all this history, from before even the written word, you ask?"
    ost"For I was there for all of it."
    ost"I am the immortal consort of Cessair, Fintan Mac Bóchra."

    show fintan at right
    with fade

    stop music fadeout 1.0
    play music "music/Mystical_Beauty.ogg" fadein 1.0

    fmb "I have watched Ireland, a name brought by our newest invaders, for countless generations to convey its history and advise its greatest kings."
    fmb "And as these seventh invaders, those men of pale hair and eyes?"

    show norse at left
    with dissolve

    fmb "They are Norse. A people of the eastern Sea, past the Isles. A people of a harsh land and the cold, bringing steel and new gods to Ireland."
    fmb "While they came to dominate and enslave, they have since chosen to settle and create cities to link themselves with the disparate ports of their people across the seas."
    fmb "Perhaps the Norse will come to dominate the Gaels, as the Gaels first dominated this land's earlier peoples? Or perhaps they will just be a footnote like Partholon."

    hide norse
    with dissolve

    fmb "But, I think, this island will be united again under a single High King as it was under the Tuath Dé Danann."
    fmb "The tension between Gael and Norse has broken, and war has resumed. The Gaels lose faith in the old ways, the old families."
    fmb "Time shall tell who reigns and who falls in this story."
    fmb "History is not pre-written."
    fmb "But first...."

    fmb "Why don't you tell me about yourself, young heir?"
label backstory:
    menu backstory_1: #Birth
        tan "Well, I was born to a noble of the Ó Durcáin Tuath, my homeland, and her lover the...{fast}"
        "Connachtman Herdsman":
            $ Vitality = 3
            $ Might = 2
            $ Seanchas = 1
            $ heritage = 1
            $ dad = Character("Aengus", color="6633FF", image="dad")
            show heritage herd at left
            with dissolve
            tan "Not quite the local, but my mother met him while traveling along the Great Sea's coast. A few meetings and they were inseparable."
            tan "She brought him and his herds, a fairly sizable collection of sheep and a few cattle, to her home and married him."
            tan "I was raised helping out with the animals. Pleasant creatures, all said, but very tiring to raise and care for!"
        "Ulsterian Huntsman":
            $ Finesse = 3
            $ Seanchas = 2
            $ Might = 1
            $ heritage = 2
            $ dad = Character("Fionn", color="6633FF", image="dad")
            show heritage hunt at left
            with dissolve
            tan "A local hunter of our Tuath, who'd been infatuated with Mom since they first met in childhood. He courted her, and she fell hard."
            tan "He's a humble fellow and taught me everything I needed to know about moving through the forests of Eire safely, hunting its beasts, and bowmanship."
            tan "Though, he's usually was away in the forests, he did always regale me with wondrous stories of the Fae he met out there."
        "Norseman Settler":
            $ Might = 3
            $ Vitality = 2
            $ Fili = 1
            $ heritage = 3
            $ dad = Character("Asulf",color="6633FF", image="dad")
            show heritage norse at left
            with dissolve
            tan "He's not much alike the Gaelic fathers I know, he's somehow even more boisterous and foolhardy! But he caught my mother's eye all the same."
            tan "I've never met a better fighter, hardened by his years as a raider in the Saxon Tuaths of England."
            tan "But he chose to settle in Eire. He and his other Norse friends in town taught me how to fight, brawl, all those fun things. Bet I can hold my ale better than you too."
        "Priest from Armagh":
            $ Seanchas = 3
            $ Fili = 2
            $ Finesse = 1
            $ heritage = 4
            $ dad = Character("Siomón", color="6633FF", image="dad")
            show heritage priest at left
            with dissolve
            tan "A holy man, no abbot nor missionary, but firm in his belief in the Divine God. He never tried converting my ma for he was a Gaelic priest rather than a hardliner, but they fell in love and respected each other."
            tan "He taught me to read, to write, to appreciate the land. Most of all he was an expert in the Seanchas, our traditional wisdom and laws, on top of the word of God."
            tan "Dad's teaching left me knowledgeable and worldly, more than many might expect from a small Tuath in Ireland."
        "Wandering Bard":
            $ Fili = 5
            $ Finesse = 3
            $ Vitality = 2
            $ heritage = 5
            $ dad = Character("Artúr",color="6633FF", image="dad")
            show heritage bard at left
            with dissolve
            tan "He was quite a bit of a rogue. He'd spent his days wandering Ireland and the Isles, regaling everyone with tales of history, the Gods, and his own fabrication."
            tan "While he shunned learning the Seanchas, our traditional wisdom and laws, or taking any permeant role in any tuath he passed through during his travels, Mom convinced him to finally settle and start a family."
            tan "He certainly kept the bedtime stories interesting, and I feel I picked up his flair for the dramatic."

    tan "Aside from my colorful parentage, I got along like any of noble heritage in our Tuath. I was allowed in the Youth Troop of our Tuath and trained to be a warrior."
    tan "I learned all the skills for life in Eire and even a bit of leadership. I was always the head of my little group of friends."
    tan "My friends Niall, Nora, and Séan, my elder brother Conn, and I were, and still are, inseparable."
    tan "And as most members of the tuath, I have to thank the fosterage of the tuath's skilled members for my early childhood."

    menu backstory_2: #Childhood
        tan "I especially have to thank the person who took the highest interest in me...{fast}"
        "the Old Rí.":
            $ Might += 3
            $ Fili += 2
            $ Seanchas += 1
            $ childhood = 1
            show foster ri at left
            tan"The King was the one who first decided to take me under his wing. He figured I might one day run the clan, I suppose."
            tan"So he began to teach me how to rule, how to convince, and how to prove my strength. I learned to use swords, shields and javelin, all sorts of weapons."
            tan"He was a kind man, and always taught me it was easier to get people to like you by being genuine and honorable than through manipulation."
        "the Druid Matron [td].":
            $ Seanchas += 3
            $ Vitality += 2
            $ Fili += 1
            $ childhood = 2
            show foster druid at left
            tan"She perceived an intelligent gleam in my eye even as young as I was, so chose me as her foster child before any other elder did."
            tan"The Matron taught me about the natural world and its wonders, our history and the stories of the gods. Fintan, you didn't really need to remind me of our origin!"
            tan"But she also had me work hard. She didn't want a student who sacrificed the vitality of the body for strength in mind."
        "Our blacksmith and weaponsmith, Conchobhar.":
            $ Vitality += 3
            $ Finesse += 2
            $ Might += 1
            $ childhood = 3
            show foster weaponsmith at left
            tan"He picked me up after deciding he wanted an apprentice to teach his crafts. Both fine metalwork and the fine iron and steel weapons of our Tuath was his role."
            tan"The work trained my body, but also the skill of my hands. Conchobhar proved a good mentor in those early years."
            tan"He made me a dependable, solid person to rely on in the Tuath."
        "Our chief hunter, the ranger Liam.":
            $ Finesse += 3
            $ Might += 2
            $ Vitality += 1
            $ childhood = 4
            show foster ranger at left
            tan"A very relaxed, yet skilled warrior who preferred bows and skilled combat over the force of a curadh like our Smith. Liam brought me out to the forests to help him hunt."
            tan"Both my own strength and skill would be improved, and he taught me life was something to be taken slow and enjoyed."
            tan"'To rush through life was to miss its beauty' were his exact words."
        "Our local faetouched poet, [fp].":
            $ Fili += 3
            $ Seanchas += 2
            $ Finesse += 1
            $ childhood = 5
            show foster poet at left
            tan"My childhood was an odd one with [fp]."
            tan"She had encounters with the Sidhe, and the angels, often enough to make her perception a bit odd and wider than most. She knew secrets of the world even the druids didn't."
            tan"But her greatest gift was her skill with wordsmithing and verse, to inspire hearts and bring comfort around the hearths of the Tuath."
            tan"I like to think she taught me to do the same."
    tan"The first time I met someone I hadn't known my entire life was when my brother and I were brought along on a trip near the end of the Old Rí's life, in 966."
    tan"He had to show his submission to the newest king of Dyflinn, the largest of the Norse towns, as we lived in its sphere."
    tan"[kod] mac Sitric proved a vital man, even at to what seemed like an ancient age to me then. He's still ruling Dyflinn, though, so he must not have been that old."
    tan"Though, he was rather intimidating with his conquests across the Isles being displayed in his throne room. Glorous jewels and artifacts of all faiths of the land."
    tan"Twice King of Dyflinn, and former king of Northumbria. He was brilliant red of hair and icy blue eyes like his Norse brethren."
    tan"The old [king], however, didn't prove as long lived. He died of an old wound shortly before my own proper training began."
    tan"After the trip to Dublin, my childhood passed quickly enough under the fosterage of my mentors. I learned much of the world beyond the Tuath, beyond our people."

    menu backstory_3: #Training
        tan "As I grew, my training became more specialized. After the Old Rí passed and our mother was made the Rí, I chose my direction...{fast}"
        "and I took up Sword, Spear, and Shield to become part of my mother's Fiann.":
            $ Might += 3
            $ Seanchas += 2
            $ Vitality += 1
            $ training = 1
            show train fianna at left
            tan"The training was rigorous. Any Tuath worth its silver and iron had the most expert warriors possible in the King's fiann."
            tan"While we didn't go adventuring as some Fianna did, Mother was a homebody who preferred helping around the villages, we still watched the borders for raids."
            tan"I like to think I learned a bit more about the world while I served under her. I certainly did learn quite a few stories about hunting."
            tan"I also got to know [aoife], my mother's rígfénnid. She is one of the youngest but most accomplished warriors in the Tuath. A bit stern, but well-meaning and gentle with children."
        "and I would join the Druid Matron in her circle to learn the secrets of the world.":
            $ Seanchas += 3
            $ Finesse += 2
            $ Fili += 1
            $ training = 2
            show train druid at left
            tan"The Matron was more than ecstatic to accept my request to join the circle. The mysteries of our people were laid open to me, beyond the stories."
            tan"I became quite adept at natural magic, in fact. The deftness of my movements during rituals calling upon the gods and the natural world to aid the Tuath spoke of practiced knowledge made manifest."
            tan"While I could not claim your own great knowledge, Fintan, I certainly was taught plenty of Ireland's secret knowledge."
        "and I decided becoming a ranger and huntsman of the tuath was my calling.":
            $ Finesse += 3
            $ Vitality += 2
            $ Might += 1
            $ training = 3
            show train ranger at left
            tan"The forest called, and the animals could provide for the Villages. Liam was happy to have me aid him."
            tan"My bow arm grew strong, and I learned to stalk like a wolf. Nothing in those forests was unknown to me."
            tan"I also happened to get a good number of scars. It's surprising just how dangerous fallen logs can be when you trip on them!"
        "and I went for a humble profession, an artisan and builder for the Tuath.":
            $ Vitality += 3
            $ Fili += 2
            $ Finesse += 1
            $ training = 4
            show train artisan at left
            tan"Hard work, and not very glamorous work compared to hunting or being a warrior."
            tan"But I could express myself in the clay. I found ways to tell our stories in them as well."
            tan"Plus, you get plenty of time to chat up people while working since you aren't out of the village and busy all day."
        "and I decided for the more carefree lifestyle, perhaps that of an itinerant artist, poet, or bard.":
            $ Fili += 3
            $ Might += 2
            $ Seanchas += 1
            $ training = 5
            show train bard at left

            tan"It might be claimed I am lazy to choose a more sedentary, creative life, but is it not the place of a poet to challenge the minds of others?"
            tan"I certainly tried, spending my time writing satire and praise and for all the divines we in Ireland know."
            tan"I did get some practice with my weapons too, as it happened: Turns out not everyone appreciates criticism."
    tan"But as all Irish, I still had to earn my full place in the tuath before I could get a full role."
    tan"This was delayed, as was many rites of peacetime, by war."
    tan"A band of raiders crossed into our territory. They were of mixed heritage, from across the Isles and beyond."
    tan"It didn't matter from where they came, for several years they plundered our Tuath and the territories of the Ulaidh and the Uí Néill."
    tan"But, luckily they were driven off. Not slain like the rogues they were, sadly, but we haven't seen their ilk since."

    menu backstory_4: #Rite of Passage
        tan "But finally, time came for my rite of passage to be a full adult among the people of our Tuath, proving it by performing a feat.{fast}"
        "I challenged the finest warriors in the clan to honorable duels.":
            $ Might += 3
            $ Finesse += 2
            $ Vitality += 1
            $ rite = 1
            show rite battle at left
            tan"And what glorious battles they were!"
            tan"Blood and Bruises, steel swords and oaken shields. What more could a warrior desire?"
            tan"They were happy to give me a few pointers once they finally took me down, but by then I'd already bested the strongest of the clann."
            tan"I'd already given a few a hearty strikes though, and I swear I fought with the fury of Cú Chulainn himself."
        "I communed with the ancestors and gods in the Nemeton, fasting for a week.":
            $ Seanchas += 3
            $ Fili += 2
            $ Vitality += 1
            $ rite = 2
            show rite commune at left
            tan"A week of solemn silence, rituals, and meditation. Only drinking water and eating the barest needed to avoid fully passing into the Otherworld."
            tan"Not an experience for the weak of will, certainly."
            tan"But I grew stronger, both in my faith and my strength, after I ventured deep enough among the Sidhe to earn the secrets of the [tdd] Danann."
            tan"I even met a few of the gods! Brigit was a lovely woman to chat with, though I felt the Dagda feared I had further intentions."
        "I went on an expedition deep into the woods of the Sidhe, to hunt for a White Stag":
            $ Finesse += 3
            $ Fili += 2
            $ Vitality += 1
            $ rite = 3
            show rite hunt at left
            tan"I doubt one as long lived as you would mock a youth for trying. The legendary beasts of the Otherworld had sometimes been spotted in our Forests, so I felt I should try my luck."
            tan"So, I spent a week living from the land alone and searching. On the third day I found my way into a Sidhe mound itself and was turned out into the otherworld."
            tan"Such beauty, but such oddness. The forest was deep, alive, ancient, even more than the ones of Ireland."
            tan"The animals moved with practiced grace of a domestic beast, from the smallest sparrow to the greatest of bucks."
            tan"I turned back. Even then I was a half-week late to return. But I at least did return, and with the largest deer they had ever seen someone hunt in the woods for generations."
        "I worked to singlehandedly build a new storehouse for the tuath village.":
            $ Vitality += 3
            $ Seanchas += 2
            $ Might += 1
            $ rite = 4
            show rite build at left
            tan"T'was long, grueling work. Without so much of the help of [tb], I had to forge the nails, cut the wood, learn the crafts, everything."
            tan"Took me a whole half-moon in the end. Day-in day-out, hammering, forming, shaping, making nature bend to my will."
            tan"Plus, it was useful to the tuath. I even took the time to fix up the other storehouses after."
            tan"Conchobhar certainly wasn't happy hearing me mention he could use some more help keeping up repairs but bless him he is turning grey and bald already!"
        "I created a new telling of one of the old stories, to add my own voice to the tapestry of our people's history.":
            $ Fili += 3
            $ Seanchas += 2
            $ Vitality += 1
            $ rite = 5
            show rite story at left
            tan"Over an entire moon I labored in secret, not letting a soul hear my {i}Magnum Opus{/i}, as the Romans would say. But I certainly will create more works after."
            tan"Finally, at the night of the full moon, around the roaring bonfire, I shared the story. I spared no effort in my presentation!"
            tan"I chose the Wasting of Cú Chulainn, partially for the humor of the piece. The story of Cú pining for a Sí woman, leading to his great strength waning until his wife takes matters into her own hands!"
            tan"The telling was a great success, and brought a night of revelry. It was all I could have asked for, and it was worth seeing the delight on the faces of the youths, inspired by my work."
    tan"And that brings us to today. My rite was but a scant few months ago and save some... unfortunate news of my mother's passing in the last week, the Tuath has been quiet."
    tan"My brother had been the [heir], me the second, so he's become the new [king]. Young, like me, but already loved by the whole of the Clann and Tuath."
    tan"But I am sure he'll be an amazing one."
    tan"Was there anything else, Elder Fintan?"
label virtues:
    fmb "Perhaps in a moment."
    fmb"First, I should explain an important aspect of Ireland in case you have never been told."
    fmb"Have the Virtues of Ireland been properly explained to you?"

    menu virtueExplain: #Skip explanation if already played.
        "Of course, Fintan, how would I not know?":
            fmb"Clever child."
            jump virtuesExplained
        "Could you explain to me again?":
            jump explanationVirtue

    label explanationVirtue:
        fmb"Very well."
        fmb"The five primary virtues are Might, Finesse, Seanchas, Fili, and Vitality. Not moral virtues, mind you, but things all those of noble blood in in Ireland aspire to gain."
        fmb"Might.\nThe strength of your arm, of your body. Athleticism, raw power, and skill at arms. One of the truest virtues of a warrior of Eire."
        fmb"Finesse.\nAccuracy of strikes. Quickness of wit and body. Finesse is delicate and precise where Might smashes through. Both choices worthy of warriors, just different ones."
        fmb"Seanchas.\nFrom the lore of books, the wisdom of the Elders, and their own cleverness, those versed in Seanchas reason their way through life's puzzles."
        fmb"Fili.\nThe power of the voice, of the will, made manifest. It pulls together the throngs of faithful in song, the warriors of a land to battle, and weaves magic of all sorts."
        fmb"Finally, Vitality.\nThe endurance to keep struggling and working on harder, to take the time to build something lasting, and to work with tools and the land. Honorable, durable, and strong like stone."
        fmb"A more vital person will be able to take more punishment before falling in battle."
        fmb"Sometimes in life you will be faced with challenges that test these virtues."
        fmb"While you cannot always predict the outcome of these tests as only Fate can, your experience will improve your tested virtue even in failure."
        fmb"Do you understand?"

    menu virtueDoubleCheck:#To really make sure
        "Yes, I understand.":
            jump virtuesExplained
        "No, can you go through them again?":
            jump explanationVirtue

    label virtuesExplained:

    fmb "I believe that is most of my time visiting you, [tan] of the Ó Durcáin Tuath."
    fmb "You've told me quite the story so far, I'm excited to see your future unfold alongside Ireland's own."
    fmb "But are you truly happy with your choices?"

    menu redo: #Gives option to jump back and redo, lists out current stat array.
        "Might: [Might],
        Finesse: [Finesse],
        Seanchas: [Seanchas],
        Fili: [Fili],
        Vitality: [Vitality]{fast}"
        "Actually, let me try again...":
            fmb"Let us start over then. How did you actually live your life?"
            scene bg fire
            show fintan at right
            with dissolve
            jump backstory
        "I wouldn't have lived any other way.":
            scene bg fire
            show fintan at right
            with dissolve
            fmb"Excellent."

    fmb "Be confident in your choices going forward from today. Actions shape history, even minor ones can lead to unknown futures."
    fmb "And some choices will set your future on an irrevocable path. Be wary of this. Know when to stop and think."
    #nicknames here
label nickname:
    fmb "Before I go, allow me to learn a bit more about you."
    fmb "Many are better known by their bynames, nicknames, and epithets."
    fmb "What about you, [tan]? How are you referred to?"
    menu nickChoice:
        "My byname is..."
        "My title.":
                $tan = Character("Tánaiste", color="#006400", image="player")
                tan "It may seem stuffy, but it is accurate. I go by my title in everyday life."
        "From my heritage.":
                if heritage == 1:
                    tan"Because I aided my father in the fields, I started being called a sheepdog. My nickname became Caorach."
                    $tan = Character("Caorach", color="#006400", image="player")
                if heritage == 2:
                    tan"While dad taught me some of his hunting skills, I was more distracted with picking up sticks than the bow. He started calling me Twig."
                    $tan = Character("Twig", color="#006400", image="player")
                if heritage == 3:
                    tan"I inherited the pale hair more common of the Norse, so I was given the byname Fionn, pale-haired."
                    $tan = Character("Fionn", color="#006400", image="player")
                if heritage == 4:
                    tan"My father had plenty of manuscripts and books for me to read through. I started being called a Leamhan! A Moth!"
                    $tan = Character("Leamhan", color="#006400", image="player")
                if heritage == 5:
                    tan"I inherited Dad's energy and drive, and he couldn't help but compare me to his favored instrument, a fiddle. So I became Fidil."
                    $tan =Character("Fidil", color="#006400", image="player")
        "From my childhood.":
                if childhood == 1:
                    tan"The Ri saw something special when he trained me. Before he died, he started calling me Fáil, Destiny. I wonder what he saw."
                    $tan = Character("Fáil", color="#006400", image="player")
                if childhood == 2:
                    tan"[td] often lamented my independent streak by calling me a wildflower. I took the name as my own."
                    $tan = Character("Wildflower", color="#006400", image="player")
                if childhood == 3:
                    tan"[tb] was a straightforward man. He simply called me Iron, because he saw me as dependable."
                    $tan = Character("Iron", color="#006400", image="player")
                if childhood == 4:
                    tan"Liam couldn't help but compare me to a deer, fia, when he saw my long loping run to chase down animals."
                    $tan = Character("Fia", color="#006400", image="player")
                if childhood == 5:
                    tan"I wouldn't, even for a moment, stop asking [fp] about the Fae and Gods. She started calling me Sí Cara, fairy-friend, within the week."
                    $tan = Character("Sí Cara", color="#006400", image="player")
        "From my training.":
                if training == 1:
                    tan"My fellows in the fiann knew me for my wit as well as my skill with a blade. They called me Witty, Scéalta."
                    $tan = Character("Scéalta", color="#006400", image="player")
                if training == 2:
                    tan"While working with the circle, I was known for my wisdom despite my age. They began calling me salmon, bradán, after the fish of knowledge."
                    $tan = Character("Bradán", color="#006400", image="player")
                if training == 3:
                    tan"Rianaigh is the name I earned while training as a ranger. I was an expert at tracking and wayfinding, so they honored me for it."
                    $tan = Character("Rianaigh", color="#006400", image="player")
                if training == 4:
                    tan"My training in forges and pottery and other strenuous fields made me strong, so folk began calling me strong-arm, géagláidir."
                    $tan = Character("Géagláidir", color="#006400", image="player")
                if training == 5:
                    tan"Ironically, the name I got learning to be a poet wasn't very creative! They started calling me the Young Poet, An Fhéile Óg."
                    $tan = Character("An Fhéile Óg", color="#006400", image="player")
        "From my rite of passage.":
                if rite == 1:
                    tan"For my struggles in our arena, I began to be called a champion, a Curadh! I quite like the name."
                    $tan = Character("An Curadh", color="#006400", image="player")
                if rite == 2:
                    tan"With my contact with the Gods, I have a new reputation as one who follows them, a Godseeker."
                    $tan = Character("Godseeker", color="#006400", image="player")
                if rite == 3:
                    tan"Even though I failed by task, they began calling me a hunter, sealgair, and the title stuck."
                    $tan = Character("Sealgair", color="#006400", image="player")
                if rite == 4:
                    tan"I built a storehouse, people started calling me The Builder, An Tógálaí. Pretty simple."
                    $tan = Character("An Tógálaí", color="#006400", image="player")
                if rite == 5:
                    tan"The people called me Storyweaver once the new tale settled. I must have impressed them enough!"
                    $tan = Character("Fíochán Scéal", color="#006400", image="player")
        "Something Unique":
                "The name I go by isn't a typical one, just something random from childhood."
                python:
                    tan = renpy.input("Enter your nickname:")
                    tan = Character(tan.strip(), color="#006400", image="player")
                    if not tan:
                        tan = Character("Iora", color="#006400", image="player")
                "My nickname is [tan]."
    fmb "An interesting name, [tan]."

    menu checkNick:
        "Are you sure that's what you are referred by?"
        "Certainly.":
            tan"Since I earned it, [fmb]."
        "No.":
            tan"I have been called that, but I prefer something else."
            jump nickChoice

    fmb "I'd love to hear the story of that name, someday."
label portrait:
    fmb "And what do you look like? My eyes aren't what they used to be."
    show portraitselect at left with dissolve

    menu portraits:
        "(1) Curly hair, brawny and bearded":
            $PCportrait = 1
            hide portraitselect
            tan "Quite manly, with this beard. Even my brother lacks one still."
        "(2) Shaggy hair, willowy and tall":
            $PCportrait = 2
            hide portraitselect
            tan "I think I look quite dashing, myself."
        "(3) Flowers in my hair and messy all around":
            $PCportrait = 3
            hide portraitselect
            tan "It helps me feel in touch with the world to have a piece of it with me."
        "(4) Long braided hair and war paint":
            $PCportrait = 4
            hide portraitselect
            tan "Best to be as intimidating as possible, aye?"
        "(5) Cowled and lean, curly hair":
            $PCportrait = 5
            hide portraitselect
            tan "It helps shield my eyes from the sun."
        "(6) I always wear my helmet":
            $PCportrait = 6
            hide portraitselect
            tan "I don't like being without protection, after all."

    menu checkPortrait:
        "Are you sure?"
        "Certainly.":
            tan"At least, now that I'm grown."
        "No.":
            tan"No, I look like something else"
            jump portraits
    fmb "Ah yes, now I can see it. The fog clears."

fmb "However..."
fmb "Its time to wake up, [tan]. You have a life to keep living, a brother to protect."
fmb "It is a geas, a holy obligation, upon your soul to aid him, forged by your love and devotion."
fmb "Don't disappoint."
fmb "Perhaps we shall meet again someday. But perhaps not."
fmb "But the story shall carry on, so you should wake up."

stop sound fadeout 1.0
scene black
with dissolve
jump chapter_one_half_one

label work_in_progress:
    scene black
    with dissolve
    "This game is currently a work in progress, and you have hit the end of the fully fleshed out portion."
    "As of the current time, this goes up to the end of Act 1!"
    "I hope you have enjoyed what you've seen so far! Feel free to give any feedback, or note any typos for us to improve the game."
    "Goodbye!"
return
