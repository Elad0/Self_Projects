'''
Created on Mar 27, 2023

@author: eohay
'''
from django.shortcuts import render
from math import inf

def dinosaur(board):
    board[0][0]="O"
    board[1][2]="O"
    board[0][2]="O"

"""
Checks the board to determine if there is a winner
@return: 'X' if x wins, 'O' if O wins. None otherwise
"""    
def check_board_for_winner(board: list)->str:
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # No winner
    return None

"""
Uses the minmax algorithim to determine what the ai should do 
"""
def determine_best_move_ai(board: list):
    max_score = float('-inf')
    best_move=()
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]='O'
                max_score= max(min_max(board, 0, 'O'), max_score)
                board[i][j]=' '
                best_move= (i,j)
    return best_move
            
                
                    
def min_max(board: list, depth: float, turn: str):
    winner=check_board_for_winner(board)
    score=determine_score(winner)

def determine_score(board_state: str):
    if board_state == 'X':
        return -1
    if board_state== 'O':
        return 1
    return 0

def random_move(board):
    print("fart")


