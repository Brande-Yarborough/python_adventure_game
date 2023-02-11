class BrandeRoom:
    def __init__(self, key):
        self.key = key

    def entrance(self):
        print("Welcome to the cave of computers!")
        print("As you enter, you see glowing screens with people seated, typing away, and meet your guide, Mady Hatter.")
        print("Mady Hatter tells you that you have two choices, follow her into the cave and help solve a riddle to obtain a key or leave. ")
        choice = input(
            "Do you wish to stay or leave? Enter Stay or Leave: ").lower()
        if choice == "stay":
            print("This journey will be unforgettable! Good choice!")
            # How do I move from here to the cave if choice is stay??
            self.cave()
        elif choice == "leave":
            print(
                "You thought you were leaving, but get stuck in an infinite loop of nonsense. Adventure over.")
            # Do we quit adventure here or send back to start of main??
            # else: ?? do we need an else statement here for incorrect input?

    def cave(self):
        print("Mady Hatter says we are all mad here, mad about code.")
        print("Now that you are here, you must also finish your pixel perfect project in addition to solving the riddle.")
        print("Mady Hatter knows you can do it, but you are doubting yourself.")
        print("It feels like you are in a dream, where there are lines of code but when you wake up, your screen is totally blank.")
        print("Mady Hatter asks what you got, and helps you persist through the project. ")
        print("You finally finish your project, and can continue on to solve the riddle. ")
        response = input("Are you up for the challenge: Yes or No").lower()
        if response == "yes":
            print("Riddle me this...")
            # How do I move on to the riddle or play part? call it here?
            self.play()
        elif response == "no":
            print(
                "You did not accept the challenge, and are now sent down a python hole that leads to the brain of a computer.")
            print(
                "It appears the computer has a virus, or a terminal illness-did you catch that knee slapping joke? Adventure over.")
            # Do we quit here or send back to main to start over??
            # else? do we need an else statement here for incorrect input?

    def play(self):
        print("Solve this riddle to move on and make your way to the tea party!")
        print("I have keys but do not lock. I have space but have no room. You can enter but not come in. What am I? ")
        response = input("_ _ _ _ _ _ _ _").lower()
        if response == "keyboard":
            print("Way to go!")
            # Do we move back to main to start over?
            # How do we give key here and move on??
        elif response != "keyboard":
            print("Stumped you. Adventure over.")
            # Do we quit or go back to main here??
        self.key += 1
        print(self.key)

    def check_out(self):
        # Do we go back to main here??
        print("Hello traveler!")
