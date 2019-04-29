# This is the file that implements a flask server

from __future__ import print_function

import flask


# The flask app
app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return flask.Response(response='\n', status=200,
                          mimetype='application/json')


@app.route('/invocation', methods=['POST'])
def invocations():
    return flask.Response(response='\n', status=200,
                          mimetype='application/json')

if __name__ == '__main__':
   app.run()