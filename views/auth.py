from flask import request, jsonify


def auth(controller):
    def inner():
        token = request.headers.get('Authorization', None)
        if token and token[7:] == 'SHEBAK@2022':
            return controller()
        else:
            return jsonify({
                "message": "You are not authorized to use this API!"
            }), 403
    return inner
