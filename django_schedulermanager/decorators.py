def schedulable(interval, scheduled_time=None, repeat=None, id=None, queue='default'):
    def schedulable_decorator(inner_function):
        inner_function.django_scheduler = {}
        inner_function.django_scheduler['is_schedulable'] = True
        inner_function.django_scheduler['interval'] = interval
        inner_function.django_scheduler['scheduled_time'] = scheduled_time
        inner_function.django_scheduler['repeat'] = repeat
        inner_function.django_scheduler['queue'] = queue
        inner_function.django_scheduler['func'] = inner_function
        inner_function.django_scheduler['id'] = id if id else inner_function.__name__
        return inner_function

    return schedulable_decorator
