import SqlInjectionIndetifier
import pandas as pd

df = pd.read_csv('dataNew.csv')


#df['SQLInjection'] = np.where(SqlInjectionIndetifier.detectRFI(df['Endpoint']), "SQLInjection", "NO")
print(df.info())
sqlInjRFI = []
sqliInj =[]
webShell =[]
xss =[]
for index, row in df.iterrows():
    sqlInjRFI.append(SqlInjectionIndetifier.detectRFI(row['Endpoint']))
    sqliInj.append(SqlInjectionIndetifier.detectSQLi(row['Endpoint']))
    webShell.append(SqlInjectionIndetifier.detectWebShell(row['Endpoint']))
    xss.append(SqlInjectionIndetifier.detectSXX(row['Endpoint']))


df['SqliInjection'] = sqliInj
df['Webshell'] = webShell
df['SQLInjectionRFI'] = sqlInjRFI
df['XSS'] = xss
print(df.info())
print(df.head())
df.to_csv(r'dataSqlInj.csv')

#df['SQLInjection'] = df.apply(lambda row: SqlInjectionIndetifier.detectRFI(row['Endpoint']))

