from datetime import datetime

from django_schedulermanager.decorators import schedulable


@schedulable(interval=10, scheduled_time=datetime.utcnow)
def test_function():
    print('hello')
