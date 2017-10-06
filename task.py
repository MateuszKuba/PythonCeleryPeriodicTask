from celery import Celery
from os import environ

app = Celery('task')

REDIS_URL = environ.get('REDISTOGO_URL','redis://localhost')
app.conf.update(
        BROKER_URL=REDIS_URL,
        CELERY_TASK_SERIALIZER='json')

@app.on_after_configure.connect
def periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s("extreme values occured"),
                             name='every 10 seconds')
    
@app.task
def test(arg):
    print(arg)