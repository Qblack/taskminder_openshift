#!/usr/bin/env python
import os
import imp
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(os.path.join('wsgi', 'openshift'))

#
# Below for testing only
#
if __name__ == '__main__':
    if 'OPENSHIFT_REPO_DIR' in os.environ:
        ip   = 'localhost'
        port = 8051
        app = imp.load_source('application', 'wsgi/application')

        from wsgiref.simple_server import make_server
        httpd = make_server(ip, port, app.application)
        httpd.serve_forever()
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()