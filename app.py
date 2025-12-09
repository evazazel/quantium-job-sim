from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load data
df = pd.read_csv(r'D:\gradjobs\quantium\quantium-job-sim\cleaned_data\combined_cleaned_sales_data.csv')
df["date"] = pd.to_datetime(df["date"])

regions = sorted(df["region"].unique())

app.layout = html.Div(className="container", children=[
    html.H1("Sales data for Pink Morsels", className="title"),

    html.P("A cool dashboard to show the sales of Pink Morsels for Soul Foods.",
           className="subtitle"),

    dcc.RadioItems(
        id='region-selector',
        options=[{"label": r.title(), "value": r} for r in regions],
        value=regions[0],
        inline=True,
        className="radio-group"
    ),

    dcc.Graph(
        id='sales_date-graph',
        className="graph-card"
    )
])

@app.callback(
    Output('sales_date-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sale',
        title=f"{selected_region.title()} Region Sales",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Poppins, sans-serif")
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
