from django.core.management.base import BaseCommand
from finalapp.models import CustomUser

class Command(BaseCommand):
    help = 'Create a superuser with email admin@example.com and password admin123'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email='admin@example.com').exists():
            CustomUser.objects.create_superuser(
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser created: admin@example.com / admin123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Superuser already exists')
            )