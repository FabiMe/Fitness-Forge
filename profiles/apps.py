from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = "profiles"

    def ready(self):
        # Importing profiles.signals for future use
        # import profiles.signals
        pass
