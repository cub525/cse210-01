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

    def __exit__(self, *_):
        sys.stdout = sys.__stdout__


class TestDisplay(unittest.TestCase):
    def test_display(self):
        with CapturePrint() as captured_output:
            board = tictactoe.Board()
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)

    def test_display_changes(self):
        board = tictactoe.Board()
        board.board[0] = 'x'
        with CapturePrint() as captured_output:
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("\nx|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)


class TestInteraction(unittest.TestCase):
    @patch('tictactoe.input', create=True)
    def test_prompt(self, mocked_input):
        mocked_input.side_effect = ["1"]
        board = tictactoe.Board()
        board.prompt()
        with CapturePrint() as captured_output:
            board.display()
            message = captured_output.getvalue()
        self.assertEqual("\nx|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n", message)

    @patch('tictactoe.input', create=True)
    def test_interact(self, mocked_input):
            mocked_input.side_effect = ["2", "5", "q"]
            board = tictactoe.Board()
            with CapturePrint() as _:
                board.interact()
            expected_board = [" ", "x", " ", " ", "o", " ", " ", " ", " "] 
            self.assertEqual(expected_board, board.board)

    def test_interact_win(self):
            board = tictactoe.Board()
            board.board = ["x", "x", "x", " ", " ", " ", " ", " ", " "]
            with CapturePrint() as captured_output:
                board.interact()
                message = captured_output.getvalue()
            self.assertEqual("Good game. Thanks for playing!", message)



class TestWinCondition(unittest.TestCase):
    board = tictactoe.Board()
    def test_win_horizontal(self):
        self.board.board = ["x", "x", "x", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.board.is_win())

    def test_win_horizontal2(self):
        self.board.board = [" ", " ", " ", "x", "x", "x", " ", " ", " "]
        self.assertTrue(self.board.is_win())

    def test_win_horizontal3(self):
        self.board.board = [ " ", " ", " ", " ", " ", ", ""x", "x", "x"]
        self.assertTrue(self.board.is_win())
    
    def test_win_vertical(self):
        self.board.board = ["x", " ", " ", "x", " ", " ", "x", " ", " "]
        self.assertTrue(self.board.is_win())

    def test_win_vertical2(self):
        self.board.board = [" ", "x", " ", " ", "x", " ", " ", "x", " "]
        self.assertTrue(self.board.is_win())

    def test_win_vertical3(self):
        self.board.board = [ " ", " ", "x", " ", " ", "x", " ", " ", "x"]
        self.assertTrue(self.board.is_win())

    def test_win_diagonal(self):
        self.board.board = ["x", " ", " ", " ", "x", " ", " ", " ", "x"]
        self.assertTrue(self.board.is_win())

    def test_win_diagonal2(self):
        self.board.board = [" ", " ", "x", " ", "x", " ", "x", " ", " "]
        self.assertTrue(self.board.is_win())
