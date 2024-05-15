# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Player = Character('Main Player')
define Derek = Character('Derek Rae', color="#808080")
define Stewart = Character('Stewart Robson', color="#808080")
define Narrator = Character('Narrator', color="#008000")
define Newspaper = Character('The Times', color="#FFFFFF")
define Press1 = Character('Reporter for The Guardians', color="#FF0000")
define Press2 = Character('Reporter for NBC Sports', color="#FF0000")
define Press3 = Character('Reporter for The Athletic', color="#FF0000")
define Manager = Character('The Gafa', color="#808080")
image The_Guardian:
    "interviewer_1.png"
    zoom 0.75

image Press_conference_background:
    "bg press_room.png"
    zoom 1.25

# adding variables that are assigned to the character
# First variable is to set a max just incase it gets to high. e.g if the player keeps making good choices with 

$ skill = 50
if skill > max_value:
        $ skill = max_value

$ speed = 50
if speed > max_value:
        $ speed = max_value

$ strength = 50
if strength > max_value:
        $ strength = max_value

$ endurance = 50
if endurance > max_value:
        $ endurance = max_value

$ tactical_awareness = 20
if tactical_awareness > max_value:
        $ tactical_awareness = max_value

$ passing = 50
if passing > max_value:
        $ passing = max_value

$ public_perception = 50
if public_perception > max_value:
        $ public_perception = max_value

$ mental_strength = 50
if mental_strength > max_value:
        $ mental_strength = max_value

$ ego = 50
if ego > max_value:
        $ ego = max_value

# The game starts here.
# We start with a loss with the team in the starting game of the league

label start:
    $ max_value = 100
    show The_Guardian at left
    Derek "And that is the tenth game of the season, and that is 10 losses in a row for Haddonfield United."
    hide The_Guardian
    show The_Guardian at right
    Stewart "The Final Score is 3 neil for Nott'm Forrest and you just have to wonder... "
    Stewart "Where will Haddonfield end up if they have consistent scorelines like that?"
    hide The_Guardian
# You are given a choice of position to play

label character_selection:
    Narrator "What position are you gonna play?"
    $ position = None
menu:
    "Striker":
            $ position = "Striker"
            jump choice1_striker
    "Midfielder":
            $ position = "Midfielder"
            jump choice1_midfielder
    "Defender":
            $ position = "Defender"
            jump choice1_defender

label choice1_striker:
    Narrator "The Striker"
    Narrator "You will be asked to be in open situations. Available for a pass in to goal."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    jump choices1_common

label choice1_midfielder:
    Narrator "The Midfielder"
    Narrator ""
    jump choices1_common

label choice1_defender:
    Narrator "The Defender"
    Narrator ""
    jump choices1_common

label choices1_common:
    Newspaper "New Signing At Haddonfield United!"
    Newspaper "Will this player be a catalyst in a team that needs it most?"

label press_conference_signing_1:
    Narrator "You have been signed to a team that is currently in the papers for their bad result on the weekend."
    Narrator "You will be asked by the press to give a statement on your teams performance and how you will help."
    scene Press_conference_background
    show The_Guardian
    Press1 "Are you aware that the team you have signed for are on a tragectary for relegation?"
    hide The_Guardian
menu:
    "I am well aware of the controversy that is surrounding this club.":
                                                                    jump press_conference_signing_a1
    "I have not been informed of this but now I am.":
                                                jump press_conference_signing_a2

label press_conference_signing_a1:
    show The_Guardian
    Press1 "That in mind, how do you think you will help the club out of this position?"
    hide The_Guardian
menu:
    "I have been signed to score goals so that is what I intend to do":
                                                                    jump press_conference_signing_a_finish
    "I will try to get open for assists and be available to a pass if necessary":
                                                                                jump press_conference_signing_a_finish

label press_conference_signing_a2:
    show The_Guardian
    Press1 "Seems like you aren't very aware of the team you have signed for."
    Press1 "How do you intend to help from the lackluster performance that occured on the weekend?"
    hide The_Guardian
menu:
    "I have been signed to score goals so that is what I intend to do":
                                                                    jump press_conference_signing_a_finish
    "I will try to get open for assists and be available to a pass if necessary":
                                                                                jump press_conference_signing_a_finish

label press_conference_signing_a_finish:
    show The_Guardian
    Press1 "Thank you for your time"
    hide The_Guardian

label press_conference_signing_b:
    Press2 "How long do you see yourself being at this team?"
menu:
    "I see myself being here for a long time":
                                            jump press_conference_signing_b2
    "I will be here for aslong as the manager needs me":
                                                    jump press_conference_signing_b2

label press_conference_signing_b2:
    Press2 "What are you opinions on the manager at the moment?"
menu:
    "From what I have heard, he is a reliable person and I trust that he will put me in the right tragectory":
                                                                                                            jump press_conference_signing_b_finish
    "From what I have seen of his team performances, I believe that he needs help to keep this team up":
                                                                                                        jump press_conference_signing_b_finish
label press_conference_signing_b_finish:
    Press2 "Can't wait to see you on the pitch"

label press_conference_signing_c:
    Press3 "How do you handle defeat, particularly when the team's performance is under scrutiny?"
    $ modest = False
    $ arrogant = False
    $ egotistical = False
menu:
    "I try to accept responsibility for my own mistakes and work harder to improve.":
                                                                                    $ modest = True
                                                                                    jump press_conference_signing_b_finish_1
    "Redirect responsibility to others and offer justifications for subpar outcomes.":
                                                                                    $ arrogant = True
                                                                                    jump press_conference_signing_b_finish_1
    "Demonstrate frustration through less constructive behavior both on and off the field.":
                                                                                            $ egotistical = True
                                                                                            jump press_conference_signing_b_finish_1

label press_conference_signing_b_finish_1:
    Press3 "Interesting..."
    Press3 "As a newcomer to the sport, what do you hope to achieve in your rookie season?"
    $ inexperience = False
    $ cocky = False
    $ ego = False
menu:
    "I'm eager to learn and adapt to the challenges of professional competition, aiming to make a significant impact on the team.":
                                                                                                                                jump press_conference_signing_b_ending
    "I've been training relentlessly to prepare for this opportunity and am confident in my abilities to contribute to the team's success.":
                                                                                                                                jump press_conference_signing_b_ending
    "My goal is to become a fan favorite and inspire others to pursue their dreams in this sport.": 
                                                                                                    jump press_conference_signing_b_ending
label press_conference_signing_b_ending:
    Press3 "Thank you for your time."

return

