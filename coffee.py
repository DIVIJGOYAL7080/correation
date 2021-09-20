import plotly_express as px
import pandas as pd
'''import csv
with open("C:/Users/DIVIJ/python/c106/tv.csv") as csv_file:
    df=csv.DictReader(csv_file)'''
df=pd.read_csv("coffee.csv")
fig=px.scatter(df,x="Coffeeinml",y="sleepinhours",color="week")
fig.show()