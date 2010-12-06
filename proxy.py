from flask import Flask, request
app = Flask(__name__)

@app.route("/pass")
def proxy_pass():
    import urllib
    import custom_parser
    url_string = request.args.get("url")
    try:
        url_sock = urllib.urlopen(url_string)
        text = url_sock.read()
        url_sock.close()
    except:
        return "Please include a valid URL parameter" 
    return custom_parser.fix_resources(text, url_string)

if __name__ == "__main__":
    app.run(debug=True)