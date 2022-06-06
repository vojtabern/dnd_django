from polls.models import Class, Character, Player, Level, Skills
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    num_characters = Character.objects.all().count()
    characters = Character.objects.order_by('-level')[:3]
    classes = Class.objects.all()
    skills = Skills.objects.all()
    players = Player.objects.all()
    context = {
        'num_characters': num_characters,
        'characters': characters,
        'classes': classes,
        'skills': skills,
        'players': players
    }

    return render(request, 'index.html', context=context)


def CharacterDetailView(request, pk):
    num_characters = Character.objects.all().count()
    character = Character.objects.get(pk=pk)
    characters = Character.objects.order_by('-level')[:3]

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
        'players': players
    }

    return render(request, 'character_detail.html', context=context)


def ClassDetailView(request, pk):
    model = Class
    classe = Class.objects.get(class_name=pk)
    characters = Character.objects.order_by('-level')[:3]
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

