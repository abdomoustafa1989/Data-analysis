import pandas as pd


ls=[1000,"3000","5000",7000,"9000"]
ls2=[2000,"4000","6000",None,"10000"]
ls3=[11000,"13000","15000",17000,"19000"]

df=pd.DataFrame([ls,ls2,ls3])

print(df)

print("\n")
#print(df.describe())
print(df.dropna())
