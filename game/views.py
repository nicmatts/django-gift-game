from django.shortcuts import render

from .models import Game, Person, Gift


def index(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'index.html', context)


def detail(request, game_name):
    game = Game.objects.get(game_name=game_name)
    people = game.person_set.all().order_by('order')
    gifts = Gift.objects.all()
    context = { 'game': game,
                'people': people, 
                'gifts': gifts, }
    return render(request, 'game.html', context)
