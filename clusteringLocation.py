import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('dataNew.csv')

df_location = pd.DataFrame(columns=["Latitude", "Longitude"])
df_location["Latitude"] = df["Latitude"]
df_location["Longitude"] = df["Longitude"]

km = KMeans(n_clusters=3).fit(df_location)
centroids = km.cluster_centers_
print(centroids)

plt.scatter(df['Latitude'], df['Longitude'], c=km.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
