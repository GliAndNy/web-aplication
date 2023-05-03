import dash
from dash import html, dcc, dash_table, Input, Output, callback
import pandas as pd

dash.register_page(__name__, path='/')
df = pd.read_csv('./pages/Houses.csv')

layout = html.Div(children=[
    html.H1(children='This is our dataset - "Houses"'),

    html.Div(children='''
        This is our initial Datset: you can use some filters.
    '''),
    html.Div([

                   dash_table.DataTable(id='table',
                                        data=df.to_dict('records'),
                                        columns=[{'name': i, 'id': i, 'deletable': True, 'selectable': True}
                                        for i in df.columns],
                                        filter_action='native',
                                        filter_options={'placeholder_text': 'Filter column...'},
                                        row_selectable='multi',
                                        row_deletable=True,
                                        style_table={'width': '1200px', 'height': '800px', 
                                        'overflowY': 'auto'},
                                        column_selectable='multi',
                                        style_header={'textAlign':'center'},
                                        page_size=1000,
                                        style_cell={'padding': '5px',
                                        'textAlign': 'center'}
                                        )
                ],
                    style={'margin-left': '80px',
                           'margin-right': '80px'})

]),