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
