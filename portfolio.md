---
layout: page
title: Portfolio
permalink: /portfolio/
---

A snippet of personal (and some work-related) things I've been working on. I'm fortunate that most of day job is open source, you can check out my daily contributions on my [github](https://github.com/Charlie-Henry).

***

## Machine Learning

### Austin Airport TSA Wait Time Forecasting

I created and maintain [a bluesky bot](https://bsky.app/profile/forecastaus.bsky.social) that posts a daily forecast for how busy the airport will be using a simple ARIMA model trained on historical TSA checkpoint volume data. As part of this work, I set up an ETL that processes hundreds of thousands of pages of PDFs posted to the [TSA website](https://www.tsa.gov/foia/readingroom).

{: .center}
![Data flow diagram of the forecast bot]({{site.baseurl}}/images/flow_diagram_forecast_aus.png)
*Data flow diagram of the forecast bot*

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:igdjkgwavulssahqpkrgz5xl/app.bsky.feed.post/3lgc2pkbdg22k" data-bluesky-cid="bafyreihwtbilk46hmm22ytalbg55poobveokmbydtiqou4j5z563aj4iki"><p lang="en">Below normal wait times expected tomorrow: Higher than 0% of days.<br><br><a href="https://bsky.app/profile/did:plc:igdjkgwavulssahqpkrgz5xl/post/3lgc2pkbdg22k?ref_src=embed">[image or embed]</a></p>&mdash; 🤖 Austin Airport Daily Wait Time Forecasting  (<a href="https://bsky.app/profile/did:plc:igdjkgwavulssahqpkrgz5xl?ref_src=embed">@forecastaus.bsky.social</a>) <a href="https://bsky.app/profile/did:plc:igdjkgwavulssahqpkrgz5xl/post/3lgc2pkbdg22k?ref_src=embed">January 21, 2025 at 5:59 PM</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>
{: .center}
*Example prediction*

***

## Data Visualization

### 2024 Elections Visualizations

One topic I frequently visualize is elections. My [atx-elections-data](https://github.com/Charlie-Henry/atx-elections-data) repo contains several examples of code I have written to visualize elections mostly in Texas.

{: .center}
![Precinct-level election shifts](https://raw.githubusercontent.com/Charlie-Henry/atx-elections-data/refs/heads/main/visualization/20_to_24_shifts/2020_vs_2024_tx.png)
*Precinct-level election shifts*

For 2024's early voting period I set up an [ETL script](https://github.com/Charlie-Henry/atx-elections-data/tree/main/etl/travis_county_roster_scrape) that scraped live voter turnout data and plotted it alongside a comparison to the the 2020 election. 

{: .center}
![2024 live voter turnout comparison](https://raw.githubusercontent.com/Charlie-Henry/atx-elections-data/refs/heads/main/etl/travis_county_roster_scrape/2024-voter-turnout-timeline.png)
*2024 live voter turnout comparison*

### Austin MetroBike Trips Visualization

Using a tool called [flowmap.blue](https://flowmap.blue) I was able to quickly visualize multiple years of docked bicycle data. It is featured on [flowmap.blue's examples page.](https://flowmap.blue/#examples) 

Created with: Python, Google sheets

<iframe width="100%" height="600" src="https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc/embed" frameborder="0" allowfullscreen></iframe>

[Link to the interactive](https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc)

***

## Skills Summary

Programming: 
- Python (expert)
- R (intermediate)
- Javascript (intermediate)

Data Engineering:
- Extract transform load (ETL) scripting with Python and dbt
- Building and deploying Docker containers
- SQL (Postgres, Oracle) for database administration and data extraction/transformation
- Cloud orchestration with Prefect, on-premises orchestration with Apache Airflow
- Amazon Web Services (AWS): S3, EC2 
- Google Cloud Service (GCS): BigQuery, Cloud Functions, Cloud Storage

Data Science/Machine Learning
- Machine learning: Pytorch, XGBoost, Scikit learn
- Experience applying deep learning, PCA, and supervised learning to real world problems

Business Intelligence
- Power BI (expert)
- Hex (expert)
- Tableau (intermediate)
- MicroStrategy (intermediate)
- Geospatial analysis and mapping with ArcGIS Online, geopandas, postGIS

***

## Education & Certifications

Education:
- Master's of Science in Data Science, *The University of Texas at Austin*. Dec 2024
- Bachelor's of Science in Aerospace Engineering, *The University of Texas at Austin*. Dec 2018

Certifications: 
- [Prefect Associate](https://www.credential.net/746691ba-73ab-4a31-8f1c-00b99c367f4e#acc.E4o6KFhL)

Master's Coursework:
- DSC 385T: Data Science for Health Discovery and Innovation
- DSC 391L: Principles of Machine Learning
- DSC 394R: Reinforcement Learning
- [CS 388: Natural Language Processing](https://courses.edx.org/certificates/f0460d4329844ae8bad4630c167969a7)
- [CS 394D: Deep Learning](https://courses.edx.org/certificates/9e77858ad5fe4406b561f31d68bd01e9)
- [CS 395T: Data Structures and Algorithms](https://courses.edx.org/certificates/9054a3d73f9d4002a9c07333808db655)
- [DSC 385: Data Exploration and Visualization](https://courses.edx.org/certificates/38a0239523b6453bb0d0e05cb0c60028)
- [DSC 383: Advanced Predictive Models for Complex Data](https://courses.edx.org/certificates/f7b5e6a0636a4048a230a638b0b4873f)
- [DSC 382: Foundations of Regression and Predictive Modeling](https://courses.edx.org/certificates/8d01dc49224e4745a9023a4f47d5166d)
- [DSC 381: Probability and Simulation-Based Inference](https://courses.edx.org/certificates/6e0bb056bd6f4d3a8982a1f392967eec)