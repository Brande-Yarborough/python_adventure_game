import time
import os


class ConorRoom:
    def __init__(self, key):
        self.key = key
        self.riddle_correct = False

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("welcome to the beach \n the ocean is a powerful and mysterious creature")

    def play(self):
        # This is the first function called.
        self.key += 1
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
        answer1 = input('Oh my......It looks like I have gotten myself\n                                         into quite a bit of trouble...\n\nI don''t look anything like a groundhog anymore...and where is my watch??\n do you want to (1) dive deeper or (2) come up for air?')
        if answer1 == '1':
            print('Hmmm....what a devastating choice.')
            self.sinking_down()
        if answer1 == '2':
            print(
                'I do believe my flippers are a flailing....WE''RE SINKING WE''RE SINKING')
            self.sinking_down()

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
                 """)
        print("Oh! I see my watch! It's wayyyyyyyy down there...under that ugly fish fellow...")
        answer2 = input(
            'Will you go grab it for me? (1) Of course! I would love to help or (2) Absolutely not...get me back to the surface!')
        if answer2 == 1:
            print('Thanks!')
        else:
            print('This is a lousy way to repay our friendship...')

    def ask_the_riddle(self):
        # This is the first function called
        print(r"""
        I once lived on the shore, amongst the trees so green
        With my friends Walrus and the Carpenter, in a place so serene
        We’d bask in the sun, the warmth of the day
        And talk about life, in our own special way

        I recall the days, when I was so fair
        An albino groundhog, with shocking white hair
        But now I’m a creature of the deep blue sea
	I swim and play among the fields of seaweed

	I miss my friends, and the life that I knew
	The walrus and carpenter were my friends that were true
        But the sea is my home, now with a beautiful view //fix

	In my dreams, I visit the shore once more
	I still see the Walrus, rolling in sand
	And the Carpenter, with his great chiseled hand
	And we laugh and we dance, just like we did before

	But now I must wake, and return to the sea
	So if you please answer a single riddle for me: 

	I tap when I talk, in a strange sort of way
	And my name is another for a friend I have made

	Full answers only! No more and no less
	Punctation correct and all that mess
	If you answer wrong I will keep you here
	Until you rot in the ocean and your bones disappear
        
        
        """)
