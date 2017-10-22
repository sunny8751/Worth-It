from flask import Flask
import os
from website_package import website
import website_package
from alexa_package import alexa

from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

app = Flask(__name__)
app.register_blueprint(website)
app.register_blueprint(alexa)
# app.run(threaded=True)
# debug=True, 


flask_site = WSGIResource(reactor, reactor.getThreadPool(), app)

root = Resource()
root.putChild('my_flask', flask_site)

site_example = ReverseProxyResource('www.example.com', 80, '/')
root.putChild('example', site_example)


reactor.listenTCP(8081, Site(root))
reactor.run()