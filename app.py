from flask import Flask
from uuid import uuid4
import os

app = Flask(__name__)

uuid = uuid4()
uuid = uuid.hex


@app.route('/')
def hello_world():
    return uuid


port = 8080 if str(os.getenv('PORT')) == '' else os.getenv('PORT')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
