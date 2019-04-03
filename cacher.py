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

def do_caching_or_request(reqfunc, url, container=container, caches=caches, data=None):
    # while True:
        # url = random.choice(urls)
    resp = None
    notincache = False
    if (len(caches) == 5):
        print("caches length > 3")
        delet = random.choice(list(caches.keys()))
        print(f"deleting a one of them randomly {delet}") # lru can be used
        del caches[delet]

    try:
        print("trying to find resp in caches")
        resp = caches[url].getdata() # if fails it means it's not cached
        print("found data")
    except KeyError as _e:
        print("not found sending request")
        notincache = True # i.e. isnotincache = true
        resp = reqfunc(url, data) # send request as not in cache
        # print("got data", resp)

    try:
        if (notincache): # if not in cache
            curr = container[url] # current req
            curr.count += 1
            curr.time.append(time()) # appending the last accessed time
            if (
                curr.count > 2 and\
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

    return resp, not notincache

if __name__ == "__main__":
    urls = ['lsak', 'saa', 'das']
    while True:
        do_caching_or_request(timeConsumer, random.choice(urls)) # test it
