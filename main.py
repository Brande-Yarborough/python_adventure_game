import ambers_room

amber = ambers_room.Amber()

amber.check_out()

name = input('Enter your name: ')
print(f'Hello, {name}! Welcome to your adventure!')

# put story about following groundhog here?
start = input(
    'Would you like to follow the witty albino groundhog with an Apple watch down the rabbit hole into Wonderland? Yes or No: ')
if start == 'Yes'.lower:
    print("Here we go! Get ready to encounter many mythical creatures on your adventure. May the odds be ever in your favor!")
else:
    print('The groundhog and Mad Hatter are sad you did not join them :( ')
