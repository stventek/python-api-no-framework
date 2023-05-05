from werkzeug.routing import Rule

def create_route(path, controller, method):
    return Rule(path, endpoint=lambda *args, **kwargs: controller(*args, **kwargs), methods=[method])
