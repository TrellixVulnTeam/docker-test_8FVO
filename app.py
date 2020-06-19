from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

class Vars(object):
    total = 0

    def __init__(self):
        Vars.total+=1

    @staticmethod
    def status():
        return str(Vars.total)


@app.route('/')
def hello_world():
    me = Vars()
    if request.method == "GET":
        vari = me.status()
        curr_time = datetime.now()
        response = f'Calls: {vari}, {curr_time}'
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
