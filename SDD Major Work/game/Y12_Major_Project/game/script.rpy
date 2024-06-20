# The script of the game goes in this file.

# ChatGPT Code For Images Name "Artisitic Visionary"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character('[povname]')
define Commentator = Character('Commentator', color="#808080")
define Narrator = Character('The Narrator', color="#008000")
define Newspaper = Character('The Times', color="#FFFFFF")
define Press1 = Character('The Guardians', color="#FF0000")
define Press2 = Character('NBC Sports', color="#FF0000")
define Press3 = Character('The Athletic', color="#FF0000")
define Manager = Character('The Gafa', color="#808080")
define Captain = Character('The Captain', color="#00008B")
define Creator = Character('The Creator', color="#A020F0")
define Doc = Character('Physio', color='#FFFFFF')

# Declare images used by this game. The zoom argument scales the image.

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

image Commentator:
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
    show Commentator at left
    with dissolve
    Commentator "And that is the 22nd game of the season, and that is only 19 points for Haddonfield United."
    Commentator "The Final Score is 4-0 for Haddonfield United and that is their first good result of the 22 matches, which makes you wonder... "
    Commentator "Where will Haddonfield end up if they have consistent scorelines like that?"
    hide Commentator
    jump character_selection

# You are given a choice of position to play
# This choice also comes with a base value of 0 with all stats
# This is to ensure that the player does not have an advantage over the other classes

label character_selection:
    $ povname = renpy.input("What is my name?", length=32)
    pov "My name is [povname]."
    show Narrator at left
    with dissolve
    Narrator "Interesting Name Choice."
    Narrator "You are the new striker for Haddonfield United."
    hide Narrator 
    $ pace = 70
    $ shooting = 80
    $ passing = 45
    $ dribbling = 55
    $ physical = 45
    jump choices1_common

# Little newspaper snippet to show the player has been signed to the team

label choices1_common:
    show Breaking_News_Background
    with dissolve
    Newspaper "New Striker Signing At Haddonfield United!"
    Newspaper "Will this player be a catalyst in a team that needs it most?"

# The player is introduce to the press conference where they will be asked questions about their signing to the team

label press_conference_signing_1:
    $ press_perception = 50
    show Narrator at left
    with dissolve
    Narrator "You have been signed to a team that is currently in the papers for their bad results throughout the season."
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
    Press3 "How do you handle defeat, particularly when the team's performance is under scrutiny?"
    $ modest = False
    $ arrogant = False
    $ egotistical = False
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
    Press3 "Interesting..."
    Press3 "As a newcomer to the sport, what do you hope to achieve in your rookie season?"
    $ inexperience = False
    $ cocky = False
    $ ego = False
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
    Press3 "Thank you for your time."

# The player is then introduced to the manager

label meet_the_manager:
    show Narrator at left
    with dissolve
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
    with fade
    Manager "That's good to hear."
    Manager "I hope you can bring some good results to the team."
    jump meet_the_manager_finish

label meet_the_manager_b:
    show The_Gafa at left
    with fade
    Manager "I'm sorry to hear that."
    Manager "Just remember that the press are always looking for a story."
    jump meet_the_manager_finish

label meet_the_manager_finish:
    Manager "Now it's time to meet the captain."
    hide The_Gafa
    jump meet_the_captain

# The player is then introduced to the captain of the team
# The captain will give the player a brief on what is expected of them

label meet_the_captain:
    $ captain_impression = 25
    scene Neutral_Background
    with dissolve
    show Captain_Sprite at left
    with fade
    show The_Gafa at right
    with fade
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

# The player is then given a choice of what they want to say to the captain
# Depending on the choice the captain will have a different response
                                                            
label continue_meet_the_captain:
    show Captain_Sprite at left
    with fade
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
    with fade
    Captain "We will see."
    Captain "Actions speak louder than words."
    Captain "Show me on the field."
    Captain "Until then..."
    Captain "do not expect any favors or special treatment."
    Captain "You are just another player until you prove otherwise."
    jump finish_meet_the_captain
                                                               
label continue_meet_the_captain_need:
    show Captain_Sprite at left
    with fade
    Captain "Commitment."
    Captain "Consistency."
    Captain "A willingness to listen and learn."
    Captain "This is not about you fitting into our system;"
    Captain "it is about becoming a part of our family."
    Captain "You need to show everyone here that you are willing to put the team first."
    hide Captain_Sprite
    with fade
menu:
    "Understood. I am ready to do whatever it takes.":
                                                    $ captain_impression += 5
                                                    jump continue_meet_the_captain_need_1

label continue_meet_the_captain_need_1:
    show Captain_Sprite at left
    with fade
    Captain "That is a start."
    Captain "Keep that attitude,"
    Captain "and you might just earn a place here."
    Captain "It is up to you now."
    jump finish_meet_the_captain

label continue_meet_the_captain_understand:
    show Captain_Sprite at left
    with fade
    Captain "Making a difference is not about making headlines."
    Captain "It is about the little things..."
    Captain "tracking back,"
    Captain "making the right pass,"
    Captain "supporting your teammates."
    Captain "Show me that you can do that,"
    Captain "and maybe we will see eye to eye."
    hide Captain_Sprite
menu:
    "I can do that. Just watch.":
                                $ captain_impression += 5
                                jump continue_meet_the_captain_understand_1

label continue_meet_the_captain_understand_1:
    show Captain_Sprite at left
    with fade
    Captain "Alright."
    Captain "You have confidence,"
    Captain "I will give you that."
    Captain "But confidence alone will not cut it."
    Captain "Back it up with hard work, and we'll see."
    jump finish_meet_the_captain    

label continue_meet_the_captain_underestimate:
    show Captain_Sprite at left
    with fade
    Captain "Underestimating you?"
    Captain "This is not about what I think of you;"
    Captain "it is about what you bring to the team."
    Captain "Drop the attitude and focus on proving yourself."
    Captain "If you can't do that, you will not last long here."
    jump finish_meet_the_captain

# The player is then given a brief on what is expected of them

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
    with fade
    Captain "Good."
    Captain "I will see you tomorrow."
    jump end_first_day

# Depending on the choice of last answers to questions on press conference there will be a news report on response.
# Links back from line 210-248

label end_first_day:
    hide Captain_Sprite
    scene Breaking_News_Background
    with fade
    jump end_first_day_news_modest

# From choices that were made in the press conference the player will be given a news report on their response
# most of the time the player will be given a negative response

label end_first_day_news_modest:
    if modest == True:
        Press3 "Player admitted to recurring errors and the need for continual improvement,"
        Press3 "raising questions about his reliability and consistency on the field."
        Press3 "Critics argue that his statement highlights a troubling pattern of underperformance and a lack of accountability."
        jump end_first_day_news_inexperience
    if modest == False:
        jump end_first_day_news_arrogant

label end_first_day_news_arrogant:
    if arrogant == True:
        Press3 "In new signing's interview,"
        Press3 "when asked about the possibility of poor team performance,"
        Press3 "player seems to try to deflect blame onto his teammates and external factors."
        Press3 "'Redirect responsibility to others and offer justifications for subpar outcomes,' He said."
        Press3 "Critics are calling out this player for his apparent unwillingness to take accountability for the team's struggles,"
        Press3 "suggesting that this attitude might be contributing to the ongoing issues within the squad."
        jump end_first_day_news_inexperience
    if arrogant == False:
        jump end_first_day_news_egotistical

label end_first_day_news_egotistical:
    if egotistical == True:
        Press3 "Player has openly admitted to expressing frustration through unproductive behavior both on and off the field."
        Press3 "In a recent interview,"
        Press3 "he acknowledged, 'I demonstrate my frustration through less constructive behavior both on and off the field.'"
        Press3 "This admission raises concerns about his professionalism and commitment to maintaining a positive team environment."
        jump end_first_day_news_inexperience

label end_first_day_news_inexperience:
    if inexperience == True:
        Press3 "Additionally, in a recent interview, the player seemed more focused on personal ambitions rather than team success, saying,"
        Press3 "'I'm eager to learn and adapt to the challenges of professional competition, aiming to make a significant impact on the team.'"
        Press3 "Critics argue that this statement reveals a self-centered attitude, "
        Press3 "with the player prioritizing their own development over the collective goals of the team."
    if inexperience == False:
        jump end_first_day_news_cocky

label end_first_day_news_cocky:
    if cocky == True:
        Press3 "Additionally, despite the confidence assertions from the player,"
        Press3 "some critics argue that talk is cheap without the results to back it up."
        Press3 "With speculation swirling around whether their performance will match their contract,"
        Press3 "all eyes will be on the player as they take the field."
        Press3 "Will their training translate into tangible success, or will it fall short of expectations?"
    if cocky == False:
        jump end_first_day_news_ego

label end_first_day_news_ego:
    if ego == True:
        Press3 "In a recent interview, the player claimed their goal is 'to become a fan favorite,'"
        Press3 "revealing a focus on personal popularity rather than team success."
        Press3 "Critics argue that this self-centered attitude could undermine team morale"
        Press3 "and detract from the collective effort needed to achieve victory."
        jump end_first_day_news_end

label end_first_day_news_end:
    Press3 "Only time will tell if this player's ambition will lead to team glory or personal gain."
    Press3 "For now, fans and analysts alike will be watching closely."
    Press3 "This is Laurence Mizzi with the Athletic, signing off. Stay tuned for more updates."

label second_day:
    scene Neutral_Background
    with fade
    show Narrator at left
    with dissolve
    Narrator "This is your second day."
    Narrator "In order for you to go any further, you're gonna have to head over to the medical wing for a check-up."
    Narrator "The doctors will ensure everything is in top shape."
    Narrator "Then, you'll complete some fitness assessments."
    Narrator "This will help you understand your physical condition and tailor your training accordingly."
    hide Narrator
    with dissolve
    jump check_up_first_week

label check_up_first_week:
    Doc "Welcome to the medical wing."
    Doc "I'm the team's physio, and I'll be conducting your check-up today."
    Doc "Let's start with a few basic checks to ensure everything is in top shape."
    jump check_up_first_week_progress

label check_up_first_week_progress:
    Doc "Now that we've covered the basics, we'll move on to the fitness assessments."
    Doc "These will help us understand your physical condition better and how your stats are looking."
    Doc "We'll have you do a series of tasks including a treadmill run, some strength tests, and flexibility measurements. Ready?"
menu:
    "Yes I am":
            jump check_up_first_week_progress_treadmill

label check_up_first_week_progress_treadmill:
    Doc "Excellent. We'll begin with the treadmill."
    Doc "I need you to run at a steady pace. Don't push too hard..." 
    Doc "we want to see your natural speed level."
    jump check_up_first_week_progress_strength

label check_up_first_week_progress_strength:
    Doc "Now let's move on to the strength tests."
    Doc "We'll measure your upper and lower body strength with some weight exercises."
    jump check_up_first_week_progress_agility

label check_up_first_week_progress_agility:
    Doc "The last part of the assessment is checking your agility."
    Doc "We'll do a few simple stretches to see your range of motion."

label check_up_first_week_end:
    Doc "Here are your stats"
# Need to display stats here so player knows what their stats are.

# The player is then given a choice of what they want to do next
# They are being told what choice they have of training
# Depending on the choice the player makes, their stats will change

label training_session_1_1:
    $ stamina = 100
    show Narrator at left
    with dissolve
    Narrator "This time, it's all about you."
    Narrator "We're diving deep into individual skill development."
    Narrator "You'll be working closely with specialized coaches,"
    Narrator "fine-tuning those technical drills,"
    Narrator "honing your positional play, and diving into personalized exercises designed just for you."
    Narrator "This is where the magic happens,"
    Narrator "where every touch, every move, brings you closer to your peak performance. Let's get to work."
    Narrator "This first set of training will be light, low risk, but also low reward."
    Narrator "What are you going to train first?"
    hide Narrator
    with dissolve
menu:
    "pace":
        jump training_session_1_1_pace
    "shooting":
            jump training_session_1_1_shooting
    "passing":
            jump training_session_1_1_passing
    "dribbling":
            jump training_session_1_1_dribbling
    "physical":
            jump training_session_1_1_physical
    "skip training...":
                    jump second_day_continue

label training_session_1_1_pace:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ pace += 5
            $ stamina -= 2
            jump second_day_continue
    "1 hour":
            $ pace += 10
            $ stamina -= 5
            jump second_day_continue

label training_session_1_1_shooting:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ shooting += 5
            $ stamina -= 2
            jump second_day_continue
    "1 hour":
            $ shooting += 10
            $ stamina -= 5
            jump second_day_continue

label training_session_1_1_passing:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ passing += 5
            $ stamina -= 2
            jump second_day_continue
    "1 hour":
            $ passing += 10
            $ stamina -= 5
            jump second_day_continue

label training_session_1_1_dribbling:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ dribbling += 5
            $ stamina -= 2
            jump second_day_continue
    "1 hour":
            $ dribbling += 10
            $ stamina -= 5
            jump second_day_continue

label training_session_1_1_physical:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ physical += 5
            $ stamina -= 2
            jump second_day_continue
    "1 hour":
            $ physical += 10
            $ stamina -= 5
            jump second_day_continue

# The player is then given a choice of what they want to do next
# They can either meet up with their teammates or go to their second training session
# Depending on the choice the player makes, their relationship with their teammates will change

label second_day_continue:
    $ team_impression = 50
    show Narrator at left
    with dissolve
    Narrator "You have finished your first training session for the first week."
    Narrator "You can now have lunch with your teammates or you can jump straight into your second training session."
    hide Narrator
    with dissolve
menu:
    "Meet up with teammates":
                        $ team_impression += 10
                        jump meet_teammates_1

    "Go to second training":
                        $ team_impression -= 10
                        show Narrator at left
                        with dissolve
                        Narrator "Your teammates will remember this..."
                        hide Narrator
                        with dissolve
                        jump training_session_1_2

label meet_teammates_1:
    show Narrator at left
    with dissolve
    Narrator "You have decided to meet up with your teammates."
    Narrator "This is a great opportunity to bond with them and build relationships."
    Narrator "You head over to the team cafeteria where your teammates are already gathered."
    Narrator "What food will you be having?"
    hide Narrator
    with dissolve
menu:
    "Healthy salad":
                $ team_impression += 5
                $ stamina += 5
                jump meet_teammates_1_2
    "Burger and fries":
                $ stamina -= 5
                jump meet_teammates_1_2
    "Protein shake":
                $ team_impression += 5
                $ stamina += 10
                jump meet_teammates_1_2
    "Skip lunch...":
                $ team_impression -= 5
                jump training_session_1_2

label meet_teammates_1_2:
    show Narrator at left
    with dissolve
    Narrator "You sit down with your teammates and engage in some light conversation."
    Narrator "You get to know them better, and they get to know you."
    Narrator "This is a great way to build camaraderie and trust within the team."
    Narrator "After lunch, you head back to the training ground for your second session."
    hide Narrator
    with dissolve
    jump training_session_1_2

label training_session_1_2:
    show Narrator at left
    with dissolve
    Narrator "Welcome to your second training session."
    Narrator "This session will be more intense, high risk, but also high reward."
    Narrator "What are you going to train this time?"
    hide Narrator
    with dissolve
menu:
    "pace":
        jump training_session_1_2_pace
    "shooting":
            jump training_session_1_2_shooting
    "passing":
            jump training_session_1_2_passing
    "dribbling":
            jump training_session_1_2_dribbling
    "physical":
            jump training_session_1_2_physical
    "skip training...":
                    jump match_day_1

label training_session_1_2_pace:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ pace += 10
            $ stamina -= 5
            jump match_day_1
    "1 hour":
            $ pace += 15
            $ stamina -= 10
            jump match_day_1

label training_session_1_2_shooting:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ shooting += 10
            $ stamina -= 5
            jump match_day_1
    "1 hour":
            $ shooting += 15
            $ stamina -= 10
            jump match_day_1

label training_session_1_2_passing:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ passing += 10
            $ stamina -= 5
            jump match_day_1
    "1 hour":
            $ passing += 15
            $ stamina -= 10
            jump match_day_1

label training_session_1_2_dribbling:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ dribbling += 10
            $ stamina -= 5
            jump match_day_1
    "1 hour":
            $ dribbling += 15
            $ stamina -= 10
            jump match_day_1

label training_session_1_2_physical:
    show Narrator at left
    with dissolve
    Narrator "How long do you want to train this attribute?"
    hide Narrator
    with dissolve
menu:
    "30 minutes":
            $ physical += 10
            $ stamina -= 5
            jump match_day_1
    "1 hour":
            $ physical += 15
            $ stamina -= 10
            jump match_day_1

# There is a list of teams that have a set of points for the amount of points they had at that point in the Premier League.

label match_day_1:
    $ manchester_city = 46
    $ arsenal = 46
    $ liverpool = 51
    $ aston_villa = 43
    $ tottenham = 40
    $ chelsea = 31
    $ newcastle = 32
    $ manchester_united = 35
    $ west_ham = 36
    $ crystal_palace = 24
    $ brighton = 32
    $ bournemouth = 26
    $ fulham = 25
    $ wolves = 29
    $ everton = 28
    $ brentford = 20
    $ nottm_forest = 20
    $ haddonfield_united = 19
    $ burnly = 12
    $ sheffield_united = 10
    show Narrator at left
    with dissolve
    Narrator "It's match day."
    Narrator "You've trained hard, built relationships with your teammates, and honed your skills."
    Narrator "Now it's time to put it all to the test on the pitch."
    Narrator "The team is counting on you to make a difference."
    hide Narrator
    with dissolve
    jump match_day_1_start

label match_day_1_start:
    $ score_for_1 = 0
    $ score_against_1 = 4
    show Narrator at left
    with dissolve 
    Narrator "In reality Newcastle drew this game 4-4 so you'll have options to make this scoreline better then the realife life result."
    hide Narrator
    with dissolve
    show Commentator at left
    with dissolve
    Commentator "Here we are at St. James' Park for Haddonfield United v Newcastle United"
    Commentator "The referee blows the whistle, and the game begins."
    hide Commentator
    with dissolve
    jump match_day_1_play_s_1

# Striker scenario 13th minute

label match_day_1_play_s_1:
        show Commentator at left
        Commentator "Haddonfield United's new signing [povname] starts in his new position as the central forward, ready to lead the attack."
        Commentator "We are going into the 13th minute and..."
        Commentator "Haddonfield United's new signing receives a through ball from the midfield, finding himself one-on-one with the goalkeeper just outside the penalty box."
        hide Commentator
        with dissolve
menu:
    "Quick shot":
                jump match_day_1_play_s_quick_shot
    "Dribble past":
                jump match_day_1_play_s_dribble_past

label match_day_1_play_s_quick_shot:
    if shooting >= 80:
        show Commentator at left
        Commentator "[povname] takes a quick shot on goal."
        Commentator "AND ITS IN!!!"
        Commentator "The ball sails past the goalkeeper into the net, giving Haddonfield United an early goal."
        $ score_for_1 += 1
        jump match_day_1_play_s_2
    if shooting < 80:
        show Commentator at left
        Commentator "[povname] takes a quick shot on goal."
        Commentator "AND HE'S MISSED!!!"
        Commentator "The shot is rushed and goes wide of the post, missing a clear opportunity."
        jump match_day_1_play_s_2

label match_day_1_play_s_dribble_past:
    if dribbling >= 60:
        show Commentator at left
        Commentator "[povname] tries to dribble past the keeper."
        Commentator "HE'S DONE IT!!!"
        Commentator "[povname] skillfully dribbles around the goalkeeper and slots the ball into the empty net."
        $ score_for_1 += 1
        jump match_day_1_play_s_2
    if dribbling < 60:
        show Commentator at left
        Commentator "[povname] tries to dribble past the keeper"
        Commentator "OH NO!!!"
        Commentator "The goalkeeper anticipates the move and dives to steal the ball from [povname] feet."
        jump match_day_1_play_s_2

label match_day_1_play_s_2:
    show Commentator at left
    with dissolve
    Commentator "It is the 28th minute."
    Commentator "[povname] now finds himself at the edge of the penalty area with the ball at his feet."
    Commentator "He notices a teammate, making a run into the box."
    hide Commentator
    with dissolve
menu:
    "direct shot":
                jump match_day_1_play_s_direct_shot
    "make pass":
            jump match_day_1_play_s_make_pass

label match_day_1_play_s_direct_shot:
    if shooting >= 85:
        show Commentator at left
        Commentator "[povname] attempts a direct shot on goal"
        Commentator "And its in!!!"
        Commentator "The shot is powerful and accurate, beating the goalkeeper adding to Haddonfield's score."
        $ score_for_1 += 1
        jump match_day_1_play_s_3
    if shooting < 85:
        show Commentator at left
        Commentator "[povname] attempts a direct shot on goal"
        Commentator "And oh no!!!"
        Commentator "The shot is blocked by a defender who lunges in at the last moment."
        jump match_day_1_play_s_3

label match_day_1_play_s_make_pass:
    if passing >= 50:
        show Commentator at left
        Commentator "[povname] goes to make the pass"
        Commentator "I don't believe it!!!"
        Commentator "He receives the ball and scores, showcasing excellent teamwork."
        $ score_for_1 += 1
        jump match_day_1_play_s_3
    if passing < 50:
        show Commentator at left
        Commentator "[povname] goes to make the pass"
        Commentator "And would you believe it???"
        Commentator "The pass is intercepted by a defender, and the opportunity is wasted."
        jump match_day_1_play_s_3

label match_day_1_play_s_3:
    show Commentator at left
    with dissolve
    Commentator "It is the 54th minute"
    Commentator "And [povname] is fouled just outside the penalty area," 
    Commentator "earning a free-kick in a dangerous position."
    hide Commentator
    with dissolve
menu:
    "Take the free-kick yourself":
                                jump match_day_1_play_s_freekick
    "Lay ball off to teammate":
                            jump match_day_1_play_s_lay_off

label match_day_1_play_s_freekick:
    if shooting >= 90:
        show Commentator at left
        Commentator "[povname] takes the run-up and..."
        Commentator "It's in!!!"
        Commentator "He curls the ball over the wall and into the top corner, scoring a stunning goal."
        $ score_for_1 += 1
        jump match_day_1_play_s_4
    if shooting < 90:
        show Commentator at left 
        Commentator "[povname] takes the run-up and..."
        Commentator "Oh no!!!"
        Commentator "The free-kick lacks precision and is easily caught by the goalkeeper."
        jump match_day_1_play_s_4

label match_day_1_play_s_lay_off:
    if passing >= 50:
        show Commentator at left
        Commentator "[povname] makes a quick short pass and..."
        Commentator "He has done it!!!"
        Commentator "The teammate strikes the ball first-time into the net, surprising the defense."
        $ score_for_1 += 1
        jump match_day_1_play_s_4
    if passing < 50:
        show Commentator at left
        Commentator "[povname] make a quick short pass and..."
        Commentator "Whats happenend here???"
        Commentator "The routine is poorly executed, and the ball is cleared by the defense."
        jump match_day_1_play_s_4

label match_day_1_play_s_4:
    show Commentator at left
    with dissolve
    Commentator "It is the 79th minute"
    Commentator "And the new signing [povname] makes a run into the box and recieves a cross from the right wing."
    hide Commentator
    with dissolve
menu:
    "Make Header":
                jump match_day_1_play_s_make_header
    "Control Ball":
                jump match_day_1_play_s_control_ball

label match_day_1_play_s_make_header:
    if shooting >= 90:
        show Commentator at left
        Commentator "[povname] goes for the header..."
        Commentator "And hes done it!!!"
        Commentator "The header is perfectly placed, beating the goalkeeper and giving Haddonfield United a goal."
        $ score_for_1 += 1
        jump match_day_1_play_s_5
    if shooting < 90:
        show Commentator at left
        Commentator "[povname] goes for the header..."
        Commentator "Oh Dear!!!"
        Commentator "The header is mistimed, and the ball goes over the bar."
        jump match_day_1_play_s_5
     
label match_day_1_play_s_control_ball:
    if physical >= 50:
        show Commentator at left
        Commentator "[povname] controls the ball with his chest and tries to shoot..."
        Commentator "And look at that!!!"
        Commentator "He controls the ball beautifully and smashes it into the net, securing the goal."
        $ score_for_1 += 1
        jump match_day_1_play_s_5
    if physical < 50:
        show Commentator at left
        Commentator "[povname] controls the ball with his chest and tries to shoot..."
        Commentator "And oh no!!!"
        Commentator "The control is poor, and a defender clears the ball before he can shoot."
        jump match_day_1_play_s_5

label match_day_1_play_s_5:
    show Commentator at left
    with dissolve
    Commentator "With only seconds remaining, Haddonfield United win a corner."
    Commentator "[povname] positions himself near the penalty spot, ready for one last chance."
    hide Commentator
    with dissolve
menu:
    "Call for ball":
                jump match_day_1_play_s_call_for_ball
    "Late run to post":
                jump match_day_1_play_s_run_post

label match_day_1_play_s_call_for_ball:
    if shooting >= 85:
        show Commentator at left
        Commentator "[povname] calls for the ball to be crossed to him."
        Commentator "And can you believe it!!!"
        Commentator "He leaps above the defenders and heads the ball into the goal, scoring in dramatic fashion. Who would've seen this coming from [povname]?"
        $ score_for_1 += 1
        jump match_day_1_play_s_final_whistle
    if shooting < 85:
        show Commentator at left
        Commentator "[povname] calls for the ball to be crossed to him."
        Commentator "Oh no no no!!!"
        Commentator "The cross is too high, and the ball goes out for a goal kick."
        jump match_day_1_play_s_final_whistle

label match_day_1_play_s_run_post:
    if pace >= 75:
        show Commentator at left
        Commentator "[povname] makes a late run to the near post..."
        Commentator "And would you look at that!!!"
        Commentator "The ball is perfectly delivered to the near post, and [povname] flicks it into the net for a goal."
        $ score_for_1 += 1
        jump match_day_1_play_s_final_whistle
    if pace < 75:
        show Commentator at left 
        Commentator "[povname] makes a late run to the near post..."
        Commentator "That is not good!!!"
        Commentator "The delivery is intercepted by the goalkeeper, and the chance is lost."
        jump match_day_1_play_s_final_whistle
        
# After having a result from this match it will change the points for the main team
# I also went onto the real premier league matches and had a change in points depending on their real result.

label match_day_1_play_s_final_whistle:
    $ everton += 1
    $ tottenham += 1
    $ brighton += 3
    $ burnley += 1
    $ fulham += 1
    $ aston_villa += 3
    $ bournemouth += 1
    $ nottm_forest += 1
    $ manchester_united += 3
    $ wolves += 3
    $ arsenal += 3
    $ manchester_city += 3
    if score_for_1 > score_against_1:
        $ haddonfield_united += 3
    if score_for_1 == score_against_1:
        $ haddonfield_united += 1
        $ newcastle += 1
    if score_for_1 < score_against_1:
        $ newcastle += 3
        show Commentator at left
        Commentator "The game ends with a thrilling conclusion,"
        Commentator "the scorline is Haddonfield [score_for_1]-[score_against_1] Newcastle United."
        Commentator "Now we will come down to the post match interviews with some of the players."
        jump post_match_day_1_interview

label post_match_day_1_interview:
    show Commentator at left
    with dissolve
    Commentator "The Captain is now being interviewed after the game."
    Commentator "Let's see what they have to say."
    hide Commentator
    with dissolve
    show The_Gafa at left
    with dissolve
    The_Gafa "While the Captain is getting interviewed I want to know how you're doing"
    The_Gafa "Great game out there today, [povname]."
    The_Gafa "You made a real impact on the pitch."
    The_Gafa "How are you feeling after that performance?"
    hide The_Gafa
    with dissolve
menu:


label match_day_2_start:
    $ score_for_2 = 0
    $ score_against_2 = 3
    show Narrator at left
    with dissolve 
    Narrator "In reality Sheffield won this game 3-1 so you'll have options to make this scoreline better then the realife life result."
    hide Narrator
    with dissolve
    show Commentator at left
    with dissolve
    Commentator "Here we are at Haddonfield park for Haddonfield United v Sheffield United"
    Commentator "The referee blows the whistle, and the game begins."
    hide Commentator
    with dissolve
    jump match_day_2_play_1

label match_day_2_play_1:
    show Commentator at left
    Commentator "Haddonfield United's new signing [povname] starts in his position as the central forward, ready to lead the attack."
    Commentator "We are going into the 8th minute and..."
    Commentator "[povname] finds himself on the edge of the penalty box with the ball, facing a lone defender."
    hide Commentator
    with dissolve
menu:
    "Attempt dribble":
                    jump match_day_2_play_attempt_dribble
    "Opt for pass":
                jump match_day_2_play_opt_for_pass

label match_day_2_play_attempt_dribble:
    if dribbling >= 75:
        show Commentator at left
        Commentator ""

label match_day_2_play_opt_for_pass:
    
label injured_end:

label failed_end:

return