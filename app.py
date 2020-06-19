from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    curr_time = datetime.now()
    return str(curr_time)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
