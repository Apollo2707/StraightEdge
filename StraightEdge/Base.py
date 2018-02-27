import urllib3

def getRawData(url):
  http = urllib3.PoolManager()
  r = http.request('GET', url)
  html = str(r.data)
  return html
