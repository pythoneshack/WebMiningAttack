import pandas as pd
import geoip2.database

fn = r'data/dataAgg'
cols = ['Host','l','userid','Date','tz','Endpoint','Status','Data','referer','useragent']
reader = geoip2.database.Reader('GeoLite2-City.mmdb')
df = pd.read_csv(fn, delim_whitespace=True, names=cols).drop('l', 1)
# response = reader.city(df.host)


df['Date'] = df['Date'].map(lambda x: x.lstrip('[').rstrip(''))
df['Date'] = df['Date'].map(lambda x: x.replace(":", " ",1))

# df['Date'] = df['Date'].replace("[", "")
# df['Date'] = df['Date'].replace(":", " ", 1)
countries = []
latitude = []
longitude = []
for x in df['Host']:
    response = reader.city(x)
    countries.append(response.country.name)
    latitude.append(response.location.latitude)
    longitude.append(response.location.longitude)
df['Country'] = countries
df['Latitude'] = latitude
df['Longitude'] = longitude
print(df.head())
df.to_csv(r'dataNew.csv')
