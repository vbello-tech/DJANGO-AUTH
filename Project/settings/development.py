from .settings import *

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        },
    },
    "root": {"level": "INFO", "handlers": ["file"]},
}

SECURE_SSL_REDIRECT = False

#mail
"""EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
MAILJET_API_KEY = config('MAILJET_API_KEY')
MAILJET_SECRET_KEY = config('MAILJET_SECRET_KEY')

ANYMAIL = {
    "MAILJET_API_KEY": MAILJET_API_KEY,
    "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY,
}
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
DEFAULT_FROM_EMAIL = 'vbellotech@gmail.com'
SERVER_EMAIL = 'vbellotech@gmail.com'