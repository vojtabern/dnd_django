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




class CharacterDetailView(DetailView):
    model = Character
    context_object_name = 'character_detail'
    template_name = 'character_detail.html'


class ClassDetailView(DetailView):
    model = Class
    context_object_name = 'class_detail'
    template_name = 'class_detail.html'
