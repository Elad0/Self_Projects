from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
import json
import TicTacToeAI.AIDriver as computerAI



@never_cache
def index(request):
    return render(request, 'MainMenu.html')

@never_cache
def tictactoeHuman(request):
    return render(request, "TicTacToe.html")

@never_cache
def tictactoeComputer(request):
    return render(request, "AITicTacToe.html")

@never_cache
def process_board(request):
    if request.method == 'POST':
        board = json.loads(request.body).get('board', None)     #Board is extracted correctly
        if board is not None:
            computerAI.dinosaur(board)
            response_data = {'success': True, 'board': board}
            return JsonResponse(response_data)
    return JsonResponse({'success': False})

def check_board_for_winner(request):
    if request.method=='POST':
        board = json.loads(request.body).get('board', None)
        if board is not None:
            boardCondition=computerAI.check_board_for_winner(board)
            response_data = {'success': True, 'Winner': boardCondition, 'board': board}
            return JsonResponse(response_data)
    return JsonResponse({'success': False})