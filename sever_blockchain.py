from flask import Flask, jsonify

import blockchain
import wallet

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app.config["port"] = port

    app.run(host="127.0.0.1", port=port, threaded=True, debug=True)
