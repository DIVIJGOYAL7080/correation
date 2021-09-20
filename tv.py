import plotly_express as px
import pandas as pd

df=pd.read_csv("tv.csv")
fig=px.scatter(df,x="SizeofTV",y="TimeSpent ")
fig.show()