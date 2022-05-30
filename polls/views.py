from polls.models import Class, Character, Player, Level
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def index(request):
    num_characters = Character.objects.all().count()

    characters = Character.objects.order_by('-level')[:3]

    context = {
        'num_characters': num_characters,
        'characters': characters
    }

    return render(request, 'index.html', context=context)


class ClassDetailView(DetailView):
    # Nastavení požadovaného modelu
    model = Class
    # Pojmenování objektu, v němž budou šabloně předána data z modelu (tj. databázové tabulky)
    context_object_name = 'class_detail'
    # Umístění a název šablony
    template_name = 'class/class_detail.html'
