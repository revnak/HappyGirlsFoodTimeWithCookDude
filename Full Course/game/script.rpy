# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Morgan = Character("Morgan")
define Julie = Character("Julie")
define Rob = Character("Rob")
define Dad = Character("Dad")
define Mom = Character("Mom")
define Nick = Character("Nick")
define Aria = Character("Aria")
define Diana = Character("Diana")
define Dave = Character("Dave")
define Woman = Character("Woman")
define Guide = Character("Guide")
define Jogstudent = Character("Jogging Student")
define Alexandra = Character("Alexandra")
define James = Character("James")

# Declare background images
image bg kitchen = im.Scale("kitchen.png", 1280, 720)
image bg school = im.Scale("school.png", 1280, 720)
image bg app = im.Scale("apartment.png", 1280, 720)
image bg cafe = im.Scale("cafe.png", 1280, 720)
image bg dorm = im.Scale("Dorm.png", 1280, 720)
image bg indkitchen = im.Scale("industrial-kitchen.png", 1280, 720)
image bg resttables = im.Scale("restaurant-tables.png", 1280, 720)
image bg credits = im.Scale("credits.png", 1280, 720)


#Define Audio Files
define audio.morgan = "audio/Comic Hero.mp3"
define audio.title = "audio/Delightful D.mp3"
define audio.general = "audio/Doobly Doo.mp3"
define audio.minigame = "audio/Jaunty Gumption.mp3"
define audio.diana = "audio/Jesu.mp3"
define audio.alexandra = "audio/Master of the Feast.mp3"
define audio.nick = "audio/MeatBall Parade.mp3"
define audio.aria = "audio/Mighty Like Us.mp3"

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

image tso prez day = "tso prez.png"
image tso prez flustered = "tso prez flustered.png"
image tso prez tired = "tso prez tired.png"
image tso prez worried = "tso prez worried.png"
image tso food = "tso food.png"

image female = "silhouette female.png"
image male = "silhouette male.png"
image food = "silhouette food.png"


#Variable Defaults
default schoolFlag = True
default succFlag = True

#Screens
screen clickScreen():
    key "mousedown_1" action Return(True)

#Declare sprite positions
transform left:
        xalign .25
        yalign -.1        
transform center:
        xalign .5
        yalign -.1
transform right:
        xalign .75
        yalign -.1
transform farleft:
        xalign 0.0
        yalign -.1
transform farright:
        xalign 1.0
        yalign -.1
#Food positions
transform foodleft:
        xalign 0.25
        yalign 0.5        
transform foodcenter:
        xalign 0.5
        yalign 0.5
transform foodright:
        xalign 0.75
        yalign 0.5
transform foodfarleft:
        xalign 0.0
        yalign 0.5
transform foodfarright:
        xalign 1.0
        yalign 0.5

#Declaring Transitions
define longfade = Fade(0.5,1.5,0.5)

label start:
    
    
# ######DEBUG JUMPS###############################
#    scene bg kitchen with longfade
#    menu:
#        "Start from beginning":
#            jump intro
#        "Sausage intro":
#            jump sausage_intro
#        "Cooking 1":
#            jump cook1_start
#        "Lasagna intro 1":
#            jump lasagna_intro_1
#        "Tiramisu intro":
#            jump tiramisu_intro
#        "Lasagna intro 2":
#            jump lasagna_intro_2
#        "Tso intro":
#            jump tso_intro
# ################################################
# ################################################

    #1 INTRODUCTION START
label intro:
    scene bg kitchen
    with longfade
    play music morgan fadeout 1
    

    #Morgan(V.O.): 
    "All my life I’ve been told that the fastest way to a person’s heart is through their stomach."
    
    #Morgan(V.O.):
    "I find those cliche’ sayings stupid. But my dad has always lived by that cheesy old saying and I’ve never met a person more popular than him."
    
    #Morgan(V.O.):
    "His restaurant is always packed with people smiling, laughing, and eating."
    
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
    "We got everything you’d need to to make pretty much anything! Flippers, Flappers, Noodlegrabbers, Wirlymagigs, Potatoflays, Tinybidents, and so many other different utensils."
    
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
    
    play music general fadeout 1
    
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
    
    hide male
    show food at foodright

    "..."
    
    #Morgan(V.O.):
    "Why does this always make me feel better? What was I doing? Oh, right. I have to go talk to dad."
    
    Rob "-F YOU AREN’T GOING TO LISTEN TO ME THEN GO TALK TO-"
    
    #[Hastened footsteps echo off the floor]
    
    Morgan "OK I’ll go talk to him, then I’ll get on the next order when I get back!"
#SCENE 2
##################################################

scene bg kitchen
with fade

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
    
##School Flag Choice##
    
menu:
    "Do I want to go back to school this Fall?"
        
    "Yes":
        $ schoolFlag = True
        jump school1_yes
    "No":
        $ schoolFlag = False
        jump school1_no
            
label school1_yes:
    Morgan "... You know what, fine. I guess I can’t keep working in this place forever anyways."
        
    Dad "Good to hear! You're finally taking your future into your own hands. You need to set a good example for Julie."
        
    jump school1_done
        
label school1_no:
    Morgan "But why can’t you guys just hire me as a full time cook here? I already know all of your recipes."
        
    Dad "That’s not going to happen, Morgan. It’s about time you stood on your own two feet. You ARE going to start college this fall."
        
    jump school1_done

        
label school1_done:
    #[Swinging Door Sounds]
    show male at left
    show female at right
        
    Julie "Morgan, we need you back inside, we have a customer asking for you."
        
    Dad "Go on, we will talk about this later."
        
    "Why would a customer want to talk to me? I just cook here…"
        
    #[Footsteps and Swinging Door sounds]
        
#Scene 3 NIKOLAUS INTRO
#######################################
label sausage_intro:
    scene bg kitchen
    with fade

    show female at center
    
    Julie "Hey, there’s this weird guy out there asking for a meatball menu? What should I tell him?"
    
    Morgan "That we don’t have one, this is a family style restaurant."
    
    Julie "Well, he did say something about pickled herring?"
    
    Morgan "Tell him this is a good family restaurant."
    
    Julie "Ok, well the guy’s a bit excitable and I don’t-"
    
    #[door slams open]
    
    hide female
    show sausage day angry at left
    show female at right
    
    play music nick fadeout 1
    
    Nick "I DEMAND TO SEE THE CHEF!"
    
    #Morgan (V.O):
    "Who does this man made mostly of fucking thick ass steaks with a fluffy yellow poof for hair want?" 
    
    "Well whatever it is I sure as hell don’t want to deal with it."
    
    #Morgan (V.O.):
    "And why does he have to have a shirt so tight it shows off all of his- nevermind!"
    
    Morgan "I think he’s out back on a smoke break, big metal door, can’t miss it."
    
    hide sausage day angry
    show sausage day at left
    
    Nick "Thank you sir."
    
    hide sausage day
    hide female
    show female at center
    
    Julie "We have a back door?"
    
    Morgan "There’s a door-"
    
    Nick "WHY IS THIS ROOM SO COLD?!?"
 
    Morgan "-it’s to the refrigerator. But it is a door and it is in the back."
    
    show sausage day angry at left
    hide female
    show female at right

    Nick "What is meaning of this! I just want to talk to the chef here!" 
    
    Morgan "Well the other guy is handling smoked fish back there. I’ve done worse."
    
    Nick "He said you were the chef!" 
    
    Morgan "I am, so is he. We are both the chef, chefs. Sometimes there is more than one person that can satisfy the role."
    
    Morgan "For example, Julie is not the only person getting on my nerves today."
    
    Nick "Why is there no authentic German cuisine on your menu!" 
    
    Morgan "Because this is primarily an american family style restaurant."
    
    hide sausage day angry
    show sausage day at left
    
    Nick "Then why not have authentic German-" 
    
    Morgan "Because this is a good family style restaurant."
    
    hide sausage day
    show sausage day angry at left
    
    Nick "You didn’t even let me finish!"
    
    Morgan "Because it was going to be awful." 
    
    Nick "HOW DARE YOU INSULT MY PROUD AND MAGNIFICENT CULTURE!?! YOU BACKWARDS AMERICANS THINK YOU KNOW EVERYTHING DON’T YOU!?!"
    
    #Morgan (V.O.): 
    "Why are we arguing about this, why can’t this guy just get that we don’t do food from germany, it's not that hard to understand."
    
    Morgan "I think I know how to make good food without grinding it into a flavourless paste. Or, do you think I have something already pickled, we don’t!"
    
    Nick "Meatballs are not flavourless and not paste."
    
    hide sausage day angry
    show sausage day happy at left
    
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
    
    hide sausage day happy
    show sausage food at foodleft
    #[Nick sprite pops into sausage sprite]
    
    #Morgan (V.O.)
    "Ha! He is a meathead, a stubborn meathead! Ha... Yeah."
    
    #Morgan (V.O.)
    "I should stop doing this, well at least it’s easier than dealing with this fucking meathead!"
    
    show sausage food at foodfarleft
    show male at center
    show female at farright
    
    Rob "What the hell is going on now?"
    
    Morgan "Oh Rob, this poor German youth is ranting about his struggle with the concept of decent food to me. Sounds like a best seller, revolutionary even. At least for the German people."
    
    Nick "Sir, this “chef” is insulting the proud traditional cooking of my great people, and I will not stand for it!"
    
    Rob "Julie?"
    
    Julie "The german one’s crazy, and Morgan is being Morgan."
    
    Rob "Typical. Morgan I don’t know how better to say this, JUST MAKE THE DAMN FOOD!"
    
    #Morgan (V.O.):
    "I don’t want Rob to start yelling again. It always gets easier to get him going after he’s started."
    
    Morgan "Fine, fine I’ll make the paste-food!"
    
    scene bg kitchen
    
    play music minigame fadeout 1
    
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
        "Back to recipe list":
            jump cook1_start

label cook1_food_2:
    "Chicken Fried Steak- A pretty normal dish on the menu, popular for lunch."
    menu:
        "Prepare this?":
            jump cook1_bad
        "Back to recipe list":
            jump cook1_start

label cook1_notes:
    menu:
        "The Meathead":
            jump cook1_note_1
        "Recipe List":
            jump cook1_start
    
label cook1_note_1:
    "This guy seems to like German food. I should probably make him something German."
    jump cook1_notes



label cook1_good:
    "Ok so to start I need to lay down a piece of plastic wrap down big enough to also cover the top of the pork chop then lay the chop down and fold plastic over."

    "Then I got to take the flat wide meat.. mallet to the chop hitting in the middle pressing towards the outside. Give it a couple goes and tada, perfectly pounded meat!"

    "Now that we got the meat pounded but clearly not to the level of paste, I gotta get the things for the breading. I got flour, eggs beaten with a splash of milk and lastly breadcrumbs with parsley and some seasoning salt." 

    "First for making an excellent crust is to coat the chop in flour, then egg wash, bread crumbs, back into the egg and a final dose of breadcrumbs. Need to press into the meat to get the breading to really stick to the meat." 

    "Now onto the frying, gotta get one of the large frying pans and heat some oil in it. Put that meat in for a few minutes on the first side then flip. Now i gotta just a couple chunks of butter to bring some richness to the crust."

    "Just a few minutes in there and it is ready to plate! Take some cucumber salad we have in the fridge and garnish the meat with a lemon wedge."

    "Order up!"

    play music nick fadeout 1
    
    show sausage day happy at center
    
    #Morgan (V.O.) (+):
    "He eyes his food for a few seconds and then shoves it into his meat hole with a audible omph, which quickly became a very light muffled crunch."
    "Then, going through the more tender beef inside the breaded exterior his eyes widen with a kind of overwhelming desire, and some nonsense of the PROUD GERMAN PEOPLE."
    
    #Morgan (V.O.)(+):
    "Chewing intensifies, as if it was the meatiest meat grinder that has ever consumed meat, and then ends with more audible gulps."

    Nick "OH MY THIS IS WUNDERBAR!" 
    jump cook1_done
    
label cook1_bad:
    
    "I first need to grab some cubed steak from the fridge. Season it with salt, pepper, cayenne, and paprika."

    "Now we do the double dredge. Coat it in flour, then some lightly beaten egg because its best to have an uneven kind of crust to it, and then back into the flour. Then take a skillet with some oil turn up the heat."

    "Now to let if crisp up on one side, then flip it over and get the other. Now to take that out and start that thick gravy that customers always come back for."

    "Just need to add some flour and little more oil into the pan with all the greasy bits left over from the steak. Mix it around, and once it reaches a paste like consistency add a little milk."

    "Add in some salt and a bunch of pepper just need to whisk-whisk away until it thickens up. Finally I just need to spread that gravy all over that chickened steak! Serve with a side of fries."

    play music nick fadeout 1
    
    show sausage day confused at center
    
    "He looks at it very confused at the breaded fried beef steak lightly covered in gravy made from the steak. He dips the steak into the gravy then shoves it in his face with gusto."

    "A loud crispy bite. He gives a “hmm” before he continues, chewing for a bit."
    
    Nick "Gravy taste like thick pepper milk, and small bite in crust flip flop from how it is back home."
    
    "Well I guess that’s how we like it here, you don’t have to make it sound like we're doing it wrong just because we aren’t doing it the way of the great meatpaste barons of yore!"

    Nick "I meant no offence, but I see what you mean, I guess you have much different stuff than back home! But is good different!"


label cook1_done:
    scene bg kitchen
    
    show sausage day confused at center
    
    #Morgan (V.O.):
    "Why the fuck did he come back here, I was just about to quit for the day."
    
    Nick "Wait where are you going chef? I haven’t properly thanked you!" #[confused]
    
    Morgan " No that’s fine just doing my job really."
    
    hide sausage day confused
    show sausage day happy at center
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
    
    hide sausage day happy
    show sausage day surprised at center
    
    Nick "Oh?-" 
    
    Morgan "Well I need to get ready to leave, glad you enjoyed the meal."
    
    hide sausage day surprised
    
    #Morgan (V.O.):
    "Finally, I can go! Just need to drop off my apron and grab my keys and shit."
    
#Scene 4
##################################################
    scene bg resttables
    with fade

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

#Scene 5 Aria introduction
##################################################

label lasagna_intro_1:
    scene bg resttables
    with longfade
    play music morgan fadeout 1
    #Morgan (V.O.): 
    "Well, today could be going better. Definitely better, this is just so many dishes, how do we have so many dishes!? I’m not sure if it could have gone worse."
    
    #Morgan(V.O.):
    "I mean, even if something bizarre had happened, like if I lost my pants or something, I would have just left at that point."
    
    if schoolFlag == True:
        jump school2_yes
    else:
        jump school2_no
    
label school2_yes:
    "Being put on dishwasher duty kinda sucks but only working so many hours will leave time for class work, which is gonna start up soon I guess." 
    
    "At least, that’s what dad has been telling me. Didn’t think he ever had to start as a dishwasher, he’s such a good cook."
    
    "I even got all the moving a paperwork junk taken care of super fast!"
    jump school2_done

label school2_no:
    "Ugh this is so fucking stupid. There is no way that dad was a dishwasher, ever. Bullshit. Now I’m stuck getting gross, pruney hands."
    
    "I also couldn’t say no to Meathead and his offer to keep this ruse going. I can’t just couldn’t leave an offer that good. And now I have to live with him."
    jump school2_done

label school2_done:
    show female at center
    play music general fadeout 1
    
    Julie "Morgan, stop daydreaming and hurry up with those dishes already, you’re getting behind."
    
    Morgan "Hey, I just got most of these alright."
    
    Julie "Well I’ve got two big reservations leaving soon so after you get all of their dishes done I’m going to need your help moving tables around for Karaoke night."
    
    Morgan "Fine."
    
    hide female
    
    #Morgan (V.O.): 
    "Work... is work I guess. I just don’t feel like it’s worth the effort really. But I need the money. They even said every so often I can cook if I behave. I’m always behaved!"
    
    #Morgan (V.O.)
    "And, I’m gonna have to move again, ugh. Moving is always the worst, you leave all your memories and everything familiar, but I can’t stay, so yeah..."
    
    #[ding noise]
    
    "...the dishes are done. Well, I guess I should get to moving those tables around."
    
    #[transition to muffled voices, maybe some pop-y sounding music in the background]
    
    Morgan "Ok got the tables moved for you, I’ll be back to-"
    
    show lasagna work drunk at center
    #[music notes]
    Aria "Heyyyyy Evryonne, I'm Aria an thiz is the BEHST song!"

    Aria "-Maked room wif me is to soon to saw if I’m glad im herre-"
    
    #Morgan (V.O.):
    "It's some girl with fiery hair with blonde streaks and a complexion to match. Which, from the almost inaudible sounds she is making, is probably from drinking way too much."
    
    Morgan "The crazies are out in full force tonight, huh?"
    
    hide lasagna work drunk
    show lasagna work drunk at right
    show female at left
    
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

    scene bg resttables
    with dissolve
    play music morgan fadeout 1

    "Now time to leave for the night, finally. Wait, Is that the poof I think it is?"

    show sausage day happy at center
    
    Nick "MORGAN!"
    
    "Yup."
    
    Morgan "Not so loud! What is it?"
    
    Nick "It is about the dorms, you can sign this to get you in. I also brought pen, then I can give it back in morning."
    
    Morgan "Ugh sure meatman."
    
    "Sign the thing get it done with."
    
    Nick "Yes, this is good."
    
    Nick "Now you will need to pack, and be ready in a week."


#Scene 5.5
##################################################
    scene bg app
    with longfade
    
    "Been slowly getting things packed for the past couple days."

    if schoolFlag == True:
        jump school3_yes
    else:
        jump school3_no
    
label school3_yes:
    "It’s really bizarre for my stuff to not be in its places. Soon I’ll make new homes for everything though! I wonder where my new space for the clicker will be? Or, the new plate cave?"
    jump school3_done

label school3_no:
    "It's usually kinda hard for me to get up the motivation to clean up around here, let alone get it put into boxes to go to college."
    jump school3_done
        
label school3_done:
    "I’m kinda glad that I didn’t have to do any of the work, I would have probably backed down otherwise."
    
    "I know that I’ve heard that dorms are often just like a single room that everyone kinda shares as a collective bedroom-living room thing... and now that I’m going over this to myself, fuck I don’t want to live in that for what... four years...? ugh."
    
    "And my discomforted groaning is quickly drowned out by a THUD at the door."
    
    play music nick
    
    Nick "COMING IN!"
    
    Morgan "No, what, don't, stop."
    
    "And as I say that, the door comes flying open."
    
    show sausage day happy at center
    
    Nick "Hello, is everything all ready!?"
    
    Morgan "What? Why did you just barge in like that?!"

    show sausage day at center
    
    Nick "Well you knew I was coming so either you’d left it unlocked for me or I wouldn’t be able to enter, yes?"
    
    Morgan "I um uh."
    
    "Actually it's more that I either forget or was too lazy to lock it..."
    
    "But he doesn’t need to know that!"
    
    Morgan "Yeah, I got everything packed."
    
    show sausage day happy at center

    Nick "Is good!"
    
    Morgan "So, do you have like a car or something."
    
    Nick "I got my friend to let me borrow truck!"
    
    Morgan "Uh, ok then..."
    
    "After less trips than I expected we got everything loaded and were on our way."
    
    "There were more times that I had to remind meatyboy which side of the road was correct then I thought I would ever need to."
    
    scene bg dorm
    with fade

    show sausage day at center

    "OK, now that we get here, the outside looks pretty standard, is this actually just a house disguised as a dorm!?"
    
    Nick "They let you have full bedroom like me."

    "Is this just a big house at the college?"
    
    Nick "We have one kitchen and one bathroom that everyone shares."
    
    "This is just a big house at the college."
    
    Nick "Here is the-"
    
    Morgan "Is this just a house on campus?"
    
    show sausage day confused at center

    Nick "Uh. It is house but it’s owned by the school, and is on school, with people that go to school. Is school house!"
    
    Morgan "Uh yeah, ok."

    show sausage day at center
    
    "There were a few hours of just one by one taking everything into my new room. It's a little bigger than my old room, but definitely smaller that my old living room, but there is still the big living room here, but I’m not sure how much I want to encroach into their space like that."
    
    "Now I need to run over and tell Dad the news."
    
    scene bg resttables
    with fade
    play music morgan fadeout 1
    
    "Pretty busy today, but we always manage to get everything out at a reasonable rate."

    show female at center
    
    Julie "Hey you can’t work today, them’s the rules."
    
    Morgan "Wait, what, no, that's not why I’m here!"
    
    Julie "Right, then what else would you be here for?"
    
    Julie "Spread lies about me to some more ignorant bystander?"
    
    Morgan "No!"
    
    Morgan "Not yet. But, to the point, is Dad around?"
    
    Julie "Uh, he might be in the office, I haven’t seen him in a while. Also, Mom was back there, so who knows what could be going on."
    
    Morgan "Well I need to tell dad about the move."
    
    Julie "Good luck."
    
    hide female
    
    "Not Out front huh. Usually he would be out greeting everyone then running back to make the orders in his goofball way."
    
    "Maybe it has something to do with whatever Mom's here for?"
    
    "Somehow I managed to wander into the back while daydreaming about what's going on."

    show female at center
    
    Mom "Son, hello? Hey!?"
    
    Morgan "Huh?"
    
    Mom "What are you doing here? Shouldn't you be off getting ready for school?"
    
    Morgan "Uh yeah, actually came by to say that I got everything moved in to the dorm..  thou-"
    
    Mom "That's nice dear, when are you starting classes?"
    
    Morgan "About a week. Uh where's Dad?"
    
    Mom "He's out."
    
    Morgan "Aw, I want to tell him. You know when he'll get back?"
    
    Mom "I will tell him after he has had some time to think about his actions."
    
    Morgan "What?"
    
    Mom "It's nothing you should be worrying yourself about. Father-Chef problems."
    
    "Problems? I didn't think that Dad could have any problems he'd need to stop doing things around the restaurant during rush time for."
    
    Morgan "Oh, uh ok."
    
    Mom "I know you look up to your father Morgan, but you want more than this, right?"
    
####  Be Successful Flag Choice  ##########
    menu:
        "Can I be better than what dad has here."
        
        "Sure":
            $ succFlag = True
            jump succ1_yes
            
        "No":
            $ succFlag = False
            jump succ1_no
            
label succ1_yes:
    "Uh, sure."
    
    "I’m not really sure what shes talking about, but I could be down with maybe branching out a bit more than hometown cooking."
    
    "Morgan I think it would be cool to do more things."
    
    if schoolFlag == True:
        Mom "That’s what college is for. Get you the knowledge to do great things."
        
        Mom "A degree is always good to put on a resume when applying to any job, Chef included."
        
    else:
        "I’ll need to find time when I’m not in culinary jail to find my untapped potential."
        
    Mom "If you focus I know you can do it."
    jump succ1_done

label succ1_no:
    Morgan "No"
    
    "What could she mean, there is no way I could do more than here. More than dad? I’m not some cuisine wizard beamed down from on high!"
    
    "That is clearly dad."
    
    "Mom what are you gonna do if the restaurant goes away or we can’t keep having you around."
    jump succ1_done
    
label succ1_done:
    Mom "Well, I’m very sure he’ll be happy to hear about the apartment, I’ll make sure to tell him when he gets back."
    
label dorm_intro:
    scene bg app
    with fade
    play music morgan fadeout 1
    
    "And now, back to the dorm."
    
    "The walk feels a lot longer on way back. I don’t know if it’s all uphill going this way, or the weirdness with Mom just now."
    
    "Is there something going on?"
    
    "She sounded ominus, which to be fair is how she always sounds."
    
    scene bg dorm
    with fade
    
    "Well, back here at the dorm. I wonder if anything’s going on?"

    show sausage day happy at center
    play music nick fadeout 1
    
    Nick "WELCOME HOME!"
    
    Morgan "I’m out."
    
    Nick "NO, I am welcome, and this is home."
    
    "He then puts his hand on my shoulder to keep me in place."
    
    show sausage day sad at center
    
    Nick "I am sorry I tried to gather rest of room mates but they are all absent. Saddest of events."
    
    Morgan "I mean that’s fine, I’m not big on those kinds of thing-"
    
    show sausage day angry at center
    
    Nick "Nonsense!"
    
    show sausage day happy at center

    Nick "Soon you will meet them. They are Dan, James, and Chris."
    
    Morgan "Uh, ok."
    
    show sausage day confused at center

    Nick "Dan and James don’t talk much, and Dan isn’t here much, so he doesn’t really know people. I try to know him, but he’s never here."
    
    show sausage day at center
    
    Nick "Dan is Engineer major, and James is Graphics Design."

    Morgan "Huh, interesting. I guess they don’t work with people too much."
    
    Nick "Well Dan does."
    
    Nick "Chis is other room mate, is also busy."

    show sausage day happy at center
    
    Nick "But full of charisma, like me!"
    
    Nick "He is Architect."
    
    Nick "You should see him talk about his big plans."
    
    Morgan "Ah yeah, sounds fun."

    show sausage day at center
    
    "We then got the rest of the boxes into the room unpacked a bit more."

    hide sausage
    
    "Which quickly devolved into me doing it by myself until I decided to call it for the night."

#Scene 6
##################################################
label tiramisu_intro:
    scene bg kitchen
    with longfade
    
    "Glad they are letting me cook on some of the low staff days. Gets me away from all the pruny hands, and DISHES."
    
    show female at center
    
    Julie "table 7’s asking for you Morgan."
    
    Morgan "What do they want?"
    
    Julie "I don’t know, but she does come in pretty regularly."
    
    show female at left
    show male at right
    
    Rob "Yeah, I always try to put in a little extra for her but she never leaves very high tips. I don’t know if she’s just stingy with her money or what?"
    
    Julie "Whatever, just go!"
    
    hide female
    hide male
    play music diana fadeout 1
    
    scene bg resttables
    with fade
    show tiramisu day disgust at center
    
    "oh my god. why is she- why is this happening."
    
    "there’s a girl calling me over to her table?"
    
    Morgan "Hello, I’m Morgan, I was told that you wanted to see me?"
    
    "This girl? Whaa, she’s got dark skin and blonde hair? Does she like dye it, or does she like tan... a lot? Her clothes are also probably designer. What could she possibly want with me??"
    
    Diana "Yeah. Although, I can’t say I’m very impressed."
    
    Diana "When I asked to see the cook I expected a more well-groomed adult. "
    
    "so... did i fuck up? that was faster than i thought it would take."
    
    show tiramisu day at center
    
    Diana "... Oh well, it’s not like you can embarrass yourself all the way back in the kitchen. My name is Diana, and I’m looking for a new personal cook, come work for me. "
    
    "my heart feels like it’s about to burst out of my chest, she has such pretty--"
    
    "Wait, she wants me to come work for her? I can’t do that, that would mean I would have to (A-:leave this place.) (A+:put off school.)"
    
    Morgan "I... I’m sorry but I can’t do that."
    
    show tiramisu day surprised at center
    
    Diana "There are- wait, are you for real?"
    
    Diana "I just can’t believe that you’d rather keep your part time job over- you know what, how much to get you out of this place that is so beneath your skill?"
    
    Morgan "Oh no, I get paid plenty here. I mean not enough to pay rent- but it’s all covered. Uh it’s fine, I don’t need extra money."
    
    Diana "You can’t... make... rent?"
    
    "don’tyelldon’tyelldon’t-"
    
    Diana "How could someone with the kind of talent that you have not be able to pay for your living?"
    
    "...is she flirting with me???"
    
    show tiramisu day at center
    
    Diana "I have come here a number of times and the food always has a surprising elegance to it on certain days, and those must be days that you are the one in front of the stove."
    
    "she is, what do i do, I DON’T KNOOOW!"
    
    Diana "There is so much more that you can 	do with a much better facility. And I want that, and am willing to pa-"
    
    "idon’tknowidon’tknowidon’tknow"
    
    "I guess i could... hmmm..."
    
    show tiramisu food at foodcenter
    
    "That’s better I guess. It’s just so luxurious on the palette. A garnish is common but the topping works all on its own."
    
    Morgan "Hey, Speaking of food, have you made your order yet?"
    
    Diana "Wha- Now that you mentioned it I have not. I would like the-"
    
    Morgan "I think I can whip up something for you. Be right back!"
    
################ FILL OUT TEXT HERE WITH PROPER ENTRIES #######################
    scene bg kitchen
    with fade
label cook2_start:
    play music minigame fadeout 1
    menu:
        "Caprese Salad":
            jump cook2_food_1
        "Spaghetti":
            jump cook2_food_2
        "Notes":
            jump cook2_notes
            
label cook2_food_1:
    "Caprese salad, elegant stack of basil, cheese, and tomato, and surprisingly little salad."
    menu:
        "Prepare this?":
            jump cook2_good
        "Back to recipe list":
            jump cook2_start

label cook2_food_2:
    "Spaghetti, it's a tomato sauce with ground beef over... spaghetti. Pretty standard for the restaurant."
    menu:
        "Prepare this?":
            jump cook2_bad
        "Back to recipe list":
            jump cook2_start

label cook2_notes:
    menu:
        "Diana":
            jump cook2_note_1
        "Recipe List":
            jump cook2_start
    
label cook2_note_1:
    "She seems really elegant, I should probably make something fancy for her."
    jump cook2_notes
##############################################################################


label cook2_good:
    scene bg kitchen
    "First start with the balsamic reduction, that can stay out a bit after cooking. Take a cup of balsamic and a few tablespoons of sugar on medium just wait a bit for that to boil and reduce down."

    "Need to take some fresh mozzarella, if it's not really high quality it really shows because it is the center focus of the dish, even though I plan on adding some side shrimps." 

    "Cut it into equal portions, almost like large thick cheese coins. Then slice up the tomato." 

    "Now we assemble it into two lines, alternating between tomato, mozzarella, and basil, until it goes nearly from one side of the plate to the other."

    "Now that I think about it I could pair this really well with some shrimp, just need something that ties them together, basil. I can finely dice up some basil and garlic to put with the shrimp in some olive oil." 

    "Just a bit on each side should do nicely, just need to make sure that it’s not overcooked or it’ll turn out tough. She’d like it if I keep everything neat so I’ll line them up in the middle, and order up!"

    scene bg resttables
    with fade
    show tiramisu food at foodcenter
    play music diana fadeout 1
    
    "She eyes the salad with a gleam of approval, which is a nice change from the slight disapproving look she was giving off earlier."
    
    "She then cuts into the toppings, with a level of grace I don’t even think I’ve seen in the kitchen, let alone someone eating anything! Then, piercing the bits onto her fork with some of the basil."
    
    "She slowly raises it to her mouth and pops it in, before sliding the fork out between her lips."
    
    "She chews with slow small bites, making sure to keep her mouth closed. Then, silently swallows."
    
    Diana "Oh my, such elegance you have here. Simple, but refined."
    
    Morgan "Thanks, I hope everything is to you liking."
    
    "After getting praise from her, she then goes back to taking small elegant bites until she finishes her plate."
    
    Diana "MMMMM, you have really outdone yourself."
    
    "While she’s enjoying it I can probably slip away and hope I don’t have to deal with this chick anymore."
    
    Diana "What, were did that chef go?"
    
    show male at left
    show tiramisu day surprised at right
    
    Rob "I think he left for the night."
    
    Diana "I wasn’t even able to pay him for the delicious meal."
    
    Rob "Oh don’t worry about it miss, I’ll cover the meal. I mean you didn’t actually even order it."
    
    show tiramisu day disgust at right
    
    Diana "That is not what I- Thank you, uh bye. "
    
    jump scene7

label cook2_bad:
    scene bg kitchen
    "First we need to brown up some meat, crank up that pan up."

    "While thats going start with some spaghetti noodles into a pot with water and a dash of salt. And by that time the sauce is done."

    "Now that that its on its way to brown town gotta put in a few tablespoons of diced onion and a clove of garlic then let that go for a while longer."

    "Now that it's ready I can put in the sauce, just need to take dad’s homemade sauce which has the three levels of tomato, diced, puree, and crushed, with various herbs and spices."

    "It's mostly oregano and basil with some other stuff that he really likes in there. Probably more garlic."

    "Heat it up with the meat and pour that delicious sludge over the pasta. Order up!"

    scene bg resttables
    with fade
    show tiramisu food at foodcenter
    play music diana fadeout 1
    
    Morgan "Well this is what I could whip up for you."
    
    "She looks utterly baffled at the spaghetti. Like, how could you possibly be this stupid, you probably shouldn’t be allowed to cook, what was I thinking."
    
    Diana "This is not what I was expecting... This is the best that this establishment has to offer?"
    
    Morgan "Yes. At least to my knowledge."
    
    Diana "I would like to talk to you manager."
    
    Morgan "I don’t think dad’s in, but I can grab Rob for you?"
    
    Diana "That will be fine."
    
    hide tiramisu food
    
    "Uh this doesn’t seem like it will end well. I better just leave."
    
    show male at left
    
    Rob "Yes ma’am is something wrong?"
    
    show tiramisu day disgust at right
    
    Diana "Yes there is, you are clearly not well equipped enough to make a fine meal."
    
    Rob "Are you saying the food is bad?!"
    
    show tiramisu day at right
    
    Diana "I’m saying what you have in stock does not hold up. If you want, I would be more than willing to help you get in touch with someone that can facilitate your chef, or maybe I can now convince him on coming to wor-"
    
    Diana "..."
    
    Diana "Where did he go?"
    
    Rob "I think he took off for the night."
    
    Diana "Well charge my card and and be on my way."
    
    jump scene7

#7 ARIA CONTINUED
########################################################
label lasagna_intro_2:
    label scene7:
    scene bg cafe
    with longfade
    #coffee shop 

    Morgan "I’ve been here a couple times before morning shifts. I usually just grab whatever’s written biggest on the board super quick and less than fully awake. It’s really close to work, always a plus. Now also on the way to campus."

    show lasagna work at center
    play music aria fadeout 1

    Aria "What’s your order?"
    
    Morgan "A large mocha and a muffin."
    
    show lasagna work happy at center

    Aria "Great, your order will be right out."
    
    Morgan "Thanks."
    
    hide lasagna
    
    #Morgan (V.O): 
    "I’m glad I’ve got somewhere I can go for a bit of peace and quiet. It’s nice to have a some time to myself. Take a break from all the crazy I’ve been dealing with lately."
    
    #Morgan (V.O):
    "Gotta give myself a little breather before I have to head off to the campus, this coffee shop is tucked away enough that it doesn’t get too many customers."
    
    #Morgan (V.O.):
    "Taking my breaks from work and school here will be some of the best parts of my day. Taking my breaks from Nick here are some of the best parts of my week."
    
    show sausage day happy at center

    Nick "Hello friend! Are you getting lunch?"
    
    Morgan "..."
    
    show sausage day confused at center
    
    Nick "If you had listened to me earlier you would not be having this problem."
    
    Morgan "..."
    
    show sausage day sad at center
    
    Nick "The advice of my grandmother is flawless see, never leave the house without your lunch."
    
    Morgan "What are you doing here?"
    
    show sausage day at center
    
    Nick "Oh, little sister called. She needed help moving things. She asked for you, but I am a strapping young gentleman, and thought I could do heavy moving."
    
    Morgan "So, you’re here because you were helping out my lazy sister at work across the street. Great."
    
    show sausage angry at center
    
    Nick "Do not insult sister. She is good beautiful girl."
    
    Morgan "Meat. Were you, hitting, on MY SISTER?!"
    
    show sausage day confused at center
    
    Nick "I would never harm such a delicate flower."
    
    Morgan "OH IT IS ON NOW YOU YODELING SACK OF SH-"
    
    show lasagna work angry at left
    show sausage day confused at right
    
    Aria "HEY, YOU TWO, PIPE DOWN!"
    
    Morgan "Uh... dude’s trying to bang my sister..."
    
    Nick "I have no violent intentions!"
    
    Aria "I will throw you two out! This is not some kind of boxing ring, this is a coffee shop. Now you two calm down or take it outside, do I make myself clear?"
    
    show sausage day at right
    Nick "Yes, I am very calm. Always calm."
    
    #Morgan (V.O.):
    "It’s my fault I overreacted. It's just this meathead is being a creep, on my little sister!"
    
    #Morgan (V.O.):
    "and now I’m disrupting her work, even though there is like no one here to really disrupt."
    
    #Morgan (V.O.):
    "i don’t know what to do..."
    
    Morgan "I!... i..."
            
    show lasagna food at foodleft
    
    Morgan "I guess I’m sorry. I didn’t mean to cause an issue. Sorry for yelling. We’ll be going once my order’s out."
    
    Aria "Ok. You can stay if you want, just don’t both the other guests anymore than you have."
    
    #Morgan (V.O.): 
    "But, there’s no one else here..."
    
    Morgan "Will do ma’am."
    
    show sausage day happy at right
    Nick "We will do no bothering sing lady."
    
    Morgan "Sing?"
    
    show sausage day at right
    Nick "You do not recognize lady?"
    
    Morgan "Recognize what?"
    
    show sausage day surprised at right
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
    
    show sausage day angry at right
    Nick "He is not PROUD GERM-"
    
    Morgan "Whatever. Your secret is safe with us."
    
    Aria "Good. Now take your order and go."
    
    Morgan "But I thought you said we could stay?"
    
    Aria "GET OUT!"
    
    #Morgan (V.O.):
    "How did I still manage to fuck it up with saucy girl, uh now I have to get to campus and hope that she isn’t going to be mad at me if I come back, I really like it there."

#Scene 8
##################################################
label tso_intro:
    scene bg school
    with longfade
    
    show female at center
    play music morgan fadeout 1
    
    Guide "...on your left you’ll see the Student Union. You can get yourself something to eat there, get a new student ID…"
    
    hide female
    
    "I can’t believe that girl. Try to be nice and you get the door?"
    
    "Just really met someone and they are mad at me and whatever. This is the worst feeling! Ugh."
    
    "It was so disorientating."
    
    "It’s all been really disorientating!"
    
    if schoolFlag == True:
        jump school4_yes
    else:
        jump school4_no
        
label school4_yes:
    "Now I got to make sure to make a better impression here if I’m gonna be going through with this."
    
    "At least the grounds look pretty amazing. A good amount of different interesting buildings with some older more traditional style buildings and some non typical sleek designs. I wonder which one they hold the cooking classes in!"
    jump school4_done

label school4_no:
    "Let's just get this over with. Ugh why can’t I just go to the cooking building and be done already."
    
    "Their campus is some kind of hodgepodge of buildings. Some of them are almost falling apart, and some that were just built. They make it really confusing to try to commit them all to memory."
    
    "Why would they try to get you to remember so many names and locations for buildings, AND THEN make you learn everything required for the classes you have to take."
    
    "It’s just a whole lot to try to keep in your head, how am I supposed to concentrate on not messing up these first impressions with all of the new people I meet!"
    jump school4_done
    
label school4_done:
    "Wait... where am I?"
    
    "I think I lost my group."
    
    "Er, everybody else was in cooking together too, right? This was a tour for cooking students..."
    
    "I think... But that probably wouldn’t explain the high schoolers... Maybe I shou-"
    
    "*WHAM*"
    
    Morgan "AH!"
    
    show male at center
    
    Jogstudent "Oh, sorry, didn’t mean to run into you."
    
    Morgan "Yeah, sorry..."
    
    "He’s polite at least."
    
    Morgan "Uh, do you know where the cooking classes are held?"
    
    Jogstudent "Well, class rooms can be anywhere, but I think most of their classes are in that building over there."
    
    Morgan "Thanks!"
    
    hide male
    play music morgan fadeout 1
    
    "A strong concrete building, must house some pretty powerful equipment."
    
    "Also has windows on the top, maybe for more office type rooms. Do they have... Specialty business classes for restaurants!?!"
    
    # BG CLASSROOM HERE###################
    scene bg indkitchen
    with fade
    
    "So this is what culinary school is going to look like. Man, these guys have everything."
    
    show tso prez worried at center
    play music alexandra fadeout 1
    
    Alexandra "Hello? Are you by chance with the tour?"
    
    "Oh, this must be one of the high schoolers with the tour. They have some pretty neat uniforms. He’s rather slim as well, probably stays pretty darn busy."
    
    "Most private schools around here are cheap and just have you dress up, they hardly even care what color."
    
    Morgan "Yeah, I just got a bit lost."
    
    Morgan "But, I found my way here after all, so it’s all good."
    
    Morgan "This place is great. I mean, look at all this stuff they’ve got. I don’t know if I’ve seen cooking equipment this good in my life."
    
    Morgan "You know, my dad always says, a good kitchen is like a good woman, fully equipped with at least seven ovens."
    
    show tso prez flustered at center
    
    Alexandra "I’m not sure if I want to know what he meant by that..."
    
    Morgan "Neither do I honestly, but he says it all the time. I think it’s some kind of joke about my mom."
    
    Morgan "She always gives him this glares when he says it."
    
    Morgan "Then again, she always glares at him. Between that and the cat story I guess she has a point."
    
    show tso prez worried at center
    
    Alexandra "What did your father do to a cat?"
    
    Morgan "It wasn’t so much to a cat as it was around a cat. A lot of cats."
    
    Morgan "And, I don’t think he actually did anything. It’s probably a lie, or an extreme over-exaggeration..."
    
    Morgan "At least I really hope it is..."
    
    Morgan "But anyway, have you ever seen a mixer this big? You could probably mix, like, a person in that thing! Shoot, maybe two people."
    
    Morgan "Ha, mixing people, that’s kinda dirty. Though I guess that mixing up any number of people would be dirty, now that I think about it. Or mixing anything really."
    
    show tso prez flustered at center
    
    Alexandra "Uhuh. haha."
    
    Morgan "Mixers really are messy devices, no matter what you mix. It’s in their nature."
    
    Morgan "Still, I think I love this room. And to think, there’s probably a dozen more."
    
    Morgan "Filled to the brim with flippers, floppers, and so many knives. Well, hopefully there are knives."
    
    Morgan "I mean, I know it’s school so I would understand if they laid off the knives, but that would be such a disappointment. Knives are important, for any kitchen."
    
    Alexandra "Well, if you’re done ranting about dirty mixers and knives, we really should get you back to the tour."
    
    Morgan "What, isn’t this where the tour was supposed to be going?"
    
    show tso prez day at center
    
    Alexandra "No. The tour doesn’t actually go to this building at all. We don’t get too many culinary students here."
    
    Morgan "Oh, so you got lost too then? Man, your teacher must be looking everywhere for you little guy."
    
    show tso prez tired at center
    
    Alexandra "What? I’m here to look for you."
    
    Alexandra "I’m Alexandra, and I’m one of the people in charge of the tour."
    
    Alexandra "I understand that you got a little lost, but we need to get back to the tour."
    
    Alexandra "I’ve got a meeting after this with Leadership, and I’m not really sure how they’d react if I was late to my first meeting as president."
    
    "president... alexandra... oh, oh no!"
    
    show tso food at foodcenter
    
    "This is not good. This is definitely not good. They’re going to kill me. This is gonna end up in the school paper."
    
    "Certainly."
    
    "And, at a school like this, who wouldn’t read it? I’m going to lose everything for misgendering the student body president. My life is over."
    
    Alexandra "Hello?"
    
    "No, wait, I just need to apologize somehow. Think, think, I need to come up with something."
    
    "I could make her food."
    
    "No, no time. Maybe a novelty gift?"
    
    "One that says, “I’m sorry I thought you were a fourteen year-old boy, and am now imagine you as a bowl of basically the chinese equivalent of buffalo wings! But hey, that’s in the past.” Like a puppy. "
    
    "No, that is not what puppies say. Maybe there’s something in the language of flowers for this..."
    
    Alexandra "Are you ok, my dude?"
    
    "That’s it, flowers! That’s what dad always gets mom when he screws up."
    
    "It sometimes works. "
    
    "Now, which would even work?... Carnations? Tulips? Roses?"
    
    "Man, dad has had to buy so many flowers I can’t remember... i can’t think, ... i can’t-"
    
    Alexandra "Is there something wrong?"
    
    Morgan "GAH, WHY ARE FLOWERS SO DAMN COMPLICATED!"
    
    Alexandra "I-"
    
    Alexandra "Do you need a moment?"
    
    Alexandra "..."
    
    Morgan "..."
    
    Alexandra "If you do it’s no problem really."
    
    Morgan "...no, no."
    
    Morgan "Let’s just forget that this ever happened."
    
    Alexandra "Good, because we really should be going."
    
#####  END OF DEMO BOIS  ###################################
label credits:
    scene bg credits
    with longfade
    play music title fadeout 1

    call screen clickScreen


    # This ends the game.

    return
