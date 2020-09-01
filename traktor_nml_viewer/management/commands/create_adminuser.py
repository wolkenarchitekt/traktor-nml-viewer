from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create dummy admin user'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            u = User(username='admin')
            u.set_password('adminadmin')
            u.is_superuser = True
            u.is_staff = True
            u.save()
