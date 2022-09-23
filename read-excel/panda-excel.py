import sys
import pandas as pd

# Read Sheet 0
data = pd.read_excel(r"C:\Source\pyton\learn-pyton\read-excel\data\clients.xlsx",sheet_name=1)

df = pd.DataFrame(data, columns = ["Client","Name","Sex"])
print (df)

# Read Sheet 1
data = pd.read_excel(r"C:\Source\pyton\learn-pyton\read-excel\data\clients.xlsx",sheet_name=0)

df = pd.DataFrame(data, columns = ["Client","Name","Sex"])
print (df)

# Read Multiple Sheets

data = pd.read_excel(r"C:\Source\pyton\learn-pyton\read-excel\data\clients.xlsx", sheet_name=[0, 'Sheet2'])

print (data)