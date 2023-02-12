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
        time.sleep(1)
        print("As you follow the groundhog inside, you see glowing screens with people seated, typing away, and meet \nyour guide, Mady Hatter.\n")
        time.sleep(1)
        print("Mady Hatter tells you that you have two choices, follow her into the cave and help solve a riddle to \n obtain a key or leave and try to find your way back out of the cave all by yourself.\n")
        time.sleep(1)
        choice = input(
            "Do you wish to stay or leave? Enter Stay or Leave: ").lower()
        if choice == "stay":
            print("\n This journey will be unforgettable! Good choice!")
            time.sleep(1)
            # call self.cave to move from here to the cave if choice is stay
            update_value = self.cave()

        elif choice == "leave":
            print(
                "You thought you were leaving, but get stuck in an infinite loop of nonsense. Adventure over.")
            # sends back to next sequence with no key
            # return self.key
            update_value = self.key
        return update_value

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
        time.sleep(1)
        print("Now that you are here, you must also finish your pixel perfect project in addition to solving \n the riddle.\n")
        time.sleep(1)
        print("Mady Hatter knows you can do it, but you are doubting yourself.\n")
        time.sleep(1)
        print("It feels like you are in a dream, where there are lines of code, but when you wake up, your screen is \n totally blank.\n")
        time.sleep(1)
        print("Mady Hatter asks what you got, and helps you persist through the project.\n")
        time.sleep(1)
        print("You finally finish your project, and can continue on to solve the riddle.\n")
        time.sleep(1)
        response = input(
            "Are you up for the challenge? Enter Yes or No: ").lower()
        if response == "yes":
            print("\nRiddle me this...")
            # call self.play here to move on to riddle
            update_value = self.play()
        elif response == "no":
            print(
                "You did not accept the challenge, and are now sent down a python hole that leads to the brain of \na computer.")
            print(
                "It appears the computer has a virus, or a terminal illness-did you catch that knee slapping joke? \nAdventure over.")
            # Do we quit here or send back to main to start over??
            # what do I return here? can i get back to next sequence from here?
            update_value = self.key
        return update_value

    def play(self):
        print("Solve this riddle to move on and make your way to the tea party!\n")
        time.sleep(1)
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

        else:
            for guesses in range(0, 2):
                print("Guess again-you have 2 more chances to make it to the tea party.")
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

            print("Stumped you. Adventure over.")
    # Do we quit or go back to main here??
            return self.key
