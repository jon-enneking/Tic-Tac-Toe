import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        print(f"Player {self.letter}\'s turn:")
        return random.choice(game.availableMoves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validMove = False
        print(f"Player {self.letter}\'s turn.", end=' ')
        
        while(not validMove):
            try:
                choice = input("Choose a spot [0-8]: ")
                val = int(choice)
                if val not in game.availableMoves():
                    raise ValueError
                validMove = True
            except ValueError:
                print("That spot is taken already or invalid. Try again")
        
        return val


        

