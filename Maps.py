import folium
from folium.plugins import HeatMapWithTime
from folium import CircleMarker
import pandas as pd
import sys

sys.setrecursionlimit(10000)
df = pd.read_csv('dataNew.csv')
dfN = df.drop(df[df.Latitude == 'UNKNOWN'].index)
folium_map = folium.Map(location=[dfN['Latitude'].astype(float).mean(), dfN['Longitude'].astype(float).mean()],
                        zoom_start=2.1,
                        tiles="CartoDB dark_matter")
dfP = dfN.groupby(['Latitude', 'Longitude']).last().reset_index()
for index, row in dfP.iterrows():
    marker = folium.CircleMarker(location=[row.Latitude, row.Longitude], radius=6, popup=row.Host)
    folium.PolyLine(locations=[(float(row.Latitude), float(row.Longitude)), (41.074864, 23.555059)],
                    line_opacity=0.5).add_to(folium_map)
    marker.add_to(folium_map)
folium_map.save("my_map.html")

heat_map = folium.Map(location=[dfN['Latitude'].astype(float).mean(), dfN['Longitude'].astype(float).mean()],
                      zoom_start=2.1,
                      tiles="CartoDB dark_matter")

df.Date = pd.to_datetime(df.Date)
df['month'] = df.Date.apply(lambda x: x.month)
df['week'] = df.Date.apply(lambda x: x.week)
df['day'] = df.Date.apply(lambda x: x.day)
df['hour'] = df.Date.apply(lambda x: x.hour)
df['minutes'] = df.Date.dt.minute
df['seconds'] = df.Date.dt.second

folium_map = folium.Map(location=[dfN['Latitude'].astype(float).mean(), dfN['Longitude'].astype(float).mean()],
                        zoom_start=2.1,
                        tiles="CartoDB dark_matter")
for index, row in dfP.iterrows():
    marker = folium.CircleMarker(location=[float(row.Latitude), float(row.Longitude)],radius=5,
                        color="#0A8A9F",
                        fill=True, popup=row["Host"])
    marker.add_to(folium_map)
folium_map.save("my_map.html")
print(df.seconds)

df_five = df[df.hour == 5]

df_hour_list = []
for minute in df_five.minutes.sort_values().unique():
    df_hour_list.append(df.loc[df.minutes == minute, ['Latitude', 'Longitude']].groupby(
        ['Latitude', 'Longitude']).sum().reset_index().values.tolist())

print(df_hour_list)
HeatMapWithTime(df_hour_list, radius=8, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}, min_opacity=0.5,
                max_opacity=0.8, use_local_extrema=True).add_to(heat_map)
heat_map.save("my_mapHeat.html")
