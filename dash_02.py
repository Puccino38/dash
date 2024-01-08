import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

url = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'
skip_indices = [3349,4703,5878,8980]
df = pd.read_csv(url, sep=',', encoding='latin1',skiprows=skip_indices)

fig = px.bar(df.head(10), x='title', y='  num_pages', labels={'  num_pages': 'Number of Pages'}, title='Top 10 Books by Number of Pages')

# Building the Dash layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Ten Books'),
    dcc.Graph(
        id='books-graph',
        figure=fig
    ),
    html.Div([
        dcc.Dropdown(
            id='author-dropdown',
            options=[{'label': author, 'value': author} for author in df['authors'].unique()],
            placeholder='Select an author'
        ),
        dcc.Input(
            id='page-input',
            type='number',
            placeholder='Max number of pages'
        )
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
