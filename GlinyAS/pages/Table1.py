import dash
from dash import html, dcc, dash_table, Input, Output, callback

import pandas as pd


dash.register_page(__name__)

path = './pages/Houses.csv'

df = pd.read_csv(path)

df = df.astype({'Neighborhood':'category', 'GarageType':'category',
                       'HouseStyle':'category',

                       'OverallQual':float, 'LotArea':float, 'SalePrice':float})


layout = html.Div([
    html.H1("Settings House"),
    html.H2("Tables with selection o Neighborhood & HouseStyle"),
    html.H3("Select Neighborhood"),
    dcc.Dropdown(df.Neighborhood.unique(), df.at[0, 'Neighborhood'],
                placeholder="Neighborhood selection", id='Neighborhood'),
    html.H3("Select HouseStyle"),
    dcc.Dropdown(df['HouseStyle'].unique(), df.at[0, 'HouseStyle'],
                placeholder="Level selection", id='ploe'),
    dash_table.DataTable(df.to_dict('records'), 
                  [{"name": i, "id": i} for i in df.columns], 
                  style_cell={'padding': '5px',
                              'textAlign': 'center'},
                  style_header={
                                'backgroundColor': 'pink',
                                'color': 'black',
                                'fontWeight': 'bold'},
                  style_table={'width': '1400px', 'height': '800px', 
                               'overflowY': 'auto'},
                  id='df')
], className="table-1")

@callback(
    Output('df', 'data'),
    Input('Neighborhood', 'value'),
    Input('ploe', 'value'))
def update_figure(Neighborhood, ploe):
    filt = (df['Neighborhood'] == Neighborhood) & (df['HouseStyle'] == ploe)
    table = df[filt].to_dict('records')
    return table
