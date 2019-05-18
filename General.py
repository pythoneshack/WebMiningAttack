import pandas as pd
df = pd.read_csv("datah")


#Convert Data Column to numeric/ Bytes to Gb
df["Data"] = pd.to_numeric(df.Data, errors='coerce')

df['Data'] = df['Data'].div(1000)
df['Data'] = df['Data'].div(1000)


#SECOND TASK
#Create status frequency error in status_freq\we need only 5xx error
status_freq = (df.groupby('Status').size())


#FIRST TASK
freq_traffic = df.Endpoint.count()
data_traffic = df.Data.sum()

#THIRD TASK
ip_freq = df.groupby('Host').size().count()


print(freq_traffic)
print(data_traffic)
print(status_freq)
print(ip_freq)