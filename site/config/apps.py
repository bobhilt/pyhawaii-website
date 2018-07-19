from django.apps import AppConfig
import session_csrf


class Config(AppConfig):

    name = 'config.apps'

    def ready(self):
        session_csrf.monkeypatch()
