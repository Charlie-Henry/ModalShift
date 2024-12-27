import pandas as pd
import geopandas
import matplotlib.pyplot as plt

MASS_SHOOTINGS = ["GALVESTON", "EL PASO", "MIDLAND", "ECTOR", "TARRANT", "UVALDE"]
MASS_SHOOTINGS_FRST_TERM = ["DENTON", "COLLIN", "DALLAS", "HARRIS"]

Counties = geopandas.read_file(
    "Texas_County_Boundaries_Detailed.geojson"
)
Counties["CNTY_NM"] = Counties["CNTY_NM"].str.upper()

data = pd.read_csv("abbott by county.csv")
vmin, vmax = -0.13, 0.13
Counties = Counties.merge(data, left_on="CNTY_NM", right_on="County")
Counties["D-shift"] = (Counties["2022"] - Counties["2018"]) * -1
# background is gray for counties with missing google data
ax = Counties.plot(color="gray", edgecolor="black", linewidths=0.0)

fig = Counties.plot(
    column="D-shift",
    ax=ax,
    cmap="RdBu",
    figsize=(10, 10),
    linewidth=0.25,
    edgecolor="black",
    vmin=vmin,
    vmax=vmax,
    legend=True,
    norm=plt.Normalize(vmin=vmin, vmax=vmax),
)

# remove axis of chart
fig.axis("off")

# add a title
csfont = {"fontname": "Courier New"}
plt.title("Partisan Shift Governor 2018 to 2022", **csfont)

# this will save the figure as a high-res png in the output path. you can also save as svg if you prefer.
chart = fig.get_figure()
chart.savefig("abbott.png", dpi=300)

print(data[data["County"].isin(MASS_SHOOTINGS)])