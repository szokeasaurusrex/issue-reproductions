import time
import sentry_sdk

sentry_sdk.init(traces_sample_rate=1.0, profiles_sample_rate=1.0, debug=True)

if __name__ == "__main__":
    print("Hello world")
    sentry_sdk.metrics.increment("counter_metric", 10)
    sentry_sdk.metrics.incr("drank-drinks", 1, tags={"kind": "coffee"})

    with sentry_sdk.metrics.timing(key="timing_metric"):
        print("Sleeping for 3 seconds")
        print("Pressing Ctrl+C will send the metrics immediately")
        time.sleep(3)
        print("Done sleeping")

    sentry_sdk.metrics.incr("sleep-finished", 1)

    # Metrics are only sent when the line below is uncommented
    # sentry_sdk.flush()
