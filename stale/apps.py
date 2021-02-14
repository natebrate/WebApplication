from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'Main'

    def ready(self):
    	import Main.signals