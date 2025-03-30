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
            if char:
                row['characters'].append({
                    'id': char.id,
                    'symbol': char.symbol,
                    'romaji': char.romaji,
                    'audio': char.audio.url if char.audio else None,
                })
            else:
                row['characters'].append({
                    'id': None,
                    'symbol': '',
                    'romaji': '',
                    'audio': None,
                })
        katakana_rows.append(row)

    return render(request, 'symbol_table.html', {
        'consonants': consonants,
        'katakana_rows': katakana_rows,
    })
