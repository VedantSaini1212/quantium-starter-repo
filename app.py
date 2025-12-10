import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import csv
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df0, df1, df2])
df = df[df["product"] == "pink morsel"]
df['price'] = df['price'].str[1:].astype(float)
df["sales"] = df["quantity"] * df["quantity"]
df.drop(columns=["price", "quantity", "product"], axis=1, inplace=True)

df.to_csv("formatted.csv", index=False)

fig = px.line(df, x='date', y = 'sales')
fig.add_vline(x='2021-01-15', line_width=3, line_dash="dash", line_color="red")
app = Dash()
app.layout = html.Div(children=[
  html.H1(children='Line graph visualiser'),
  dcc.RadioItems(
                ['North', 'East', 'West', 'South', 'All'],
                'All',
                id='region',
                inline=True
            ),
  dcc.Graph(id="sales-graph")])

@callback(
Output('sales-graph', 'figure'),
Input('region', 'value'))

def update_graph(region):
  if region == 'All':
    fig = px.line(df, x='date', y = 'sales')
    fig.add_vline(x='2021-01-15', line_width=3, line_dash="dash", line_color="red")
  else:
    filtered = df[df['region'] == region.lower()]
    fig = px.line(filtered, x='date', y = 'sales')
    fig.add_vline(x='2021-01-15', line_width=3, line_dash="dash", line_color="red")

  return fig


app.run(debug=True)
