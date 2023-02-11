class Hearts_Room:
    def __init__(self, key):
        self.key = key
        self.riddle_correct = False

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("welcome to the beach \n the ocean is a powerful and mysterious creature")

    def play(self):
        self.key += 1
        print(self.key)


word = ['watermelon']

word_display = '_' * len(word)
guessed = False
guessed_letters = []
guessed_words = []
tries = 3
print("You have stumbled into thekingdom of hearts. The queen is convinced you have stolen her tarts. If you wish to be free, and avoid her majesty.You must answer this rhyme, but make haste, make haste! three guesses seal you fate.")
print("There was a green house. Inside the green house there was a white house. Inside the white house there was a red house. Inside the red house there were lots of babies. What is it?")
print(word_display)
print("you have", tries, "tries")
print("\n")

while not guessed and tries < 4:
    guess = input("you may guess a letter or word!_")

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("There is guessing twice or thrice of the same letter,if you wish to escape I suggest you do better", guess)
        elif guess not in word:
            print(guess, "Better guess again, or its off with your head!")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print("Great job!", guess, "is in the word")
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
            print("You have guessed this word already", guess)
        elif guess != word:
            print(guess, "is not the word :(")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_display = word

    else:
        print("Youre time is running short traveler")
    print(word_display)
    print(tries)
    print("\n")
    if guessed:
        print("It seems to me that her majesty is appeased, you may now flee and take with you this key")
        break
    if tries == 0:
        print("I do hope the tart was worth it.", word)
        break
