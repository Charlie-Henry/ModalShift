import pandas as pd
import geopandas as gpd


precincts = gpd.read_file('election_pcts_coa.geojson',index_col='pct')
precincts.set_index("PCTCODE")
data = pd.read_csv('mayor-runoff.csv',index_col='pct')
pct_merge = precincts.merge(data, left_index=True, right_index=True,how='left')

pct_merge["A_for_pct"] = pct_merge["A-For"]/pct_merge["A-Total"]
pct_merge["A_against_pct"] = pct_merge["A-Against"]/pct_merge["A-Total"]
pct_merge["B_for_pct"] = pct_merge["B-For"]/pct_merge["B-Total"]
pct_merge["B_against_pct"] = pct_merge["B-Against"]/pct_merge["B-Total"]

pct_merge.to_file("may-23-election.geojson", driver="GeoJSON")