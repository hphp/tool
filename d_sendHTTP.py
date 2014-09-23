import httplib
import contextlib
import json
import urlparse
import sys

def basic():

    req = json.dumps({
        'jsonrpc': '2.0',
        'method': 'set_search_env',
        'params': 'hello',
        'id': 12345
    })
    headers = {
        'Content-Length': str(len(req)),
        'Accept': 'text/plain'
    }
    address = "http://cp01-rdqa-pool514.cp01.baidu.com:8989/cgi-bin/demo_echoPostRawData.py"
    address = urlparse.urlparse(address)
    with contextlib.closing(httplib.HTTPConnection(address.netloc)) as c:
        c.request('POST', address.path, req, headers)
        #resp = json.loads(c.getresponse().read())
        print '%s' % c.getresponse().read()
        #if 'error' not in resp:
        #    print '%s' % json.dumps(resp)
        #else:
        #print 'jsonRet: %s' % resp['result']['_ret']['jsonRet']

def d_get_return_msg():

    req = json.dumps({
        'jsonrpc': '2.0',
        'method': 'set_search_env',
        'params': 'hello',
        'id': 12345
    })
    headers = {
        'Content-Length': str(len(req)),
        'Accept': 'text/plain'
    }
    address = "http://cp01-rdqa-pool514.cp01.baidu.com:8989/cgi-bin/demo_echoPostRawData.py"
    address = urlparse.urlparse(address)
    with contextlib.closing(httplib.HTTPConnection(address.netloc)) as c:
        c.request('POST', address.path, req, headers)
        #resp = json.loads(c.getresponse().read())

        response = c.getresponse()
        # use the response instance.
        print response.getheaders()
        print response.status, type(response.status)
        print response.read()

def tool_send_post(address):

    req = json.dumps({
        'jsonrpc': '2.0',
        'method': 'set_search_env',
        'params': 'hello',
        'id': 12345
    })
    headers = {
        'Content-Length': str(len(req)),
        'Accept': 'text/plain'
    }
    address = urlparse.urlparse(address)
    with contextlib.closing(httplib.HTTPConnection(address.netloc)) as c:
        c.request('POST', address.path, req, headers)
        response = c.getresponse()
        print response.getheaders()
        print response.status, type(response.status)
        print response.read()


#basic()
#d_get_return_msg()
tool_send_post( address = "http://cp01-rdqa-pool514.cp01.baidu.com:8989/cgi-bin/ROPDeploy.py" )
