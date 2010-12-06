import urllib

from flask import Flask, request
app = Flask(__name__)

@app.route("/pass")
def proxy_pass():
    from custom_parser import AssetAttributeFixer

    try:
        url_sock = urllib.urlopen(request.args.get("url"))
        text = url_sock.read()
        url_sock.close()
    except:
        return "Please include a valid URL parameter" 
        
    parser = AssetAttributeFixer()
    return text

if __name__ == "__main__":
    app.run(debug=True)