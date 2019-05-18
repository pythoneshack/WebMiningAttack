import SqlInjectionIndetifier
import pandas as pd


df = pd.read_csv('dataNew.csv')

xss = []
sqlInjRFI = []
sqliInj = []
webShell = []
for index, row in df.iterrows():
    xss.append(SqlInjectionIndetifier.detectSXX(row['Endpoint']))
    sqlInjRFI.append(SqlInjectionIndetifier.detectRFI(row['Endpoint']))
    sqliInj.append(SqlInjectionIndetifier.detectSQLi(row['Endpoint']))
    webShell.append(SqlInjectionIndetifier.detectWebShell(row['Endpoint']))

df['sqli_injection'] = sqliInj
df['Webshell'] = webShell
df['SQLInjectionRFI'] = sqlInjRFI
df['xss'] = xss

count_rows = len(df)
print(count_rows)

df.Date = pd.to_datetime(df.Date)
df['month'] = df.Date.apply(lambda x: x.month)
df['week'] = df.Date.apply(lambda x: x.week)
df['day'] = df.Date.apply(lambda x: x.day)
df['hour'] = df.Date.apply(lambda x: x.hour)

xss_number = len(df[df.xss==True])
sql_inj_number = len(df[df.sqli_injection==True])
df_pages = df[(df.sqli_injection==True) | (df.xss==True)]

count_attacks = len(df_pages)
print(count_attacks)
percentages = count_attacks/count_rows *100
print(percentages)


pages_count = df_pages.groupby('Endpoint').count()
print('Page Count :' + str(pages_count))
sorted_pages = pages_count.sort_values(['xss', 'sqli_injection'], ascending=[False, False]).head(5)

country_count = df_pages.groupby('Country').count()
sorted_countries = country_count.sort_values('xss', ascending=False).head(5)

hour_count = df_pages.groupby('hour').count()
sorted_hours = hour_count.sort_values('xss', ascending=False).head(5)

df.to_csv("SQl-XSS.csv")

print(sorted_pages)
print(sorted_countries)
print(sorted_hours)
print(xss_number)
print(sql_inj_number)

