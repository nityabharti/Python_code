"""
are you satisfied with yourself?
can you do better?
Are you happy with good?
"""
import pandas as pd
df = pd.read_csv('train.csv')
print(df.head())

import folium
from folium import plugins

stationArr = df[['Y', 'X']].values

# plot heatmap
m = folium.Map(location=[stationArr[0][0],stationArr[0][1]], zoom_start=12)
m.add_child(plugins.HeatMap(stationArr[:50000], radius=15))
m.save('abc.html')