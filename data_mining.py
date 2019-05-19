import SqlInjectionIndetifier
import pandas as pd
import pygal


df = pd.read_csv('dataNew.csv')

xss = []
sqlInjRFI = []
sqliInj = []
webShell = []
lost_fi = []
for index, row in df.iterrows():
    xss.append(SqlInjectionIndetifier.detectSXX(row['Endpoint']))
    sqlInjRFI.append(SqlInjectionIndetifier.detectRFI(row['Endpoint']))
    sqliInj.append(SqlInjectionIndetifier.detectSQLi(row['Endpoint']))
    # webShell.append(SqlInjectionIndetifier.detectWebShell(row['Endpoint']))
    # lost_fi.append(SqlInjectionIndetifier.detectLFI(row['Endpoint']))

df['sqli_injection'] = sqliInj
df['SQLInjectionRFI'] = sqlInjRFI
df['xss'] = xss

for x in df['Endpoint']:
    if str(x).__contains__('/etc/passwd'):
        lost_fi.append(True)
    else:
        lost_fi.append(False)

    if str(x).__contains__('cmd'):
        webShell.append(True)
    else:
        webShell.append(False)

df['lfi'] = lost_fi

df['Webshell'] = webShell

count_rows = len(df)
print(count_rows)

df.Date = pd.to_datetime(df.Date)
df['month'] = df.Date.apply(lambda x: x.month)
df['week'] = df.Date.apply(lambda x: x.week)
df['day'] = df.Date.apply(lambda x: x.day)
df['hour'] = df.Date.apply(lambda x: x.hour)

xss_number = len(df[df.xss==True])
webs = len(df[df.Webshell==True])
sql_inj_number = len(df[df.sqli_injection==True])
lfi = len(df[df.lfi == True])
rfi = len(df[df.SQLInjectionRFI == True])

df_pages = df[(df.sqli_injection==True) | (df.xss==True) | (df.Webshell == True) | (df.lfi == True)]

pages_count = df_pages.groupby('Endpoint').count()
print(pages_count)
sorted_pages = pages_count.sort_values(['xss', 'sqli_injection', 'lfi', 'Webshell'], ascending=[False, False, False, False]).head(5)

country_count = df_pages.groupby('Country').count()
sorted_countries = country_count.sort_values(['xss', 'sqli_injection', 'lfi', 'Webshell'], ascending=[False, False, False, False]).head(5)

hour_count = df_pages.groupby('hour').count()
sorted_hours = hour_count.sort_values('xss', ascending=False).head(5)



df.to_csv("SQl-XSS.csv")

print(sorted_pages)
print(sorted_countries)
print(sorted_hours)
print(xss_number)
print(sql_inj_number)
print(webs)
print(lfi)
count_attacks = (xss_number + sql_inj_number + webs + lfi)
normal_req = count_rows - count_attacks
print(count_attacks)
percentages = count_attacks/count_rows *100
print(percentages)

#Attacking pie plot
pie_chart = pygal.Pie()
pie_chart.title = 'Server Status (12.289% Attacked)'
pie_chart.add('Abnormal Requests', count_attacks)
pie_chart.add('Normal Requests', normal_req)
pie_chart.render_to_file("Normal_Abnormal.svg")

pie_chart = pygal.Pie()
pie_chart.title = 'Web Attack Percentage'
pie_chart.add('Cross-site Scripting', xss_number)
pie_chart.add('SQL Injection', sql_inj_number)
pie_chart.add('Web Shell', webs)
pie_chart.add('Local File Inclusion', lfi)
pie_chart.render_to_file("AttackPercentages.svg")



