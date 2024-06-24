---
layout: page
title: Portfolio
permalink: /portfolio/
---

A snippet of personal (and some work-related) things I've been working on. I'm fortunate that most of day job is on open source, you can check out my daily contributions on my [github](https://github.com/Charlie-Henry).

## Machine Learning

### Austin Airport TSA Wait Time Forecasting

I created and maintain [a twitter bot](https://x.com/ForecastAUS) that tweets daily a forecast for how busy the airport will be using a simple ARIMA model trained on historical TSA checkpoint volume data. As part of this work, I set up an ETL that processes hundreds of thousands of pages of PDFs posted to the [TSA website](https://www.tsa.gov/foia/readingroom).

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Longer wait times expected tomorrow: Higher than 90% of days. <a href="https://t.co/4z9TT4y9OS">pic.twitter.com/4z9TT4y9OS</a></p>&mdash; Austin Airport Wait Time Forecasting (@ForecastAUS) <a href="https://twitter.com/ForecastAUS/status/1803880885726646274?ref_src=twsrc%5Etfw">June 20, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


***

## Data Analysis & Visualization

### Austin MetroBike Trips Visualization

Using a tool called [flowmap.blue](https://flowmap.blue) I was able to quickly visualize multiple years of docked bicycle data. It is featured on [flowmap.blue's examples page.](https://flowmap.blue/#examples) 

Created with: Python, Google sheets

<iframe width="100%" height="600" src="https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc/embed" frameborder="0" allowfullscreen></iframe>

[Link to the interactive](https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc)


### Change in commute patterns in Texas

I wanted to track how the state of Texas has been doing on returning to "normal" following the COVID-19 pandemic. [Google's Mobility data](https://www.google.com/covid19/mobility/) tracks the % change (relative to February 2020) to how often their users are going to residential areas, parks, grocery stores, and others. I was particularly interested in the "workplaces" category which should be a good indicator of how many workers are returning to office. 

The return to the office hasn't been even. The cities and the Permian Basin are lagging behind the more rural areas of the state.

Created with: Python + Geopandas

[Project repo](https://github.com/Charlie-Henry/ModalShift/tree/master/visualizations/Texas-Mobility-Maps)

![config.yml]({{site.baseurl}}/visualizations/Texas-Mobility-Maps/TX%20Google%20Workplaces.gif) 

### COVID-19 Mobility Impacts Dashboard

From April 2020 to August 2021, [I kept a running blogpost](https://modalshift.co/COVID19/) tracking the changes to Austin's mobility caused by COVID-19. Using data sourced from the City's open data portal, I created some live-updating charts showing vehicle volume, micromobility trips, and traffic incidents. Every month I posted a full report showing trends in the data along with a few takeaways of mine. 

Created with: Google apps script, plotly studio


***

## Speaking Engagements & Presentations

American Society Of Highway Engineers Central Texas Region July 2021 Meeting: *Planes, Strains, and Automobiles* - [Presentation Slides](https://drive.google.com/drive/folders/1qFWhqVciXfjjkXHq3ODAg_7GMpaXyK3g?usp=sharing)

South by Southwest 2019 Lightning Talk: *Unlocking the future of Transportation with Open Data*

Open Austin July 2020 Meeting: Measuring COVID-19 Update - [Presentation slides](https://docs.google.com/presentation/d/1KSpYtZUCd4QDFFznqJ6ZJngQLanqOHeZcMB6Tsh4EpE/edit?usp=sharing)

Saving Lives with Connected Vehicle Data: [Link to webinar recording](https://drive.google.com/file/d/112bk87Vqy6t0zd_MniikZ-y010n0e3Ny/view)

![config.yml]({{site.baseurl}}/images/SXSW.JPG)
