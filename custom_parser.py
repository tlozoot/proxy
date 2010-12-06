import re

def fix_resources(html, url):
    '''An incredibly naive resource fixer'''
    return re.sub(r'(src|href)=(\'|")(?!http)', r'\1=\2' + url, html)