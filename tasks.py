import celery
import os
from datetime import timedelta

app = celery.Celery("example")

app.conf.update(BROKER_URL = os.environ['REDIS_URL'],
                CELERY_TASK_SERIALIZER='json',
                CELERY_RESULT_BACKEND = os.environ['REDIS_URL'],
                CELERYBEAT_SCHEDULE ={
                        'check extremes': {
                                'task': 'tasks.check_for_extreme',
                                'schedule': timedelta(seconds=60)
                                }
                        })

@app.task
def check_for_extreme():
    print("extreme extreme")
    
