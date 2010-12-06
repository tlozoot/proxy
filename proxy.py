
from flask import Flask, request
app = Flask(__name__)

@app.route("/pass")
def proxy_pass():
    from custom_parser import AssetAttributeFixer
    import urllib
    url_string = request.args.get("url")
    try:
        url_sock = urllib.urlopen(url_string)
        text = url_sock.read()
        url_sock.close()
    except:
        return "Please include a valid URL parameter" 
        
    parser = AssetAttributeFixer()
    parser.feed(text)
    return parser.fix_attrs(url_string)

if __name__ == "__main__":
    app.run(debug=True)