from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

data = {}

@app.route('/', methods=['POST'])
def post_data():
    payload = request.get_json()
    data[payload["id"]] = payload["msg"]
    logging.info(f"Received and stored message: {payload['msg']}\n")
    return "Message logged successfully\n", 200

@app.route('/', methods=['GET'])
def get_data():
    logging.info("Returned all stored messages\n")
    return "\n".join(data.values()), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
