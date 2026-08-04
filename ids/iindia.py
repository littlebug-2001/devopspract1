import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip")

india = world[world["NAME"] == "India"]

fig, ax = plt.subplots(figsize=(12, 10))
india.plot(ax=ax, color="orange", edgecolor="green")
ax.set_title("Map of India")
ax.set_axis_off()

plt.show()
