---
layout: post
title:  "Happy Birthday"
date:   2015-09-16 00:00:33
categories: tech
image:
  background: ps_neutral.png
---
Grew up +1 in numbers yesterday. Had a super awesome day. But this post is not about that. So while going through quora/reddit I came through thread that had the implementation of automatic replying to a birthday post on facebook. I tried to implement the same using facebook's graph api's. So first you need to get a token for your app to work from <a href="https://developers.facebook.com/tools/explorer/"> here</a>. Add this token in the code ( it expires every 1 hour, so make sure the token is fresh). Second you need the epoch time of your Birthdate ie: [15-09-2015 = 1442275200] from any <a href="www.epochconverter.com">online epoch converter</a>. 

Then run this python script the next day. It auto replies and comments on each of the post from previous day. Mine took 30 minutes to reply to all the posts. Had to change some replies though :P

```
import requests
import os
import json
import facebook
import time
from random import choice
from urllib import urlencode

#static stuff
token="--add token here--"
graph = facebook.GraphAPI("--add token here--")
#the list of messages from which you want a random message to be selected
reply_set = ['Thank you very much :) ', 'Thanks a lot :) ', 'Thank you! :) ', 'Thanku :)']
parameters = {'access_token': token}

def get_posts(url, ids):
    feed = ids
    r = requests.get(url)
    result = r.json()
    for post in result['data']:
        feed.append(post['id'])
    try:
        get_posts(result['paging']['next'],feed)
    except KeyError:
        add_comment_like(ids)
        
def add_comment_like(ids):
    for uid in ids:
        reply = choice(reply_set)
        url = 'https://graph.facebook.com/%s/comments?access_token=%s' %(uid, token)
        requests.post(url, data={'message': reply})
        url = 'https://graph.facebook.com/%s/likes?access_token=%s' % (uid, token)
        requests.post(url, data="")
        
if __name__ == '__main__':

    url = 'https://graph.facebook.com/v2.4/me/feed'
    params = {'since': '1442275200', 'access_token': token}
    url = '%s?%s' % (url, urlencode(params))
    get_posts(url,[])

```

<img src="/images/mum_trip/a.png" alt="">

>Autoreply in action.

Reuse and Happy Hacking :)
