Reproduction of getsentry/sentry-python#3040.

## Reproduction steps

1. Clone this repository.
2. Enter this directory:

   ```zsh
   cd issue-reproductions/getsentry/sentry-python/3040
   ```

3. Set the `SENTRY_DSN` environment variable to your Sentry DSN (if not already set).
4. Run the `run.zsh` script:

   ```zsh
   ./run.zsh
   ```

5. Navigate to http://localhost:5000 in your favorite browser.
6. Notice 500 error in the Quart server logs.
