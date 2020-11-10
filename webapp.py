#!/usr/bin/env python

import textwrap

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello Automation Logic</h1>
                <p>This is running on vagrant created machines.
                An nginx loadbalancer is servicing 2 web servers, running a python application 
                </p>
                <h3>Justification for approach</h3>
                <p>> Decided to create a 4th host to run ansible instead of using vagrants built-in provisioner to not exclude windows users</p>
                <h3>Improvements</h3>
                <p>> Use boxes that already come with the desired services/packages preinstalled to save time on provisioning</p>
                <h3>Compromises</h3>
                <p>> Functionality of app</p>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
