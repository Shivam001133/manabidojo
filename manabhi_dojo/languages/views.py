from django.shortcuts import render

from manabhi_dojo.languages.models import Character

# Create your views here.
def KatakanaView(request):
    symbols = Character.objects.filter(script__name='katakana')
    context = {
        'symbols': symbols
    }

    return render(request, 'symbol_table.html', context=context)