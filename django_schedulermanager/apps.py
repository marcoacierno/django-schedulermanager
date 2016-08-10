from __future__ import unicode_literals

import importlib
import inspect

from django.apps import AppConfig
from django.conf import settings


AVAILABLE_JOBS = []


class DjangoSchedulerManagerConfig(AppConfig):
    name = 'django_schedulermanager'

    def ready(self):
        apps = settings.INSTALLED_APPS

        for app in apps:
            try:
                jobs_module = importlib.import_module(app + '.jobs')
            except ImportError:
                continue

            members = inspect.getmembers(jobs_module, self.schedulable_only)

            for name, instance in members:
                print(name, 'instance', instance.django_scheduler['interval'])
                AVAILABLE_JOBS.append(name, instance.django_scheduler)

    def schedulable_only(self, x):
        return (
            hasattr(x, 'django_scheduler') and
            x.django_scheduler['is_schedulable']
        )


AVAILABLE_JOBS = []
