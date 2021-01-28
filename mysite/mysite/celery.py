import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "parsing": {
        "task": "polls.tasks.parse_quote",
        "schedule": crontab(hour='1-23/2'),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')   # noqa: T001
