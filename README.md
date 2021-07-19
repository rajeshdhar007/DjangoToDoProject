# DjangoToDoProject

This project is setup to be monitored using Sentry (https://github.com/getsentry/onpremise) - Sentry.io
Sentry Version - 21.7.0
Follow the documentation here: https://develop.sentry.dev/self-hosted/


## Steps For Setup on Ubuntu 20.04
### Pre-requisites
```
$ python3 -V
Python 3.8.5

$ sudo apt install python3-django

$ django-admin --version
2.2.12

$ sudo apt install python3-pip python3-venv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-venv is already the newest version (3.8.2-0ubuntu2).
python3-pip is already the newest version (20.0.2-5ubuntu1.5).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

$ mkdir djangoProject
$ cd djangoProject

$ python3 -m venv my_env

$ source my_env/bin/activate

$ pip install django
Collecting django
  Using cached Django-3.2.4-py3-none-any.whl (7.9 MB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.3.4-py3-none-any.whl (22 kB)
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Installing collected packages: asgiref, pytz, sqlparse, django
Successfully installed asgiref-3.3.4 django-3.2.4 pytz-2021.1 sqlparse-0.4.1

$ django-admin --version
3.2.4

```


### Creating the todoProject and migrate database (SQLite default)
```
$ django-admin startproject todoProject .

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(my_env)

```

### Finally, let’s create an administrative user so that you can use the Djano admin interface. Let’s do this with the createsuperuser command

```
$ python manage.py createsuperuser
Username (leave blank to use 'rdhar'):      
Email address: rajeshdhar007@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(my_env)

```

### Launching the framework
```
 python manage.py runserver 0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 23, 2021 - 20:44:31
Django version 3.2.4, using settings 'todoProject.settings'
Starting development server at http://0:8000/
Quit the server with CONTROL-C.
[23/Jun/2021 20:44:33] "GET / HTTP/1.1" 200 10697

```
![image](https://user-images.githubusercontent.com/77116268/123165533-5ab9fb00-d442-11eb-9ec6-b57c60a04681.png)


Ref: https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04

### To configure the application to be monitored
1. Create a Project in Sentry
![image](https://user-images.githubusercontent.com/77116268/126216859-27be20bf-e9b1-4f4f-b17f-eaff931b283e.png)


2. There will be instructions on the page to setup the application:
```
pip install --upgrade sentry-sdk
```
3. Update ```/DjangoToDoProject/djangoProject/todoProject/settings.py``` as include:
```
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="http://2e5d022cd7c6484cb1c33f59d7d4b8c1@127.0.0.1:9000/2",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
```

4. Configure a view so that we can trigger the sentry debug. Update ```/DjangoToDoProject/djangoProject/todoProject/urls.py```

```
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    ...
    ...
    path('sentry-debug/', trigger_error),
]
```
5. Run the app as you would normally do.
```
$ python manage.py runserver 0:8000
```

6. From the browser, hit ```http://localhost:8000/sentry-debug```

![image](https://user-images.githubusercontent.com/77116268/126216904-48ed3405-9fdb-4eb8-aef5-f90b8bc0ca97.png)

7. In Sentry:

![image](https://user-images.githubusercontent.com/77116268/126217011-8f332218-e45c-4ebf-9e0e-b35157fae680.png)

