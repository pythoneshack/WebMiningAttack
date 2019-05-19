import pandas as pd
import pygal
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_csv('SQl-XSS.csv')

df_cluster = pd.DataFrame(columns =['Frequency', 'Data', 'Ip'])
df_cluster['Frequency'] = df[df['hour'] == 5].groupby('Host').size()
df_cluster['Ip'] = df[df['hour'] == 5].groupby('Host').agg({'Host': lambda x: list(x).__getitem__(1)})
df_cluster['Data'] = df[df['hour'] == 5].groupby('Host')['Data'].sum()

print(df_cluster)

# Anomaly Detecth with k means in time range 5 to 6



# Plot Clustering and labeling IP
xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Clusters'

sse = []
for x in range(2,20):
    kmeans = KMeans(n_clusters=x).fit(df_cluster[['Frequency', 'Data']])
    sse.append(kmeans.inertia_)
    centroids = kmeans.cluster_centers_
print(sse)
plt.plot(sse)
plt.show()

# plt.scatter(df_cluster['Frequency'], df_cluster['Data'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
# for index, row in df_cluster.iterrows():
#     plt.annotate(row['Ip'], (row['Frequency'],row['Data']))
# plt.show()
# plt.savefig('AnomalyDetction.png')
#print(df_cluster)