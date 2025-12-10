---
layout: page
title: Portfolio
permalink: /portfolio/
---

A snippet of personal (and some work-related) things I've been working on. 

I'm fortunate that most of my day job is open source, you can check out my daily contributions on my [github](https://github.com/Charlie-Henry).

***

## Machine Learning

### [AeroVolumes](https://www.aerovolumes.com/)

I built an automated forecasting system that predicts how busy major U.S. airports will be, posting a daily forecast to Bluesky. The ML pipeline uses a simple ARIMA model trained on historical TSA checkpoint throughput.

To support the forecasting system, I engineered a full ETL pipeline that parses and cleans hundreds of thousands of pages of TSA PDF reports, extracting historical checkpoint counts into a structured database.

As part of this project, I also deployed a public API on [RapidAPI](https://rapidapi.com/CharlieHenry/api/aerovolumes) that allows anyone to query and download data

{: .center}
![Data flow diagram of the forecast bot]({{site.baseurl}}/images/flow_diagram_forecast_aus.png)
*Data flow diagram of the forecast bot*

{: .center}
[![Example post: Relatively normal wait times expected tomorrow: Higher than 26% of days.]({{site.baseurl}}/images/forecast.png)](https://bsky.app/profile/forecastaus.bsky.social/post/3lmdbdmrjrd2t)
*Example prediction*

***

### [CFL Negotiation list tracker](https://cfl-neg-list-website.onrender.com/)

I built an automated data pipeline that scrapes Canadian Football League (CFL) negotiation list updates from a website, parses roster information, and publishes structured player datasets to a [public site](https://cfl-neg-list-website.onrender.com/).

To enrich each player profile, I developed an ML pipeline, which analyzes historical player data, college backgrounds, and pro experience to generate high level scouting summaries. These insights are served through my site and updated automatically as new players appear on negotiation lists.

{: .center}
![Data flow diagram of the forecast bot]({{site.baseurl}}/images/cfl_neg_list.png)
*Playing history table created with an ML pipeline*

***

## Data Engineering

### Austin Road Conditions

I built a [Bluesky bot](https://bsky.app/profile/atx-road-condition.bsky.social) that posts live road condition updates for Austin using real-time roadway friction sensor data. Every 5 minutes, the ETL checks the City of Austin’s public sensor feed for changes in road conditions. When a change is detected, the bot generates a new post and attaches a screenshot from the nearest traffic camera.

The entire pipeline is [open source](https://github.com/Charlie-Henry/atx-road-conditions-bot) and designed to be deployable in other cities with similar open sensor data.

{: .center}
[![Example post: GPOOR roadway grip reported at LAKELINE BLVD / 183 HWY SVRD, was previously FAIR. Current roadway condition is Standing water.]({{site.baseurl}}/images/road_conditions.png)](https://bsky.app/profile/atx-road-condition.bsky.social/post/3lq4lzwglsr2y)
*Example post*

### Voter Turnout Scraping

For 2024's early voting period I set up an [ETL script](https://github.com/Charlie-Henry/atx-elections-data/tree/main/etl/travis_county_roster_scrape) that scraped live voter turnout data and plotted it alongside a comparison to the the 2020 election. 

The archived post along with more visualizations is available [here]({{site.baseurl}}/early-voting/). I also created a similar post for the [2025 election]({{site.baseurl}}/nov-25-election/).

{: .center}
[![2024 live voter turnout comparison](https://raw.githubusercontent.com/Charlie-Henry/atx-elections-data/refs/heads/main/etl/travis_county_roster_scrape/2024-voter-turnout-timeline.png)]({{site.baseurl}}/early-voting/)
*2024 live voter turnout comparison*

***

## Data Visualization

### 2024 Elections Visualizations

One topic I frequently visualize is elections. My [atx-elections-data](https://github.com/Charlie-Henry/atx-elections-data) repo contains several examples of code I have written to visualize elections mostly in Texas.

{: .center}
[![Precinct-level election shifts](https://raw.githubusercontent.com/Charlie-Henry/atx-elections-data/refs/heads/main/visualization/20_to_24_shifts/2020_vs_2024_tx.png)](https://github.com/Charlie-Henry/atx-elections-data?tab=readme-ov-file#20_to_24-shifts)
*Precinct-level election shifts*

### Austin MetroBike Trips Visualization

Using a tool called [flowmap.blue](https://flowmap.blue) I was able to quickly visualize multiple years of docked bicycle data. It is featured on [flowmap.blue's examples page.](https://flowmap.blue/#examples) 

Created with: Python, Google sheets

{: .center}
[![A map displaying the trip density of bicycle trips between kiosks in Austin, Texas.]({{site.baseurl}}/images/flowmap.png)](https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc)
[Link to the interactive](https://www.flowmap.blue/1qIMB8jTEGMO6u1sLcuu5vQvP90jbENt904zMCV0A3DI/82227dc)

***

## Skills Summary

**Programming**
- Python (expert): data engineering, ML modeling, automation, API development
- R 
- Java
- Javascript

**Data Engineering & Infrastructure**
- End-to-end ETL development with Python, dbt, and SQL
- Docker containerization and deployment
- SQL (Postgres, Oracle): schema design, optimization, data transformation
- Workflow orchestration: Prefect (cloud), Apache Airflow (on-prem)

**Cloud platforms:**
- AWS: S3, EC2
- GCP: BigQuery, Cloud Functions, Cloud Storage
- Automated pipelines for PDF extraction, web scraping, and real-time sensor ingestion

**Data Science & Machine Learning:**
- Machine learning with PyTorch, XGBoost, Scikit-learn
- Experience with supervised learning, deep learning, PCA, ARIMA time-series forecasting, and generative AI (Gemini, OpenAI)
- Model deployment and monitoring for production data products

**Business Intelligence & Visualization:**
- Power BI (expert): dashboards, DAX, modeling
- Hex (expert)L: notebooks, SQL + Python workflows
- Tableau (intermediate)
- MicroStrategy (intermediate)

***

## Education & Certifications

Education:
- Master's of Science in Data Science, *University of Texas at Austin*.
- Bachelor's of Science in Aerospace Engineering, *University of Texas at Austin*.

Certifications: 
- [Prefect Associate](https://www.credential.net/746691ba-73ab-4a31-8f1c-00b99c367f4e#acc.E4o6KFhL)

Master's Coursework:
- DSC 385T: Data Science for Health Discovery and Innovation
- [DSC 391L: Principles of Machine Learning](https://badgr.com/public/assertions/AaZGhwiEQb2M7Avle1g7NA)
- [DSC 394R: Reinforcement Learning](https://badgr.com/public/assertions/RsAzGD1BRwCPGyp5uxGAog)
- [CS 388: Natural Language Processing](https://courses.edx.org/certificates/f0460d4329844ae8bad4630c167969a7)
- [CS 394D: Deep Learning](https://courses.edx.org/certificates/9e77858ad5fe4406b561f31d68bd01e9)
- [CS 395T: Data Structures and Algorithms](https://courses.edx.org/certificates/9054a3d73f9d4002a9c07333808db655)
- [DSC 385: Data Exploration and Visualization](https://courses.edx.org/certificates/38a0239523b6453bb0d0e05cb0c60028)
- [DSC 383: Advanced Predictive Models for Complex Data](https://courses.edx.org/certificates/f7b5e6a0636a4048a230a638b0b4873f)
- [DSC 382: Foundations of Regression and Predictive Modeling](https://courses.edx.org/certificates/8d01dc49224e4745a9023a4f47d5166d)
- [DSC 381: Probability and Simulation-Based Inference](https://courses.edx.org/certificates/6e0bb056bd6f4d3a8982a1f392967eec)