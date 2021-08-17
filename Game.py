from Player import HumanPlayer, ComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = self.makeBoard()
        self.winner = False

    @staticmethod
    def makeBoard():
        return [" " for i in range(9)]

    @staticmethod
    def printNumBoard():
        board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in board:
            print("| " + " | ".join(row) + " |")

    def printBoard(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    
    def makeMove(self, square, letter):
        self.board[square] = letter
        print(f"Player {letter} moved to square {square}")
        return self.checkWinner(square, letter)

    def checkWinner(self, square, letter):
        row_index = square//3
        col_index = int(square/3)

        row = self.board[row_index*3:(row_index+1)*3]
        col = [self.board[col_index + (i*3)] for i in range(3)]
        left_diag = [self.board[i] for i in (0, 4, 8)]
        right_diag = [self.board[i] for i in (2, 4, 6)]
        if all(i == letter for i in row):
            return True
        elif all(i == letter for i in col):
            return True
        elif all(i == letter for i in left_diag):
            return True
        elif all(i == letter for i in right_diag):
            return True
        else:
            return False

    def availableMoves(self):
        # available = []
        # for i in self.board:
        #     if(self.board[i] == ' '):
        #         available += str(i)
        # return available
        return [i for i,x in enumerate(self.board) if x == ' ']

    def emptySquares(self):
        return ' ' in self.board

def play(game, x_player, o_player):
    game.printNumBoard()
    letter = 'X'

    while(game.emptySquares()):
        if letter == 'X':
            square = x_player.getMove(game)
        else:
            square = o_player.getMove(game)

        winner = game.makeMove(square, letter)
        game.printBoard()
        if(winner):
            print(f"Player {letter} has won the game!")
            return letter
        else:
            letter = 'O' if letter == 'X' else 'X'
    
    print("It is a tie!")


if __name__ == "__main__":
    t = TicTacToe()
    x = HumanPlayer('X')
    o = ComputerPlayer('O')
    play(t, x, o)
