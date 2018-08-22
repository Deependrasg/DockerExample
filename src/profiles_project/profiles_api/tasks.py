from celery import shared_task
from celery.schedules import crontab
from celery import Celery

celery_app = Celery('profiles_project')

@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=11, minute=38),
        hello.s(),
    )

@shared_task
def hello():
    print('+++++++++++++++++++++_____________________Hello there!______________________++++++++++++++++++++++++') 