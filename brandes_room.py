class BrandeRoom:
    def __init__(self, key):
        self.key = key

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("Welcome to the cave of computers!")

    def play(self):
        self.key += 1
        print(self.key)
