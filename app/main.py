from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Basic health-check function at root of route to validate API is live.

    Returns:
        str: A string containing a hello message.
    """
    return "Hello from K8s PySpark Matrix!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
