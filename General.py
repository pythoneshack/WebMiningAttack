import pandas as pd

# Read DataFrame
df = pd.read_csv("dataNew.csv")

# Convert Data Column to numeric/ Bytes to Gb
df["Data"] = pd.to_numeric(df.Data, errors='coerce')

df['Data'] = df['Data'].div(1000)
df['Data'] = df['Data'].div(1000)

# SECOND TASK
# Create status frequency error in status_freq\we need only 5xx error
status_freq = pd.DataFrame(columns=['Status', 'Frequency'])
status_freq['Frequency'] = df.groupby('Status').size()


status_freq['Status'] = df.groupby('Status').agg({'Status': lambda x: list(x).__getitem__(1)})
five_xx_error = status_freq[status_freq['Status'] >= 500].sum()


# FIRST TASK
freq_traffic = df.Endpoint.count()
data_traffic = df.Data.sum()

# THIRD TASK
ip_freq = df.groupby('Host').size().count()

print('Total Requests :' + str(freq_traffic))
print('Total Traffic :' + str(data_traffic))
#print('Freq / Status :' + str(status_freq))
print('Total Unique IPs :' + str(ip_freq))
print('Total 5xx Status :' + str(five_xx_error.Frequency))



