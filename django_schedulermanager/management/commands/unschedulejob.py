from django.core.management.base import BaseCommand

from django_schedulermanager.manager import manager


class Command(BaseCommand):
    help = 'Unschedules a job'

    def add_arguments(self, parser):
        parser.add_argument('jobs_name', nargs='+')

    def handle(self, *args, **options):
        jobs_to_schedule = options['jobs_name']

        for job in jobs_to_schedule:
            if job not in manager:
                self.stdout.write(
                    'Unable to find job {}. Available jobs: {}'.format(job, ','.join(manager.jobs.keys()))
                )
                continue

            if not manager.is_scheduled(job):
                self.stdout.write('Job {} never started'.format(job))
                continue

            job_options = manager.get_options(job)
            # TODO: Implement settings override
            manager.unschedule(job, job_options)
            self.stdout.write(self.style.SUCCESS('Successfully unscheduled job {}!'.format(job)))
