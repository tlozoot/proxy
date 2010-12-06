from sgmllib import SGMLParser

class AssetAttributeFixer(SGMLParser):
    def reset(self):
	    SGMLParser.reset(self)
	    self.urls = []

    def start_a(self, attrs):
	    href = [v for k, v in attrs if k=='href']
	    if href:
		    self.urls.extend(href)
			
    def fix_attrs(self, url):
        return url
