from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = "checkout"

    def ready(self):
        # Importing signals to connect them, used by Django's signal framework
        import checkout.signals  # noqa: F401
