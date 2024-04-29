import sentry_sdk
import logging

from sentry_sdk.integrations.logging import LoggingIntegration

from fastapi import FastAPI

sentry_sdk.init(
    enable_tracing=True,
    integrations=[LoggingIntegration(level=logging.DEBUG)],
    debug=True,
)

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/")
def test_logging():
    with sentry_sdk.push_scope() as scope:
        scope.set_tag("my-tag", "my value")
        scope.set_level("debug")
        scope.set_user({"id": "evvee"})
        scope.fingerprint = ["event2"]
        scope.add_breadcrumb()

        logger.debug("DEBUG")
        logger.warning("WARNING 1")
        logger.warning("WARNING 2")
        logger.warning("WARNING 3")
        logger.warning("WARNING 4")
        logger.error("🔥")

    return "OK"
