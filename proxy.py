import httplib
from HTMLParser import HTMLParser
from urlparse import urlparse
# import urllib

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        print "Encountered the end of a %s tag" % tag

from flask import Flask, request
app = Flask(__name__)


@app.route("/pass")
def proxy_pass():
    try:
        url = urlparse(request.args.get("url"))
    except:
        return "Please include a URL parameter" 
    conn = httplib.HTTPConnection(url.netloc)
    conn.request("GET", url.path)
    return conn.getresponse().read()

if __name__ == "__main__":
    app.run(debug=True)