import pygal
import pandas as pd
from datetime import time

df = pd.read_csv("dataNew.csv")
df["Data"] = pd.to_numeric(df.Data, errors='coerce')

df.Date = pd.to_datetime(df.Date)
df['year'] = df.Date.apply(lambda x: x.year)
df['month'] = df.Date.apply(lambda x: x.month)
df['week'] = df.Date.apply(lambda x: x.week)
df['day'] = df.Date.apply(lambda x: x.day)
df['hour'] = df.Date.apply(lambda x: x.hour)
df['minute'] = df.Date.apply(lambda x: x.minute)
df['second'] = df.Date.apply(lambda x: x.second)

# Data Kb to Mb
df['Data'] = df['Data'].div(1000)
df['Data'] = df['Data'].div(1000)

df_new = pd.DataFrame(columns=['Frequency', 'Data', 'hour', 'minute', 'second'])


df_new['Frequency'] = df.groupby('hour').size()
df_new['hour'] = df.groupby('hour').agg({'hour': lambda x: list(x).__getitem__(1)})

# Request Per Hour
dateline = pygal.TimeLine(x_label_rotation=25)
dates = []
for index, row in df_new.iterrows():
    dates.append((time(row['hour']), row['Frequency']))
dateline.add("Requests", dates)
dateline.render()
dateline.render_to_file("TimeSeriesRequests.svg")

df_new['Data'] = df.groupby('hour')['Data'].sum()

# Data Per Hour
dateline = pygal.TimeLine(x_label_rotation=25)
_dates_ = []
for _index_, _row_ in df_new.iterrows():
    _dates_.append((time(_row_['hour']), _row_['Data']))
dateline.add("Data (GB)", _dates_)
dateline.render()
dateline.render_to_file("TimeSeriesData.svg")



print(df_new)

# Plot


# PIE PLOT

df_country = pd.DataFrame(columns=['Country', 'Frequency'])
df_country['Frequency'] = df.groupby('Country').size()
df_country['Country'] = df.groupby('Country').agg({'Country': lambda x: list(x).__getitem__(1)})

pie_chart = pygal.Pie()
pie_chart.title = 'Total Requests Per Country (Gigabytes)'
print(df_country)
for index, row in df_country.iterrows():
    pie_chart.add(row['Country'], row['Frequency'])

pie_chart.render()
pie_chart.render_to_file("PiePlot.svg")



















