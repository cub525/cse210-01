import tictactoe
from unittest.mock import patch
import sys
import io
import unittest

TEST_GAME = """
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

x's turn to choose a square (1-9): 2

1|x|3
-+-+-
4|5|6
-+-+-
7|8|9

o's turn to choose a square (1-9): 5

1|x|3
-+-+-
4|o|6
-+-+-
7|8|9"""

class CapturePrint():
    def __enter__(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        return captured_output

    def __exit__(self, *args):
        sys.stdout = sys.__stdout__


class TestTicTacToe(unittest.TestCase):
    def test_display(self):
        with CapturePrint() as captured_output:
            board = tictactoe.Board()
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)

    @patch('tictactoe.input', create=True)
    def test_input(self, mocked_input):
        mocked_input.side_effect = [1]
        board = tictactoe.Board()
        board.prompt('x')
        with CapturePrint() as captured_output:
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("x|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)

    @patch('tictactoe.input', create=True)
    def test_interact(self, mocked_input):
            mocked_input.side_effect = [2, 5]
            board = tictactoe.Board()
            with CapturePrint() as captured_output:
                board.interact()
                message = captured_output.getvalue()
            self.assertEqual(TEST_GAME, message)
