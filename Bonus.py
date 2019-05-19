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
print(malcious_ip_xss)
print(sorted_malicious_ip)


line_chart = pygal.HorizontalBar()
line_chart.title = 'Top 5 dangerous IP'
for index, row in sorted_malicious_ip.head(5).iterrows():
    line_chart.add(row['Host'], row['Frequency_xss'] + row['Frequency_sql']+row['Frequency_lfi']+row['FrequencyWebshell'])
line_chart.render_to_file("Top5ip.svg")

# TOP 5 IP ATTACKED
# xss=[]
# sql=[]
# lfi=[]
# webshell=[]
# df_top_attack = pd.DataFrame(columns=['Endpoint', 'Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell','Frequency'])
# df_top_attack['Frequency_xss'] = df_attack[df_attack.xss == True].groupby('Endpoint').size()
# df_top_attack['Frequency_sql'] = df_attack[df_attack.sqli_injection == True].groupby('Endpoint').size()
# df_top_attack['Frequency_lfi'] = df_attack[df_attack.lfi == True].groupby('Endpoint').size()
# df_top_attack['FrequencyWebshell'] = df_attack[df_attack.Webshell == True].groupby('Endpoint').size()
# df_top_attack['Endpoint'] = df_attack.groupby('Endpoint').agg({'Endpoint': lambda x: list(x).__getitem__(1)})
# attacked_endpoint = df_top_attack.sort_values(['Frequency_xss', 'Frequency_sql'], ascending=[False, False])
# sorted_attacked_endpoint = df_top_attack.sort_values(['Frequency_xss', 'Frequency_sql', 'Frequency_lfi', 'FrequencyWebshell'], ascending=[False, False, False, False]).head(5)
# print(attacked_endpoint)
# print(sorted_attacked_endpoint)

# line_chart = pygal.HorizontalBar()
# line_chart.title = 'Top 5 attacked Endpoints'
# for index, row in sorted_attacked_endpoint.head(5).iterrows():
#     line_chart.add(row['Endpoint'], row['Frequency_xss'])
# line_chart.render_to_file("Top5ip.svg")
# #df_top_attack['FreqSqlInj'] = df_attack[df_attack]



#
# #malcious ip sqlInj
# df_most_sqlInj = pd.DataFrame(columns=['Host', 'Frequency'])
# df_most_sqlInj['Frequency'] = df_attack[df_attack.sqli_injection == True].groupby('Host').size()
# df_most_sqlInj['Host'] = df.groupby('Host').agg({'Host': lambda x: list(x).__getitem__(1)})
# malcious_ip_sqlInj = df_most_sqlInj.sort_values('Frequency', ascending=False)
# print(malcious_ip_sqlInj.info())
#
#
# #total_malcious = pd.DataFrame(columns=['Host', 'Frequency'])
# #total_malcious =
