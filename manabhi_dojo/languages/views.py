from django.shortcuts import render
from manabhi_dojo.languages.models import Character


def KatakanaView(request):
    vowels = ['a', 'i', 'u', 'e', 'o']
    consonants = ['-', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w']
    characters = Character.objects.filter(script__name='katakana')
    katakana_rows = []

    for v in vowels:
        row = {'vowel': v, 'characters': []}
        for c in consonants:
            romaji = v if c == '-' else c + v
            char = characters.filter(romaji=romaji).first()
            row['characters'].append({'symbol': char.symbol if char else '', 'romaji': char.romaji if char else ''})
        katakana_rows.append(row)

    return render(request, 'symbol_table.html', {
        'consonants': consonants,
        'katakana_rows': katakana_rows,
    })
