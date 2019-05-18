import folium
import pandas as pd
from folium.plugins import MarkerCluster


df = pd.read_csv('dataNew.csv')
SF_COORDINATES = (df['Latitude'].astype(float).mean(), df['Longitude'].astype(float).mean())

# for speed purposes


# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)

# add a marker for every record in the filtered data, use a clustered view
# for each in df.iterrows():
#     map.simple_marker(
#         location=[each[1]['Y'], each[1]['X']],
#         clustered_marker=True)
#
# display(map)


some_map = folium.Map(location=SF_COORDINATES, zoom_start = 12)

mc = MarkerCluster()

# creating a Marker for each point in df_sample. Each point will get a popup with their zip
for row in df.itertuples():
    mc.add_child(folium.Marker(location=[row.Latitude, row.Longitude],popup=row.Host))

some_map.add_child(mc)
some_map.save("Bubble-map.html")
