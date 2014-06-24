#!/usr/bin/env python
# vim: ts=4:sw=4:et
#
# malware zoo
#

from twisted.web import server, xmlrpc, resource
from twisted.internet import reactor

class MalwareZoo(resource.Resource):
    pass

class FileUploadHandler(xmlrpc.XMLRPC):

    def xmlrpc_upload(self, file_name, file_content):
        print "file_name = {0}".format(file_name)
        print "file_content size = {0}".format(len(file_content))
        return True
    
    #def render_GET(self, request):
        #request.setHeader("content-type", "text/plain")
        #return "sup bro"

    #def render_POST(self, request):
        #if 'file' not in request.args:
            #request.setResponseCode(500)
            #return 'missing file argument'

        #return 'sent {0} bytes'.format(len(request.args['file'][0]))


if __name__ == '__main__':
    root = MalwareZoo()
    root.putChild("upload", FileUploadHandler())
    
    reactor.listenTCP(8081, server.Site(root))
    reactor.run()