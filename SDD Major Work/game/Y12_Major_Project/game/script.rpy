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

# The game starts here.
# We start with a loss with the team in the starting game of the league

label start:
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
    $ pace = 0
    $ shooting = 0
    $ passing = 0
    $ defending = 0
    $ dribbling = 0
    $ physical = 0

menu:
    "Striker":
            $ position = "Striker"
            $ pace = 75
            $ shooting = 80
            $ passing = 40
            $ defending = 20
            $ dribbling = 60
            $ physical = 45
            # all up stats for striker is 320
            jump choice1_striker
    "Midfielder":
            $ position = "Midfielder"
            $ pace = 55
            $ shooting = 50
            $ passing = 75
            $ defending = 40
            $ dribbling = 50
            $ physical = 50
            # all up stats for midfielder is 320
            jump choice1_midfielder
    "Defender":
            $ position = "Defender"
            $ pace = 45
            $ shooting = 30
            $ passing = 45
            $ defending = 80
            $ dribbling = 40
            $ physical = 80
            # all up stats for defender is 320
            jump choice1_defender

label choice1_striker:
    Narrator "The Striker"
    Narrator "A striker in football is a forward player primarily tasked with scoring goals for their team by taking shots on the opposing team's goal."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    jump choices1_common

label choice1_midfielder:
    Narrator "The Midfielder"
    Narrator "A midfielder in football is a player positioned between the defenders and forwards, responsible for both defensive duties and initiating attacking plays."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    jump choices1_common

label choice1_defender:
    Narrator "The Defender"
    Narrator "A defender in soccer is a player tasked with protecting their team's goal and preventing the opposing team from scoring by intercepting passes, tackling opponents, and providing defensive support to their teammates."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
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

