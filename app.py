from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('D:\gradjobs\quantium\quantium-job-sim\cleaned_data\combined_cleaned_sales_data.csv')

fig = px.line(df, x='date',y='sale')

app.layout = html.Div(children=[
    html.H1(children='Sales data for Pink Morsels'),

    html.Div(children='''
             A cool dashboard to show the sales of Pink Morsels for Soul Foods.
             '''),

             dcc.Graph(
                 id='sales_date-graph',
                 figure=fig
             )
])

if __name__ == '__main__':
    app.run(debug=True)