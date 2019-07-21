from django.shortcuts import render

def games(req):
    return render(req, 'game/games.html')
