import django_rq

from django.core.management.base import BaseCommand

from django_schedulermanager.manager import manager


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--queue', dest='queue', default='default')

    def handle(self, queue, *args, **options):
        self.print_declared_jobs()
        self.print_jobs_on_queue(queue)
        self.print_scheduled_jobs(queue)

    def print_declared_jobs(self):
        self.stdout.write('Jobs declared in your code: {}'.format(', '.join(manager.jobs)))

    def print_jobs_on_queue(self, queue):
        jobs_on_queue = [str(job) for job in manager.jobs.values() if job.queue == queue]

        self.stdout.write(
            'Jobs declared in your code that runs on queue "{}": {}'.format(queue, ', '.join(jobs_on_queue))
        )

    def print_scheduled_jobs(self, queue):
        scheduler = django_rq.get_scheduler(queue)
        scheduled_jobs = scheduler.get_jobs(with_times=True)

        self.stdout.write('Jobs scheduled: {}'.format(', '.join(['{} at {}'.format(id, time) for id, time in scheduled_jobs])))
