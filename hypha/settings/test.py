import logging

from .base import *  # noqa

logging.disable(logging.CRITICAL)


# Should only include explicit testing settings

SECRET_KEY = 'NOT A SECRET'

PROJECTS_ENABLED = True
PROJECTS_AUTO_CREATE = True

# Need this to ensure white noise doesn't kill the speed of testing
# http://whitenoise.evans.io/en/latest/django.html#whitenoise-makes-my-tests-run-slow
WHITENOISE_AUTOREFRESH = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
