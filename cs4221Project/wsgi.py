"""
WSGI config for cs4221Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/Han Cheng/Bitnami Django Stack projects/cs4221Project')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/Han Cheng/Bitnami Django Stack projects/cs4221Project/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs4221Project.settings")

application = get_wsgi_application()
