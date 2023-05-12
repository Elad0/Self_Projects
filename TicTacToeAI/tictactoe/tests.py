from django.test import TestCase
import TicTacToeAI.AIDriver as computerAI
# Create your tests here.

class BoardTests(TestCase):
    def test_no_winner(self):
        board=[
            [" ", ' ', ' '],
            [" ", ' ', ' '],
            [" ", ' ', ' ']]
        self.assertEqual(computerAI.check_board_for_winner(board), None)
        
        board=[
            ["X", 'O', 'X'],
            [" ", ' ', ' '],
            [" ", ' ', ' ']]
        self.assertEqual(computerAI.check_board_for_winner(board), None)
        
        board=[
            ["X", 'O', 'X'],
            ["X", 'O', 'X'],
            ["O", 'X', 'O']]
        self.assertEqual(computerAI.check_board_for_winner(board), None)
        
    def test_winner_horizontal(self):
        board=[
            ["X", 'X', 'X'],
            ["X", 'O', 'X'],
            ["O", 'X', 'O']]
        self.assertEqual(computerAI.check_board_for_winner(board), "X")
        
        board=[
            ["X", 'O', 'X'],
            ["X", 'O', 'X'],
            ["O", 'O', 'O']]
        self.assertEqual(computerAI.check_board_for_winner(board), "O")
    
    def test_winner_vertical(self):
        board=[
            ["X", 'O', 'X'],
            ["X", 'O', 'X'],
            ["O", 'X', 'X']]
        self.assertEqual(computerAI.check_board_for_winner(board), "X")
        
        board=[
            ["O", 'X', 'X'],
            ["O", 'O', 'X'],
            ["O", 'X', 'O']]
        self.assertEqual(computerAI.check_board_for_winner(board), "O")
        
    def test_winner_diagonal(self):
        board=[
            ["X", 'O', 'O'],
            ["O", 'X', 'X'],
            ["O", 'X', 'X']]
        self.assertEqual(computerAI.check_board_for_winner(board), "X")
        
        board=[
            ["O", 'X', 'O'],
            ["X", 'O', 'X'],
            ["O", 'X', 'O']]
        self.assertEqual(computerAI.check_board_for_winner(board), "O")    
        
