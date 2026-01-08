import base64


def e3_basic_token(username, password):
    _upseq = ':'.join((username, password))
    return base64.b64encode(_upseq.encode('utf-8')).decode()
