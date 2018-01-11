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


    #END OF DEMO BOIS



    # This ends the game.

    return
