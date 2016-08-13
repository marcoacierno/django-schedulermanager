# Django Schedulermanager


Creates two commands `schedulejob` and `unschedulejob` that allows you to schedule (and unschedule) background
jobs.

If you have a brunch of jobs to start with your backend (e.g, if you have to update your social feed
every hour) you can just write the code of the job, mark it with the `schedulable` decorator and
the job will be schedulable with the `schedulejob` command.

Right now the library uses `django-rq` + `rq-scheduler`, but the dependency on `django-rq` is not needed
and will be removed soon.

## How to use

1. Add `django_schedulermanager.apps.DjangoSchedulerManagerConfig` to your INSTALLED_APPS
2. Write your job code in a module named 'jobs' (Remember to insert the app in the `INSTALLED_APPS` list)
3. Import the `schedulable` annotation: `from django_schedulermanager.decorators import schedulable`
4. Mark your function with `schedulable`. You can pass to the decorator the following parameters:
    - interval: The interval of the function. Required.
    - scheduled_time: When the function should start the first time. Required. It's a function.
    - repeat: Not required, by default None which means 'repeat always'
    - id: The ID of the job.
          It will also be the name of the job that you have to pass
          when using `(un)schedulejob`.
          Not required, by default None which means 'use the name of the function'
    - queue: The queue to use. By default 'default'

See also `test-project` directory to see an example, if you want to test the project, clone the repository
and run the command `make testproject`, it will copy the `django_schedulermanager` folder (the library code)
in the `test-project` folder

## TODO

- [ ] Remove dependency on `django-rq`
- [ ] If present, read 'queue' from `@job` annotation
- [ ] Add `unschedulejob all` to unschedule all the jobs
- [ ] Add a command to remove all the scheduled jobs that don't have a function in the jobs.py files
