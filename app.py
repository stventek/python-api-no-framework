import config
from wsgiref.simple_server import make_server
from routes.recipe_route import setup_routes as recipe_setup_routes
from routes.ingridient_route import setup_routes as ingridient_setup_routes
from werkzeug.routing import Map
from werkzeug.exceptions import NotFound
from werkzeug.wrappers import Request, Response

url_map = Map(ingridient_setup_routes() + recipe_setup_routes())

def wsgi_app(environ, start_response):
    request = Request(environ)
    urls = url_map.bind_to_environ(environ)
    
    try:
        endpoint, args = urls.match()
        response = endpoint(request, **args)
    except NotFound:
        response = Response("Not found", status=404, content_type="text/plain")
    
    return response(environ, start_response)

def create_app_WSGIServer():
    app = make_server('', 8080, wsgi_app)
    return app

def get_app():
    return wsgi_app