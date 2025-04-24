class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily! 🥣😋")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is now resting... 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing and having fun! 🎾😄")
        else:
            print(f"{self.name} is too tired to play! 🥱")

    def cuddle(self):
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} loves the cuddles! 🐾❤️")

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}! 🧠")
        else:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)} 🐕✨")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 😢")

    def get_status(self):
        print(f"\n📋 --- {self.name}'s Status ---")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10\n")
