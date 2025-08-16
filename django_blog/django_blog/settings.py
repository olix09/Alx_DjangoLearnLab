INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',      # your blog app
    'taggit',    # add this line for the checker
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Or keep sqlite3 if you prefer
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

