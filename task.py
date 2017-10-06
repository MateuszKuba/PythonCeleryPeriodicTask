from celery import Celery

app = Celery()

@app.on_after_configure.connect
def periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s("extreme values occured"),
                             name='every 10 seconds')
    
@app.task
def test(arg):
    print(arg)