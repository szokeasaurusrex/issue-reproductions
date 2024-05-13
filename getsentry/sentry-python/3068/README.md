Reproduction for getsentry/sentry-python#3068.

## Steps

1. Clone this repository.
2. Enter this directory:

   ```zsh
   cd issue-reproductions/getsentry/sentry-python/3068
   ```

3. Set the `SENTRY_DSN` environment variable to your Sentry DSN (if not already set).
4. Run the `run_beat.zsh` script to setup the Python virtual environment and start the Celery worker:

   ```zsh
   ./run_beat.zsh
   ```

5. Wait until the `run_beat.zsh` script displays the "Setup complete..." message. Then, from a separate terminal window (in which `SENTRY_DSN` is set) run `run_worker.zsh`:

   ```zsh
   # First, ensure $SENTRY_DSN is set to the same DSN as in the run_beat.zsh window. Then, run the following command.
   ./run_worker.zsh
   ```

6. Observe, in Sentry, that all the transactions created by this run are linked to a trace ID which does not show in Sentry, and that all transactions emitted (they are logged in the worker) have an empty `dynamic_sampling_context`.
