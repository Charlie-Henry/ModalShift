---
layout: post
title: Daily Austin Airport Wait Time Predictions
excerpt_separator: <!--more-->
---

I made a model to predict how busy the airport is going to be.

<!--more-->

During my Data Science Masters, I took a class called Advanced Predictive Models. I am applying one method I learned from that class to the Austin Airport TSA passenger counts. 


# Time Series Prediction with SARIMA Modeling

For these daily predictions, I use a form of time series modeling called SARIMA. SARIMA is an acronym for:

- Seasonal

- Autoregressive

- Integrated

- Moving Average

A SARIMA model takes in parameters for each of these sub-models and combines them to make predictions. It is typically written as:

SARIMA =(p, d, q) \times (P, D, Q, S)

S is the period of the seasonal parameter, in this case we're using 7 to account for the day-of-week effects of passenger volumes.

To pick parameters for SARIMA, we simply do a grid-search of P,D,Q,p,d,q parameters to see which has the best performance in a statistic called AIC.

The most optimal found for grid search in space 0 to 2:

SARIMA =(2, 1, 2) \times (0, 1, 2, 7)

***

# What this is good for

This model is great at including the seasonal and day-of-week effects on passenger volumes. It is not going to do a great job seeing one-off holidays like Memorial Day Weekend or big events like ACL fest. 

The data behind these predictions gets updated on a roughly two week period. This can cause some lag, especially big changes that may have recently happened.

***

# Data Source

[mikelor has been crunching the numbers for TSA passenger counts here](https://github.com/mikelor/TsaThroughput)

***

# Twitter Deployment

I'm using Google Cloud Functions to train my model, do my forecast, create the image, and tweet the results. [I used this guide.](https://anderfernandez.com/en/blog/automate-python-script-google-cloud/)

[It tweets the results daily here](https://twitter.com/ForecastAUS)

<a class="twitter-timeline" href="https://twitter.com/ForecastAUS?ref_src=twsrc%5Etfw">Tweets by ForecastAUS</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Charlie
