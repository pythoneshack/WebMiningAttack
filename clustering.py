from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataNew.csv')

dfClusters = df.groupby('Host').nunique()

kmeans = KMeans(n_clusters=3).fit(dfClusters)

centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
# plt.scatter(df[''], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)