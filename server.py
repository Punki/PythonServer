import datetime
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))

        payload = {
            "success": "0",
            "im": "empty!",
        }

        if message.has_key('url'):
            # add a property to the object, just to mess with data
            payload = {
                "success": "1",
                "data": {
                    "task_uuid": "efb625b9942e000004751393ce42030d"
                }}

        elif message.has_key("test"):
            payload = {
                "success": "1",
                "im a": "test!",
            }

        elif message.has_key("uuid"):
            with open(r'/home/pinki/PycharmProjects/PythonServer/report.json', 'r') as json_file:
                payload = json.load(json_file)

        elif message.has_key("OLDtestData"):
            timeNow = datetime.datetime.utcnow()
            timeNow = timeNow.strftime("%Y-%m-%d %H:%M:%S")
            with open('data.json') as json_file:
                payload = json.load(json_file)


        else:
            payload = {
                "success": 1,
                "data": {
                    "task": ["efb625b9942e000004751393ce42030d"],
                    "after": "2016 - 03 - 11 20:00:00",
                    "more_results_available": 0,
                    "before": "2016 - 03 - 11 20:45:22"
                }}

        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(payload))


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print 'Starting httpd on port %d...' % port
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
