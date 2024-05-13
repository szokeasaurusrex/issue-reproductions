from time import sleep
from celery import Celery, signals

import sentry_sdk


def print_transaction(event, _):
    print(f"Sending transaction: {event}")
    return event


app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
)


@signals.beat_init.connect
@signals.celeryd_init.connect
def init_sentry(**_):
    print("########## INIT SENTRY ##########")
    sentry_sdk.init(
        debug=True, enable_tracing=True, before_send_transaction=print_transaction
    )


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **_):
    sender.add_periodic_task(15.0, test.s("hello"), name="add every 10")


@app.task
def test(arg):
    print(arg)
    for i in range(5):
        add.apply_async((i, i))
        sleep(1)
    return arg


@app.task
def add(x, y):
    return x + y
