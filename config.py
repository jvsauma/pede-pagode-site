# Este arquivo centraliza as configurações da aplicação.

from datetime import timedelta


class Config:
    SECRET_KEY = "grupo-pede-pagode-2026"
    DATABASE = "database/database.db"
    DEBUG = True

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = not DEBUG