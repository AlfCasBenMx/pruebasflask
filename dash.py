import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Create a sample data frame
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
})

# Create the line chart using Plotly Express
fig = px.line(df, x="x", y="y")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children="My Simple Dash App"),
    dcc.Graph(
        id="my-line-chart",
        figure=fig
    )
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
