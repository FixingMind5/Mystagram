"""Post's views"""
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Beautiful Sky',
        'user': 'Manuel Aguilar',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/400/400/?image=992',
    },
    {
        'name': 'Here I\'m',
        'user': 'Monica Sevilla',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/400/400/?image=996',
    },
    {
        'name': 'Al verte así...',
        'user': 'Manuel Aguilar',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/400/400/?image=1011',
    }
]

def lists_posts(request):
    """Posts views"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src='{picture}'/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
