﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Player = Character('Main Player')
define Derek = Character('Derek Rae', color="#808080")
define Stewart = Character('Stewart Robson', color="#808080")
define Narrator = Character('The Narrator', color="#008000")
define Newspaper = Character('The Times', color="#FFFFFF")
define Press1 = Character('The Guardians', color="#FF0000")
define Press2 = Character('NBC Sports', color="#FF0000")
define Press3 = Character('The Athletic', color="#FF0000")
define Manager = Character('The Gafa', color="#808080")
define Captain = Character('The Captain', color="#00008B")

image Locker_Room:
    "bg locker_room.png"
    zoom 1.45

image Breaking_News_Background:
    "bg breaking_news.png"
    zoom 1.45

image Neutral_Background:
    "bg neutral.png"
    zoom 1.45

image Captain_Sprite:
    "the_captain.png"
    zoom 0.80

image Narrator:
    "narrator.png"
    zoom 0.85

image The_Athletic:
    "interviewer_1.png"
    zoom 0.75

image Press_conference_background:
    "bg press_room.png"
    zoom 1.25 

image The_Gafa:
    "manager.png"
    zoom 0.90

image Gafa_Room:
    "bg gafa_room.png"
    zoom 1.45
# The game starts here.
# We start with a 10th loss with the team in the starting game of the playthrough

label start:
    scene Neutral_Background
    show The_Athletic at left
    Derek "And that is the tenth game of the season, and that is 10 losses in a row for Haddonfield United."
    hide The_Athletic
    show The_Athletic at right
    Stewart "The Final Score is 3 neil for Nott'm Forrest and you just have to wonder... "
    Stewart "Where will Haddonfield end up if they have consistent scorelines like that?"
    hide The_Athletic
# You are given a choice of position to play
# This choice also comes with a base value of 0 with all stats
label character_selection:
    show Narrator at left
    Narrator "What position are you going to play?"
    hide Narrator 
    $ position = None
    $ pace = 0
    $ shooting = 0
    $ passing = 0
    $ defending = 0
    $ dribbling = 0
    $ physical = 0

# From the choices they will all equal a base of 320 stats as to not have a class that is better.

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

# From the choice of position there will be a brief summary of the position to give to the user some context.

label choice1_striker:
    show Narrator at left
    Narrator "The Striker"
    Narrator "A striker in football is a forward player primarily tasked with scoring goals for their team by taking shots on the opposing team's goal."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    hide Narrator
    jump choices1_common

label choice1_midfielder:
    show Narrator at left
    Narrator "The Midfielder"
    Narrator "A midfielder in football is a player positioned between the defenders and forwards, responsible for both defensive duties and initiating attacking plays."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    hide Narrator
    jump choices1_common

label choice1_defender:
    show Narrator at left
    Narrator "The Defender"
    Narrator "A defender in football is a player tasked with protecting their team's goal and preventing the opposing team from scoring by intercepting passes, tackling opponents, and providing defensive support to their teammates."
    Narrator "The press will be onto you if any bad performances arise, and whether you're the reason your team lost the game."
    jump choices1_common
    hide Narrator

# Little newspaper snippet to show the player has been signed to the team

label choices1_common:
    show Breaking_News_Background
    with dissolve
    Newspaper "New Signing At Haddonfield United!"
    Newspaper "Will this player be a catalyst in a team that needs it most?"

# The player is introduce to the press conference where they will be asked questions about their signing to the team

label press_conference_signing_1:
    $ press_perception = 50
    show Narrator at left
    Narrator "You have been signed to a team that is currently in the papers for their bad result on the weekend."
    Narrator "You will be asked by the press to give a statement on your teams performance and how you will help."
    hide Narrator
    scene Press_conference_background
    with dissolve
    Press1 "Are you aware that the team you have signed for are on a tragectary for relegation?"
menu:
    "I am well aware of the controversy that is surrounding this club.":
                                                                    $ press_perception += 5
                                                                    jump press_conference_signing_a1
    "I have not been informed of this but now I am.":
                                                $ press_perception -= 5
                                                jump press_conference_signing_a2

label press_conference_signing_a1:
    Press1 "That in mind, how do you think you will help the club out of this position?"
menu:
    "I have been signed to score goals so that is what I intend to do.":
                                                                    jump press_conference_signing_a_finish
    "I will try to get open for assists and be available to a pass if necessary.":
                                                                                jump press_conference_signing_a_finish

label press_conference_signing_a2:
    Press1 "Seems like you aren't very aware of the team you have signed for..."
    Press1 "How do you intend to help from the lackluster performance that occured on the weekend?"
menu:
    "I have been signed to score goals so that is what I intend to do.":
                                                                    jump press_conference_signing_a_finish
    "I will try to get open for assists and be available to a pass if necessary.":
                                                                                jump press_conference_signing_a_finish

label press_conference_signing_a_finish:
    Press1 "Thank you for your time."

label press_conference_signing_b:
    Press2 "How long do you see yourself being at this team?"
menu:
    "I see myself being here for a long time.":
                                            $ press_perception += 5
                                            jump press_conference_signing_b2
    "I will be here for aslong as the manager needs me.":
                                                    jump press_conference_signing_b2

label press_conference_signing_b2:
    Press2 "What are you opinions on the manager at the moment?"
menu:
    "From what I have heard, he is a reliable person and I trust that he will put me in the right tragectory.":
                                                                                                            $ press_perception -= 5
                                                                                                            jump press_conference_signing_b_finish
    "From what I have seen of his team performances, I believe that he needs help to keep this team up.":
                                                                                                        $ press_perception += 5
                                                                                                        jump press_conference_signing_b_finish
label press_conference_signing_b_finish:
    Press2 "I'm sure he would be interested to hear your comments..."
    Press2 "Can't wait to see you on the pitch."

# This is the first time the player will be asked about their personality and how they handle defeat
# No matter what choice you make in this scene there will always be a negative outcome

label press_conference_signing_c:
    show The_Athletic
    Press3 "How do you handle defeat, particularly when the team's performance is under scrutiny?"
    $ modest = False
    $ arrogant = False
    $ egotistical = False
    hide The_Athletic
menu:
    "I try to accept responsibility for my own mistakes and work harder to improve.":
                                                                                    $ press_perception += 5
                                                                                    $ modest = True
                                                                                    jump press_conference_signing_b_finish_1
    "Redirect responsibility to others and offer justifications for subpar outcomes.":
                                                                                    $ press_perception -= 5
                                                                                    $ arrogant = True
                                                                                    jump press_conference_signing_b_finish_1
    "Demonstrate frustration through less constructive behavior both on and off the field.":
                                                                                            $ press_perception -= 10
                                                                                            $ egotistical = True
                                                                                            jump press_conference_signing_b_finish_1

label press_conference_signing_b_finish_1:
    show The_Athletic
    Press3 "Interesting..."
    Press3 "As a newcomer to the sport, what do you hope to achieve in your rookie season?"
    $ inexperience = False
    $ cocky = False
    $ ego = False
    hide The_Athletic
menu:
    "I'm eager to learn and adapt to the challenges of professional competition, aiming to make a significant impact on the team.":
                                                                                                                                $ inexperience = True      
                                                                                                                                jump press_conference_signing_ending
    "I've been training relentlessly to prepare for this opportunity and am confident in my abilities to contribute to the team's success.":
                                                                                                                                    $ cocky = True
                                                                                                                                    jump press_conference_signing_ending
    "My goal is to become a fan favorite and inspire others to pursue their dreams in this sport.": 
                                                                                                    $ ego = True
                                                                                                    jump press_conference_signing_ending
label press_conference_signing_ending:
    show The_Athletic
    Press3 "Thank you for your time."
    hide The_Athletic

# The player is then introduced to the manager

label meet_the_manager:
    show Narrator at left
    Narrator "After that eventful press conference..."
    Narrator "It's time to meet the gafa."
    scene Gafa_Room
    with dissolve
    show The_Gafa at left
    Manager "How was the press conference?"
    hide The_Gafa
menu: 
    "It went a lot better than I expected":
                                            jump meet_the_manager_a
    "Some of those questions were pretty hardcore":
                                                    jump meet_the_manager_b

label meet_the_manager_a:
    show The_Gafa at left
    Manager "That's good to hear."
    Manager "I hope you can bring some good results to the team."
    jump meet_the_manager_finish

label meet_the_manager_b:
    show The_Gafa at left
    Manager "I'm sorry to hear that."
    Manager "Just remember that the press are always looking for a story."
    jump meet_the_manager_finish

label meet_the_manager_finish:
    Manager "Now it's time to meet the captain."
    hide The_Gafa
    jump meet_the_captain

# The player is then introduced to the captain of the team

label meet_the_captain:
    $ captain_impression = 25
    scene Neutral_Background
    with dissolve
    show Captain_Sprite at left
    show The_Gafa at right
    Manager "This is your captain..."
    Manager "If you have any questions about the team..."
    Manager "Ask him"
    hide The_Gafa
    Captain "See ya gafa"
    Captain "Hey, can we talk for a minute?"
    scene Locker_Room
    with dissolve
    show Captain_Sprite at left
    Captain "Look, I am going to be straight with you..."
    Captain "I was not thrilled when I heard we were signing you."
    Captain "This team has been building something special, and I am not convinced you are what we need right now."
    Captain "We have got a tight-knit group here."
    Captain "We know each of our strengths,"
    Captain "weaknesses,"
    Captain "and how to cover for each other."
    Captain "You coming in throws a wrench into that dynamic."
    hide Captain_Sprite
menu:
    "I understand. I just want to contribute and prove myself.":
                                                            $ captain_impression += 5
                                                            jump continue_meet_the_captain
                                                            
label continue_meet_the_captain:
    show Captain_Sprite at left
    Captain "*nods*"
    Captain "That is all well and good, but words do not mean much on the pitch."
    Captain "Around here, respect is earned through hard work and dedication, not just showing up with a big contract."
    Captain "You need to put in the effort, every single day,"
    Captain "and prove that you are not just here for yourself but for the team."
    hide Captain_Sprite
menu:
    "I will. I will not let you down.":
                                    $ captain_impression += 10
                                    jump continue_meet_the_captain_will
    "What do you need from me?":
                            $ captain_impression += 5
                            jump continue_meet_the_captain_need
    "I understand your concerns, but I am here to make a difference.":
                                                                    $ captain_impression += 0
                                                                    jump continue_meet_the_captain_understand
    "I think you are underestimating me.":
                                        $ captain_impression -= 5 
                                        jump continue_meet_the_captain_underestimate

label continue_meet_the_captain_will:
    show Captain_Sprite at left
    Captain "We will see."
    Captain "Actions speak louder than words."
    Captain "Show me on the field."
    Captain "Until then..."
    Captain "do not expect any favors or special treatment."
    Captain "You are just another player until you prove otherwise."
    jump finish_meet_the_captain
                                                               
label continue_meet_the_captain_need:
    show Captain_Sprite at left
    Captain "Commitment."
    Captain "Consistency."
    Captain "A willingness to listen and learn."
    Captain "This is not about you fitting into our system;"
    Captain "it is about becoming a part of our family."
    Captain "You need to show everyone here that you are willing to put the team first."
    hide Captain_Sprite
menu:
    "Understood. I am ready to do whatever it takes.":
                                                    $ captain_impression += 5
                                                    jump continue_meet_the_captain_need_1

label continue_meet_the_captain_need_1:
    show Captain_Sprite at left
    Captain "That is a start."
    Captain "Keep that attitude,"
    Captain "and you might just earn a place here."
    Captain "It is up to you now."
    jump finish_meet_the_captain

label continue_meet_the_captain_understand:
    show Captain_Sprite at left
    Captain "Making a difference is not about making headlines."
    Captain "It is about the little things..."
    Captain "tracking back,"
    Captain "making the right pass,"
    Captain "supporting your teammates."
    Captain "Show me that you can do that,"
    Captain "and meybe we will see eye to eye."
    hide Captain_Sprite
menu:
    "I can do that. Just watch.":
                                $ captain_impression += 5
                                jump continue_meet_the_captain_understand_1

label continue_meet_the_captain_understand_1:
    show Captain_Sprite at left
    Captain "Alright."
    Captain "You have confidence,"
    Captain "I will give you that."
    Captain "But confidence alone will not cut it."
    Captain "Back it up with hard work, and we'll see."
    jump finish_meet_the_captain    

label continue_meet_the_captain_underestimate:
    show Captain_Sprite at left
    Captain "Underestimating you?"
    Captain "This is not about what I think of you;"
    Captain "it is about what you bring to the team."
    Captain "Drop the attitude and focus on proving yourself."
    Captain "If you ca not do that, you will not last long here."
    jump finish_meet_the_captain

label finish_meet_the_captain:
    Captain "So, here is the deal..."
    Captain "you have got a lot to prove."
    Captain "Show up, put in the work, and earn your place."
    Captain "Because right now,"
    Captain "you are just another name on the roster."
    Captain "Got it?"
    hide Captain_Sprite
menu:
    "Got it":
            $ captain_impression += 5
            jump finish_meet_the_captain_1

label finish_meet_the_captain_1:
    show Captain_Sprite at left
    Captain "Good."
    Captain "I will see you tomorrow."
    jump end_first_day

# Depending on the choice of last answers to questions on press conference there will be a news report on response.
# Links back from line 210-248

label end_first_day:
    hide Captain_Sprite
    hide Locker_Room
    scene Breaking_News_Background
    with fade

#label end_first_day_news_:
    #if $ modest = True:
    #Press3 "New signing "





return

