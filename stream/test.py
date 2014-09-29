#!/usr/bin/python -tt

# imports
import Queue, threading
from packages.twitter.data import *
from packages.twitter.streams import *

# main function
def main():

  # API's keys and secrets
  consumerKey = 'xxQqcecOrkEyg2HUo6AJug'
  consumerSecret = '6x19sUt5rg4Z2OeM75Qj5Ygq6PcDA6VN09fCLoUYM'
  tokenKey = '2357212256-hf7ixTlPUqh699omByLTHu2Keir8pkwss0Eyyeg'
  tokenSecret = 'xqgPzT9ecLMujyCZyj001YayUoCWdbuDp0GESX4lvassd'

  # twitter ID's: http://gettwitterid.com
  wsjbusiness = '28140646'
  wsjmarkets = '28164923'
  foxbusiness = '56413858'
  abcbusinessnews = '399182898'
  abc = '28785486'
  foxnews = '1367531'
  cbsnews = '15012486'
  cbsmoneywatch = '29057694'
  bloombergnews = '34713362'
  bloomberg = '104237736'
  bloombergmrkts = '69620713'
  forbes = '91478624'

  # log file absolute location
  logfile = '/tmp/twitter-urls.log'

  # create thread to consume url's in log and place content into a queue
  urlContent_q = Queue.Queue()
  url_t = threading.Thread(target=extractUrlContent,\
                           args=(urlContent_q, logfile,))
  url_t.setDaemon(True)
  url_t.start()

  # TODO create thread to output url content in queue

  # follow twitter stream and add urls to queue
  follow = [wsjbusiness, wsjmarkets, foxbusiness, abcbusinessnews, abc, \
            foxnews, cbsnews, cbsmoneywatch, bloombergnews, bloomberg, \
            bloombergmrkts, forbes]
  auth, api = initTwitter(consumerKey, consumerSecret, tokenKey, tokenSecret)
  listener = Listener(logfile, api)
  stream = initStream(auth, listener)
  stream.filter(follow)

if __name__ == '__main__':
  main()
