from flask import jsonify

def buildResponse(status = 'Success',message='',code=200,data=None):
    res = {'status':status,'message':message}
    if data is not None:
        res['data'] = data
    return jsonify(res) ,code
