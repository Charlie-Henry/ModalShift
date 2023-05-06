import pandas as pd
import geopandas

FEATURE_DIR = "Travis_County_elections_results_may23.geojson"
AGOL_COA_LAYER = "https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/BOUNDARIES_jurisdictions/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token="


def get_election_map_coa():
    precincts = geopandas.read_file(FEATURE_DIR, index_col='pct')
    coa_limits = geopandas.read_file(AGOL_COA_LAYER)
    coa_limits = coa_limits[coa_limits["JURISDICTION_LABEL"] == 'AUSTIN FULL PURPOSE']
    precincts = geopandas.overlay(precincts, coa_limits, how='intersection')
    return precincts


def main():
    precincts = get_election_map_coa()
    precincts.to_file("election_pcts_coa.geojson", driver="GeoJSON")

main()
