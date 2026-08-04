import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")
print(world.head())
world.plot()
plt.title("World Map")
plt.show()




import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
world_asia = world[world.continent == "Asia"]
world_asia.plot(column='gdp_md_est',cmap='Reds', legend=True)
plt.title("GDP of Countries in Asia")
plt.show()


    
