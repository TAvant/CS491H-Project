#!/usr/bin/python -tt

# streams.py

# Copyright 2014 Pat York and Thomas Avant
# CS 491H - Data Science Project: Twitter Sentiment and U.S. Markets

# imports
import tweepy, os, sys, Queue, logging

def initTwitter(consumerKey, consumerSecret, tokenKey, tokenSecret):
  """member takes the two keys and two secrets required to get the O
  authorization and api instances from Twitter. The member returns both the
  authorization and api as a tuple: (auth, api)."""

  # create OAuthHandler instance and set with access token
  auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
  auth.set_access_token(tokenKey, tokenSecret)

  # return the authorization and authorized api
  return (auth, tweepy.API(auth))

def initStream(auth, listener):
  """member takes the Twitter authorization and the tweepy listner object as 
  parameters. The member returns a tweepy stream."""

  return tweepy.Stream(auth, listener)

# https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py
class Listener(tweepy.StreamListener):
  """The Listener class inherits form the tweepy base class StreamListener.
  StreamListener members on_status, on_error and on_timeout are overridden. """

  def __init__(self, logfile, api=None):
    """Added a logfing file to the constructor, so the urls can be 
    placed in log."""
    self.api = api or API()
    logging.basicConfig(filename=logfile, level=logging.NOTSET, \
                        format='%(message)s') 

  def on_status(self, status):
    """member outputs the urls found in tweets to a file"""

    # TODO remove or comment out print command
    # Print the tweet
    print('Tweet: ' + status.text)

    # for each url in the tweet
    for url in status.entities['urls']:

      # get the fully resolved media URL and output it to the log
      # Entities in Twitter Objects: https://dev.twitter.com/docs/entities
      logging.info(url['expanded_url'])

    return True
 
  def on_error(self, status_code):
    """member returns true upon receiving an error in order to 
    continue listening."""
    return True
 
  def on_timeout(self):
    """member returns 'True'upon receiving a timeout in order to 
    continue listing."""
    return True
