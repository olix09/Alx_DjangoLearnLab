INSTALLED_APPS = [
    # default apps...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
