import tictactoe
from unittest.mock import patch
import sys
import io
import unittest


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
        board.prompt()
        with CapturePrint() as captured_output:
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("x|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)

    @patch('tictactoe.input', create=True)
    def test_interact(self, mocked_input):
            mocked_input.side_effect = [2, 5]
            board = tictactoe.Board()
            board.interact()
            expected_board = [" ", "x", " ", " ", "o", " ", " ", " ", " "] 
            self.assertEqual(expected_board, board.board)

    @patch('tictactoe.input', create=True)
    def test_win(self, mocked_input):
        mocked_input.side_effect = [1, 4, 2, 5, 3]
        board = tictactoe.Board()
        for _ in range(4):
            board.prompt()
        with CapturePrint() as captured_output:
            board.interact()
