"""Post's views"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Beautiful Sky',
        'user': {
            'name': 'Manuel Aguilar',
            'picture': 'https://picsum.photos/50/50/?image=1004',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/400/400/?image=992',
    },
    {
        'title': 'Here I\'m',
        'user': {
            'name': 'Monica Sevilla',
            'picture': 'https://picsum.photos/50/50/?image=996',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/400/400/?image=1020',
    },
    {
        'title': 'Al verte así',
        'user': {
            'name': 'Manuel Aguilar',
            'picture': 'https://picsum.photos/50/50/?image=1004',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/400/400/?image=1011',
    }
]

@login_required
def lists_posts(request):
    """Posts views"""
    return render(request, 'posts/feed.html', {'posts': posts})
