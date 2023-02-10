import string
import josiahs_room
import conors_room
import ambers_room
import brandes_room

# amber = ambers_room.Amber()

# conor_object = conors_room.ConorRoom.check_out()


class Main:
    def __init__(self, key):
        self.key = key

    def main_play(self):
        conors_room.ConorRoom(self.key).play()

    def start_adventure(self):
        start = input(
            'Would you like to follow the witty albino groundhog with an Apple watch down the rabbit hole into Wonderland? Yes or No: ')
        if start == 'Yes'.lower:
            print("Here we go! Get ready to encounter many mythical creatures on your adventure. May the odds be ever in your favor!")
            players_choice = input(
                'which adventure would you like to start with?')

            if players_choice == 1:
                print("you have chose to the journey to the kingdom of hearts")
            elif players_choice == 2:
                pass
            else:
                print("I get that you think you're a special snowflake, but imma really need for you to stick with that status quo here.")
        else:
            print('The groundhog and Mad Hatter are sad you did not join them :')


game = Main()

game.main_play()


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
