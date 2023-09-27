from .settings import *

#MAIL
MAILJET_API_KEY = config('MAILJET_API_KEY')
MAILJET_SECRET_KEY = config('MAILJET_SECRET_KEY')

ANYMAIL = {
    "MAILJET_API_KEY": MAILJET_API_KEY,
    "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY,
}
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
DEFAULT_FROM_EMAIL = 'vbellotech@gmail.com'
SERVER_EMAIL = 'vbellotech@gmail.com'
