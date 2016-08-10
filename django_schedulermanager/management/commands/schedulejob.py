from django.core.management.base import BaseCommand

from django_schedulermanager.manager import manager


class Command(BaseCommand):
    help = 'Schedules a job'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('jobs_name', nargs='+')

    def handle(self, *args, **options):
        jobs_to_schedule = options['jobs_name']

        for job in jobs_to_schedule:
            if job not in manager:
                self.stdout.write(
                    'Unable to find job {}. Avalable jobs: {}'.format(job, ','.join([job for job, _ in manager.jobs.items()]))
                )
                continue

            if manager.is_scheduled(job):
                self.stdout.write('Job {} already started'.format(job))
                continue

            job_options = manager.get_options(job)
            # TODO: Implement settings override
            manager.schedule(job, job_options)
            self.stdout.write(self.style.SUCCESS('Successfully scheduled job {}!'.format(job)))
