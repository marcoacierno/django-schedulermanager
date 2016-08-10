from django_schedulermanager.decorators import schedulable


@schedulable(interval=1)
def test_function():
    print('hello')
