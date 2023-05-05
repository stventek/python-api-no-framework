from app import create_app_WSGIServer

server = create_app_WSGIServer()

if __name__ == '__main__':
    server.serve_forever()