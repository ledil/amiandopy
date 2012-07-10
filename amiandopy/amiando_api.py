from urllib import urlencode
from urlparse import urlparse, parse_qs
import requests

try:
    import simplejson as json
except ImportError:
    import json

class AmiandoAPI(object):
    def __init__(self, apikey, url='https://www.amiando.com/api'):
        self.apikey = apikey
        self.session = requests.session()
        self.url = url.strip('/')

    def get (self, path='', retry=3, **options):
        response = self._query(
            method = 'GET',
            path = path,
            data = options,
            retry = retry
        )
        return response

    def _query(self, method, path, data=None, retry=0):
        data = data or {}
        
        def load(method, url, data):
            try:
                if method in ['GET', 'DELETE']:
                    response = self.session.request(method, url, params=data, allow_redirects=True)
                if method in ['POST','PUT']:
                    files = {}
                    
                    for key in data:
                        if hasattr(data[key], 'read'):
                            files[key] = data[key]
                            
                    for key in files:
                        data.pop(key)
                        
                    response = self.session.request(method, url, data=data, files=files)
            except requests.RequestException as exception:
                raise #self.HTTPError(exception.message)

            result = self._parse(response.content)
            return result
            
        for key in data:
            if isinstance(data[key], (list, set, tuple)) and all([isinstance(item, basestring) for item in data[key]]):
                data[key] = ','.join(data[key])

        data['version'] = '1'
        data['format'] = 'json'
        data['apikey'] = self.apikey
            
        url = '%s/%s' % (self.url, path)

        return load(method, url, data)

    def _parse(self, data):
        try:
            data = json.loads(data)
        except ValueError:
            return data            
        return data            
