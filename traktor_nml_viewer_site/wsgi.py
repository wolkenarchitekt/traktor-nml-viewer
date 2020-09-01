import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "traktor_nml_viewer_site.settings")

application = get_wsgi_application()
