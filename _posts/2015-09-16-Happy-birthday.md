---
layout: post
title:  "Happy Birthday"
date:   2015-09-16 00:00:33
categories: Tech
tags: [Life, Learning, Coding, DIY]
image:
  background: ps_neutral.png
---
Grew up +1 in numbers yesterday. Had a super awesome day. But this post is not about that. Few Months back, while browsing through quora/reddit I came across a thread that had the implementation of automatic replying to a birthday post on facebook. I tried to implement the same using facebook's graph api's.

First you need to get a token for your app to work from <a href="https://developers.facebook.com/tools/explorer/"> here</a>. Add this token in the code ( it expires every 1 hour, so make sure the token is fresh). Second you need the epoch time of your Birthdate ie: [15-09-2015 = 1442275200] from any <a href="www.epochconverter.com">online epoch converter</a>.

Then run this python script the next day. It auto replies and comments on each of the post from previous day. Mine took 30 minutes to reply to all the posts. Had to change some replies though :P.

<img src="https://i.imgur.com/RdU599R.png" alt="">

>Code.

You can download the code from <a href="https://github.com/yogeshmpandey/codesamples/blob/master/automatic_replier.py">here</a>.

<img src="https://i.imgur.com/rQxtTTn.png" alt="">

>Autoreply in action.

Reuse and Happy Hacking :)
