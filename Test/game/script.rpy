# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
label cook_start:
    menu:
        "Food 1":
            jump food_1
        "Food 2":
            jump food_2
        "Notes":
            jump notes
            
label food_1:
    "Description of Food 1"
    menu:
        "Prepare this?":
            "You made Food 1"
            jump done
        "Back to recipie list":
            jump cook_start

label food_2:
    "Description of Food 2"
    menu:
        "Prepare this?":
            "You made Food 2"
            jump done
        "Back to recipie list":
            jump cook_start

label notes:
    menu:
        "Note 1":
            jump note_1
        "Note 2":
            jump note_2
        "Recipie List":
            jump cook_start
    
label note_1:
    "Text for note 1"
    jump notes

label note_2:
    "Text for note 2"
    jump notes

label done:
    "You have completed the minigame"

    # This ends the game.

    return
