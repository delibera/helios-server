import os, sys

sys.path.append('/var/www/html/helios-server')

sys.path.append('/var/www/html/helios-server/my-venv/lib/python3.8/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
