# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Morgan = Character("Morgan")
define Julie = Character("Julie")
define Rob = Character("Rob")
define Dad = Character("Dad")
define Nick = Character("Nick")
define Aria = Character("Aria")
define Diana = Character("Diana")
define Dave = Character("Dave")
define Woman = Character("Woman")
define Guide = Character("Guide")
define Jogstudent = Character("Jogging Student")
define Alexandra = Character("Alexandra")

# Declare images
image bg kitchen = "kitchen resize.png"
image bg school = "school.png"
image bg app = "apartment.png"
image bg cafe = "cafe.png"

#Declare sprite images
image lasagna work = "lasagna work.png"
image lasagna work angry = "lasagna work angry.png"
image lasagna work drunk = "lasagna work drunk.png"
image lasagna work embarrassed = "lasagna work embarrassed.png"
image lasagna work smile = "lasagna work smile.png"
image lasagna food = "lasagna food.png"

image sausage day = "sausage day.png"
image sausage day angry = "sausage day angry.png"
image sausage day confused = "sausage day confused.png"
image sausage day happy = "sausage day happy.png"
image sausage day sad = "sausage day sad.png"
image sausage day surprised = "sausage day surprised.png"
image sausage food = "sausage food.png"

image tiramisu day = "tiramisu day.png"
image tiramisu day disgust = "tiramisu day disgust.png"
image tiramisu day surprised = "tiramisu day surprised.png"
image tiramisu food = "tiramisu food.png"

image tso prez = "tso prez.png"
image tso prez flustered = "tso prez flustered.png"
image tso prez tired = "tso prez tired.png"
image tso prez worried = "tso prez worried.png"
image tso food = "tso food.png"

label start:
    
    
# ######DEBUG JUMPS###############################
    scene bg kitchen
    menu:
        "Start from beginning":
            jump intro
        "Sausage intro":
            jump sausage_intro
        "Cooking 1":
            jump cook1_start
        "Lasagna intro 1":
            jump lasagna_intro_1
        "Tiramisu intro":
            jump tiramisu_intro
        "Lasagna intro 2":
            jump lasagna_intro_2
        "Tso intro":
            jump tso_intro
# ################################################

    #1 INTRODUCTION START
label intro:
    scene bg kitchen 
    #bg Kitchen
    
    #MORGAN (V.O.):
    "All my life I’ve been told that the fastest way to a person’s heart is through their stomach. I find those cliche’ sayings stupid. But my dad has always lived by that cheesy old saying and I’ve never met a person more popular than him."

    #MORGAN (V.O.):
    "His restaurant is always packed with people smiling, laughing, and eating. They even paying for it. The food is famous, but it’s his personality that keeps people coming in again and again. He’s always welcoming and knows everyone by name."

    #MORGAN(V.O.):
    "To him people are worth opening up to, and bear your emotions to others. He’s kind of an idiot I guess. I’d give anything to see people the way he does."

    #[Kitchen sounds and muffled crowd noises in the background]

    #MORGAN(V.O.):
    "For as long as I could remember I’ve felt more at home in a kitchen. I can do what I love without worrying about so much."

    Morgan "OOORDER UP!"

    Julie "You do know we have a bell for a reason, right?"

    #MORGAN(V.O.):
    "Julie, my two faced little sister. I wonder if she hears half the shit that comes out of her mouth."

    Morgan "Yeah, I know. We ring it when you get too far from home. We wouldn’t want them to snatch you up and take you to the pound."

    Julie "Ha. Ha. I’m a dog? Your the one with breath so bad he can’t get a girlfriend."

    #MORGAN (V.O.):
    "My breath doesn’t smell *sniff sniff*"

    Morgan "Why are you back here anyway, isn’t there some pervy old man you should be chatting up for tips?"

    Julie "Whatever, just stop sitting there with that stupid look on your face. I came to tell you that dad needs to talk with you. He is out on his break right now. Have Rob take over for you, He’s a better cook than you anyway."

    Morgan "You know, if you keep talking the only thing that will find your body will be rats in a basement in the middle of nowhere."

    #[Split-screen sprite, JULIE left, ROB right]

    Rob "Quit bickering, if a customer overhears this it would be highly unprofessional."


    #MORGAN (V.O.):
    "Rob, the restaurant’s host. He is a hard working, honest guy. Too bad there isn’t a doctor that could do something about that stick up his ass."

    #[Return JULIE sprite]

    Morgan "Julie, I’m going to go before you finally bug Rob to the point where he actually tries to kill himself in my kitchen. Take a hint, the guy hates you."
    
    Rob "What! Huh, no!"

    Rob "AND I DON’T WANT TO KILL MYSELF, YOU DISRESPECTFUL LITTLE PIECE OF--"

    #MORGAN(V.O.):
    "i hate it when people start yelling..."

    Rob "--AND FURTHERMORE, YOU’RE ALWAYS SITTING THERE WITH THIS SMUG AS F--"

    #MORGAN(V.O.):
    "…i just shouldn’t have come to work today, i don’t have to listen to this… i can’t… "

    Rob "--JUST BECAUSE YOUR PARENTS OWN THE PLACE DOESN’T MEAN YOU CAN GO AROUND SAYING WHATEVER YOU--"

    #MORGAN(V.O.):
    "…i can’t… it’s just so loud… i can’t just leave, but if i leave he’ll just yell more…"

    Rob "--WHY ARE YOU JUST STARING, SAY SOME--"

    #MORGAN(V.O.):
    "…my arms feel like they’re noodles. why is my chest feels like a pressure cooker. i just want to leave…"

    Rob "--ARE YOU EVEN LISTE--"

    #MORGAN(V.O.):
    "…i just…"

    Rob "--JULIE, GET BACK TO THE FRONT ALREADY, THERE ARE CUSTOMERS WAITING!"

    #MORGAN(V.O.):
    "…leave..."

    Julie "Quit yelling, the customers will hear you! What was that about being prof--"

    #MORGAN(V.O.):
    "I just want to leave."

    #MORGAN(V.O.):
    "Let me leave"

    #MORGAN(V.O.):
    "letmeleaveletmeleaveLETMELEAVELETMELEA-"

    #[ROB turns into food sprite, with playful pop sound]

    #MORGAN(V.O.):
    "Why does this always make me feel better? What was I doing? Oh, right. I have to go talk to dad."

    Rob "-F YOU AREN’T GOING TO LISTEN TO ME THEN GO TALK TO-"

    #[Hastened footsteps echo off the floor]

    Morgan "Gonna talk to dad, I'll be right back!"

    #[Swinging door]
    #:FADE OUT

    #2
    scene bg kitchen
    #MORGAN(V.O.):
    "Julie and Rob seem to think that I don’t like them, but really I can’t say I give them good reason to think that."

    #MORGAN(V.O.): 
    "Rob is a stern, to-the-point older guy with a lot of life experience. I couldn’t ask for a better host. The guy even taught me how to tie my tie when I started working here."

    #MORGAN(V.O.):
    "And Julie? I mean she IS my little sister. Even though she’s a little gremlin I still love her."

    #MORGAN(V.O.):
    "I remember when we were growing up she would always make me cook for her because she was so afraid of burning herself."

    #MORGAN(V.O.):
    "She always has been afraid of fire. She won’t even come into the kitchen when I’m cooking." 

    #MORGAN(V.O.):
    "Then she went and started cooking for herself. “I’m an adult, I can do it myself!”... yeah, sure thing Iron Chef Julie." 

    #MORGAN(V.O.):
    "...I just hope they both know how much they mean to me."
 
    Dad "Heya peaches, about time you got out here. I was beginning to think you finally got the courage to run off with one of the customers and make me a grandfather."

    Morgan "You know I hate it when you call me that."

    Morgan "And, if I ever DID manage to talk to a cute customer here, Julie would just scare them away."

    Dad "Sure. Julie. She’d be the problem. Ha! Anyway, I didn’t call you out here just to beat a dead horse."

    #MORGAN(V.O.):
    "God I hope not, he knows I’ve never had a girlfriend. I mean, how do I even begin to talk to a gir-"

    Dad "Hey, focus. It’s almost Fall. Have you given what your mother and I talked to you about any thought?"

    Morgan "..."

    Dad "It’s about time you went to college. You’ve been out of highschool for three years now, and your mother and I can’t keep taking care of you forever."

    Morgan "I know that, but..."

    #Do I want to go back to school this Fall? (Α-FLAG)
    #Δ1: YES
    #Δ2: NO


    #Δ1: A-FLAG POSITIVE
    #Δ2: A-FLAG NEGATIVE
    Morgan "...You know what, fine. I guess I can’t keep working in this place forever anyways."

    Dad "Good to hear! You're finally taking your future into your own hands. You need to set a good example for Julie."

    Dad "Oh, and about the rent, I almost forgot to tell you--"

    Morgan "But why can’t you guys just hire me as a full time cook here? I already know all of your recipes."

    Dad "That’s not going to happen, Morgan. You are a man and it’s about time stood on your own two feet. You ARE going to start college this fall."

    Dad "And about rent--"

    #[Swinging door, JULIE enters frame]

    Julie "Morgan, we need you back inside, we have a customer asking for you."

    Dad "Go on, we will finish talking after we close."

    #MORGAN(V.O.):
    "Why would a customer want to talk to me, I just cook here…"

    #[Footsteps, swinging door]
    #:FADE OUT

    #3 NIKOLAUS INTRO
label sausage_intro:


    Julie "Hey, there’s this weird guy out there asking for a meatball menu? What should I tell him?"

    Morgan "That we don’t have one, this is a family style restaurant."

    Julie "Well, he did say something about pickled herring?"

    Morgan "Tell him this is a good family restaurant."

    Julie "Ok, well the guy’s a bit excitable and I don’t-"

    #[door slams open]
    
    show sausage day at center

    Nick "I DEMAND TO SEE THE CHEF."

    Morgan "I think he’s out back on a smoke break, big metal door, can’t miss it."

    Nick "Thank you sir."

    Julie "We have a back door?"

    Morgan "There’s a door-"

    Nick "WHY IS THIS ROOM SO COLD?!?"

    Morgan  "-it’s to the refrigerator. But it is a door and it is in the back."

    Nick "What is meaning of this!"

    Morgan "Kinda. I mean, the other guy is handling smoked fish back there. I’ve done worse."

    Nick "He said you were the chef!"

    Morgan "I am, so is he. We are both the chef, chefs. Sometimes there is more than one person that can satisfy the role. For example, Julie is not the only pain in my ass today."

    Nick "Why is there no authentic German cuisine on your menu!"

    Morgan "Because this is primarily an american family style restaurant."
    
    Nick "Then why not have authentic German-"

    Morgan "Because this is a good family style restaurant."

    Nick "You didn’t even let me finish!"

    Morgan "Because it was going to be awful."

    Nick "HOW DARE YOU INSULT MY PROUD AND MAGNIFICENT CULTURE!?! YOU BACKWARDS AMERICANS THINK YOU KNOW EVERYTHING DON’T YOU!?!"

    #MORGAN (V.O.): 
    "Why are we arguing about this, why can’t this guy just get that we don’t do German food it's not that hard to understand."

    Morgan "I think I know how to make good food without grinding it into a flavourless paste. Or do you think I have something already pickled, we don’t!"

    Nick "Meatballs are not flavourless and not paste, they are a moist and bouncy! Also you can buy it can-"

    Morgan "This is a GOOD family restaurant!"

    #MORGAN (V.O.):
    "Now he got me yelling. why is he still here, we don’t have what he fucking wants! I don’t want to deal with this right now."

    #MORGAN (V.O.):
    "I don’t know why this has to happen right after that stuff with dad, is this some kind of test." 

    Nick "All the more reason to have it!"

    Morgan "No it's not meathead."

    #Morgan (V.O.)
    "He is a meathead, a stubborn meathead!"
    
    hide sausage day

    #[pops into sausage sprite]

    #MORGAN (V.O.)
    "Ha... Yeah."

    #MORGAN (V.O.)
    "I should stop doing this, but it’s easier than dealing with this fucking meathead!"

    Rob "What the hell is going on now?"

    Morgan "Oh Rob, this poor German youth is ranting about his struggle with the concept of decent seafood to me. Sounds like a best seller. Revolutionary even. At least for the German people."

    Nick "Sir, this “chef” is insulting the proud traditional cooking of my great people, and I will not stand for it!"

    Rob "Julie?"

    Julie "The german one’s crazy and Morgan is being an asshole."

    Rob "Typical. Morgan I don’t know how better to say this, JUST MAKE DAMN THE FOOD!"

    #MORGAN (V.O.):
    "I don’t want Rob to start yelling again. It always gets easier to get him going after he’s started."

    Morgan "Fine, Fine I’ll make the paste-food!"

    #[INSERT FUCKING COOKING GAME]
label cook1_start:
    menu:
        "Beef Schnitzel":
            jump cook1_food_1
        "Chicken Fried Steak":
            jump cook1_food_2
        "Notes":
            jump cook1_notes
            
label cook1_food_1:
    "Beef Schnitzel- A German dish. I should be able to make this with the beef and breading we have, I'll just have to tenderize it first."
    menu:
        "Prepare this?":
            jump cook1_good
        "Back to recipie list":
            jump cook1_start

label cook1_food_2:
    "Chicken Fried Steak- A pretty normal dish on the menu, popular for lunch."
    menu:
        "Prepare this?":
            jump cook1_bad
        "Back to recipie list":
            jump cook1_start

label cook1_notes:
    menu:
        "The Meathead":
            jump cook1_note_1
        "Recipie List":
            jump cook1_start
    
label cook1_note_1:
    "This guy seems to like German food. I should probably make him something German"
    jump cook1_notes



label cook1_good:
    Nick "OH MY THIS IS WUNDERBAR!" 
    jump cook1_done

label cook1_bad:
    Nick "OH MY, I see what you mean, well maybe we have something back home you don’t have in your kitchen!"

label cook1_done:
    #MORGAN (V.O.):
    "I think I’ll just gonna be going now jobs done."

    Nick "Wait where are you going chef? I haven’t properly thanked you!"

    Morgan "No that’s fine just doing my job re-."

    #*HUG*

    #MORGAN (V.O.):
    "Grip tight. Oxygen. Need oxygen."

    Morgan "Can't... breathe..."

    Nick "Oh! Well i’m very sorry sometimes I don’t realize my own strength but I am very grateful that you went out of your way to make specialty meal for me!" 
    #[sparkles if we have them]

    #[nick sprite]
    show sausage day at center

    Morgan "Yeah meathead it was no problem, my boss was gonna get angry at me and I would really enjoy working here, but that might end soon I don’t know."
    
    #4
    scene bg app
    Morgan "Ugh!"
    
    show sausage day at center

    Nick "I am very sorry, is there any way I could help?"

    Morgan "I don’t know, do you have an apartment that doesn’t cost an arm and a leg?"

    Nick "Well, yes. Yes I do. I’ve been looking for a roommate, but everyone keeps turning me down. It’s for an apartment designated for international students, so it’s actually rather inexpensive."

    Morgan "That was rhetorical. I mean, I appreciate it, but I don’t think it will be enough."

    Nick "Also you can work somewhere else? You sure seem to be a very good cook. The first two plates I had were delicious, though I would have preferred some more proud traditional-"

    Morgan "You ate two plates? You ate two whole plates of food and then came into the back complain to both chefs about the menu?"

    Nick "Food was very good. A bit light for my tastes, but very good!"

    Morgan "Well, that’s not enough I guess. I’m too ignorant of cooking terms, at least that’s what my mom told me she’s going to throw her own child out to fend for himself."

    Nick "What kind of mother would do such a thing?"

    Morgan "Exactly what I’ve been thinking! And all because I don’t know what a spatula is!"

    Nick "Spatula?"

    Morgan "Exactly! Who knows what a spatula is!"

    Nick "No, I’m sorry, I think you misunderstand, I was surprised you did not know. It is a very simple thing."

    Morgan "Oh. Well, the short of it is that in a few weeks I’ll be out of my house and might be out of a job to start college."
    
    Nick "OH is that what it is, you can probably do both! And move in with me! University has many courses of study. I think there is a cooking school. You could learn what a spatula is, or other things too!"

    Morgan "You know, that sounds like a plan. What’s your name?"

    Nick "Nikolas. And you?"

    Morgan "Morgan. I think this may be a great opportunity for me. I’m not much of a school guy, but maybe this could work out. My dad always talked about how much he enjoyed cooking school." 

    Nick "Your father also cooks?"

    Morgan "Yeah."

    Nick "Hmm, so he must know what a spatula is then. Your mother has not kicked him out yet."

    Morgan "Yeah totally... *cough*"

    #5 ARIA INTRO? Also new job
label lasagna_intro_1:
    scene bg kitchen
    #MORGAN (V.O.): 
    "Well, today could have gone better. Definitely better, this is just so many dishes how do we have so many dishes!"

    #Δ1: Being put on dishwasher duty kinda sucks but only working so many hours will leave time for class work. At least, that’s what dad has been telling me. Didn’t think he ever had to start as a dishwasher, he’s such a good cook.

    #Δ2: Ugh this is so fucking stupid. There is no way that Dad was a dishwasher, ever. Bullshit. Now I’m stuck getting all gross and pruney hands. 


    Julie "Morgan, stop daydreaming and hurry up with those dishes already, you’re getting behind."

    Morgan "Hey, I just got most of these alright."

    Julie "Well I’ve got two big reservations leaving soon so after you get all of their dishes done I’m going to need your help moving tables around for Karaoke night."

    Morgan "Fine."

    #MORGAN (V.O.): 
    "Work... is work I guess. I just don’t feel like it’s worth the effort really. But I need the money. Even if I have to be put to work part time as a dishwasher."

    #MORGAN (V.O.)
    "And I’m gonna have to move again, ugh. I moving is always the worst, you leave all memories and everything familiar, but I just can’t stay, so yeah..."

    #[ding noise]

    "...the dishes are done. Well, I guess I should get to moving those tables around."

    #[transition to muffled voices, maybe some pop-y sounding music in the background]

    Morgan "Ok got the tables moved for you, I’ll be back to" 
    
    show lasagna work at center

    Aria "-Maked room wif me is to soon to saw if I’m glad im herre-"

    Morgan "Huh, the crazies are out in full force tonight huh?"

    Julie "Oh her? She’s just some dumb college student. She works across the street and comes here after her shift ends gets hammered and sings on Karaoke nights."

    Julie "Alone." 

    Julie "Kinda sad really."

    Aria "-CAUSE YOU AX FUR IT CaUSE you need SOME!-"

    Morgan "She’s not that bad. I mean, I’ve heard worse tonight."

    Julie "You just think she’s hot don’t you?"

    Morgan "Well, I can barely see her."

    Julie "She can barely put a sentence together and you think that she’s singing well?"

    Morgan "Putting a sentence together isn’t the only point of singing, sometimes you’re just trying to express a feeling or something."

    Julie "The feeling of intense queeziness brought about by one too many cocktails? Or five too many. I better get a good tip from her."

    Morgan "Well, there are other feelings there too. I just can’t put my finger on them."

    Julie "I think you’re just trying to start a fight for no reason again."

    Morgan "I think you’re getting too good at this. Alright, I’m taking off. Have fun with the rest of tonight’s drunks."

    Julie "I’ll try. No guarantees but I’ll certainly try."

    #6 DIANA INTRO
label tiramisu_intro:
    scene bg kitchen
    #[Restaurant lobby]


    #[Footsteps, restaurant murmur audio]

    Julie "Table seven’s asking for you Morgan."

    Morgan "What does she want?"

    Julie "I don’t know, but she does come in pretty regularly."

    Rob "Yeah I always try to put in a little extra for her but she never leaves very high tips. I don’t know if she’s just stingy with her money or what?"

    Julie "Whatever, just go!"

    #[JULIE sprite fade out, fade in DIANA sprite]
    
    show tiramisu day at center

    #MORGAN(V.O.):
    "Oh my god. Why is she- why is this happening."

    #MORGAN(V.O.):
    "There’s a cute girl calling me over to her table?"

    Morgan "Hello, I am Morgan, I was told that you wanted to see me?"

    Diana "Yeah. Although I can’t say I’m very impressed. When I asked to see the cook I expected a more  well-groomed adult."

    #MORGAN(V.O.):
    "So... Did I fuck up? That was faster than I thought it would take."

    Diana "Oh well, it’s not like you can embarrass yourself all the way back in the kitchen. I’m looking for a new personal cook, come work for me."

    #MORGAN(V.O.):
    "My heart feels like it’s about to burst out of my chest, she has such pretty--"

    #MORGAN(V.O.):
    "Wait, she wants me to come work for her? I can’t do that, that would mean I would have to (A-:leave this place.) (A+:put off school.)"

    Morgan "I... I’m sorry but I can’t do that."

    Diana "There are- wait, are you for real?"

    Diana "I just can’t believe that you’d rather keep your part time job over- you know what how much to get you out of this place is so beneath your skill?"

    Morgan "Oh no, I get paid plenty here. I mean not enough to pay rent but it’s all covered everything, it’s fine, I don’t need extra money."

    Diana "You can’t... make... rent?"

    #MORGAN(V.O ):
    "Don’tyelldon’tyelldon’t-"

    Diana "How could some one with the kind of talent that you have not be able to pay for your living?"

    #MORGAN (V.O.): 
    "Is she flirting with me???"

    Diana "I have come here a number of times and food always have a surprising elegance to it on certain days, and those must be days that you are the one in front of the stove."

    #MORGAN (V.O.)
    "She is, what do I do, I DON’T KNOOOW!"

    Diana "There is so much more that you can do with a much better facility. And I want that and am willing to pa-"

    #MORGAN (V.O.):
    "Idon’tknowidon’tknowidon’tknow"

    #MORGAN (V.O.):
    "I guess i could just"

    #[pop in food sprite of tiramisu]

    hide tiramisu day

    #MORGAN (V.O.):
    "That’s better I guess. It’s just so luxurious on the palette. A garnish is common but the topping works all on its own."

    Morgan "Hey, Speaking of food, have you made your order yet?"

    Diana "Wha- Now that you mentioned it I have not. I would like the-"

    Morgan "I think I can whip up something for you. Be right back!"

    #[INSERT FUCKING MINI GAME] I don't think one is going to work here.


    #Good
    
    show tiramisu day at center
    
    Diana "Oh my, such elegance you have here. Simple but refined."

    Morgan "Thanks, I hope everything is to you liking."

    Diana "MMMMM you have really outdone yourself."

    #MORGAN (V.O.):
    "Now to slip away and hope to not have to deal with-"

    Diana "What were did that chef go?"

    Rob "I think he left for the night."

    Diana "I wasn’t even able to pay him for the delicious meal."

    Rob "Oh don’t worry about it miss, I’ll cover the meal. I mean you didn’t actually even order it."

    Diana "That is not what I- Thank you. I’ll just be leaving then." 


    #Bad
    Morgan "Well this is what I could whip up for you."
    
    show tiramisu day at center
    
    Diana "This is not what I was expecting... This is the best that this establishment has to offer?"

    Morgan "Yes. At least to my knowledge."

    Diana "I would like to talk to you manager."

    Morgan "I don’t think dad’s in but I can grab Rob for you?"

    Diana "That will be fine."

    #MORGAN (V.O.)
    "Uh this doesn’t seem like it will end well."

    Rob "Yes ma’am is something wrong?"

    Diana "Yes there is, you are clearly not well equipped enough to make a fine meal."

    Rob "Are you saying the food is bad?!"

    Diana "I’m saying what you have in stock does not hold up. If you want I would be more than willing to help you get in touch with someone that can facilitate your chef, or maybe I can now convince him on coming to wor-"

    Diana "Where did he go?"

    Rob "I think he took off for the night."

    Diana "well charge my card and let me be on my way."



    #7 HOME
    #[Door closing sound, no music]
    scene bg app
    #[Paper rustling]

    #MORGAN (V.O.): 
    "That was an event, oh now what another notice? I’m not that far behind on rent... Eh, I’ll try going down and talk with him tomorrow. I’m sure I’ll be able to work something out with him. Just gotta pull a bit out of my savings is all."

    #[Heavy Knocking at door]

    Dave "Hello?"

    #[MC opens door]


    Morgan "...Hey?"

    Dave "Hey! My girlfriend and I just moved on! Thought I’d go around and say hello to the neighbors."

    Morgan "...Well, I guess I’m one of them."

    Dave "Uh, yeah... Name’s Dave, pleased to meet ya!"

    Morgan "Morgan..."

    Dave "Cool. So we’re from out of town and were wondering if you knew any places that are fun to hang out or eat around here. Thought it’d be fun to have a party!"

    Morgan "Uh, no. I don’t go out much."

    Dave "Oh. Uh, well, one of the other neighbors offered to take us to a place. You wanna join?"

    Morgan "Nah. I’ve got... plans for the rest of the night."

    Dave "Oh..."

    Dave "So, what do you do for a living?"

    Morgan "Cook, wash dishes."

    Dave "Interesting, you must have some crazy stories about customers."

    Morgan "Not really."

    Dave "Uh-huh..."

    Dave "Well I’m a mechanic, work on cars. Last week, we had this ‘67 Impala come through the shop. Man, I’d give a leg to drive that, though I probably wouldn’t be able to without the leg haha."

    Morgan "I’m not really into cars."

    Woman "Honey, who are you talking to?"

    Dave "This is Morgan. He’s out new neighbor, he’s a cook."

    Morgan "Yep... well I guess i’ll see you two later, bye."

    Dave "Goodnight Morgan, see you around man!"

    #MORGAN (V.O.): 
    "They seem nice. I think that’s the problem with communal living, really. It’s not like I really have anything to do, but doing nothing is better than being around strangers. I guess I should get to bed, tomorrow is my tour for college."

    #9 ARIA CONTINUED
label lasagna_intro_2:
    scene bg cafe
    #[coffee shop sounds]
    
    show lasagna work at center

    Aria "What’s your order?"

    Morgan "A large mocha and a muffin."

    Aria "Great, your order will be right out."

    Morgan "Thanks."
    
    hide lasagna work

    #MORGAN (V.O): 
    "I’m glad I’ve got somewhere I can go for a bit of peace and quiet. Sometimes it’s nice to have a some time to myself. Take a break from all the crazy I’ve been dealing with lately."

    "Gotta give myself a little breather before I have to head off to the campus, this coffee shop is tucked away enough that it doesn’t get too many customers."

    "Taking my breaks from work and school here will be some of the best parts of my day. Taking my breaks from Nick here will be some of the best parts of my week."

    show sausage day at center

    Nick "Hello friend! Are you getting lunch?"

    Morgan "..."

    Nick "If you had listened to my advice you would not be having this problem."

    Morgan "..."

    Nick "The advice of my grandmother is flawless see, never leave the house without your lunch."

    Morgan "What are you doing here?"

    Nick "Oh, the little sister called. She needed help moving things. She asked for you, but I am a strapping young gentleman and thought I could do heavy moving."

    Morgan "So you’re here because you were helping out my lazy sister at work across the street. Great."

    Nick "Do not insult your sister. She is a good beautiful girl."

    Morgan "Meat. Were you, hitting, on my SISTER?"

    Nick "I would never harm such a delicate flower."

    Morgan "OH IT IS ON NOW YOU YODELING SACK OF SH-"
    
    show sausage day at right
    show lasagna work at left

    Aria "HEY, YOU TWO, PIPE DOWN!"

    Morgan "Uh... dude’s trying to bang my sister..."

    Nick "I have no violent intentions!"

    Aria "I will throw you two out! This is not some kind of boxing ring, this is a coffee shop. Now you two calm down or take it outside, do I make myself clear?"

    Nick "Yes, I am very calm. Always calm."

    #MORGAN (V.O.)
    "It’s my fault I over reacted. It's just this meathead is being a creep, on my little sister!"

    "And now I’m disrupting her work, even though there is like no one here to really disrupt." 

    "I don’t know what to do.."



    Morgan "I... I..."

    #[lasagna sprite]
    hide lasagna work

    Morgan "I guess I’m sorry. I didn’t mean to cause an issue. Sorry for yelling. We’ll be going once my order’s out."

    Aria "Ok. You can stay if you want, just don’t both the other guests anymore than you have."

    #MORGAN (V.O.): 
    "But, there is no one else here..."

    Morgan "Will do ma’am."

    Nick "We will do no bothering sing lady."

    Morgan "Sing lady?"

    Nick "You do not recognize sing lady?"

    Morgan "Recognize what?"

    Nick "She is at your place of work all the time. She is sing lady. You must at least remember her voice."

    Morgan "Well I hear her voice all the time, she works here and I come here all the time. Though, come to think of it... are you the girl who was singing karaoke across the street last night?"

    Aria "..."

    Aria "Listen here you-  How do you two know about that?"

    #MORGAN (V.O.):
    "Should I not of said anything. Fuck, I totally shouldn’t of said anything. She is pissed."


    Morgan "Well, uh I work there and he... eats there a lot, he also just eats a lot in general. Why whats wrong?"

    Nick "I miss you sometimes sing lady."

    Morgan "We’re over there a lot. Is what we’re trying to say."

    Aria "Ok, but you cannot tell anybody here about it. Or just anyone in general, got it."

    Morgan "I can certainly do that. And nobody will be able to make heads or tails of whatever Arnie is saying anyway."

    Nick "I have told you many times he is not a proud Ger-"

    Morgan "Whatever. Your secret is safe with us."

    Aria "Good. Now take your order and go."

    Morgan "But I thought you said we could stay?"

    Aria "GET OUT!"

    #MORGAN (V.O.)
    "How did I still manage to fuck it up with saucy girl, uh now I have to get to campus and hope that she isn’t going to be mad at me if I come back I really like it there."

    #9 INTRO ALEXANDRA
label tso_intro:
    scene bg school
    Guide "...on your left you’ll see the Student Union. You can get yourself something to eat there, get a new student ID..."

    #MORGAN (V.O.): 
    "I can’t believe that girl. Try to be nice and you get the door? Why are my soft hands made for delicate practices being used on such things like washing gross dishes? Well, at least I’m still working there."

    "I wish the other staff wasn’t so rude to me though. It’s not my fault I don’t know what anything is! Ok, I guess it is kind of my fault, but they don’t have to be so mean about it."

    "Who am I kidding, if I were in their position I’d be making jokes too. At least everyone is friendly enough. Not Nick levels of friendly, but nobody else is also that crazy. Sometimes I wonder about that guy..."

    "Wait... where am I? I think I lost my group. Er, everybody else was in cooking together too, right? This was a tour for cooking students... I think... But that probably wouldn’t explain the high schoolers... Maybe I shou-"

    #Wham

    Morgan "AH!"

    Jogstudent "Oh, sorry, didn’t mean to run into you, you just kinda jumped out there."

    Morgan "Yeah, sorry, I guess I should have paid better attention, uh do you know where the cooking classes are held?"

    Jogstudent "Well, class rooms can be anywhere, but I think most of their classes are in that building over there."

    Morgan "Thanks!"

    #[transition to inside class]

    #MORGAN (V.O.): 
    "So this is what culinary school is going to look like. Man, these guys have everything."

    #[LATER]
    
    show tso prez at center

    Alexandra "Hello? Are you by chance with the tour?"

    #MORGAN (V.O.): 
    "Oh, this must be one of the high schoolers with the tour. They have some pretty neat uniforms. Most private schools around here are cheap and just have you dress up, they hardly even care what color."

    Morgan "Yeah, I just got a bit lost. But I found my way here after all, so it’s all good. This place is great. I mean, look at all this stuff they got. I don’t know if I’ve seen cooking equipment this good in my life."

    Morgan "You know, my dad always says, a good kitchen is like a good woman, fully equipped with at least seven ovens."

    Alexandra "I’m not sure if I want to know what he meant by that..."

    Morgan "Neither do I honestly, but he says it all the time. I think it’s some kind of to be a joke about my mom. She always gives him this glares when he says it. Then again, she always glares at him. Between that and the cat story I guess she has a point."

    Alexandra "What did your father do to a cat?"

    Morgan "It wasn’t so much to a cat as it was around a cat. A lot of cats. And I don’t think he actually did anything. It’s probably a lie, or an extreme over exaggeration... At least I really hope it is."
    
    Morgan "But anyway, have you even seen a mixer this big? You could probably mix, like, a person in that thing! Shoot, maybe two people."

    Morgan "Ha, mixing two people, that’s kinda dirty. Though I guess that mixing up any number of people would be dirty now that I think about it. Or anything." 

    Alexandra "Uhuh. Haha."

    Morgan "Mixers really are messy devices, no matter what you mix. It’s in their nature. Still, I think I love this room. And to think, there’s probably a dozen more of them. Filled to the brim with flippers, floppers, and so many knives. Well, hopefully there are knives."
            
    Morgan "I mean, I know it’s school so I would understand if they laid off the knives, but that would be a disappointment. Knives are important, for any kitchen."

    Alexandra "Well, if you’re done ranting about dirty mixers and knives, I think we should get back to the tour."

    Morgan "What, isn’t this where the tour was supposed to be going?"

    Alexandra "No. The tour doesn’t actually go to this building at all. We don’t get too many culinary students here."

    Morgan "Oh, so you got lost too then? Man, your teacher must be looking everywhere for you little guy."

    Alexandra "What? I’m here to look for you. I’m Alexandra, and I’m the one in charge of the tour."
    
    Alexandra "I understand that you got a little lost, but we need to get back to the tour. I’ve got a meeting after this with leadership and I’m not really sure how they’d react if I was late to my first meeting as president."

    #MORGAN (V.O.): 
    "President... Alexandra... oh, oh no!"

    #[tso sprite]
    hide tso prez

    "This is not good. This is definitely not good. They’re going to kill me. This is gonna end up in the school paper. Certainly. And at a school like this, who wouldn’t read it? I’m going to lose everything for misgendering the student body president. My life is over."

    Alexandra "Hello?"

    #MORGAN (V.O.): 
    "No, wait, I just need to apologize somehow. Think, think, I need to come up with something. I could make her food. No, no time."
    "Maybe a novelty gift? One that says, “I’m sorry I thought you were a fourteen year-old boy, but that’s in the past.” Like a puppy. No, that is not what puppies say. Maybe there’s something in the language of flowers for this..."

    Alexandra "Are you ok, my dude?"

    Morgan "That’s it, flowers! That’s what dad always gets mom when he screws up, it sometimes works."
    
    Morgan "Now, which would even work?... carnations? Tulips? Roses? Man, dad has had to buy so many flowers I can’t remember... I can’t think... I can’t-"

    Alexandra "Is there something wrong?"

    Morgan "GAH, WHY ARE FLOWERS SO DAMN COMPLICATED!"

    Alexandra "I- Do you need a moment? If you do it’s no problem really."

    Morgan "...no, no. Let’s just forget that this ever happened."

    Alexandra "Good, because we really should be going."

    #END OF DEMO BOIS



    # This ends the game.

    return
