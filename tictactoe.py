"""
This script starts an interactive tic tac toe game for two players. Valid inputs are 1-9, 'q', 'quit' and 'exit'

@author: Emmett Hart
@assignment: W02 Prove: Tic Tac Toe
"""
class Board():
    def __init__(self) -> None:
        self.board = 9*[" "]
        self.turn = 'x'

    def display(self):
        print()
        for i in range(9):
            end="\n" if i == 8 else "\n-+-+-\n" if ( i + 1 ) % 3 == 0 else "|"
            print(i + 1 if self.board[i] == " " else self.board[i], end=end) 

    def prompt(self):
        choice = input(f"\n{self.turn}'s turn to choose a square (1-9): ") 
        if choice.isalpha() and choice in ["q", "exit", "quit"]:
            print("Quitting... ")
            return True
        elif choice.isdecimal():
            square = int(choice) - 1
            if 0 > square > 10:
                raise ValueError(f"\"{choice}\" is not a valid input")
            elif self.board[square] != " ":
                raise ValueError(f"Square \"{square}\" is already filled")
            else:
                self.board[square] = self.turn
                self.turn = 'o' if self.turn == 'x' else 'x'
        else:
            raise ValueError(f"\"{choice}\" is not a valid input\nValid Inputs are numbers 1-9, 'quit', 'q', and 'exit'")

    def interact(self):
        quit_ = False
        self.display()
        while not (quit_ or self.is_win()):
            try:
                quit_ = self.prompt()
            except ValueError as verror:
                print(verror)
                continue
            self.display()

    def is_win(self) -> bool:
        return self.board[0] == self.board[1] == self.board[2]

def main():
    board = Board()
    board.interact()

if __name__ == "__main__":
    board = main()
