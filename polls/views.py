from polls.models import Class, Character, Player, Level, Skills
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    num_characters = Character.objects.all().count()

    characters = Character.objects.order_by('-level')[:3]

    classes = Class.objects.all()

    skills = Skills.objects.all()

    context = {
        'num_characters': num_characters,
        'characters': characters,
        'classes': classes,
        'skills': skills
    }

    return render(request, 'index.html', context=context)


def class_detail(request):

    skills = Skills.objects.all()

    context = {
        'skills': skills
    }

    return render(request, 'class/class_detail.html', context=context)


def navbar(request):

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'page/navbar.html', context=context)


class CharacterDetailView(DetailView):

    model = Character
    context_object_name = 'character_detail'
    template_name = 'character_detail.html'


class ClassDetailView(DetailView):
    model = Class
    context_object_name = 'class_detail'
    template_name = 'class_detail.html'
