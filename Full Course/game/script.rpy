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

# Declare background images
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

image female = "silhouette female.png"
image male = "silhouette male.png"

#Declare sprite positions
transform left:
        xalign 0
        yalign .05        
transform center:
        xalign .5
        yalign .05
transform right:
        xalign 1.0
        yalign .05

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
# ################################################

    #1 INTRODUCTION START
label intro:
    scene bg kitchen 
    #bg Kitchen
    

    #Morgan(V.O.): 
    "All my life I’ve been told that the fastest way to a person’s heart is through their stomach."
    
    #Morgan(V.O.):
    "I find those cliche’ sayings stupid. But my dad has always lived by that cheesy old saying and I’ve never met a person more popular than him."
    
    #Morgan(V.O.):
    "His restaurant is always packed with people smiling, laughing, and eating. They’re even paying for it."
    
    #Morgan(V.O.):
    "The food is famous, but it’s his personality that keeps people coming back again and again. He’s always welcoming and knows everyone by name."
    
    #Morgan(V.O.):
    "To him people are worth opening up and bearing your emotions to. He’s kind of an idiot I guess."
    
    #Morgan(V.O.):
    "..."
    
    #Morgan(V.O.):
    "I’d give anything to see people the way he does."
    
    #[Kitchen sounds and muffled crowd noises in the background]
    #[fade in]
    
    #Morgan(V.O.):
    "For as long as I could remember I’ve felt more at home in a kitchen than anywhere else. I can do what I love without worrying so much."
    
    #Morgan(V.O.):
    "This kitchen is a lot of white walls and chrome appliances for the most part. Though there is some older more plastic ones that Dad has never been able to part with."
    
    #Morgan (V.O.)
    "It might be a little old and worn down but it has its charms about it. Like How all the stoves and ovens work, but it takes a little longer for the second oven to get up to temperature."
    
    #Morgan (V.O.):
    "We got everything you’d need to to make pretty much anything! Flippers, Flappers, Wirewands, Noodlegrabbers, Bowlsticks, Wirlymagigs, Potatoflays, Tinybidents, and so many other different utensils."
    
    #Morgan (V.O.):
    "With these specialty tools being at a chefs disposal and proper know-how they can make all kinds of wonderful foods!"
    
    #Morgan (V.O.):
    "Between the sizzling of stove tops, banging of kitchen ware, orders coming in, and all the people about, everyone has to talk louder."
    
    #Morgan (V.O.):
    "This does mean that if things get heated even the slightest someone is bound to start yelling, and I really hate it."
    
    #Morgan (V.O.):
    "However, it’s really important to be able communicate well, that way we get every order for each of the guests correct!"
    
    Morgan "OOORDER UP!"
    
    show female at center
    
    Julie "You do know we have a bell for a reason, right?"
    
    #Morgan(V.O.):
    "Julie, my two faced little sister. I wonder if she hears half the shit that comes out of her mouth."
    
    Morgan "Yeah, I know. We ring it when you get too far from home. We wouldn’t want anyone to snatch you up and take you off to the pound."
    
    Julie "Ha. Ha. I’m a dog? Your the one with breath so bad he can’t get a girlfriend."
    
    #Morgan (V.O.):
    "My breath doesn’t smell. *sniff sniff*"
    
    Morgan "Why are you back here anyway, isn’t there some pervy old man you should be chatting up for tips?"
    
    Julie "Whatever, just stop sitting there with that stupid look on your face. I came to tell you that Dad needs to talk with you. He’s out on his break right now."
    
    Julie "Have Rob take over for you, he’s a better cook than you anyway."
    
    Morgan "You know, It’s almost impossible to identify a body after its been charred to the bone."
    
    show female at left
    show male at right
    
    Rob "Quit bickering, if a customer overhears, it would look highly unprofessional."
    
    #Mogan (V.O.):
    "Rob, the restaurant’s host. He is a hard working, honest guy. Too bad there isn’t a doctor that could do something about that stick up his ass."
    
    Morgan "Julie, see you’re finally bugging Rob to the point where he’s actually going to try to kill himself in my kitchen."
    
    Rob "What! Huh, no!"
    
    Rob "AND I DON’T WANT TO KILL MYSELF, YOU DISRESPECTFUL LITTLE PIECE OF--"
    
    #Morgan(V.O.):
    "...i fucking hate it when people start yelling..."
    
    Rob "--AND FURTHERMORE, YOU’RE ALWAYS SITTING THERE WITH THIS SMUG AS F--"
    
    #Morgan(V.O.):
    "...i just shouldn’t have come to work today, i don’t have to listen to this… i can’t..."
    
    Rob "--JUST BECAUSE YOUR PARENTS OWN THE PLACE DOESN’T MEAN YOU CAN GO AROUND SAYING WHATEVER YOU--"
    
    #Morgan(V.O.):
    "...i can’t... it’s just so loud… i can’t just leave, if i leave he’ll just yell more…"
    
    Rob "-WHY ARE YOU JUST STARING, SAY SOME-"
    
    #Morgan(V.O.):
    "...my arms feel like they’re noodles. why is it my chest feels like a pressure cooker. i just want to leave..."
    
    Rob "-ARE YOU EVEN LISTE-"
    
    #Morgan(V.O.):
    "...i just..."
    
    Rob "--JULIE, GET BACK TO THE FRONT ALREADY, THERE ARE CUSTOMERS WAITING!--"
    
    #Morgan(V.O.):
    "...leave"
    
    Julie "Quit yelling, the customers will hear you! What was that about being professio--"
    
    #Morgan(V.O.):
    "i just want to leave."
    
    #Morgan(V.O.):
    "let me leave"
    
    #Morgan(V.O.):
    "letmeleaveletmeleaveLETMELEAVELETMELEA-"
    
    #[ROB turns into food sprite, with playful pop sound]
    
    #Morgan(V.O.):
    "Why does this always make me feel better? What was I doing? Oh, right. I have to go talk to dad."
    
    Rob "-F YOU AREN’T GOING TO LISTEN TO ME THEN GO TALK TO-"
    
    #[Hastened footsteps echo off the floor]
    
    Morgan "OK I’ll go talk to him, then I’ll get on the next order when I get back!"
#SCENE 2
##################################################

label intro:

scene bg kitchen

"Julie and Rob seem to think that I don’t like them, but really I can’t say I give them good reason to think that."

"Rob can be stern, to-the-point, and yell a lot, but he has a lot of life experience. I couldn’t ask for a better host. The guy even taught me how to tie my tie when I started working here."
    
"And Julie? I mean she IS my little sister. Even though she’s a little gremlin, I still love her. That’s kind of how siblings work."
    
"I remember when we were growing up she would always make me cook for her because she was so afraid of burning herself."
    
"After a while she was like, “I’m an adult, I can do it myself!”... Yeah, sure thing Iron Chef Julie."
    
"... I just hope they both know how much they mean to me."
    
show male at center
    
Dad "Heya Peaches, about time you got out here. I was beginning to think you finally got the courage to start flirting with a customer on the way out."
    
"My Dad. He’s a big man with basically the manliest beard I’ve ever seen. He wears a standard polo shirt that all the cooks wear, but all the time."
    
"He also always has one of those stereotypical chefs hats on. He got it back  when he first became a chef, so like when he was born."
    
Morgan "You know I hate it when you call me that."
    
Morgan "And, if I ever DID manage to talk to a cute customer here, Julie would just scare them away."
    
Dad "Sure. Julie. She’d be the problem. Ha! Anyway, I didn’t call you out here just to beat a dead horse."
    
"God I hope not, he knows I’ve never had a girlfriend. I mean, how do I even begin to talk to a gir-"
    
Dad "Hey, focus. It’s almost Fall. Have you given what your mother and I talked with you about any thought?"
    
Morgan "..."
    
Dad "It’s about time you went to college. You’ve been out of highschool, for how long now, three years? And as much as we love you your mother and I can’t keep paying for you forever."
    
Dad "And, you really should take some time to actually learn the fundamentals of cooking."
    
Morgan "I know that, but..."
    
##Δ Flag Choice##
    
menu:
    "Do I want to go back to school this Fall?"
        
    "Yes":
        #schoolFlag = true
        jump school_yes
    "No":
        #schoolFlag = false
        jump school_no
            
label school_yes:
    Morgan "... You know what, fine. I guess I can’t keep working in this place forever anyways."
        
    Dad "Good to hear! You're finally taking your future into your own hands. You need to set a good example for Julie."
        
    Dad "Oh, and about the rent, I almost forgot to tell you--"
        
    jump school_done
        
label school_no:
    Morgan "But why can’t you guys just hire me as a full time cook here? I already know all of your recipes."
        
    Dad "That’s not going to happen, Morgan. It’s about time you stood on your own two feet. You ARE going to start college this fall."
        
    Dad "And about rent--"
        
    jump school_done

        
label school_done:
    #[Swinging Door Sounds]
    show male at left
    show female at right
        
    Julie "Morgan, we need you back inside, we have a customer asking for you."
        
    Dad "Go on, we will talk about this later."
        
    "Why would a customer want to talk to me? I just cook here…"
        
    #[Footsteps and Swinging Door sounds]
        
            #3 NIKOLAUS INTRO
label sausage_intro:
    scene bg kitchen 

    show Female at center
    
    Julie "Hey, there’s this weird guy out there asking for a meatball menu? What should I tell him?"
    
    Morgan "That we don’t have one, this is a family style restaurant."
    
    Julie "Well, he did say something about pickled herring?"
    
    Morgan "Tell him this is a good family restaurant."
    
    Julie "Ok, well the guy’s a bit excitable and I don’t-"
    
    #[door slams open]
    
    #[Nick sprite left, Female sprite right]
    
    Nick "I DEMAND TO SEE THE CHEF!" #[angry]
    
    #Morgan (V.O):
    "Who does this man made mostly of fucking thick ass steaks with a fluffy yellow poof for hair want, well whatever it is I sure as hell don’t want to deal with it."
    
    #Morgan (V.O.):
    "And why does he have to have a shirt so tight it shows off all of his- nevermind!"
    
    Morgan "I think he’s out back on a smoke break, big metal door, can’t miss it."
    
    Nick "Thank you sir." #[neutral]
    
    #[Nick sprite hide, Female center]
    
    Julie "We have a back door?"
    
    Morgan "There’s a door-"
    
    Nick "WHY IS THIS ROOM SO COLD?!?" #[angry]
 
    Morgan "-it’s to the refrigerator. But it is a door and it is in the back."
    
    #[Nick sprite left, Female sprite right]

    Nick "What is meaning of this! I just want to talk to the chef here!" #[angry]
    
    Morgan "Well the other guy is handling smoked fish back there. I’ve done worse."
    
    Nick "He said you were the chef!" #[angry]
    
    Morgan "I am, so is he. We are both the chef, chefs. Sometimes there is more than one person that can satisfy the role."
    
    Morgan "For example, Julie is not the only person getting on my nerves today."
    
    Nick "Why is there no authentic German cuisine on your menu!" #[angry]
    
    Morgan "Because this is primarily an american family style restaurant."
    
    Nick "Then why not have authentic German-" #[neutral]
    
    Morgan "Because this is a good family style restaurant."
    
    Nick "You didn’t even let me finish!" #[angry]
    
    Morgan "Because it was going to be awful." 
    
    Nick "HOW DARE YOU INSULT MY PROUD AND MAGNIFICENT CULTURE!?! YOU BACKWARDS AMERICANS THINK YOU KNOW EVERYTHING DON’T YOU!?!" #[angry]
    
    #Morgan (V.O.): 
    "Why are we arguing about this, why can’t this guy just get that we don’t do food from germany, it's not that hard to understand."
    
    Morgan "I think I know how to make good food without grinding it into a flavourless paste. Or, do you think I have something already pickled, we don’t!"
    
    Nick "Meatballs are not flavourless and not paste." #[angry]
    
    Nick "They are a moist and bouncy! Also you can buy it can-" #[happy]
    
    Morgan "This is a GOOD family restaurant!"
    
    #Morgan (V.O.):
    "Now he’s got me yelling. why is he still here, we don’t have what he fucking wants! I don’t want to deal with this right now."
    
    #Morgan (V.O.):
    "I don’t know why this has to happen right after that stuff with Dad, is this some kind of test? Are they testing me, why do I need this right now?"
    
    Nick "All the more reason to have it!" #[happy]
    
    #Morgan (V.O.):
    "We shouldn’t be arguing, why are we arguing, this is stupid, why does this guy have to be so stupid!"
    
    #Morgan (V.O.):
    "whyamiarguingwithastupidmeatheadwhyarewearguing"
    
    Morgan "No it's not meathead!"
    
    #Morgan (V.O.)
    "UGH whyarewestillarguingwhyarewestillarguing"
    
    #[Nick sprite pops into sausage sprite]
    
    #Morgan (V.O.)
    "Ha! He is a meathead, a stubborn meathead! Ha... Yeah."
    
    #Morgan (V.O.)
    "I should stop doing this, well at least it’s easier than dealing with this fucking meathead!"
    
    #[Nick food sprite left, Male center, Female right]
    
    Rob "What the hell is going on now?"
    
    Morgan "Oh Rob, this poor German youth is ranting about his struggle with the concept of decent food to me. Sounds like a best seller, revolutionary even. At least for the German people."
    
    Nick "Sir, this “chef” is insulting the proud traditional cooking of my great people, and I will not stand for it!"
    
    Rob "Julie?"
    
    Julie "The german one’s crazy, and Morgan is being Morgan."
    
    Rob "Typical. Morgan I don’t know how better to say this, JUST MAKE THE DAMN FOOD!"
    
    #Morgan (V.O.):
    "I don’t want Rob to start yelling again. It always gets easier to get him going after he’s started."
    
    Morgan "Fine, fine I’ll make the paste-food!"
    #[Clear Sprites]
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

    #Morgan (V.O.) (+):
    "He eyes his food for a few seconds and then shoves it into his meat hole with a audible omph, which quickly became a very light muffled crunch."
    "Then, going through the more tender beef inside the breaded exterior his eyes widen with a kind of overwhelming desire, and some nonsense of the PROUD GERMAN PEOPLE."
    
    #Morgan (V.O.)(+):
    "Chewing intensifies, as if it was the meatiest meat grinder that has ever consumed meat, and then ends with more audible gulps."

    Nick "OH MY THIS IS WUNDERBAR!" 
    jump cook1_done

label cook1_bad:
    #Morgan (V.O.)(-):
    "He looks at it very confused at the breaded fried beef steak lightly covered in gravy made from the steak. He dips the steak into the gravy then shoves it in his face with gusto."

    #Morgan (V.O.) (-):
    "A loud crispy bite. He gives a “hmm” before he continues, chewing for a bit, his eyes start to water a bit but he keeps going, maybe the hot sauce was too much for him."
    
    Nick "Could I have some milk please, I wasn’t expecting spicy."
    
    #Morgan (V.O.) (-):
    "I wasn’t expecting someone so beefy to be such a weeny to spicy foods."
    
    #Morgan (V.O) (-):
    "I bring him back a glass of milk add it to his ticket, then watch as he continues to go from eating, to pain, to relief."
    
    Nick "OH MY, I see what you mean, I guess you have much different stuff than back home!"


label cook1_done:
    #Morgan (V.O.):
    "Why the fuck did he come back here, I was just about to quit for the day."
    
    Nick "Wait where are you going chef? I haven’t properly thanked you!" #[confused]
    
    Morgan " No that’s fine just doing my job really."
    
    #[If we can, zoom Nick sprite in till it covers the scene]
    
    #Morgan (V.O.):
    "Suddenly, a hug that feels more like a panzer has rolled over me, all around me..."
    
    #Morgan (V.O.):
    "Grip tight. Oxygen. Need oxygen."
    
    Morgan "I CAN’T BREATHE!"
    
    #[Zoom back out]
    
    Nick "Well, I’m very sorry, sometimes I don’t realize my own strength, but I am very grateful that you went out of your way to make specialty meal for me!" #[happy]
  
    #[Nick sprite center]
    
    Morgan "Yeah meathead, it was no problem. My boss was gonna get angry at me, and I would really enjoy keeping my job. Sadly it might end soon, I don’t know."
    
    Nick "Oh?-" #[surprised]
    
    Morgan "Well I need to get ready to leave, glad you enjoyed the meal."
    
    #[Exit Nick Sprite]
    
    #Morgan (V.O.):
    "Finally, I can go! Just need to drop off my apron and grab my keys and shit."
    
#Scene 4
##################################################
    scene bg kitchen

    "Still pretty warm outside at least. Ugh, now I’ve got to handle where to live, I heard college helps with that."
    
    show sausage day happy at center
    
    Nick "Hello again! You are looking very sad there in front of Good Family Restaurant door. Also, name is too long."
    
    Morgan "AH! FU- why are you still standing out here. Late. Like a creep."
    
    "THE FUCK IS WITH THIS GUY!"
    
    show sausage day surprised at center
    
    Nick "I am not creepy, I am wholesome proud German boy!"
    
    Morgan "Well, I am poor sad chef..."
    
    show sausage day sad at center
    
    Nick "I am very sorry, is there any way I could help?"
    
    Morgan "I don’t know, do you have an apartment that doesn’t cost an arm and a leg?"
    
    show sausage day at center
    
    Nick "Well, yes. Yes I do. I’ve been looking for a roommate, but everyone keeps turning me down. It’s for an apartment designated for international students, so it’s actually rather inexpensive."
    
    Morgan "That was rhetorical. I mean, I appreciate it, but I don’t think it will be enough."
    
    show sausage day surprised at center
    
    Nick "Also, you can work somewhere else? You sure seem to be a very good cook. The first two plates I had were delicious, though I would have preferred some more proud traditional-"
    
    Morgan "You ate two plates? You ate two whole plates of food, and then came into the back to complain to both chefs about the menu?"
    
    show sausage day happy at center
    
    Nick "Food was very good. A bit light for my tastes, but very good!"
    
    Morgan "Well, that’s not enough I guess. I’m too ignorant of cooking fundamentals, at least that’s what my family told me, they are going to throw their own child out to fend for himself."
    
    show sausage day surprised at center
    
    Nick "What kind of family would do such a thing?"
    
    Morgan "Exactly what I’ve been thinking! And all because I don’t know what a spatula is!"
    
    show sausage day confused at center
    
    Nick "Spatula?"
    
    Morgan "Exactly! Who knows what a spatula is."
    
    Nick "No, I’m sorry, I think you misunderstand, I was surprised you did not know. It is a very simple thing."
    
    Morgan "Oh. Well, the short of it is that in a few weeks I’ll be out of my house and might be out of a job, to start college."
    
    show sausage day happy at center
    
    Nick "OH! Is that what it is, you can probably do both and move in with me! University has many courses of study. I think there is a cooking school. You could learn what a spatula is, or other things too!"
    
    Morgan "You know, that sounds like a plan. What’s your name?"
    
    Nick "Nikolaus, and you?"
    
    Morgan "Morgan. I think this may be a great opportunity for me. I’m not much of a school guy, but maybe this could work out. My dad always talked about how much he enjoyed cooking school. "
    
    show sausage day at center
    
    Nick "Your father also cooks?"
    
    Morgan "Yeah."
    
    Nick "Hmm, so he must know what a spatula is then. Your mother has not kicked him out yet."
    
    Morgan "Yeah totally... *cough*"
    
    Morgan "Well, I’ll see you around."
    
    show sausage day happy at center
    
    Nick "I will come by the restaurant!"
    
    #KITCHEN
    #Morgan (V.O.): 
    "Well, today could be going better. Definitely better, this is just so many dishes, how do we have so many dishes!? I’m not sure if it could have gone worse."
    
    #Morgan(V.O.):
    "I mean, even if something bizarre had happened, like if I lost my pants or something, I would have just left at that point."
    
    #Δ1: 
    "Being put on dishwasher duty kinda sucks but only working so many hours will leave time for class work, which is gonna start up soon I guess." 
    
    #Δ1: 
    "At least, that’s what dad has been telling me. Didn’t think he ever had to start as a dishwasher, he’s such a good cook."
    
    #Δ2: 
    "Ugh this is so fucking stupid. There is no way that dad was a dishwasher, ever. Bullshit. Now I’m stuck getting gross, pruney hands."
    
    #[Female sprite center]
    Julie "Morgan, stop daydreaming and hurry up with those dishes already, you’re getting behind."
    
    Morgan "Hey, I just got most of these alright."
    
    Julie "Well I’ve got two big reservations leaving soon so after you get all of their dishes done I’m going to need your help moving tables around for Karaoke night."
    
    Morgan "Fine."
    
    #[hide female sprite]
    
    #Morgan (V.O.): 
    "Work... is work I guess. I just don’t feel like it’s worth the effort really. But I need the money. They even said every so often I can cook if I behave. I’m always behaved!"
    
    #Morgan (V.O.)
    "And, I’m gonna have to move again, ugh. Moving is always the worst, you leave all your memories and everything familiar, but I can’t stay, so yeah..."
    
    #[ding noise]
    
    "...the dishes are done. Well, I guess I should get to moving those tables around."
    
    #[transition to muffled voices, maybe some pop-y sounding music in the background]
    
    Morgan "Ok got the tables moved for you, I’ll be back to-"
    
    #[Aria sprite center]
    #[music notes]
    Aria "-Maked room wif me is to soon to saw if I’m glad im herre-"
    
    #Morgan (V.O.):
    "It's some girl with fiery hair with blonde streaks and a complexion to match. Which, from the almost inaudible sounds she is making, is probably from drinking way too much."
    
    Morgan "The crazies are out in full force tonight, huh?"
    
    #[female sprite left Aria sprite right]
    
    Julie "Oh her? She’s just some dumb college student. She works across the street and comes here after her shift ends, gets hammered and sings on Karaoke nights."
    
    Julie "Alone."
    
    Julie "Kinda sad really."
    
    Aria "-CAUSE YOU AX FUR IT CaUSE you need SOME!-"
    
    Morgan "She’s not that bad. I mean, I’ve heard worse tonight."
    
    Julie "You just think she’s hot don’t you?"
    
    Morgan "Well, I can barely see her."
    
    Julie "Well, she can barely say a word let alone a full sentence and you think that she’s singing well?"
    
    Morgan "Putting a sentence together isn’t the only point of singing, sometimes you’re just trying to express a feeling or something."
    
    Julie "The feeling of intense queasiness brought about by one too many cocktails? Or five."
    
    Morgan "Well, there are other feelings there too. I just can’t put my finger on them."
    
    Julie "I think you’re just trying to start a fight for no reason again."
    
    Morgan "I think you’re getting too good at this. Alright, I’m taking off. Have fun with the rest of tonight’s drunks."
    
    Julie "I’ll try. No guarantees, but I’ll certainly try."

    #7 ARIA CONTINUED
    #coffee shop 
    #[Aria center, neutral]
    Aria "What’s your order?"
    
    Morgan "A large mocha and a muffin."
    
    #[happy]
    Aria "Great, your order will be right out."
    
    Morgan "Thanks."
    
    #[hide Aria]
    
    #Morgan (V.O): 
    "I’m glad I’ve got somewhere I can go for a bit of peace and quiet. Sometimes it’s nice to have a some time to myself. Take a break from all the crazy I’ve been dealing with lately."
    
    #Morgan (V.O):
    "Gotta give myself a little breather before I have to head off to the campus, this coffee shop is tucked away enough that it doesn’t get too many customers."
    
    #Morgan (V.O.):
    "Taking my breaks from work and school here will be some of the best parts of my day. Taking my breaks from Nick here are some of the best parts of my week."
    
    #[Nick center, happy]
    Nick "Hello friend! Are you getting lunch?"
    
    Morgan "..."
    
    #[confused]
    Nick "If you had listened to me earlier you would not be having this problem."
    
    Morgan "..."
    
    #[sad]
    Nick "The advice of my grandmother is flawless see, never leave the house without your lunch."
    
    Morgan "What are you doing here?"
    
    #[neutral]
    Nick "Oh, little sister called. She needed help moving things. She asked for you, but I am a strapping young gentleman, and thought I could do heavy moving."
    
    Morgan "So, you’re here because you were helping out my lazy sister at work across the street. Great."
    
    #[angry]
    Nick "Do not insult sister. She is good beautiful girl."
    
    Morgan "Meat. Were you, hitting, on MY SISTER?!"
    
    #[confused]
    Nick "I would never harm such a delicate flower."
    
    Morgan "OH IT IS ON NOW YOU YODELING SACK OF SH-"
    
    #[Aria left angry, Nick right]
    Aria "HEY, YOU TWO, PIPE DOWN!"
    
    Morgan "Uh... dude’s trying to bang my sister..."
    
    Nick "I have no violent intentions!"
    
    Aria "I will throw you two out! This is not some kind of boxing ring, this is a coffee shop. Now you two calm down or take it outside, do I make myself clear?"
    
    #[neutral]
    Nick "Yes, I am very calm. Always calm."
    
    #Morgan (V.O.):
    "It’s my fault I overreacted. It's just this meathead is being a creep, on my little sister!"
    
    #Morgan (V.O.):
    "and now I’m disrupting her work, even though there is like no one here to really disrupt."
    
    #Morgan (V.O.):
    "i don’t know what to do..."
    
    Morgan "I!... i..."
            
    #[lasagna sprite]
    
    Morgan "I guess I’m sorry. I didn’t mean to cause an issue. Sorry for yelling. We’ll be going once my order’s out."
    
    Aria "Ok. You can stay if you want, just don’t both the other guests anymore than you have."
    
    #Morgan (V.O.): 
    "But, there’s no one else here..."
    
    Morgan "Will do ma’am."
    
    #[happy]
    Nick "We will do no bothering sing lady."
    
    Morgan "Sing?"
    
    #[neutral]
    Nick "You do not recognize lady?"
    
    Morgan "Recognize what?"
    
    #[surprised]
    Nick "She is at your place of work all the time. She is sing lady. You must at least remember her voice."
    
    Morgan "Well I hear her voice all the time, she works here, and I come here all the time. Though, come to think of it... are you the girl who was singing karaoke across the street last night?"
    
    Aria "..."
    Aria "Listen here you-  How do you two know about that?"
                                                             
    #Morgan (V.O.):
    "Should I not of said anything. Fuck, I totally shouldn’t of said anything. She is pissed."
    
    Morgan "Well, uh I work there and he... eats there a lot, he also just eats a lot in general. Why, whats wrong?"
    
    Nick "Yes, Grandmother always said never miss five meals a da-"
    
    Morgan "We’re over there a lot. Is what we’re trying to say."
    
    Aria "Ok, but you cannot tell anybody here about it. Or, just anyone in general, got it."
    
    Morgan "I can certainly do that. And nobody will be able to make heads or tails of whatever Arnie is saying anyway."
    
    #[angry]
    Nick "He is not PROUD GERM-"
    
    Morgan "Whatever. Your secret is safe with us."
    
    Aria "Good. Now take your order and go."
    
    Morgan "But I thought you said we could stay?"
    
    Aria "GET OUT!"
    
    #Morgan (V.O.):
    "How did I still manage to fuck it up with saucy girl, uh now I have to get to campus and hope that she isn’t going to be mad at me if I come back, I really like it there."




    #END OF DEMO BOIS



    # This ends the game.

    return
