import time
import random


class Player:
    def __init__(self, name, p1, p2):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def get_score(self, player):
        if player == "p1":
            return self.score_p1
        elif player == "p2":
            return self.score_p2
        else:
            return None

    def __str__(self):
        return f"\nThis match is between {self.p1} and {self.p2}! Lets get ready to rumble!\n"

    def play_game(self):
        i = 0

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        while i < 7:
            if self.score_p1 >= 15 or self.score_p2 >= 15:
                print("\nGame Over!\n")
                return

            player_number = random.choice(numbers)
            time.sleep(0.5)
            p1answer = int(input(f"{self.p1.name} guess the number: "))
            p2answer = int(input(f"{self.p2.name} guess the number: "))
            time.sleep(0.5)
            if p1answer not in numbers:
                print(f"{self.p1.name} Invalid Entry. Pick a # between 1-15")
                continue
            if p2answer not in numbers:
                print(f"{self.p2.name} Invalid Entry. Pick a # between 1-15")
                continue

            if p1answer == player_number:
                print(f"\nThe number was: {player_number}, {self.p1.name} gets 5 points.\n")
                self.score_p1 += 5
            elif abs(p1answer - player_number) <= 5:
                print(f"\n{self.p1.name} was close to {player_number}, you scored 2 points.\n")
                self.score_p1 += 2
            else:
                print(f"\n{self.p1.name} was way off from {player_number}, you lose 2 points.\n")
                self.score_p1 -= 2

            if p2answer == player_number:
                print(f"\nThe number was: {player_number}, {self.p2.name} gets 5 points.\n")
                self.score_p2 += 5
            elif abs(p2answer - player_number) <= 5:
                print(f"{self.p2.name} was close to {player_number}, you scored 2 points.\n")
                self.score_p2 += 2
            else:
                print(f"\n{self.p2.name} was way off from {player_number}, you lose 2 points.\n")
                self.score_p2 -= 2

            time.sleep(0.5)
            print(f"{self.p1.name}'s current score is: {self.score_p1}\n")
            print(f"{self.p2.name}'s current score is: {self.score_p2}\n")

            i += 1

        print(
            f"Maximum attempts reached!\n{self.p1.name} finished with: {self.score_p1}\n{self.p2.name} finished with: {self.score_p2}"
        )
        return self.score_p1, self.score_p2


class PlayerOne(Player):
    def __init__(self, name):
        super().__init__(name, p1=None, p2=None)
        self.score = 0


class PlayerTwo(Player):
    def __init__(self, name):
        super().__init__(name, p1=None, p2=None)
        self.score = 0


def main():
    p1 = input("Challenger one... Enter your name: ")
    p2 = input("\nChallenger two... Enter your name: ")
    gamer_one = PlayerOne(p1)
    gamer_two = PlayerTwo(p2)
    play = Player("play", gamer_one, gamer_two)
    print(Player("start", p1, p2))
    play.play_game()

    if play.get_score("p1") > play.get_score("p2"):
        print(f"{gamer_one.name} wins with {play.get_score}")
    elif play.get_score("p1") < play.get_score("p2"):
        print(f"{gamer_two.name} wins!")
    else:
        print("Its a Tie!")


main()
