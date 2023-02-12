import time
import os


class BrandeRoom:
    def __init__(self, key):
        self.key = key

    def entrance(self):
        update_value = self.key  # This sets it to the initilization value.

        print("Welcome to the cave of computers!")
        print(r"""
                         | ___  o|
                         |[_-_]_ |
      ______________     |[_____]|
     |.------------.|    |[_____]|
     ||            ||    |[====o]|
     ||            ||    |[_.--_]|
     ||            ||    |[_____]|
     ||            ||    |      :|
     ||____________||    |      :|
 .==.|""  ......    |.==.|      :|
 |::| '-.________.-' |::||      :|
 |''|  (__________)-.|''||______:|
 `""`_.............._\""`______
    /:::::::::::'':::\`;'-.-.  `\
   /::=========.:.-::"\ \ \--\   \
   \`""""""""""""""""`/  \ \__)   \
 `""""""""""""""""`    '========'
""")
        time.sleep(2)
        print("As you follow the groundhog inside, you see glowing screens with people seated, typing away, and meet \nyour guide, Mady Hatter.\n")
        time.sleep(2)
        print("Mady Hatter tells you that you have two choices, follow her into the cave and help solve a riddle to \n obtain a key or leave and try to find your way back out of the cave all by yourself.\n")
        time.sleep(2)
        choice = input(
            "Do you wish to stay or leave? Enter Stay or Leave: ").lower()
        if choice == "stay":
            print("\n This journey will be unforgettable! Good choice!")
            time.sleep(3)
            # call self.cave to move from here to the cave if choice is stay
            update_value = self.cave()
            print(update_value)
            return update_value

        # self.cave()
        elif choice == "leave":
            print(
                "You thought you were leaving, but get stuck in an infinite loop of nonsense. Adventure over.")
            # Do we quit adventure here or send back to start of main??

    def cave(self):
        os.system('clear')
        print("Mady Hatter says we are all mad here, mad about code.")
        print(r"""
        
                                ,.--""-._
                            __/         `.
                      _,**"   "*-.       `.
                  ,'            `.       \
                  ;    _,.---._    \  ,'\  \
                   :   ,'   ,-.. `.   \'   \ :
                   |  ;_\  (___)`  `-..__  : |
                   ;-'`*'"  `*'    `--._ ` | ;
                  /,-'/  -.        `---.`  |"
                  /_,'`--='.       `-.._,-" _
                   (/\\,--. \    ___-.`:   //___
                      /\'''\ '  |   |-`|  ( -__,'
                     '. `--'    ;   ;  ; ;/_/
                       `. `.__,/   /_,' /`.~;
                       _.-._|_/_,'.____/   /
                  ..--" /  =/  \=  \      /
                 /  ;._.\_.-`--'-._/ ____/
                 \ /   /._/|.\     ."
                  `*--'._ "-.:     :
                       :/".A` \    |
                       |   |.  `.  :
                       ;   |.    `. 
                       """)
        time.sleep(2)
        print("Now that you are here, you must also finish your pixel perfect project in addition to solving \n the riddle.\n")
        time.sleep(2)
        print("Mady Hatter knows you can do it, but you are doubting yourself.\n")
        time.sleep(2)
        print("It feels like you are in a dream, where there are lines of code, but when you wake up, your screen is \n totally blank.\n")
        time.sleep(2)
        print("Mady Hatter asks what you got, and helps you persist through the project.\n")
        time.sleep(2)
        print("You finally finish your project, and can continue on to solve the riddle.\n")
        time.sleep(2)
        response = input(
            "Are you up for the challenge? Enter Yes or No: ").lower()
        if response == "yes":
            print("\nRiddle me this...")
            # call self.play here to move on to riddle
            return self.play()
            # self.play()
        elif response == "no":
            print(
                "You did not accept the challenge, and are now sent down a python hole that leads to the brain of a computer.")
            print(
                "It appears the computer has a virus, or a terminal illness-did you catch that knee slapping joke? Adventure over.")
            # Do we quit here or send back to main to start over??
            return self.key

    def play(self):
        print("Solve this riddle to move on and make your way to the tea party!\n")
        time.sleep(2)
        print("I have keys but do not lock. I have space but have no room. You can enter but not come in. What am I? ")
        response = input("_ _ _ _ _ _ _ _: ").lower()
        if response == "keyboard":
            result = self.key + 1
            os.system('clear')
            print("You did it! Here's your key, now head for the tea!")
            print(r"""
    )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'

                     """)
            update_value = result
            return update_value

        elif response != "keyboard":
            print("Stumped you. Adventure over.")
            # Do we quit or go back to main here??
            return self.key
