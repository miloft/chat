# Chat Project

This project use 
* bootstrap for css/js [documentation](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
* PostgreSQL as DataBase

## Attention

Before you start the project, open the configuration file and change the settings for your database. 
Example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chatdb',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
And install bootstrap:
```
pip install django-bootstrap3
```

## Run
To start a chat just run:

```
python manage.py makemigrations
python manage.py makemigrations users 
python manage.py migrate
python manage.py createsuperuser #for create admin
python manage.py runserver
```

**For use this chat you have to do the steps:**

0. Open the browser at '127.0.0.0:8000'
1. Registration two or more users
2. Log in as the first user
3. Select user for dialog
4. Write a text message and send it
5. Log out
6. Log in as the second user
7. Open a dialog with the 1st user and write the answer

**For the administrator:**

1. Open the browser at '127.0.0.0:8000/admin'
2. Authorize
3. Select User for create or delete users
4. Select Chat for create or delete dialogs
5. Select Message for edit or delete any messages
