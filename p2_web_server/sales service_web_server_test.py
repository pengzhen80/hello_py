from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import codecs

# def hello_world(request):
#     return Response('Hello World!')

# if __name__ == '__main__':
#     with Configurator() as config:
#         config.add_route('hello', '/')
#         config.add_view(hello_world, route_name='hello')
#         app = config.make_wsgi_app()
#     server = make_server('192.168.66.19', 6543, app)
#     server.serve_forever()

def hello_world(request):
    f=codecs.open("ui_test.html", 'r','utf-8')
        # print(f.read())
    return Response(f.read())

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('192.168.66.19', 6543, app)
    server.serve_forever()