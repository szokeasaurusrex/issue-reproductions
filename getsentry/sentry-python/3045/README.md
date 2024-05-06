Attempted reproduction for getsentry/sentry-python#3045. The reproduction follows the setup in getsentry/sentry-python#3045, but fails to reproduce the issue described by the user. Instead, following the steps below leads to expected behavior.

## Steps

1. Clone this repository.
2. Enter this directory:

   ```zsh
   cd issue-reproductions/getsentry/sentry-python/3045
   ```

3. Set the `SENTRY_DSN` environment variable to your Sentry DSN (if not already set).
4. Run the `run.zsh` script:

   ```zsh
   ./run.zsh
   ```

5. Observe expected behavior.
