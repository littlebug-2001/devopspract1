import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)


asia = world[world["CONTINENT"] == "Asia"]

highlight_countries = {
    "India": "orange",
    "Japan": "red",
    "China": "green",
    "Thailand": "purple",
    "South Korea": "cyan",
    
}


fig, ax = plt.subplots(figsize=(15, 10))

asia.plot(ax=ax, color="lightgray", edgecolor="white", linewidth=0.5)

for country, color in highlight_countries.items():
    country_gdf = asia[asia["NAME"] == country]
    country_gdf.plot(ax=ax, color=color, edgecolor="black", linewidth=0.7)


ax.set_title("Highlighted Countries in Asia", fontsize=16)
ax.set_axis_off()

plt.show()
