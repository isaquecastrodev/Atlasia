# modules/noop_module.py
def run(params):
    return {'status': 'ok', 'message': 'no operation', 'received': params}
