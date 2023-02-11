import time
import os
import string


class ConorRoom:
    def __init__(self, key):
        self.key = key

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("welcome to the beach \n the ocean is a powerful and mysterious creature")

    def play(self):
        # This is the first function called.
        update_value = self.key  # This sets it to the initilization value.
        print(self.key)
        for each in range(0, 5):
            print(r"""
                   /\                       /\                        /\                       /\
                  /**\                     /**\                      /**\                     /**\
                 /****\   /\      /\      /****\   /\               /****\   /\      /\      /****\   /\
                /      \ /**\    /  \    /      \ /**\             /      \ /**\    /  \    /      \ /**\
               /  /\    /    \  /    \  /  /\    /    \    /\     /  /\    /    \  /    \  /  /\    /    \
              /  /  \  /      \/      \/  /  \  /      \  /  \   /  /  \  /      \/      \/  /  \  /      \
             /  /    \/ /\     \      /  /    \/ /\     \/     \/  /    \/ /\     \      /  /    \/ /\     \
            /  /      \/  \/\   \    /  /      \/  \/\   \     /  /      \/  \/\   \    /  /      \/  \/\   \
         __/__/_______/___/__\___\__/__/_______/___/__\___\___/__/_______/___/__\___\__/__/_______/___/__\___\_
    """)
            time.sleep(0.5)
        os.system('clear')
        print(r"""
                                                                                        ╔╦╦╦═╦╗╔═╦═╦══╦═╗
                                                                                        ║║║║╩╣╚╣═╣║║║║║╩╣
                                                                                        ╚══╩═╩═╩═╩═╩╩╩╩═╝""")
        print(r"""
                                                 ,adBBB8B88B8888b,
                            ,d8888ba,,,,,,,adBBBB8B888888888888888BB#,
         ;.              d8888888888888888BBB8888888888888888(O;8B###RRR88b,
                            `VB888888888888888888888888888888888888PY8888P'
                              VWWB88888BB88B8B8888888888888888888P'
                             dWWBBBBBBBBB8BB8B888888888888888P'
                         ,dBBBBBBBBBBBBB8B88888888888888888P'
                      ,dBBBBBBBBBBBB888888888888P'  d8888P
                   ,dBBBBBBBBBBB8888888888P'     ,d8888P'
               ,adBBBBBBBBB888888888P'         d888P'
            ,dBBBBBBBBBB888888P'
         ,dBBBBBBBBBB888P'
;.aaad88bad8BBBBBBBBP'                     ;.
 V88888888BBBP'
  Y888888P                ;.
  8888888
  I8888P
  888P
 88P
 V""")
        answer1 = input('Oh my......It looks like I have gotten myself\n                                                  ...into quite a bit of trouble...\n\nI don''t look anything like a groundhog anymore...and where is my watch??\n\n do you want to (1) dive deeper or (2) come up for air?')
        if answer1 == '1':
            update_value = self.sinking_down()
            print('Hmmm....that is a brave choice.')
        if answer1 == '2':
            print(
                'I do believe my flippers are a flailing....WE\'RE SINKING WE\'RE SINKING')
            update_value = self.sinking_down()
        print(update_value)
        return update_value

    def sinking_down(self):
        os.system('clear')
        print(r"""                         
                         i
                        ,n.
                        dmb
                      .d#v%b.
           ......,,,,o##mnv%oo,,,.......
     .,o@@####mmmmmnmnnnnnnnnnvvvvvvvvv%%%,,.
   ,@@#######mmmmmnmnnnnnnnnnvnvvvvvvvvv%%%%%%.
  d########m#mmmmnmnnnnnnnnnnnvnvvvvvvv%v%%%%%%,             ,
 ,@#######m#mmmmmmnmnnnnnnnnnvnvvvvvvvvv%v%%%%%%.            %
 @########m#mmmmmmmnnnnnnnnnnnvnvvvvvvvvv%v%%%%%%           ;%:
.@#######mmmmmmmmmnmnnnnnnnnnvnvvvvvvvvv%v%%%%%%%.        .;%%%
i########mP'    `YmnnnnnnnnnnnvnP'    'Yv%v%%%%%%;      ,%%%%%;
i#######mm    o   nnnnnnnnnnnvnv   o    %v%%%%%%%; .::::%:%%%%'
i#######mmb.    ,dnnnnnnnnnnnnvnb.    ,dv%v%%%%%%;..:::::%:%%'
`@#####m#mmmmmmmmmnnnnnnnnnnnvnvnvvvvvvv%v%%%%%%%'.:::::%:%%%
 @######mmmmmmmmmnmnnnnnnnnnnnvnvvvvvvvvv%v%%%%%% .::::::%:%%,
 P#######mmmmmmmnmnnnnnnnnnnnvnvnvvvvvvv%v%%%%%%;..:::::%:%%%%.
 `@#####m#mmmmmmmnmnnnnnnnnnnnvnvvvvvvv%v%v%%%%%'       `%%%%%%
  P######m#mmmmmmmnnnnnnnnnnnvnvnvvvvv%v%v%%%%%;           %%%%;
   @######m;""vvmnmnnnnnnnnnnnnvvvvv"";%v%%%%%%'            `%%:
    @####mmmmo,.     v   '   v    .,ov%v%%%%%%'               %'
     Y@#####m#mmmb^aa..  A  ..a^dvv%v%v%%%%%%'                `
      `Y@@#m##mmmmnmnnnnnnnnnvnvvvvv%v%%%%%"'
         `""Y8@@@nmnnnnnnnnnvnvvvv%%%%""'
                 '''''""""""'''''
                 
                 
                 
                 
                                        _*_
                     ,;-^-:.
 .------------------'` \   `'-----------.---.
|  o  o  o          ((  ))           |-  |
 `------------------..     ',-----------'---'
                     `:._.;'         
                       `*'
                 
                 
                 
                 

                 
                 
                 
                 """)
        print("Oh wait! I see my watch! It\'s wayyyyyyyy down there...under that ugly fish fellow...")
        answer2 = input(
            'Will you go grab it for me? (1) Of course! I would love to help or (2) Absolutely not...get me back to the surface!')
        if answer2 == '1':
            print('Why thank you! Now that I can finally tell the time...\n\n')
            time.sleep(1)
            print('          ....good heavens! We are VERY late! \n\n            I will barely have time to recite my lengthy poem!...')
            time.sleep(2)
            return self.ask_the_riddle()
        else:
            print('This is a lousy way to repay our friendship...well I guess we\'ll never figure out what time it is...')
            time.sleep(1)
            print(
                '\n....since we aren\'t on a schedule, we have time to read my lengthy poem!')
            return self.ask_the_riddle()

    def ask_the_riddle(self):
        print(r"""

                  ... ....                     .. ...                           ____,--
  .. ...... .                           ........__                  __,'MMII;:.
...                                      ......|__|            _,--'MMI;:.
                                    @         /|. .          ,'MMI;:.WI;;:.
            ,d888b,                |.\       / |\           /MWI;;  WWI;.
           J8888888L               |' \     /^^|^\        ,'MWI;   WWWI;;:.
           888888888               |. o\ __/___|__\_   ,-'MWI;:.  WI;;::.
-----------------------------------|.  L\-`--------'--'_MWI;:.   WWI;;:.
      - -__--__--__--__ -           \.   \                `---. WI;:.     ____-
       - __--__--__-- _             |:    :.                   `/|-------'
        _ -__--__--_ -              |:     ::.                ,''/
          - _--__- _                |/       ::.             /: |
___        _ --__ -                 /'         :`--.______,-::  /
###\        _ -_ -                 /'   ._ .     ``        '    `-_
,--'         --__              _,-'   __/. .... .  .  ___,---.__,-'-.
              -_         __,--/'   __/##`-._____,----'::::::::::::::#\
                              `---'`````##:::::::::::::::::::::::::::#`---.
                                         `````::::::::::::#######:::####\


        I once lived on the shore, amongst the trees so green
        With my friends Walrus and Carpenter, in a place so serene
        We'd bask in the sun, the warmth of the day
        And talk about life, in our own special way

        I recall the days, when I was so fair
        An albino groundhog, with shocking white hair
        But now I'm a creature of the deep blue sea
        I swim and play among fields of seaweed

        I miss my friends, and the life that I knew
        The walrus and carpenter were my friends that were true
        Now the sea is my home, with an aqua-green view
        
        In my dreams, I visit the shore
        I still see the Walrus, rolling in sand
        And the Carpenter, with his great chiseled hand
        And we laugh and we dance, just like we did before
        
        But now I must wake, and return to the sea
        So if you please answer a riddle for me: 
        
        I tap when I talk, in a strange sort of way
        And my name is another for a friend I have made
        
        Full answers only! No more and no less
        Punctation correct and all of that mess
        If you answer wrong I will keep you here
        Until you rot in the ocean and your bones disappear...
        
        
        """)
        riddle_answer = input('Answer carefully: ').lower()
        if riddle_answer == 'morse code':
            result = self.key + 1
            print(result)
            print('Absolutely brilliant! Now, WAKE UP')
            update_value = result
            return update_value
        else:
            for each in range(0, 2):
                riddle_try = input(
                    'Those bones are starting to rot...! Guess again:')
                if riddle_try == 'morse code':
                    result = self.key + 1
                    print('Absolutely brilliant! Now, WAKE UP')
                    update_value = result
                    return update_value

            print('OOps! Hope it wasn\'t a technical snafu...you got it wrong.')
            time.sleep(2)
