import time


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
        answer1 = input('Oh my......It looks like I have gotten myself\n                into quite a bit of trouble...\n\nI don''t look anything like a groundhog anymore...\n do you want to (1) dive deeper or (2) come up for air?')
        if answer1 == '1':
            print('Hmmm....what a terrible choice.')
            self.sinking_down()
        if answer1 == '2':
            print(
                'I do believe my flippers are a flailing....WE''RE SINKING WE''RE SINKING')
            self.sinking_down()

    def sinking_down(self):
        print('TEST, down to the bottom')
