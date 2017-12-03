---
layout: post
title:  "Emotions in German TV Channels "
date:   2017-12-03 20:52:38
categories: coding
tags: [Coding, Learning, DIY]
image:
  background: witewall_3.png
---
“Because emotions can't be ignored, no matter how they seem.”  ― Anne Frank

The previous month, I had an opportunity to participate in a hackathon in Munich. For the sake of free food, scrap the rust off our brains and keeping up with the upcoming Tech, We decided to spend our weekends on the campus of the Technical University of Munich.
We chose a problem in which we had to analyse logos out around 50 thousand screenshots of 15 TV stations that operate in Germany.
Logo detection was done with RCNN using Tensorflow. But interestingly, since we had the access to this dataset, Why not find something interesting out of it.
So, the idea was to :-

- Use AZURE Cognitive Vision APIs and Emotion API for detecting the emotions the characters portray. 
- The emotions detected are happiness, sadness, surprise, anger, fear, contempt, disgust or neutral. 
- These emotions are communicated cross-culturally and universally via the same basic facial expressions
- Provide an Emotional Index for each broadcaster.

<img src="https://i.imgur.com/LgJSI4K.jpg" alt="">
>Classification

Now coming to the how? part. Microsoft Azure provides a very dense APIs for deep learning and image recognition. Out of all these, we chose the [Emotion Api](https://azure.microsoft.com/en-us/services/cognitive-services/emotion/) that can help in the detecting the Emotional values in a frame.
We patched the Dataset with a simple rough python script that consumes the API and provides the output. The code can be downloaded  [here](https://github.com/yogeshmpandey/Scripts/blob/master/hackathon_nov_munich.py).
The script ran for around 9 hours and ran on approximately 90 percent of the dataset and next morning we had some great results.


<img src="https://i.imgur.com/WEkjhbV.jpg" alt="">
>Work in Progress

The end results can be downloaded from [here](https://goo.gl/W551AN).

<img src="https://i.imgur.com/FgZppik.png" alt="">
>Output

Some of the interesting facts from the data "
- 71.53 percent of the faces German people see on their TV screens are neutral.
- The least shown emotion is fear (0.36 percent) followed by disgust (0.72 percent) and contempt (1.13).
- On an average Germans see 23 percent of happy faces on their screens.
- With 31.3 percent prosieben is the happiest channel and with 4.5 percent sadly the saddest too.

More data crunching can be done with the above Excel sheet.
Now, this Emotional Index could provide a lot of benefits to the potential advertisers. Also, it is used to complement and improve (MPAA) film rating system and/or TV parental guidelines.

Note: The Output is not Vetted nor official. Completely based on the dataset given.
