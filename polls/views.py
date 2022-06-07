from polls.models import Class, Character, Player, Level, Skills, Weapons
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    num_characters = Character.objects.all().count()
    characters = Character.objects.order_by('-level')
    charakters =  Character.objects.order_by('-level')[:3]
    classes = Class.objects.all()
    skills = Skills.objects.all()
    players = Player.objects.all()
    context = {
        'num_characters': num_characters,
        'characters': characters,
        'char_vypis': charakters,
        'classes': classes,
        'skills': skills,
        'players': players
    }

    return render(request, 'index.html', context=context)


def CharacterDetailView(request, pk):
    num_characters = Character.objects.all().count()
    character = Character.objects.get(pk=pk)
    characters = Character.objects.order_by('-level')
    weapons = Weapons.objects.all()
    classes = Class.objects.all()
    skills = Skills.objects.all()
    players = Player.objects.all()
    level = Level.objects.all()
    context = {
        'num_characters': num_characters,
        'character_detail': character,
        'classes': classes,
        'characters': characters,
        'skills': skills,
        'levels': level,
        'weapons': weapons,
        'players': players
    }

    return render(request, 'character_detail.html', context=context)


def ClassDetailView(request, pk):
    classe = Class.objects.get(class_name=pk)
    characters = Character.objects.order_by('-level')
    skills = Skills.objects.all()
    players = Player.objects.all()
    classes = Class.objects.all()
    context = {
        'characters': characters,
        'class_detail': classe,
        'skills': skills,
        'classes': classes,
        'players': players
    }

    return render(request, 'class_detail.html', context=context)


class PlayerListView(ListView):
    model = Player
    template_name = "player_list.html"

    def get_context_data(self, **kwargs):
        players = Player.objects.all()
        classes = Class.objects.all()
        characters = Character.objects.all()
        context = {
            'classes': classes,
            'players' : players,
            'characters': characters
        }
        return context

