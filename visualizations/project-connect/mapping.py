import pandas as pd
import geopandas
import os

DATA_DIR = "F:\\elections\\"

dfs = []
for file in os.listdir(DATA_DIR):
    dfs.append(pd.read_excel(f"{DATA_DIR}\\{file}"))
df = pd.concat(dfs)
# df.to_parquet(f'{DATA_DIR}\\df.parquet.gzip',
#               compression='gzip')
df.to_pickle(f"{DATA_DIR}\\election_data_2020.pkl")

pvt = df.dropna(subset=["Proposition A City of Austin (FP) (2015)"])
pvt = pd.pivot_table(pvt,index="Precinct", columns=['President/Vice President'],values=['Cast Vote Record'],aggfunc="count")
pvt.columns = pvt.columns.map("_".join)
pvt.columns = pvt.columns.str.replace('Cast Vote Record_', '')
pvt = pvt.fillna(0)
pvt_2 = pd.pivot_table(df,index="Precinct", columns=['Proposition A City of Austin (FP) (2015)'],values=['Cast Vote Record'],aggfunc="count")
pvt_2.columns = pvt_2.columns.map("_".join)
pvt_2.columns = pvt_2.columns.str.replace('Cast Vote Record_', '')
pvt_2 = pvt_2.fillna(0)
pvt = pd.merge(pvt, pvt_2, on="Precinct")
pvt["count_votes_president"] = pvt['DEM Joseph R. Biden'] + pvt['GRE Howie Hawkins'] +pvt['LIB Jo Jorgensen'] + pvt['REP Donald J. Trump'] + pvt['Write-in']
pvt["count_votes_propA"] = pvt['Against'] + pvt['For']
pvt["Prop A %"] = pvt['For']/pvt["count_votes_propA"]
pvt["Biden %"] = pvt["DEM Joseph R. Biden"]/pvt["count_votes_president"]
pvt["prop A lag biden"] = (pvt["Prop A %"] - pvt["Biden %"])* 100
pvt["pct"] = pvt.index
pvt = pvt.reset_index()
pvt.index = pvt["pct"].str.replace('[^0-9]', '').astype(int)

precincts = geopandas.read_file('precincts-2020.geojson',index_col='pct')
coa_limits = geopandas.read_file("https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/BOUNDARIES_jurisdictions/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=")
coa_limits = coa_limits[coa_limits["JURISDICTION_LABEL"]=='AUSTIN FULL PURPOSE']
#from shapely.ops import unary_union
#merged_polygons = unary_union(coa_limits.geometry)
#merged_gdf = geopandas.GeoDataFrame(geometry=[merged_polygons])
#merged_gdf = merged_gdf.set_crs(epsg=4326)
#precincts["geometry"] = precincts.intersection(merged_gdf)
precincts = geopandas.overlay(precincts, coa_limits, how='intersection')
precincts.index = precincts["pct"]
pct_merge = precincts.merge(pvt, left_index=True, right_index=True,how='left')

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax = pct_merge.plot(column="prop A lag biden",figsize=(13, 10),legend=True, cmap="RdBu")
ax.tick_params(axis='both', length=0, labelsize=0)
plt.title("Biden Share Minus Project Connect Share", fontsize= 20)
plt.savefig("Prop A lag biden.png",dpi=500)


data = pd.read_csv('prop B for early.csv',index_col='pct')
# data = pd.read_csv('change in early vote Turnout.csv',index_col=('pct'))

pct_merge = precincts.merge(data, on='pct',how='left')

from geopandas import GeoSeries
from shapely.geometry import Polygon

# base = pct_merge.plot(color='white', edgecolor='black')
# markersize = pct_merge['Votes_Total']/25 + 1



pct_merge = pct_merge[(pct_merge.FOR != 0)]

base = pct_merge.plot(column='FOR',figsize=(13, 10),legend=True)

fig = polls.plot(ax=base, marker='o',color='none',markersize=1).get_figure()

fig.savefig("Prop B.png",dpi=500)

# markersize2 = (pct_merge['Active_Registered_Voters']-pct_merge['Votes_Total'])/25 + 1
# fig2 = centroids.plot(ax=base, marker='o', edgecolor='green',color='None', markersize=markersize2).get_figure()
# fig2.savefig("bubbles2.png",dpi=500)