Attempted reproduction of getsentry/sentry-python#3019.

## Reproduction steps

1. Clone this repository.
2. Enter this directory:

   ```zsh
   cd issue-reproductions/getsentry/sentry-python/3019
   ```

3. Set the `SENTRY_DSN` environment variable to your Sentry DSN (if not already set).
4. Run the `run.zsh` script:

   ```zsh
   ./run.zsh
   ```

5. Observe results in Sentry
