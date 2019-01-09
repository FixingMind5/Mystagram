from datetime import date

family = [
    {
        'email': 'alejandro@platzi.com',
        'first_name': 'Alejandro',
        'last_name': 'Aguilar',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'teretegime@platzi.com',
        'first_name': 'Teresa',
        'last_name': 'Téllez',
        'password': '987654321'
    },
    {
        'email': 'yarii092000@platzi.com',
        'first_name': 'Yari',
        'last_name': 'Ramirez',
        'password': 'qwerty',
    }
]

from posts.models import User

for f in family:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)
