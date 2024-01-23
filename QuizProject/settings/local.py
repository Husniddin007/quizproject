from .base import *

# khohcd
# klrklg
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "../db.sqlite3",

    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": config("SQL_ENGINE"),
#         "NAME": config("SQL_DATABASE"),
#         "USER": config("SQL_USER"),
#         "PASSWORD": config("SQL_PASSWORD"),
#         "HOST": config("SQL_HOST"),
#         "PORT": config("SQL_PORT"),
#     }
# }