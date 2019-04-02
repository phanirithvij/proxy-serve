# from datetime import time, datetime
from time import sleep, time
import random

"""
    {
        'url' : Tracker(url, resp),
        ...
    }
"""
container = {}
caches = {}

class Tracker:
    def __init__(self, url, resp):
        self.url = url
        self.resp = resp
        self.count = 0
        self.time = []

class CacheObj:
    def __init__(self, data):
        self._data = data
        self._time = time()
        print(self._time)

    def getdata(self):
        return self._data

def timeConsumer(req):
    print('start req ...')
    # consume time to simulate a request
    sleep(2)
    print('...done')
    return req

def caching():
    urls = ['lsak', 'saa', 'das']
    while True:
        url = random.choice(urls)
        print(f'\nA random url, {url}')
        resp = None
        notincache = False
        if (len(caches) == 4):
            print("caches length > 3")
            delet = random.choice(caches.keys())
            print(f"deleting a one of them randomly {delet}") # lru can be used
            del caches[delet]

        try:
            print("trying to find resp in caches")
            resp = caches[url].getdata() # if fails it means it's not cached
            print("found data")
        except Exception as _e:
            print("Failed => send request")
            notincache = True # i.e. isnotincache = true
            resp = timeConsumer(url) # send request as not in cache

        try:
            if (notincache): # if not in cache
                curr = container[url] # current req
                curr.count += 1
                curr.time.append(time()) # appending the last accessed time
                if (
                    curr.count > 3 and\
                    (curr.time[-1] - curr.time[-4]) < 5*60 # less than 5min
                ):
                    print("del the first time")
                    del curr.time[0]
                    caches[url] = CacheObj(resp)
            else:
                print('in cache')

        except Exception as _e:
            # Failed implies container[url] is empty
            print("container has no url creating...")
            print(_e)
            container[url] = Tracker(url, resp)
            container[url].count += 1
            container[url].time.append(time())

if __name__ == "__main__":
    caching() # test it
