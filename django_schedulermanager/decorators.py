from django_schedulermanager.manager import JobDescriptor


def schedulable(interval, scheduled_time, repeat=None, id=None, queue='default'):
    def schedulable_decorator(inner_function):
        inner_function.django_scheduler = JobDescriptor(
            is_schedulable=True,
            interval=interval,
            scheduled_time=scheduled_time,
            repeat=repeat,
            queue=queue,
            func=inner_function,
            id=id if id else inner_function.__name__
        )
        return inner_function

    return schedulable_decorator
