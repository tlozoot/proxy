import re

def fix_resources(html, url):
    '''An incredibly naive resource fixer'''
    array = url.split('/')
    if re.search(r'\.htm?(l)', array[-1]):
        del(array[-1])
    url = '/'.join(array)
    if not re.search(r'/$', url):
        url += '/'
    return re.sub(r'(src|href)=(\'|")(?!http)', r'\1=\2' + url, html)
