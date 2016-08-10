import django_rq


class SimpleManager(object):
    def __init__(self):
        super(SimpleManager, self).__init__()
        self._available_jobs = {}

    def add_job(self, name, options):
        self._available_jobs[name] = options

    def is_scheduled(self, job_id, options=None):
        if options is None:
            options = self.get_options(job_id)

        scheduler = django_rq.get_scheduler(options['queue'])
        return job_id in scheduler

    def schedule(self, job_id, options=None):
        """
        We accept options as parameter so the user can override job parameters
        like interval etc.
        """
        if options is None:
            options = self.get_options(job_id)

        if 'queue' not in options:
            raise ValueError('Options object is not valid. Required values: queue')

        scheduler = django_rq.get_scheduler(options['queue'])
        scheduler.schedule(
            scheduled_time=options['scheduled_time'],
            id=job_id,
            func=options['func'],
            interval=options['interval'],
            repeat=options['repeat'],
        )
        return True

    def get_options(self, job_id):
        return self._available_jobs[job_id]

    def __contains__(self, value):
        return value in self._available_jobs.keys()

    @property
    def jobs(self):
        return self._available_jobs


manager = SimpleManager()
