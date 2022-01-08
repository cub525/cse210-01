class Board():
    def __init__(self) -> None:
        self.board = 9*[" "]
        self.turn = 'x'

    def display(self):
        for i in range(9):
            end="\n" if i == 8 else "\n-+-+-\n" if ( i + 1 ) % 3 == 0 else "|"
            print(i + 1 if self.board[i] == " " else self.board[i], end=end) 

    def prompt(self):
        # print("x's turn to choose a square (1-9): ", end="")
        square = int( input(f"{self.turn}'s turn to choose a square (1-9): ") ) - 1
        self.board[square] = self.turn
        self.turn = 'o' if self.turn == 'x' else 'x'

    def interact(self):
        i = 0
        while i < 2:
            self.display()
            self.prompt()



def main():
    board = Board()
    board.interact()

if __name__ == "__main__":
    board = main()
