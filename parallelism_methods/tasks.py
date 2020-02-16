from celery import Celery
from funcs_for_test import make_3_dim_list
app = Celery('tasks', broker='pyamqp://guest@ubustation//')

@app.task
def mk(add):
    make_3_dim_list(300, add)