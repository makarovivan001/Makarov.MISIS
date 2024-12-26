from django.contrib.auth.models import User
from django.core.management.commands.migrate import Command as MigrateCommand


class Command(MigrateCommand):
    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'
        email = 'admin@example.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
        print("Superuser created.")
