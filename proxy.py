from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/")
def root():
    import urllib
    import custom_parser
    url_string = request.url.split("url=")[1] # Hackish; but works if the requested URL contains query params
    try:
        url_sock = urllib.urlopen(url_string)
        print url_string
        content_type = url_sock.info()['Content-Type']
        proxied_html = custom_parser.fix_resources(url_sock.read(), url_string)
        resp = make_response(proxied_html)
        resp.headers['Content-Type'] = content_type
        url_sock.close()
        return resp
                
    except:
        return "Please include a valid URL parameter"
    
    
if __name__ == "__main__":
    app.run(debug=True)