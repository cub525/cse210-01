"""
This script starts an interactive tic tac toe game for two players. Valid inputs are 1-9, 'q', 'quit' and 'exit'

@author: Emmett Hart
@assignment: W02 Prove: Tic Tac Toe
"""


class Board():
    def __init__(self) -> None:
        self.board = list(range(1,10))
        self.turn = 'x'

    def display(self):
        print()
        for i in range(9):
            end="\n" if i == 8 else "\n-+-+-\n" if ( i + 1 ) % 3 == 0 else "|"
            print(self.board[i], end=end) 

    def prompt(self):
        choice = input(f"\n{self.turn}'s turn to choose a square (1-9): ") 
        if choice.isalpha() and choice in ["q", "exit", "quit"]:
            print("Quitting... ")
            return True
        elif choice.isdecimal():
            square = int(choice) - 1
            if 0 > square > 10:
                raise ValueError(f"\"{choice}\" is not a valid input")
            elif type(self.board[square]) == str:
                raise ValueError(f"Square \"{square}\" is already filled")
            else:
                self.board[square] = self.turn
                self.turn = 'o' if self.turn == 'x' else 'x'
        else:
            raise ValueError(f"\"{choice}\" is not a valid input\nValid Inputs are numbers 1-9, 'quit', 'q', and 'exit'")

    def interact(self):
        quit_ = False
        self.display()
        while not (quit_ or self.is_win() or self.is_draw()):
            try:
                quit_ = self.prompt()
            except ValueError as verror:
                print(verror)
                continue
            self.display()
        else:
            if self.is_win():
                print("\nGood game. Thanks for playing!")
            elif self.is_draw():
                print("\nDraw. ")


    def is_win(self) -> bool:
        return (self.board[0] == self.board[1] == self.board[2] or
                self.board[3] == self.board[4] == self.board[5] or
                self.board[6] == self.board[7] == self.board[8] or
                self.board[0] == self.board[3] == self.board[6] or
                self.board[1] == self.board[4] == self.board[7] or
                self.board[2] == self.board[5] == self.board[8] or
                self.board[0] == self.board[4] == self.board[8] or
                self.board[2] == self.board[4] == self.board[6])

    def is_draw(self):
        return set(self.board) == {'x', 'o'}

def main():
    board = Board()
    board.interact()

if __name__ == "__main__":
    board = main()
