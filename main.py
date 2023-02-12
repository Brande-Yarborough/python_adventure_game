import string
import josiahs_room
import conors_room
import ambers_room
import brandes_room
import os


class Main:
    def __init__(self, key):
        self.key = key

    def heartkingdom_room(self):
        result = ambers_room.Hearts_Room(self.key).play()
        self.key = result

    def main_play(self):
        result = conors_room.ConorRoom(self.key).play()
        self.key = result

    def mirror_room(self):
        josiahs_room.Mirror_Room(self.key).enter()

    def computer_room(self):
        result = brandes_room.BrandeRoom(self.key).entrance()
        self.key = result

    def finalroom(self):
        print("Congratulations! You\'ve managed to solve all the riddles, As a reward please join me for tea")
        print(r"""
        
                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( --------------------------------------------------------------------------------------------------------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.       ;,'
                                                            _o_    ;:;'
                                                        ,-.'---`.__ ;                    
                                                       ((j`=====',-'
                                                        `-\______/                                                                                                               
                                :----:     o8Oo./
                                C|====| ._o8o8o8Oo_.
                                |    |  \========/    
                                `----'   `------'                                                                                                         *             *
                                                     *
                                                                            *                                                               *
                                                                                    *
                                                                                                    (             )
                                                                                            )      (*)           (*)      (
                                                                                    *       (*)      |             |      (*)
                                                                                            |      |~|           |~|      |          *
                                                                                            |~|     | |           | |     |~|
                                                                                            | |     | |           | |     | |
                                                                                            ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                                                                                        .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
                                                                                    ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
                                                                                    a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
                                                                                    ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
                                                                                    ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
                                                                                    ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
                                                                                    ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
                                                                                    ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
                                                                                    ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
                                                                                    ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
                                                                                ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
                                                                            .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                                                            .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                                                            %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                                                            %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                                                            `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                                                            `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                                                `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                                                        `,,,,,,,,,'
                                                                                                        `%%%%%%%'
                                                                                                        `%%%%%'
                                                                                                            %%%     
                                                                                                        %%%%%
                                                                                                        .,%%%%%%%,.
                                                                                                ,%%%%%%%%%%%%%%%%%%%,
        ~  ~                                                                                                                        
      ( o )o)
     ( o )o )o)
   (o( ~~~~~~~~o
   ( )' ~~~~~~~'
   ( )|)       |-.
     o|     _  |-. \
     o| |_||_) |  \ \
      | | ||_) |   | |
     o|        |  / /
      |        |." "
      |        |- '
      .========.  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

    
        """)

    def start_adventure(self):

        start = input(
            'La la la la...oh! I didn\'t see you there...I was just washing my majestic white fur.\n\nYou wouldn\'t be interested in following a beautiful rodent into a hole would you?\nI am about to meander down...I got a notification that it was going to rain on my Apple Watch. \nWould you be interested in coming with me to Wonderland?\nYes or No:\n> ')
        if start.lower() == 'yes' or start.lower() == 'y' or start == '1':
            print("\nOh delightful. We barely fit...Get ready to encounter many mythical creatures on your adventure.\n May the odds be ever in your favor!\n")
            print(r"""
          ___   
         |   |
       __|__ |__
        (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
          ~"` ~"~~`
""")
            players_choice = input(
                'Which adventure would you like to start with:\n(1) The Kingdom of Hearts,\n(2) A Seafaring Journey,\n(3) The Mysterious Mirror, or\n(4) The Cave of Computers?\n>').lower()
            os.system("clear")

            if players_choice == '1':
                print("You have chosen a journey to the kingdom of hearts. With the help of you Groundhog friend you must evade the queens wrath. Be wary of her tarts of you shall paint the roses red, and possibly lose your head.")
                self.heartkingdom_room()
            elif players_choice == '2':
                self.main_play()

            elif players_choice == '3':
                self.mirror_room()

            elif players_choice == '4':
                self.computer_room()

            else:
                print("What\'s the matter, are you mad as a hatter. If you wish to have tea, pick a number to proceed. Preferably 1 through 4...\n")
        else:
            print('The groundhog and Mad Hatter are sad you did not join them :\n')

    def next_sequence(self):
        # clear the terminal
        # print(wow that was weird! Thank goodness you're still here. I am going to keep wandering around.
        # Let's check out another room!
        players_choice = input(
            'Wow that was weird! Thank goodness you\'re still here.\n\n I am going to keep wandering around.\n\n Feel free to pick another room...\n(1) The Kingdom of Hearts,\n(2) A Seafaring Journey,\n(3) The Mysterious Mirror, or\n(4) The Cave of Computers?\n>')

        if players_choice == '1':
            print("You have chosen a journey to the kingdom of hearts. With the help of your Grounhog friend you must evade the queens wrath. Be wary of her tarts of you shall pain the roses red, and possible lose your head.")
            self.heartkingdom_room()
        elif players_choice == '2':
            self.main_play()

        elif players_choice == '3':
            print("\nA mirror appears before you and you approach it. You reach out to touch it and when your hand touches the one of your reflection, fall through the veneer.")
            self.mirror_room()

        elif players_choice == '4':
            self.computer_room()


# This initializes the key to a value of zero.

game = Main(0)

game.start_adventure()


while game.key < 4:
    print(f'Current keys = {game.key}')
    game.next_sequence()

if game.key >= 4:
    # call final room here
    game.finalroom()
    print("\n\n\n----------------GAME OVER----------------")
    print(r""" 
'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
   `-._   ````    _.-'
          ``-------''
          """)


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
