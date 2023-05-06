import pandas as pd
import geopandas as gpd


precincts = gpd.read_file('Travis_County_elections_results_may23.geojson',index_col='pct')
data = pd.read_csv('mayor-runoff.csv',index_col='pct')
pct_merge = precincts.merge(data, left_index=True, right_index=True,how='left')

pct_merge["for_pct"] = pct_merge["For"]/pct_merge["Total"]
pct_merge["against_pct"] = pct_merge["Against"]/pct_merge["Total"]

pct_merge.to_file("may-23-election.geojson", driver="GeoJSON")