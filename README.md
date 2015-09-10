# archlinux.org.pl
Strona główna polskiej społecznośc Arch Linux.


W pliku local_settings.py powinieneś zdefiniować bazy danych, z których chcesz korzystać np:


```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'mysql': {
            'HOST': 'domain.com',
            'PORT': '1010',
            'NAME': 'database_name',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'user_db',
            'PASSWORD': 'password_db'
            }
        }
```

Możesz zdefiniować nowe zmienne:

```
STATIC_ROOT = '/path/to/static/root/'
```

oraz

```
STATIC = '/static/'
```

# IMPORTANT!!!

Musisz koniecznie napisać *SECRET_KEY*!

Najszybciej jest skorzystać z shell'a django:

'''
./manage shell

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
get_random_string(50, chars)
'''
