from django.apps import AppConfig


class FbMigrationsAppConfig(AppConfig):
    name = "fb_migrations"

    def ready(self):
        from fb_migrations import signals # pylint: disable=unused-variable
