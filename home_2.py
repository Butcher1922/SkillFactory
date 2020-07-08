
import sentry_sdk
import os
from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DNS"),
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route("/success")
def success():
    return

@app.route("/fail")
def fail():
    raise RuntimeError('There is an error!')
    return

app.run(host='localhost',port=8080)
