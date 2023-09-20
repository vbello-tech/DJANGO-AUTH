from .settings import *

#MAIL
"""MAILJET_API_KEY = config('MAILJET_API_KEY')
MAILJET_SECRET_KEY = config('MAILJET_SECRET_KEY')

ANYMAIL = {
    "MAILJET_API_KEY": MAILJET_API_KEY,
    "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY,
}
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
DEFAULT_FROM_EMAIL = 'vbellotech@gmail.com'
SERVER_EMAIL = 'vbellotech@gmail.com'
"""

#gmail smtp
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ' odunayobello1@gmail.com'
EMAIL_HOST_PASSWORD = 'estppelvoiexyfrq'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False