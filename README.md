# Proxy

A stupid simple [proxy server](http://en.wikipedia.org/wiki/Proxy_server), written in [Python](http://www.python.org/) and [Flask](http://flask.pocoo.org/). Useful for hacking around cross-browser restrictions and other things you're not supposed to do on the Internet.

## Deployment

To deploy on [Apache](http://httpd.apache.org/), add something like this to your `httpd.conf`:
    
    ScriptAlias /proxy /path/to/proxy/index.cgi

For more detailed info, see the [Flask documentation](http://flask.pocoo.org/docs/deploying/).