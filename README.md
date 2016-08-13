# Django Schedulermanager


Creates two commands `schedulejob` and `unschedulejob` that allows you to schedule (and unschedule) background
jobs.

If you have a brunch of jobs to start with your backend (e.g, if you have to update your social feed
every hour) you can just write the code of the job, mark it with the `schedulable` decorator and
the job will be schedulable with the `schedulejob` command.

Right now the library uses `django-rq` + `rq-scheduler`, but the dependency on `django-rq` is not needed
and will be removed soon.

## How to use

1. Write your job code in a module named 'jobs' (Remember to insert the app in the `INSTALLED_APPS` list)
2. Import the `schedulable` annotation: `from django_schedulermanager.decorators import schedulable`
3. Mark your function with `schedulable`. You can pass to the decorator the following parameters:
    - interval: Required.
    - scheduled_time: Required.
    - repeat: Not required, by default None which means 'repeat always'
    - id: The ID of the job.
          It will also be the name of the job that you have to pass
          when using `(un)schedulejob`.
          Not required, by default None which means 'use the name of the function'
    - queue: The queue to use. By default 'default'
