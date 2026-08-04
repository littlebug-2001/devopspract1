
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip")

asia = world[world["CONTINENT"] == "Asia"]

fig, ax = plt.subplots(figsize=(12, 10))
asia.plot(ax=ax, color="yellow", edgecolor="red")
ax.set_title("Map of Asia")
ax.set_axis_off()

plt.show()


