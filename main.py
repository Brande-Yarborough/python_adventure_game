import string
import josiahs_room
import conors_room
import ambers_room
import brandes_room


class Main:
    def __init__(self, key):
        self.key = key

    def heartkingdom_room(self):
        ambers_room.Hearts_Room(self.key).play()

    def main_play(self):
        conors_room.ConorRoom(self.key).play()

    def mirror_room(self):
        josiahs_room.Mirror_Room(self.key).play()

    def computer_room(self):
        brandes_room.BrandeRoom(self.key).play()

    def start_adventure(self):
        start = input(
            'La la la la...oh! I didn\'t see you there...I was just washing my majestic white fur.\n\n You wouldn\'t be interested in following a beautiful rodent into a hole would you?\n I am about to meander down...I got a notification that it was going to rain on my Apple Watch. Would you be interested in coming with me to Wonderland?\nYes or No: ')
        if start.lower() == 'yes' or start.lower() == 'y' or start == '1':
            print("\nOh delightful. We barely fit...Get ready to encounter many mythical creatures on your adventure. May the odds be ever in your favor!\n")
            players_choice = input(
                'which adventure would you like to start with: Room 1, (2) a seafaring journey , 3 or 4?\n>').lower()

            if players_choice == '1':
                print("you have chose to journey to the kingdom of hearts")
                self.heartkingdom_room()
            elif players_choice == '2':
                self.main_play()

            elif players_choice == '3':
                print("\nMirror appears before you and you approach it. You reach out to touch it and when your hand touches the one of your reflection, fall through the veneer.")
                self.mirror_room()

            elif players_choice == '4':
                self.computer_room()

            else:
                print("Whats the matter, are you mad as a hatter. If you wish to have tea, pick a number to proceed. Preferably 1 through 4...\n")
        else:
            print('The groundhog and Mad Hatter are sad you did not join them :\n')


# This initializes the key to a value of zero.
game = Main(0)

game.start_adventure()

print("\n\n\n----------------GAME OVER----------------")


#
# else:
# print('The groundhog and Mad Hatter are sad you did not join them :( ')

#
#
# items = 0
# class Room():
#     def __init__(self):
#         pass
#     def item_received():
#         items += 1

#     def to_start():
#         first_room()

# name = input('Enter your name: ')

# class Main(Room):
#     __init__(self)
#     options = [1, 2, 3, 4]

#     pass

# main = Main()

# input(f'Your choices are{options}')

# print(f'Hello, {name}! Welcome to your adventure!')

# put story about following groundhog here?

# items = 0
# class Room():
#     def __init__(self):
#         pass
#     def item_received():
#         items += 1

#     def to_start():
#         first_room()

# name = input('Enter your name: ')

# class Main(Room):
#     __init__(self)
#     options = [1, 2, 3, 4]

#     pass

# main = Main()

# input(f'Your choices are{options}')

# print(f'Hello, {name}! Welcome to your adventure!')

# put story about following groundhog here?
