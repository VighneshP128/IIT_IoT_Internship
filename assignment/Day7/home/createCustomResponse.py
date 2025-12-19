from flask import jsonify

def createCustomResponse(msg, error=False):
    if error:
        d = {
            'status code': '400',
            'string': 'ERROR',
            'msg': msg
        }
    else:
        d = {
            'status code': '200',
            'string': 'OK',
            'msg': msg
        }
    return jsonify(d)