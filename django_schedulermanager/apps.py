from __future__ import unicode_literals

import inspect

from django.apps import AppConfig
from django.conf import settings


class DjangoSchedulermanagerConfig(AppConfig):
    name = 'django_schedulermanager'

    def ready(self):
        apps = settings.INSTALLED_APPS

        for app in apps:
            try:
                jobs_module = __import__(app + '.jobs')
            except ImportError:
                continue

            members = inspect.getmembers(jobs_module)
            import pdb; pdb.set_trace()
            pass
