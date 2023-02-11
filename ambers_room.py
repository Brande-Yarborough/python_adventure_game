import random


class Hearts_Room:

    def __init__(self, key,):
        self.key = key

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("While following your groundhog friend,you have stumbled into the kingdom of hearts. \n The queen is convinced you have stolen her tarts. \n If you wish to be free, and avoid her majesty. \n You must answer this rhyme, but make haste, make haste! three guesses seal you fate.")

    def play(self):
        self.queens_riddle()
        self.key += 1
        print(self.key)

    def queens_riddle(self):

        print("While following your groundhog friend,you have stumbled into the kingdom of hearts.\n The queen is convinced you have stolen her tarts.\n If you wish to be free, and avoid her majesty. \n You must answer this rhyme, but make haste, make haste! three guesses seal you fate.")
        print(r"""
                                  ,;;;, 
                                ,;;;;;;;, 
             .;;;,            ,;;;;;;;;;;;, 
            .;;%%;;;,        ,;;;;;;;;;;;;;, 
            ;;%%%%%;;;;,.    ;;;;;;;;;;;;;;; 
            ;;%%%%%%%%;;;;;, ;;;;;;;;;;;;;;; 
            `;;%%%%%%%%%;;;;;,;;;;;;;;;;;;;' 
             `;;%%%%%%%%%%;;;;,;;;;;;;;;;;' 
               `;;;%%%%%%%%;;;;,;;;;;;;;;' 
                  `;;;%%%%%%;;;;.;;;.;;; 
                     `;;;%%%;;;;;;.;;;,; .,;;' 
                         `;;;;;;;;;;,;;;;;;'.,;;;, 
                          ;;;;;;;;;;;;;;;;;;;;;,. 
          .          ..,,;;;;;......;;;;;;;.... '; 
          ;;,..,;;;;;;;;;;;;..;;;;;;..;;;;.;;;;;. 
           ';;;;;;;;;;;;;;..;;;a@@@@a;;;;;;;a@@@@a, 
        .,;;;;;;;;;;;;;;;.;;;a@@@@@@@@;;;;;,@@@@@@@a, 
      .;;;,;;;;;;;;;;;;;;;;;@@@@@'  @@;;;;;;,@  `@@@@;, 
     ;' ,;;;,;;;;;;;;;;;;;;;@@@@@aa@@;;;;,;;;,@aa@@@@;;;,.,; 
       ;;;,;;;;;;;;;;;;;;;;;;@@@@@@@;;;,;a@@'      `;;;;;;;' 
       ' ;;;,;;;;;;;;;;;;;;;;;;;;;;;;,;a@@@       #  ;;,;;, 
.//////,,;,;;;;;;;;;;;;;;;,;;;;;;;;,;;a@@@a,        ,a;;;,;;, 
%,/////,;;;;;;;;;;;;;;;;;;;;,;,;,;;;;a@@@@@@aaaaaaa@@@;;;;;'; 
`%%%%,/,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@@@;00@@;;;;;' 
  %%%%%%,;;;;;;;;;;;;;;;;;;;;;;;;;;;a@@@@@@@@@@;00@@;;;;;' 
   `%%%%%%%%%%,;;;;;;;;;;;;;;;;;;;;a@@@@@@@@@;00@@;;;;;' 
     `%%%%%%%%%%%%%%%,::::;;;;;;;;a@@@@@@@;00@@@::;;;%%%%%, 
       `%%%%%%%%%%%%%%%,::::;;;;;@@@@@@' 0@@@@::;;%%%%%%%%' 
          Oo%%%%%%%%%%%%,::::;;a@@@@@'  ,@@@::;;%%%%%%%' 
           `OOo%%%%%%%%%%,::::@@@@@'    @@;::;%%%%%%' 
             `OOOo%%%%%%%%,:::@@@@,;;;,a@:;;%%%%%' 
               `OOOOOo%%%%%,:::@@@aaaa@';;%%%%' 
                  `OOOO;@@@@@@@@aa@@@@@@@@@' 
                      ;@@@@@@@@@@@@@@@@@@@' 
                       @@@@@@@@'`@@@@@@@@' 
                       `@@@@@'    @@@@@' 
                        `@@'       @@'
                        """)
        word_to_guess = ["watermelon"]
        word = random.choice(word_to_guess)

        word_display = '_' * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 3
        print("There was a green house. Inside the green house there was a white house.\n Inside the white house there was a red house. \n Inside the red house there were lots of babies. \n What is it?")
        print(word_display)
        print("you have", tries, "tries")
        print("\n")

        while not guessed and tries < 4:
            guess = input("you may guess a letter or word!_")

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print(
                        "There is no guessing twice or thrice of the same letter,if you wish to escape I suggest you do better", guess)
                elif guess not in word:
                    print(guess, "Better guess again, or its off with our heads!")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("What luck friend!", guess, "is in the word")
                    guessed_letters.append(guess)
                    completed_word = list(word_display)
                    indices = [i for i, letter in enumerate(
                        word) if letter == guess]
                    for index in indices:
                        completed_word[index] = guess
                    word_display = "".join(completed_word)
                    if "_" not in word_display:
                        guessed = True

            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("Please try again, I dont want to paint the roses red", guess)

                elif guess != word:
                    print(guess, "Perhaps it is a fruit of sorts")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_display = word

            else:
                print(
                    "Youre time is running short dear friend \n Please try again, I dont want to paint the roses red")
                print(r"""
                  __
                              ___  _// \
                            _/   \/__|_ \
                           /  __//_/==\_| ___
                         / | / /|// == \ \   /
                         |  | |\|| //_\ | |_/
                          \  \ \\ / \_/| || \
                           \___/\\| _  ///___\
                             \__|\_\=//_// _\_|
                                \___\_____/
                               !! \____/
                              !!
                               !!
                    ___      -(!!      __ ___ _
                   |\|  \       !!_.-~~ /|\-  \~-._
                   | -\| |      !!/   /  | |\- | |\ \
                    \__-\|______ !!  |    \___\|  \_\|
              _____ _.-~/|\     \\!!  \  |  /       ~-.
            /     /|  / /|  \    \!!    \ /          |\~-
          /  ---/| | |   |\  |     !!                 \__|
         | ---/| | |  \ /|  /    -(!!
         | -/| |  /     \|/        !!
         |/____ /                  !!)-
                                   !!
                """)
            print(word_display)
            print(tries)
            print("\n")
            if guessed:
                self.key += 1
                print(
                    "It seems to me that her majesty is appeased, perhaps we should flee \n ...I also have a confession to make. I stole the queens tart \n I am sure it will go swell with a cup of tea.")
                print(r"""
            (
              )
         __..---..__
     ,-='  /  |  \  `=-.
    :--..___________..--;
     \.,_____________,./ 
                """)

            if tries == 0:
                print("I do hope the tart was worth it.", word)
                break
