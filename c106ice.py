import plotly_express as px
import pandas as pd
'''import csv
with open("C:/Users/DIVIJ/python/c106/tv.csv") as csv_file:
    df=csv.DictReader(csv_file)'''
df=pd.read_csv("icecream.csv")
fig=px.scatter(df,x="Temperature",y="Ice-creamSales")
fig.show()
