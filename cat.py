from urllib2 import Request, urlopen, URLError
import time

request = Request('http://thecatapi.com/api/images/get?format=html')

for num in range(0,100):
    try:
        response = urlopen(request)
        random_cat = response.read()
        print (random_cat)
    except URLError, e:
        print 'Got an error code:', e
    time.sleep(2)
