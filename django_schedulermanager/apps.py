from __future__ import unicode_literals

import importlib
import inspect

from django.apps import AppConfig
from django.conf import settings

from .manager import manager


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
                manager.add_job(
                    instance.django_scheduler.id,
                    instance.django_scheduler
                )

    def schedulable_only(self, member):
        return (
            hasattr(member, 'django_scheduler') and
            member.django_scheduler.is_schedulable
        )
