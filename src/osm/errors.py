from flask import abort, jsonify


class OverpassServiceError(Exception):
    pass


# https://github.com/PythonFreeCourse/lms/blob/master/lms/models/errors.py
def fail(status_code: int, error_msg: str):
    data = {
        'status': 'failed',
        'msg': error_msg,
    }
    response = jsonify(data)
    response.status_code = status_code
    return abort(response)
