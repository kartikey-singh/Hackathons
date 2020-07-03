#!/usr/bin/env python3
from celery import Celery
from algorithm import approx

app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379/')

# run with:
# redis-server
# celery -A worker worker --loglevel=debug
# easier, if you don't care about exceptions
# integrate = app.task(approx)

@app.task
def integrate(*args, **kwargs):
    try:
        return approx(*args, **kwargs)
    except Exception:
        return
