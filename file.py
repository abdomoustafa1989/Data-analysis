import pandas as pd


data=pd.read_csv("the data-csv.csv"  )

data.insert(0,"test",1)

print(data)


data.to_excel("the data-new.xlsx")
