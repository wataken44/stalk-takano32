#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" takano32.py


"""

import sys
import urllib2
import json
import codecs

URL = "https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=false&screen_name=takano32&count=200"

def main():
    sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

    r = urllib2.Request(url=URL)
    f = urllib2.urlopen(r)
    js = json.loads(f.read(), "UTF-8")
    f.close()

    statuses_count = js[0]["user"]["statuses_count"]
    max_id = js[0]["id"] + 1

    for i in range(6):
        url = URL + ("&max_id=%s" % str(max_id))
        r = urllib2.Request(url=URL)
        f = urllib2.urlopen(r)
        js = json.loads(f.read(), "UTF-8")
        f.close()
        
        for tweet in js:
            link = "https://twitter.com/statuses/%s" % tweet["id_str"]
            text = tweet["text"]
            print("%d %s %s" % (statuses_count, link, text))
            statuses_count -= 1
            max_id = tweet["id"] - 1

if __name__ == "__main__":
    main()
