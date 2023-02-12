import random
import time


class Hearts_Room:

    def __init__(self, key,):
        self.key = key

    def entrance(self):
        print("While following your groundhog friend,you have stumbled into the kingdom of hearts. \n The queen is convinced you have stolen her tarts. \n If you wish to be free, and avoid her majesty. \n You must answer this rhyme, but make haste, make haste! three guesses seal you fate.")

    def play(self):
        update_value = self.queens_riddle()
        print(self.key)
        return update_value

    def queens_riddle(self):
        time.sleep(2)
        print(r"""
                         /\/\
                         \  /
                  /\/\    \/    /\/\                  
                  \  / _---|    \  /_ _ _ _ _ 
                   \/   ---|     \/ ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|   \ ` '  / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\

        """)
        print("While following your groundhog friend,you have stumbled into the kingdom of hearts.")
        time.sleep(2)
        print(" The queen is convinced you have stolen her tarts")
        time.sleep(2)
        print("If you wish to be free, and avoid her majesty.")
        time.sleep(2)
        print("For the tart that you ate,three guesses seal you fate. Make haste, make haste, you must solve this rhyme,\n her patience is thin, there is not much time")
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

        print("There once was a green house.")
        time.sleep(2)
        print("Inside the green house there was a white house.")
        time.sleep(2)
        print("Inside the white house there was a red house.")
        time.sleep(2)
        print("Inside the red house there were lots of babies.")
        time.sleep(2)
        print(" What is it?")
        print(word_display)
        print("you have", tries, "guesses")
        print("\n")

        while not guessed and tries < 4:
            guess = input("you may guess a letter or word!_")

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print(
                        "There is no guessing twice or thrice of a letter,if you wish to escape I suggest you do better.", guess)
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
                print("Your time is running short dear friend!")
                time.sleep(2)
                print(" Please try again, I dont want to paint the roses red.")
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

                print(
                    "It seems to me that her majesty is appeased, perhaps we should flee")
                time.sleep(2)
                print(
                    "...I also have a confession to make. I stole the queens tart you see")
                print("After all that trouble it will go well with a cup of tea.")
                print(r"""
            (
              )
         __..---..__
     ,-='  /  |  \  `=-.
    :--..___________..--;
     \.,_____________,./ 
                """)
                return self.key + 1

            if tries == 0:
                print("I do so hope that the tart was worth it...unfortunately your guesses werent perfect.So now it is time to paint roses red. As her Majesty decress Off, off, off with thier heads!")
                print(r"""
  ,   A           {}
 / \, | ,        .--.
|    =|= >      /.--.\
 \ /` | `       |====|
  `   |         |`::`|  
      |     .-;`\..../`;_.-^-._
     /\\/  /  |...::..|`   :   `|
     |:'\ |   /'''::''|   :     |
      \ /\;-,/\   ::  |. /\/\   |
      |\ <` >  >._::_.|  \  /   |
      | `""`  /   ^^  |   \/    |
      |       |       \    :    /
      |       |        \   :   / 
      |       |___/\___|`-.:.-`
      |        \_ || _/    `
      |        <_ >< _>
      |        |  ||  |
      |        |  ||  |
      |       _\.:||:./_
      |      /____/\____\

                """)
                return self.key
