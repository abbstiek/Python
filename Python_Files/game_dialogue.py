"""Main game handler for Poothon_Game"""

from characters import *
from grid import *
from items import *
from locations import *

Options: True or False
Name: NARRATOR
Dialogue: "You've just finished your knighthood training. You now serve as one of the main knights of the Kingdom of Closure."
Name: NARRATOR
Dialogue: "Everything is going well as you reach your goals and did what you’ve always dreamed of- becoming a knight."
Name: NARRATOR
Dialogue: "All good things must come to an end, and Bob, the Destroyer sneaks into the kingdom and kidnaps Princess Perl!"

Name: NARRATOR
Dialogue: "You must save the princess! Which weapon would you like to yield on your journey?"

Option: True
Option A: "Sword, duh"
Option B: "Bow & arrow"
Option C: "Small dagger"

Name: NARRATOR
Dialogue: "The king approaches you."

Name: KING
Dialogue: "I'm so glad that you are finally here, Cody Segfault. You must save my only daughter!"
Name: KING
Dialogue: "I think he took her up to the tower. I believe in you Cody!"

Option: True, 3
Option A: "Thank you, sir. I will do anything to protect your daughter"
Option B: "I don’t know if I can save her before he hurts her, but I’ll try!"
Option C: "Shut it, old man!"

Name: NARRATOR
Dialogue: "You leave the castle. Which route would you like to go?"

Option: True, 3
Option A: "On horseback, en route for the tower"
Option B: "Through the woods"
Option C: "Back to my house to take a nap"

---------------
IF A:
Text: 1
Name: NARRATOR
Dialogue: "You thought that the horse would be a good idea but he runs out of energy very quickly. You can either"

Option: True, 2
Option A: "Bring him back to the castle, then walk the rest of the way"
Option B: "Tie him up to a tree and continue on your journey"

IF A:
Text: 2
Name: NARRATOR
Dialogue: "You return to the castle and the king is FURIOUS. He ends up punishing you for your poor decisions and kills both you and the horse."
exit code = 0

IF B:
Text: 3
Name: NARRATOR
Dialogue: "A horrible storm starts. You hide for cover under some fallen trees. You sleep until the next morning."
Name: NARRATOR
Dialogue: "You didn’t prep for being out this long and wake up very hungry. What do you eat?"

Option: True, 3
Option A: "Mushrooms you found in the woods"
Option B: "A dead racoon"
Option C: "Nothing, you have to save the princess!"

    IF A:
    Text: 4
    Name: NARRATOR
    Dialogue: "You start hallucinating and end up in a tree, about 100 feet high”
    Name: NARRATOR
    Dialogue: "You start to feel normal again and come to your senses. You drop your armor to make it easier to get down from the tree. You eventually climb down and continue trekking.”

    IF B:
    Text: 5
    Name: NARRATOR
    Dialogue: "You get rabies and die a horrible, painful death”
    exit code = 0

    IF C:
    Text: 6
    Name: NARRATOR
    Dialogue:  "You continue trekking through the woods but you are very, very tired and hungry. You come across a fellow traveler and he offers you some cooked squirrel. You continue your journey.”

        IF A OR C:
        Text: 7
        Name: NARRATOR
        Dialogue: "After many days of traveling, you finally make it out of the forest. you receive word that Bob the Destroyer has been torturing the princess and you need to hurry! You are finally nearing the large tower. It is surrounded by a moat, what do you do next?”

        Option: True, 2
        Option A: "Swim across"
        Option B: "Turn around and go home"

            IF A:
            Text: 8
            Name: NARRATOR
            Dialogue: "You didn’t notice the alligators before you got in! How good are you at swimming?"

            Option: True, 3
            Option A: "I could beat Michael Phelps in a race."
            Option B: "I’m alright, probably couldn’t beat an alligator though"
            Option C: "I can’t even swim!"

                IF A OR B:
                Text: 10
                Name: NARRATOR
                Dialogue: "Those alligators nearly took a chomp out of you - but you’ve survived! You make it to the entrance of the tower."
                Name: NARRATOR
                Dialogue: " You still have to rescue the princess. You approach the wooden door. How do you enter?"

                Option: True, 3
                Option A: "Knock politely and wait for someone to open the door"
                Option B: "Turn around, there’s no way you’re getting through that wooden door."
                Option C: "Force your way by kicking it in"

                    IF A:
                    Text: 11
                    Name: NARRATOR
                    Dialogue: "You wait for many weeks, but nobody answers the door. You eventually starve on the footsteps of the tower."
                    exit code = 0
                    IF B:
                    Text: 12
                    Name: NARRATOR
                    Dialogue: "You journey for a few days and make it back to the kingdom. The king is very disappointed in you and kicks you out of the Kingdom. You are exiled and everybody that you love hates you. You die alone."
                    exit code = 0
                    IF C:
                    Text: 13
                    Name: NARRATOR
                    Dialogue: "You aren’t letting some stupid door get in the way of you and the princess! You kick your way through the wooden door."
                    Name: NARRATOR
                    Dialogue: "You can either take the stairs to the top of the tower or head to the basement. Which option do you choose?"

                    Option: True, 2
                    Option A: "Basement"
                    Option B: "The top of the tower to save the princess!"

                        IF A:
                        Text: 14
                        Name: NARRATOR
                        Dialogue: "You go downstairs into the basement. It is very dark and you make your way to the bottom of the stairs in search of a light. A dragon is tied up in the basement but you don’t realize until it is too late. He swallows you whole"
                        exit code = 0
                        IF B:
                        Text: 15
                        Name: NARRATOR
                        Dialogue: "Good choice - you make your way to the top of the tower. You reach the room and enter a long hallway. You can hear the screams of Princess Perl. How do you proceed?"

                        Option: True, 2
                        Option A: "Start screaming as loudly as possible as you run towards the end of the hallway"
                        Option B: "Try to remain as quiet as possible as you make your way to the end of the hallway"

                            IF A:
                            Text: 16
                            Name: NARRATOR
                            Dialogue: "one of Bob’s henchmen make their way towards you with a huge sword.	You panic but manage pull out your weapon and hit him in the throat, killing him and approaching Bob the Destroyer. He is aware of you being there and continues torturing the princess as you get closer. He turns to you and says *You call yourself a knight? More like a weenie in some armor.* How do you respond?"

                            Option: True, 2
                            Option A: "*Say that to my fists!* you yell as you throw your weapon down and attack him by throwing punches. This turns into wrestling. Perl is still trapped."
                            Option B: "*I worked hard for this armor* you say, trying not to act hurt. A single tear rolls down your cheek. Bob manages to attack you while you are still vulnerable. He grabs your weapon and points it towards Perl. You must act quickly"

                                IF A:
                                Text: 18
                                Name: NARRATOR
                                Dialogue: "You finally incapacitate Bob by putting him into a sleeper hold. He falls into a deep slumber and you finally release him to rescue Perl. You cut her down from the torture board and throw her over your shoulder. You escape from the tower quickly and venture towards the Kingdom of Clojure with the Princess"
                                exit code = 1
                                IF B:
                                Text: 19
                                Name: NARRATOR
                                Dialogue: "Your lack of energy and slow reflexes make it so that Perl is killed by your weapon. You yell *NOOOOOOOOOOOOOOO* as all that you have lived for lead up to this moment. You are too embarrassed to return home and live the rest of your life in the woods."
                                exit code = 0
                            IF B:
                            Text: 17
                            Name: NARRATOR
                            Dialogue: "You sneak up behind the henchmen and quietly injure him with your weapon. Bob is too busy focusing on Perl, so you are able to sneak up behind him. She is tied to a torture board, with each of her limbs tied with rope. Bob has a lever that can make the rope pull harder, stretching out her body. She is screaming with pain. What do you do next?"

                            Option: True, 2
                            Option A: "Use your weapon to release Perl from the board. Throw her over your shoulder and make a run for it. Bob chases you but quickly runs out of energy. You make it out of the tower and run towards the Kingdom of Clojure as fast as you can with the princess."
                            Option B: "Defend your honor and attempt to injure Bob with your weapon, leaving Perl on the torture board."
                                IF A:
                                Text: 20
                                Name: NARRATOR
                                Dialogue: "You try your best to escape the tower, but Bob is chasing after you. You finally make it to the bottom of the stairs and run as far away from the tower as you can. Bob is close behind you but ends up getting lost in the forest. You make your way towards the Kingdom of Clojure"
                                exit code = 1
                                IF B:
                                Text: 21
                                Name: NARRATOR
                                Dialogue: "Bob tightens the ropes on the torture board and Perl ends up losing one of her limbs. She is starting to lose a lot of blood, and Bob has taken your weapon. He ends up using a large rock and knocking you unconscious. You wake up many hours later attached to a torture board of your own. You end up dying a slow and painful death."
                                exit code = 0

                IF C:
                Text: 9
                Name: NARRATOR
                Dialogue: "You get eaten by an alligator. The princess is taken away by Bob the Destroyer and you will forever be remembered as that loser that has failed to rescue the princess. Womp womp"
                exit code = 0

            IF B:
            Text: 22
            exit code = 0

IF C:
Text: 23
Name: NARRATOR
Dialogue: "You return home for a nap. Bob the destroyer runs off with the princess. You are unknighted and spend the rest of your life in shame. You die a poor, old man. Nobody ever loved you"
exit code = 0
