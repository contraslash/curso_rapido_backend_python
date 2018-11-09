from io import StringIO
from wsgiref.simple_server import make_server

def hello_world(environ, start_response):

    stdout = StringIO()
    print("Hello world!", file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]

if __name__ == '__main__':
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
