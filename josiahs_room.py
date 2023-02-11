import random
import string
import time


class Mirror_Room:

    GROUNDHOG_NAMES = ('marmots','otchek', 'minibeast', 'vermin', 'woodchuck', 'whistlepig', 'moonack', 'land-beaver', 'gnawer', 'nudnick', 'groundpig', 'woonusk', 'siffleux')
    GROUNDHOG_APPEARANCE = ('waxen', 'albino', 'porcelain', 'cadaverous', 'peaked', 'wheyface', 'lurid')
    GROUNDHOG_DISPOSITION = ('idiosyncratic', 'vainglorious', 'chimerical', 'phantasmic', 'quixotic', )

    def __init__(self, key):
        self.key = key
        self.enter()
        
        

    def enter(self):
        print(f'You currently have {self.key} out of 4 keys')
        print("""
        \nYour eyes open and you find yourself in a dark room\n\n
        No, room isn't quite the right word.-PAUSE-\n
        Formless void? Yes! A perfectly apt description, a formless void.\n
        Curiously, your apocryphal alabastrine escort seems to be missing.""")
        
        input('\nWill you...\n1: Look Around, or\n2: Call out\n>')

    def look_around(self):
        self.choose_mirror()

    def call_out(self):
        print("You attempt to speak ")
        self.choose_mirror()

    def choose_mirror(self):
        print("""\n
        Three more mirrors appear before you. When you step in front of each one however, your reflection is different.\n
        They're all still you but in the one to the left you stand tall and valiant.\nIn the middle mirror you seem wise and assured.\nTo the right, you appear curious and inquisitive.
        """)
        mirror_choice = input("Which will you choose?\n(1) You feel courageous.\n(2) You're feeling wise\n(3)")
        if mirror_choice == '1':
            self.courage()
        elif mirror_choice == '2':
            self.wisdom()
        elif mirror_choice == '3':
            self.curiosity()
        else:
            print("Invalid")
    def courage(self):
        #Scary maze where
        self.courage_ending()

    def courage_ending(self):
        print("""\nYou walk forward, unperturbed. Holding on tightly to the mental image of yourself in the mirror, stance powerful fills you with courage.\n
        You can still here the malicious 'something' behind you as you turn on to the next hall. Its rattling/scuttling/romping moving ever close.\n
        -PAUSE-
        In spite of that, you find yourself smiling. The fact that you can hear his/her/its footsteps/stomach/growl rumbling - just a few steps behind you now - you find yourself wanting to whistle a tune.\b
        And you do. The pitch and harmony don't matter, its a jaunty tune the could inspire skipping in the most pensive of fellows.\n
        The tune overpowers any sound of the 'something' behind you, though his/her/its murderous intent can be felt as you make another turn.\n
        As you round the bend, at the end of this hall you see an open doorway. You laugh and continue your march to it.\n
        You get close to the end, the 'something' on your heels, you can feel/smell its breath/fragrance on the back of your neck. As you step through the doorway, you feel its fingers/tongue wrap around your ankle.\n
        You turn back to see nothing but a wall. The doorway is gone.\n
        You take inventory of the room you're in now. It's like a plain box, the walls white and marble-like. You look up and cen't see the top, but there's light trickling in from somewhere and shining down to the center of the room.\n
        Bathing in that light is a stone pedestal of a python. Its hood is spread and it looks poised for a strike. In its mouth, you see a crimson crystalline apple.
        """)
        self.room_end()

    def wisdom(self):
        riddle = print('"I am one and part of a pair. My front and back are mirrors. If you remove them I have to question why. The path through can only be taken without me."')
        player_answer = input("Type in your guess here:\n> ").lower()
        correct_answer = ['eye', 'eyes']
        riddle_turns = 0

        while riddle_turns < 3:
            if player_answer in correct_answer:
                print("Correct!")
                self.riddle_solved()
            else:
                print("Incorrect")
                riddle_turns += 1
        
        self.wisdom_ending()

    def riddle_solved(self):
        self.room_end()
        

    def wisdom_ending(self):
        self.room_end()

    def curiosity(self):
        #Whimsical side-quest where curiosity is rewarded
        self.curiosity_ending

    def curiosity_ending(self):
        self.room_end()

    def room_end(self):
        self.key += 1
        print("""\n
        As soon as you grab the apple, you're back in the original room. Your arm is still outstretched with just the apple in your hand.\n
        You put the apple in your pocket and turn around to your choices. You notice that the mirror you originally stepped through has shattered.
        """)
        print(f'\nYou have obtained {self.key} out of four keys.')
