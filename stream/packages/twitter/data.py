#!/usr/bin/python -tt

# data.py

# Copyright 2014 Pat York and Thomas Avant
# CS 491H - Data Science Project: Twitter Sentiment and U.S. Markets

# imports
import time

def follow(file_):
  file_.seek(0,2) # Go to the end of the file
  while True:
    line = file_.readline()
    if not line:
      time.sleep(0.1) # Sleep briefly
      continue
    yield line

def toQueue(source, queue):
  for item in source:
    queue.put(item)
  queue.put(StopIteration)

def fromQueue(queue):
  while True:
    item = queue.get()
    if item is StopIteration: break
    yield item

def extractUrlContent(qSource, file_):
  with open(file_, 'r') as f:
    for url in follow(f):
      # TODO create a function to scrapr headers and paragraphs from html
      print url
