Reproduction of getsentry/sentry-python#687. Setup based on [reproduction](https://github.com/getsentry/sentry-python/issues/687#issuecomment-1811523620) provided by @RobbieClarken.

## Reprouction steps

1. Create and enter a virtual environment.
2. Install requirements from `requirements.txt`.
3. Start Redis, e.g. by running in Docker.
4. Start Celery worker with the following command:
   ```sh
   celery -A tasks.app worker --loglevel=INFO --autoscale 4,0
   ```
5. In a separate terminal window, run interactive Python interpreter, and enter the following commands (output not shown):
   ```python
   >>> from tasks import my_task
   >>> my_task.apply_async()
   ```
6. Observe (in the Celery worker terminal) that the task error occurs, but the envelope is not immediately.
7. Run `my_task.apply_async()` in the Python interpreter again. Notice that both error events are sent immediately in the Celery worker window.

If `my_task.apply_async()` is run only once, it still appears that the error event eventually gets sent to Sentry. The event is sent after a delay, or after pressing Ctrl-C.
