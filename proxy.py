import urllib
from HTMLParser import HTMLParser

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
        text = urllib.urlopen(request.args.get("url")).read()
    except:
        return "Please include a valid URL parameter" 
    return text

if __name__ == "__main__":
    app.run(debug=True)