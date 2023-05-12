"""TicTacToeAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tictactoe import views
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('TicTacToe.html', views.tictactoeHuman, name='tictactoe'),
    path('AITicTacToe.html', views.tictactoeComputer, name='AITicTacToe'),
    path('process-board/', views.process_board, name='process_board'),
    path('check-board-for-winner-board/', views.check_board_for_winner, name='check_board_for_winner'),
    
]
