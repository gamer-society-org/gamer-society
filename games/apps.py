from django.apps import AppConfig
import ipdb


class GamesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "games"
    
    def ready(self):
        
        from games_updater import updater
        updater.start()
