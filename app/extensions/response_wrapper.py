def wrap_response(data=None, message="", http_code=200, custom_code=''):
    """
    Return general HTTP response
    """
    res = {
        'code': http_code,
        'success': http_code,
        'message': message,
        'data': data
    }

    return res, http_code
