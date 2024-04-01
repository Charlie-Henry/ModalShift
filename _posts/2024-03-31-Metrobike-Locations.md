---
layout: post
title:  20 locations where we should expand MetroBike
excerpt_separator: <!--more-->
---

Using data to estimate good places for new MetroBike kiosk locations.

<!--more-->

*Disclaimer: This is a personal project of mine. Not an official project of CapMetro or the City of Austin*

Austin's docked bike share system received [$11.3 million from TxDOT last year](https://www.austintexas.gov/news/austins-metrobike-program-gets-113m-boost-txdot-grant) to help expand. I'm a big fan of the service, but like a lot of Austinites I no longer live near any of the kiosks. So I wanted to see what locations I could suggest using data.

## Methodology 

I ranked every census block group in the Austin region by four measures: transit, walkability, micromobility demand, and equity. Each census block group was ranked on these four measures and a better ranking transferred a higher score for the block group. I weighted the four measures as such: 35% for transit, 20% for walkability, 35% for micromobility, and 10% for equity. 

If you want to play with these weights and test different results, try my tool I created for this [here](https://app.hex.tech/85e3aa70-9c96-4e48-9c72-d7abe0c41315/app/a04d424f-65ee-4ba6-bccd-e65ac63b5e47/latest).

The code I wrote for this project is located in this [repo](https://github.com/Charlie-Henry/metrobike-expansion).

## Data Sources:

### Walkability

The Environmental Protection Agency (EPA) provides walkability estimates for census block groups: https://www.epa.gov/smartgrowth/smart-location-mapping#walkability

### Transit Access

The EPA also estimates transit access in meters by census block groups:
https://www.epa.gov/smartgrowth/smart-location-mapping#Trans45


### Micromobility Trips

The number of micromobility trips (dockless scooters/bicycles) started or ended in a census tract. Data is provided by the City of Austin:
https://data.austintexas.gov/d/7d8e-dm7r

### Equity

A vulnerability index based on several census tract-level fields. Provided by the City of Austin
https://austin.maps.arcgis.com/home/item.html?id=0a095a37ea8a4eb8b835a888f00ef53f


# Top 20 expansion locations

## 1. South Congress & Oltorf

![South Congress & Oltorf area map](images/metrobike-expansion/no_1_484530023081.png)

Why it makes sense:
- High frequency transit (route 801/1) 
- Close by existing kiosk @ Congress/Mary
- H-E-B

Two parks: 
- Blunn Creek Nature Preserve
- Big Stacy Neighborhood Park

## 2. Oltorf & Parker

![Oltorf & Parker area map](images/metrobike-expansion/no_2_484530023074.png)

Why it makes sense:
- High frequency transit (route 7) 
- Linder Elementary School
  
Parks: 
- Mabel Davis District Park

## 3. Bolm District

![Bolm district area map](images/metrobike-expansion/no_3_484530021113.png)

Why it makes sense:
- Near to eastside bus plaza kiosk
- Transit service (route 350)
- Eastside Memorial HS
  
Parks: 
- Govalle Neighborhood Park
- Bolm District Park
- Walnut Creek Trail
- East Boggy Creek Greenbelt

## 4. Rio Grande @ 24th + 5. Longview

*I combined 4 and 5 as they are neighbors to each other.*

![Rio grande area map](images/metrobike-expansion/no_4_484530006033.png)

![Longview area map](images/metrobike-expansion/no_5_484530006032.png)

Why it makes sense:
- Existing kiosks north and south
- Frequent transit service on Guadalupe and Lamar
- High existing demand
- Dense walkable area near UT
- Existing two-way protected bike lane 

Parks: 
- Pease Park
- Shoal Creek Greenbelt

## 6. Rosewood + 8. Govalle

*I combined 6 and 8 as they are neighbors to each other.*

![Rosewood area map](images/metrobike-expansion/no_6_484530008023.png)

![Govalle area map](images/metrobike-expansion/no_8_484530008011.png)

Why it makes sense:
- Eastside early college HS
- ACC Eastview
- Frequent transit service (route: 300)

Parks:
- Rosewood Neighborhood Park
- Boggy Creek Greenbelt
- Parque Zaragoza Neighborhood Park

## 7. Speedway & 31st

![Speedway area map](images/metrobike-expansion/no_7_484530005001.png)

Why it makes sense:
- High existing demand near UT
- Frequent transit service (route: 7, 656)

Parks:
- Adams-Hemphill Neighborhood Park


## 9, 11, 14. South Fifth

*I combined 9, 11, and 14 as they are neighbors.*

![south 5th area map 1](images/metrobike-expansion/no_9_484530013072.png)

![south 5th area map 2](images/metrobike-expansion/no_11_484530013052.png)

![south 5th area map 3](images/metrobike-expansion/no_14_484530013054.png)

Why it makes sense:
- High existing demand 
- Frequent Transit service (route: 105, 10)

Parks:
- South Austin Neighborhood Park
- Auditorium shores
- Nicholas Dawson Neighborhood Park

## 10 and 17. Holly

*I combined 10 and 17 as they are neighbors.*

![holly area map 1](images/metrobike-expansion/no_10_484530010001.png)

![holly area map 2](images/metrobike-expansion/no_17_484530010002.png)


Why it makes sense:
- High existing demand near downtown
- Transit service (322)

Parks:
- Festival Beach
- Town Lake

## 12 and 13. More of West Campus

*I combined 10 and 17 as they are neighbors.*


![west campus area map 1](images/metrobike-expansion/no_12_484530006041.png)

![west campus area map 2](images/metrobike-expansion/no_13_484530006034.png)

Why it makes sense:
- High existing demand
- High frequency transit on Guadalupe and Lamar
- Dense, walkable area near UT

Parks:
- Pease Park
- Shoal Creek Greenbelt

## 15. East MLK

![east mlk area map 1](images/metrobike-expansion/no_15_484530021091.png)


Why it makes sense:
- Transit routes (350, 18)

Parks:
- J.J. Seabrook Greenbelt

## 16. Highland

![highland area map 1](images/metrobike-expansion/no_16_484530015034.png)


Why it makes sense:
- Transit hub (red line, 7, 337)
- Walkable area 
- ACC Highland


## 18. MLK-Manor

![mlk manor area map 1](images/metrobike-expansion/no_18_484530004023.png)


Why it makes sense:
- Transit service (Red line, 18, 20)
- High walkability and existing demand near UT 

Parks:
- Disch-Falk Field (does this count?)


## 19. Riverside & Pleasant Valley

![riverside area map 1](images/metrobike-expansion/no_19_484530023181.png)


Why it makes sense:
- Transit service (20, 670, 671, 311)

Parks:
- Roy Guerrero Metropolitan Park

## 20. Georgian Acres

![georgian area map 1](images/metrobike-expansion/no_20_484530018061.png)


Why it makes sense:
- Transit service (801/1)

Parks:
- Georgian Acres Neighborhood Park


![all areas map](images/metrobike-expansion/all_areas.png)
