import pandas as pd
import pygal
# Read DataFrame
df = pd.read_csv("dataNew.csv")

# Convert Data Column to numeric/ Bytes to Gb
df["Data"] = pd.to_numeric(df.Data, errors='coerce')

df['Data'] = df['Data'].div(1000000000)

# SECOND TASK
# Create status frequency error in status_freq\we need only 5xx error
status_freq = pd.DataFrame(columns=['Status', 'Frequency'])
status_freq['Frequency'] = df.groupby('Status').size()


status_freq['Status'] = df.groupby('Status').agg({'Status': lambda x: list(x).__getitem__(1)})
five_xx_status = status_freq[status_freq['Status'] >= 500].sum()
two_xx_status = status_freq[status_freq['Status'] < 300].sum()
four_xx_status = status_freq[(status_freq['Status'] < 500) & (status_freq['Status'] >= 400)].sum()


#plot bar status
line_chart = pygal.HorizontalBar()
line_chart.title = 'Status count'
line_chart.add('2xx', two_xx_status['Frequency'])
line_chart.add('4xx', four_xx_status['Frequency'])
line_chart.add('5xx', five_xx_status['Frequency'])
# line_chart.render()
line_chart.render_to_file("BarStatus.svg")

# FIRST TASK
freq_traffic = df.Endpoint.count()
data_traffic = df.Data.sum()
print(data_traffic)

# THIRD TASK
ip_freq = df.groupby('Host').size().count()

#print('Total Requests :' + str(freq_traffic))
#print('Total Traffic :' + str(data_traffic))
#print('Freq / Status :' + str(status_freq))
#print('Total Unique IPs :' + str(ip_freq))
#print('Total 5xx Status :' + str(five_xx_status.Frequency))
print('2xx Status :' + str(two_xx_status))
print('4xx Status :' + str(four_xx_status))
print('5xx Status :' + str(five_xx_status))



