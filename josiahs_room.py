import random
import string
import time
import os



class Mirror_Room:

    # GROUNDHOG_NAMES = ('marmots','otchek', 'minibeast', 'vermin', 'woodchuck', 'whistlepig', 'moonack', 'land-beaver', 'gnawer', 'nudnick', 'groundpig', 'woonusk', 'siffleux')
    # GROUNDHOG_APPEARANCE = ('waxen', 'albino', 'porcelain', 'cadaverous', 'peaked', 'wheyface', 'lurid')
    # GROUNDHOG_DISPOSITION = ('idiosyncratic', 'vainglorious', 'chimerical', 'phantasmic', 'quixotic', )
    
    def __init__(self, key):
        self.key = key

    def enter(self):
        update_value = self.key
        print(f'You currently have {self.key} out of 4 keys')
        time.sleep(3)
        os.system('clear')
        
        print(r"""

     // -------- \\
    //            \\
   // ~~~~~~~~~~~~ \\
  ||                ||
  || ~~~~~~~~~~~~~~ ||
  ||                ||
  || ~~~~~~~~~~~~~~ ||
  ||                ||
  || ~~~~~~~~~~~~~~ ||
  ||                ||
   \\ ~~~~~~~~~~~~ //
   //\\           //\\
  ||  \\---------//  ||
 /||\               /||\
/____\             /____\  

        """)
        print(f"Your eyes open and you find yourself in a dark room. No, room isn't quite the right word...\n\nFormless void? Yes! A perfectly apt description, a formless void.\nCuriously, your apocryphal alabastrine escort with an eye for fashionable yet functional wristwear seems to be missing.")
        
        first_choice = input('\nWill you...\n(1) Look Around\n(2) Call out\n> ')
        if first_choice == '1':
            time.sleep(0.5)

            update_value = self.look_around()
            
        elif first_choice == '2':
            update_value = self.call_out()
        
        return update_value

    def look_around(self):
        time.sleep(0.5)
        update_value = self.choose_mirror()
        return update_value

    def call_out(self):
        print("French poet Antonio Porchia once said: 'We become aware of the void as we fill it.'\nThis void, however, refuses to be filled as it absorbs your voice.")
        input("Press 'enter' to continue")
        update_value = self.choose_mirror()
        return update_value

    def choose_mirror(self):
        time.sleep(0.5)
        os.system('clear')
        print(r"""

     // -------- \\          // -------- \\          // -------- \\ 
    //            \\        //            \\        //            \\
   //              \\      //              \\      //              \\
  ||                ||     ||              ||     ||                ||
  ||    COURAGE     ||     ||    WISDOM    ||     ||  (Coming Soon) ||              
  ||                ||     ||              ||     ||                ||
  ||                ||     ||              ||     ||                ||
  ||                ||     ||              ||     ||                ||
  ||                ||     ||              ||     ||                ||
  ||                ||     ||              ||     ||                ||
   \\              //       \\             //      \\              //
   //\\           //\\     //\\           //\\     //\\           //\\
  ||  \\---------//  ||   ||  \\---------//  ||   ||  \\---------//  ||
 /__\               /__\ /__\               /__\ /__\               /__\   

        """)

        print("Three mirrors appear before you. When you step in front of each one however, your reflection is different. They're all still you but in the one to the left you stand tall and valiant. In the middle mirror you seem wise and assured. And to the right... Odd, it just saying 'Coming Soon'.")
        valid_choice = True
        while valid_choice:        
            mirror_choice = input("Which will you choose?\n(1) You feel courageous,\n(2) You feel quite perspicacious,\n(3) You feel curious.\n\n> ") 
            if mirror_choice == '1':
                print("You step up to the first mirror, the visage of yourself oozes with infectious charisma. Its charm and charisma pull at you, and you step through the glass without hesitation.")
                valid_choice = False
                input("Press 'enter' to continue")
                update_value = self.courage()
            elif mirror_choice == '2':
                print("The visage of your middle self has a twinkle in its eye, as if this version of you knows something that others don't. When you step forward the other two mirrors vanish, and words begin to appear above your head.")
                valid_choice = False
                time.sleep(0.5)
                update_value = self.wisdom()
            elif mirror_choice == '3':
                time.sleep(0.5)
                print("You approach the mirror on the right and run your hand over its surface. The glass is dark and the words don't change. Vexed, you return to your choices.")
                
            else:
                print("Yikes. Apologies, but that's not an option. Let's try that again, I know you can do it champ!")

        return update_value
    
    def courage(self):
        time.sleep(0.5)
        os.system('clear')
        print("You make your way through and look to your right. There's a hallway that seems to stretch on forever with other hallways crossing through them at intersections every few meters.\nA disembodied voice fills your mind, 'They're behind you'.")
        time.sleep(0.5)
        print(r"""
 \                           /
  \  "They're behind you"   /
   \                       /
    ]                     [    ,'|
    ]                     [   /  |
    ]___               ___[ ,'   |
    ]  ]\             /[  [ |:   |
    ]  ] \           / [  [ |:   |
    ]  ]  ]         [  [  [ |:   |
    ]  ]  ]__     __[  [  [ |:   |
    ]  ]  ] ]\ _ /[ [  [  [ |:   |
    ]  ]  ] ] (#) [ [  [  [ |:   |
    ]  ]  ]_].nHn.[_[  [  [ |:   |
    ]  ]  ]  HHHHH. [  [  [ |:   |
    ]  ] /   `HH("N  \ [  [ |:   |
    ]__]/     HHH  "  \[__[ |:   |
    ]         NNN         [ |:   |
    ]         N/"         [ |:   |
    ]         N H         [ |:   |
   /          N            \|:   |
  /           q,            \    |
 /                           \   |

        """)
        
        first_courage_choice = input("Will you:\n(1) Look behind you\n(2) Finding the way out is more important\n> ")
        if first_courage_choice == '1':
            return self.look_behind()
        elif first_courage_choice == '2':
            update_value = self.first_beckon()
            return update_value

    def look_behind(self):
        os.system('clear')
        print("You turn and see a figure with long hair down on the floor, their face covered by dark hair. You consider moving in closer or calling out to them, but the figure suddenly looks up at you, revealing a face with no eyes.")
        monster_encounter = input("The figure rises, not standing like an ordinary person. It impossibly unfolds itself until it stand, lurching. It's acrid and ancient, it's eyeless gaze fixed upon you. It looms, silent and still.\nYou curse the wheyfaced whistlepig that initiated you on this journey as well as yourself because why'd you even do it?\nThe voice from before fills your mind again, the sudden sound causing you to flinch,\n'Your eyes... Give them to me' the voice whispers, yet it's deafening in your mind.\nDo you:\n(1) Run Away\n(2) Submit\n> ")
        if monster_encounter == '1':
            string = "You take a few steps backward before turning to run and the figure moves, nimble for its size. It slinks down the hall on all fours as it follows you down corridors and bends. You don't stop, panting as desperation fills you with energy.\nYou keep going, the 'thing' sounding further and further away. You look back and see that it's gone. You almost want to cheer, but the only sound that leaves you is a choked sob.\nYou slow down, stopping to gulp down air. After recovering for a moment, you decide to try to find your way out, take a turn down the next hallway...\n"
            for char in string:
                print(char, end='', flush=True)
                time.sleep(.01)
            
            time.sleep(3)
            os.system('clear')
            time.sleep(3)
            print(r"""
⠀⠀⠀⠀⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢠⠣⠐⠀     ⠀⠀⢪⢺⣪⢣⠀⡀    .⠈⡈⠀⡀⠀⠀ 
⠀⠀⠀⠀⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡⠀⠀⠀ 
⠀⠀⠀⠀⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂
        """)
            time.sleep(.5)
            os.system('clear')
            print(r"""
    ⠀⠀⠀⠀⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⢠⠣⠐⠀     ⠀⠀⢪⢺⣪⢣⠀⡀    .⠈⡈⠀⡀⠀⠀ 
    ⠀⠀⠀⠀⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂
        """)
            time.sleep(.5)
            os.system('clear')
            print(r"""
⠀⠀⠀⠀⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢠⠣⠐⠀     ⠀⠀⢪⢺⣪⢣⠀⡀    .⠈⡈⠀⡀⠀⠀ 
⠀⠀⠀⠀⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡⠀⠀⠀ 
⠀⠀⠀⠀⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂
        """)
            time.sleep(.5)
            os.system('clear')
            time.sleep(3)
            return self.monster_ending()
    
    def monster_ending(self):
        print("You come-to on your back in complete darkness, returned to the void. You stand up shakily and take a few steps forward before running into a wall. Well, that's new. You try taking a few steps the other way and do the same.\nYou continue to wander aimlessly, praying for a mirror without realizing you never left the corridors. The beast claimed its prize, leaving you blind and terrified in this maze.\n\n")
        time.sleep(.5)
        continue_prompt = input("Though you were met with a tragic end, this doesn't have to be the end of this story:\n(1) To go back to your mirror choice\n(2) To go back to the room selections\n> ")
        if continue_prompt == '1':
            self.choose_mirror()
        elif continue_prompt == '2':
            return self.key
    
    def first_beckon(self):
        time.sleep(.5)
        print("\nYou shrug and move on, wondering how to get out. You make your way, headstrong and taking turns on a whim. Somehow, the way you're going just feels 'right'.\nAs you're walking, you pass an intersection and hear a woman's cry down a hall.")
        second_courage_choice = input("Do you:\n(1) Go check it out\n(2) I've gotta be close to the exit, I can feel it!\n> ")
        if second_courage_choice == '1':
            return self.look_behind()
        elif second_courage_choice == '2':
            update_value =  self.courage_ending()
            return update_value


    def courage_ending(self):
        os.system('clear')
        print("You walk forward, unperturbed. Holding on tightly to the mental image of yourself in the mirror, stance powerful fills you with courage. You can still here the malicious 'something' behind you as you turn on to the next hall. Its rattling/scuttling/romping moving ever close.-PAUSE- In spite of that, you find yourself smiling. The fact that you can hear his/her/its footsteps/stomach/growl rumbling - just a few steps behind you now - you find yourself wanting to whistle a tune. And you do. The pitch and harmony don't matter, its a jaunty tune the could inspire skipping in the most pensive of fellows. The tune overpowers any sound of the 'something' behind you, though his/her/its murderous intent can be felt as you make another turn.")
        input("Press 'enter' to continue.")
        print("As you round the bend, at the end of this hall you see an open doorway. You laugh and continue your march to it.")
        input("Press 'enter' to continue.")
        os.system('clear')
        print(r"""

88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|           |_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|           |l|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|           |_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|           |d|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|           |_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|           |r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|           |_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|           |1|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|           |_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|           |u||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|           |_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]           [@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 888
        
        """)

        print("You get close to the end, the 'something' on your heels, you can feel/smell its breath/fragrance on the back of your neck. As you step through the doorway, you feel its fingers/tongue wrap around your ankle.\n... You turn back to see nothing but a wall. The doorway is gone. You take inventory of the room you're in now. It's like a plain box, the walls white and marble-like. You look up and cen't see the top, but there's light trickling in from somewhere and shining down to the center of the room.\nBathing in that light is a stone pedestal of a python. Its hood is spread and it looks poised for a strike. In its mouth, you see a crimson crystalline apple.\n")
        update_value =  self.room_end()
        return update_value

    def wisdom(self):
        time.sleep(1)
        print("\nThe message is a riddle:\n")
        time.sleep(.5)
        print(f'"I am one and part of a pair.{time.sleep(.5)}\nMy front and back are mirrors.{time.sleep(.5)}\nIf you remove me I have to question why.{time.sleep(.5)}\nWhat am I?"')
        time.sleep(3)
        correct_answers = ['eye', 'eyes']
        correct_answer = ['eye']
        riddle_turns = 0
        word_blanks = '_' * len(correct_answer)
        riddle_answer = False
        print(word_blanks)

        while riddle_turns < 5 and riddle_answer == False:
            player_answer = input("Type in your guess here:\n> ").lower()
            if player_answer in correct_answers:
                riddle_answer = True
                print("Correct!")
                update_value = self.riddle_two()
            elif riddle_turns > 2:
                print("The text changes:\n'I see you're having some trouble here, try again.'")
                riddle_turns += 1
                print(f"You have {riddle_turns} turns left\n")
            else:
                print("The text changes:\n'Incorrect, try again.")
                riddle_turns += 1
                print(f"You have {riddle_turns} turns left\n")
        
        if riddle_turns == 5 and riddle_answer == False:
            update_value = self.wisdom_bad_ending()
  
        return update_value
    
    def riddle_two(self):
        print('The words vanish before the quote reappears, this time the end is different:\n"I am one and part of a pair. My front and back are mirrors. If you remove me I have to question why. The path through can only be taken without me."')
        players_wisdom_choice = input("Will you:\n(1) Run head-first into the mirror\n(2) Close your eyes\n(3) Jab your eyes like a lunatic\n> ")
        if players_wisdom_choice == '1':
            os.system('clear')
            print("You take a few steps back and brace yourself before sprinting, your intent to smash the glass into smithereens. The mirror is an unmovable object however, and you're sent flying back. You sit up, dazed.")
            return self.wisdom_bad_ending()
        elif players_wisdom_choice == '2':
            print('Understanding the riddle, you close your eyes and take a step into the mirror. Meeting no resistance as you do.')
            update_value = self.wisdom_ending()
        elif players_wisdom_choice == '3':
            print(f'Sure of yourself, you jab your thumbs into your eyes.{time.sleep(0.5)}\nThe pain in excruciating.{time.sleep(0.5)}\nYou try to step with your hands covering your throbbing corneas before you trip and fall towards the mirror. You brace yourself for the sound of shattering before hearing a disembodied voice:\n"Erm... I guess that counts!"\nThe voice sounds a bit familiar, but before you can process it you fall through the mirror and writhe on the ground in pain.\nYou pitiful thing.\nAfter your eyes (and ego) recover, you stand back up to get your bearings.\n')
            update_value = self.wisdom_ending()
        return update_value

    def wisdom_bad_ending(self):
        print("You scramble to your feet and begin to meander through the darkness. You wander aimless through the void until the darkness begins to feel like an embrace. From time to time you think about the white groundhog. You eventually descend and accept your mania, a smile perpetually on your face.\nYou quite love it here.")
        continue_prompt = input("\nThough you were met with a bittersweet end, this doesn't have to be the end of this story:\n(1) To go back to right before you solved the riddle\n(2) To go back to the room selections\n> ")
        if continue_prompt == '1':
            self.wisdom()
        elif continue_prompt == '2':
            return self.key

    def wisdom_ending(self):
        input("Press 'enter' to continue.")
        print("\nYou find yourself in forest clearing with a solitary tree standing vigil at its center. It's quiet, the sunlight pouring in a gentle heat before a refreshing breeze comes to wipe it away. The leaves of the surrounding trees are russet, letting go of their grip and finally resting after a long summer.\n\nYou walk to the tree in the middle. Despite the other trees state, this one's leaves are full of vitality - a deep emerald green in contrast to its porcelain bark.")
        input("Press 'enter' to continue.")
        print("Winding down from the branches is a stone snake - a python. Even though it's lifeless, it looks like it's sleeping. In its mouth you see a crimson crystalline apple.")
        update_value = self.room_end()
        return update_value

    # def curiosity(self):
    #     Whimsical side-quest where curiosity is rewarded
    #     self.curiosity_ending

    # def curiosity_ending(self):
    #     self.room_end()

    def room_end(self):
        update_value = self.key + 1
        input("Press 'enter' to continue.")
        os.system('clear')
        print("As soon as you grab the apple, you're back in the original room. Your arm is still outstretched with just the apple in your hand. You put the apple in your pocket and turn around to your choices. You notice that the mirror you originally stepped through has shattered.")
        print(r"""
     // ------------- \\
    //-      | |   |   \\
   //  \__   /   \ /  | \\
  ||       \|     |  / __||
  ||         \    | |_/  ||
  ||\     __  |   |/ __  ||
  ||  \__/   \|   |_/  \_||
  ||  _    ___|  /  \_   ||
  ||_/ \__/   |/_     \_/||
  ||          o  \      _||
  ||\       / |    \___/ ||
  ||  \___/   |     \   /||
  ||     |   / \_    )-<_||
  ||    /  /     \  /    ||
   \\ /   |      _><    //
   //\\   |     /   \  //\\
  ||  \\------------- //  ||
  ||                      ||
 /||\                    /||\
/____\                  /____\  

        """)
        return update_value
        
        
        # print(f'\nYou have obtained {self.key} out of four keys.')
    
