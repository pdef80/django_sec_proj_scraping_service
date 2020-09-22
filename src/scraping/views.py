from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city.lower()
        if language:
            _filter['language__slug'] = language.lower()

        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/list.html', {'object_list': qs, 'form': form})