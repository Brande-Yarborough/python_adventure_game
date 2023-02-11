import random
import string
import time
import PIL.Image

class Mirror_Room:

    GROUNDHOG_NAMES = ('marmots','otchek', 'minibeast', 'vermin', 'woodchuck', 'whistlepig', 'moonack', 'land-beaver', 'gnawer', 'nudnick', 'groundpig', 'woonusk', 'siffleux')
    GROUNDHOG_APPEARANCE = ('waxen', 'albino', 'alabastrine', 'cadaverous', 'peaked', 'wheyfaced', 'lurid')
    GROUNDHOG_DISPOSITION = ('idiosyncratic', 'vainglorious', 'chimerical', 'phantasmic', 'quixotic', )

    def __init__(self, key):
        self.key = key
        self.riddle_correct = False

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("welcome to the beach \n the ocean is a powerful and mysterious creature")

    def play(self):
        self.key += 1
        print(self.key)

    def enter(self):
        entrance_text = print("""
        \nYour eyes open and you find yourself in a dark room\n\n
        No, room isn't quite the right word.-PAUSE-\n
        Formless void? Yes! A perfectly apt description, a formless void.\n
        Curiously, your apocryphal alabastrine escort seems to be missing.""")
        
        input('\nWill you...\n1: Look Around,\n2: Call out\n>')

    def look_around(self):
        pass

    def call_out(self):
        print("You attempt to speak ")

    def courage(self):
        #Scary maze where
        pass

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

    def wisdom(self):
        #Holds the puzzle/riddle
        pass

    def wisdom_ending(self):
        pass

    def curiosity(self):
        #Whimsical side-quest where curiosity is rewarded
        pass

    def curiosity_ending(self):
        self.room_end()

    def room_end(self):
        self.key += 1
        print("""\n
        As soon as you grab the apple, you're back in the original room. Your arm is still outstretched with just the apple in your hand.\n
        You put the apple in your pocket and turn around to your choices. You notice that the mirror you originally stepped through has shattered.
        """)
        print(f'\nYou have obtained {self.key} out of four keys.')
