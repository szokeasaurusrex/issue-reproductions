from quart import Quart

import sentry_sdk
from sentry_sdk.integrations.quart import QuartIntegration

sentry_sdk.init(
    enable_tracing=True,
    integrations=[
        QuartIntegration(),
    ],
)

app = Quart(__name__)


@app.route("/")
async def hello():
    1 / 0  # raises an error
    return {"hello": "world"}


if __name__ == "__main__":
    app.run()
