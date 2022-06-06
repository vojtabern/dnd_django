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
    model = Character
    num_characters = Character.objects.all().count()
    character = Character.objects.order_by('-level')[pk]
    characters = Character.objects.order_by('-level')[:3]

    classes = Class.objects.all()
    skills = Skills.objects.all()
    players = Player.objects.all()
    context = {
        'num_characters': num_characters,
        'character_detail': character,
        'classes': classes,
        'characters': characters,
        'skills': skills,
        'players': players
    }
    context_object_name = 'character_detail'
    template_name = 'character_detail.html'

    return render(request, 'character_detail.html', context=context)


def ClassDetailView(request, pk):
    model = Character
    classes = Class.objects.order_by('-level')[pk]
    skills = Skills.objects.all()
    players = Player.objects.all()
    context = {
        'num_characters': num_characters,
        'character_detail': characters,
        'class_detail': classes,
        'skills': skills,
        'players': players
    }
    context_object_name = 'character_detail'
    template_name = 'character_detail.html'

    return render(request, 'character_detail.html', context=context)

class ClassDetailView(DetailView):
    model = Class
    context_object_name = 'class_detail'
    template_name = 'class_detail.html'
