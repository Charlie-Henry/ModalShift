---
layout: page
title: Portfolio
permalink: /portfolio/
---

# Data Analysis & Visualization

## Change in commute patterns in Texas

I wanted to track how the state of Texas has been doing on returning to "normal" following the COVID-19 pandemic. [Google's Mobility data](https://www.google.com/covid19/mobility/) tracks the % change (relative to February 2020) to how often their users are going to residential areas, parks, grocery stores, and others. I was particularly interested in the "workplaces" category which should be a good indicator of how many workers are returning to office. 

The return to the office hasn't been even. The cities and the Permian Basin are lagging behind the more rural areas of the state.

Created with: Python + Geopandas

[Project repo](https://github.com/Charlie-Henry/ModalShift/tree/master/visualizations/Texas-Mobility-Maps)

![config.yml]({{site.baseurl}}/visualizations/Texas-Mobility-Maps/TX%20Google%20Workplaces.gif) 

***

## COVID-19 Mobility Impacts Dashboard

Starting in April 2020, [I created a blogpost](https://modalshift.co/COVID19/) tracking the changes to Austin's mobility caused by COVID-19. Using data sourced from the City's open data portal, I created some live-updating charts showing vehicle volume, micromobility trips, and traffic incidents. About every month I create a full report showing trends in the data along with a few takeways of mine. Check out my archive of my thoughts & takeaways, too.

Created with: Google apps script, plotly studio

![config.yml]({{site.baseurl}}/images/Combined.png)

***

## Austin MetroBike Trips Visualization

Using a tool called [flowmap.blue](https://flowmap.blue) I was able to quickly visualize multiple years of docked bicycle data. It is featured on [flowmap.blue's examples page.](https://flowmap.blue/#examples) 

[Link to the interactive](https://flowmap.blue/11odTn4_kytEo2O9LxAXGbZspXM_OLFsX__mpxRAvAOc/5f18087)

Created with: Python, Google sheets

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Video of <a href="https://twitter.com/ATXMetroBike?ref_src=twsrc%5Etfw">@ATXMetroBike</a> trips from 2015 to 2020. <a href="https://t.co/dcUSltaPG3">https://t.co/dcUSltaPG3</a> <a href="https://t.co/UpxtwVJ4jV">pic.twitter.com/UpxtwVJ4jV</a></p>&mdash; Charlie Henry (@ShiftModal) <a href="https://twitter.com/ShiftModal/status/1397224474018189324?ref_src=twsrc%5Etfw">May 25, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


***

# Interactive Mapping 

## Bluetooth Sensor Travel Times Visualized

The city of Austin publishes travel time data using bluetooth sensors. These are largely no longer maintained but some sensors are still operational. I was interested in how COVID-19 impacted travel times and congestion.

Created with: Python, Mapbox GL JS

<iframe src='/maps/bluetooth_map.html'
        width='100%' height='400px'>
</iframe>

***