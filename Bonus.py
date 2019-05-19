import pandas as pd
import pygal

df = pd.read_csv("dataNew.csv")

host_freq = pd.DataFrame(columns=['Host', 'Frequency'])
host_freq['Frequency'] = df.groupby('Host').size()
host_freq['Host'] = df.groupby('Host').agg({'Host': lambda x: list(x).__getitem__(1)})

#print(host_freq.sort_values('Frequency', ascending=False))


df_attack = pd.read_csv("SQl-XSS.csv")
df_pages = df_attack[(df_attack.sqli_injection == True) | (df_attack.xss == True)]
# print(df_pages.sqli_injection)
# print(df_pages.xss)

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
# df_attack["xss"] = pd.to_numeric(df_attack.Data, errors='coerce')
# df_attack["Webshell"] = pd.to_numeric(df_attack.Data, errors='coerce')
# df_attack["sqli_injection"] = pd.to_numeric(df_attack.Data, errors='coerce')
# df_attack["lfi"] = pd.to_numeric(df_attack.Data, errors='coerce')
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

# df_top_attack['Frequency'] = df_top_attack.groupby('Endpoint')['Frequency'].count()
# print(df_top_attack)

# t_counter = 0
# f_counter = 0
# for x in df_top_attack['Frequency']:
#     if x == 0:
#         f_counter = f_counter + 1
#     else:
#         t_counter = t_counter + 1
#
# print('True :' + str(t_counter) + " False :"+ str(f_counter))
# x = sort_values(df_top_attack['Frequency'])
# df_top_attack['Frequency']= df_attack['xss'].size() + df_attack['sqli_injection'].size() + df_attack['lfi'].size() + df_attack['Webshell'].size()
# df_top_attack['Endpoint'] = df_attack['Endpoint']
# print(df_top_attack)

# df_top_attack['Frequency_sql'] = df_pages[df_attack.sqli_injection == 1].groupby('Endpoint').size()
# df_top_attack['Frequency_lfi'] = df_attack[df_attack.lfi == 1].groupby('Endpoint').size()
# df_top_attack['FrequencyWebshell'] = df_attack[df_attack.Webshell == 1].groupby('Endpoint').size()
#
# #df_top_attack['Endpoint'] = df_attack.groupby('Endpoint').agg({'Endpoint': lambda x: list(x).__getitem__(1)})
# attacked_endpoint = df_top_attack.sort_values(['Frequency_xss', 'Frequency_sql'], ascending=[False, False])
# print(df_top_attack.head())

#df_attack.to_csv("df_attack.csv")

# df_top_attack['Frequency_xss'] = df_pages.groupby('Endpoint')['xss' == True].count()
# print(df_top_attack.head())
# df_top_attack['Frequency_sql'] = df_pages[df_attack.sqli_injection == True].groupby('Endpoint').size()
# df_top_attack['Frequency_lfi'] = df_attack[df_attack.lfi == True].groupby('Endpoint').size()
# df_top_attack['FrequencyWebshell'] = df_attack[df_attack.Webshell == True].groupby('Endpoint').size()
#
# df_top_attack['Endpoint'] = df_attack.groupby('Endpoint').agg({'Endpoint': lambda x: list(x).__getitem__(1)})
# attacked_endpoint = df_top_attack.sort_values(['Frequency_xss', 'Frequency_sql'], ascending=[False, False])
# print(df_top_attack.head())
# sorted_attacked_endpoint = df_top_attack.sort_values(['Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell'], ascending=[False, False, False, False]).head(5)
# sort_xss_var = sort_values(xss_var)
# print(sql_var)
# print(lfi_var)
# print(webshell_var)


# line_chart = pygal.HorizontalBar()
# line_chart.title = 'Top 5 attacked Endpoints'
# for index, row in df_top_attack.iterrows():
#     sum = (row['Frequency_xss'] + row['Frequency_sql']+row['Frequency_lfi']+row['FrequencyWebshell'])
#     line_chart.add(row['Endpoint'], sum)
# line_chart.render_to_file("Top5Endpoint.svg")