import os
import logging
import time
from secrets import token_hex

from celery import Celery
import sentry_sdk


sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    enable_tracing=False,  # this changes the behaviour
    debug=True,
    send_default_pii=True,
)

app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger(__name__)

logger.error(f"SETUP {token_hex(2)}")


@app.task
def my_task():
    logger.error(f"MY_TASK2 {token_hex(2)}")
    time.sleep(1)
