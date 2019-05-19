import pandas as pd
import pygal

df = pd.read_csv("dataNew.csv")

host_freq = pd.DataFrame(columns=['Host', 'Frequency'])
host_freq['Frequency'] = df.groupby('Host').size()
host_freq['Host'] = df.groupby('Host').agg({'Host': lambda x: list(x).__getitem__(1)})

df_attack = pd.read_csv("SQl-XSS.csv")
df_pages = df_attack[(df_attack.sqli_injection == True) | (df_attack.xss == True)]

#malcious ip xss
df_most_malicious = pd.DataFrame(columns=['Host', 'Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell'])
df_most_malicious['Frequency_xss'] = df_attack[df_attack.xss == True].groupby('Host').size()
df_most_malicious['Frequency_sql'] = df_attack[df_attack.sqli_injection == True].groupby('Host').size()
df_most_malicious['Frequency_lfi'] = df_attack[df_attack.lfi == True].groupby('Host').size()
df_most_malicious['FrequencyWebshell'] = df_attack[df_attack.Webshell == True].groupby('Host').size()
df_most_malicious['Host'] = df_attack.groupby('Host').agg({'Host': lambda x: list(x).__getitem__(1)})
malcious_ip_xss = df_most_malicious.sort_values(['Frequency_xss', 'Frequency_sql'], ascending=[False, False])
sorted_malicious_ip= df_most_malicious.sort_values(['Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell'], ascending=[False, False, False, False]).head(5)


line_chart = pygal.HorizontalBar()
line_chart.title = 'Top 5 dangerous IP'
for index, row in sorted_malicious_ip.head(5).iterrows():
    line_chart.add(row['Host'], row['Frequency_xss'] + row['Frequency_sql']+row['Frequency_lfi']+row['FrequencyWebshell'])
line_chart.render_to_file("Top5ip.svg")



# #TOP 5 IP ATTACKED
df_top_attack = pd.DataFrame(columns=['Endpoint', 'Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell', 'Frequency'])
#EDW
df_attack = df_attack.applymap(lambda x: 1 if x == True else x)
df_attack = df_attack.applymap(lambda x: 0 if x == False else x)
df_top_attack['Endpoint'] = df_attack['Endpoint']

count = []
for index, row in df_attack.iterrows():
    count.append(row['xss'] + row['Webshell'] + row['sqli_injection'] + row['lfi'])
df_top_attack['Frequency'] = count

line_chart = pygal.HorizontalBar()
line_chart.title = 'Top 5 attacked endpoint'
df_new = pd.DataFrame({'count': df_top_attack.groupby('Endpoint').size()}).reset_index()
for index, row in df_new.sort_values('count', ascending=False).head(5).iterrows():
   line_chart.add(row['Endpoint'], row['count'])

line_chart.render_to_file("Top5endpoints.svg")


# TOP COUNTRIES ATTACKS
df_country = pd.DataFrame(columns=['Country', 'Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell', 'Frequency'])
df_country['Country'] = df_attack['Country']
count_ = []
for index, row_ in df_attack.iterrows():
    count_.append(row_['xss'] + row_['Webshell'] + row_['sqli_injection'] + row_['lfi'])
df_country['Frequency'] = count_

line_chart = pygal.HorizontalBar()
line_chart.title = 'Frequency of Country attacks'
df_new_ = pd.DataFrame({'count_': df_country.groupby('Country').size()}).reset_index()
for index, row_ in df_new_.sort_values('count_', ascending=False).iterrows():
   line_chart.add(row_['Country'], row_['count_'])

line_chart.render_to_file("TopCountries.svg")



