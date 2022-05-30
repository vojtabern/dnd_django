from polls.models import Class, Character, Player, Level
from django.shortcuts import render


def index(request):
    num_characters = Character.objects.all().count()

    characters = Character.objects.order_by('-level')[:3]

    context = {
        'num_characters': num_characters,
        'characters': characters
    }

    return render(request, 'index.html', context=context)
