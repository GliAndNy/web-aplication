import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output
import plotly.express as px

df = pd.read_csv('./pages/Houses.csv')

dash.register_page(__name__)


df = df.astype({'Neighborhood':'category', 'GarageType':'category', 'HouseStyle':'category',
                       'OverallQual':float, 'LotArea':float, 'SalePrice':float})
df_d = df.select_dtypes(include='float')
df_c = df.select_dtypes(include='category')

layout = html.Div([
    html.H1(children='This is our analytical graphs'),
    html.H2(children='Scatter Charts'),
    dcc.Graph(id='selected-graph'),
    "Select argument (X)",
    dcc.Dropdown(df_d.columns, df_d.columns[0], 
                placeholder="Argument selection", id='x1'),
    "Select function (Y)",
    dcc.Dropdown(df_d.columns, df_d.columns[0], 
                placeholder="Function selection", id='y'),
    "Select category",
    dcc.Dropdown(df_c.columns, df_c.columns[0], 
                placeholder="Category selection", id='c')
]), html.Div([
    html.H2(children='Histograms'),
    dcc.Graph(id='selected-graph1'),
    "Select argument (X)",
    dcc.Dropdown(df.columns, df.columns[0], 
                placeholder="Argument selection", id='x2')
]), html.Div([
    html.H2(children='Box Plots'),
    dcc.Graph(id='selected-graph2'),
    "Select argument (X)",
    dcc.Dropdown(df.columns, df.columns[0], 
                placeholder="Argument selection", id='x3'),
    "Select function (Y)",
    dcc.Dropdown(df.columns, df.columns[0], 
                placeholder="Function selection", id='y2')
]), html.Div([
    html.H2(children='Bar Charts'),
    dcc.Graph(id='selected-graph3'),
    "Select argument (X)",
    dcc.Dropdown(df_c.columns, df_c.columns[0], 
                placeholder="Argument selection", id='x4'),
    "Select function (Y)",
    dcc.Dropdown(df_d.columns, df_d.columns[0], 
                placeholder="Function selection", id='y3'),
        "Select category",
    dcc.Dropdown(df_c.columns, df_c.columns[0], 
                placeholder="Category selection", id='c2')
])



@callback(
    [Output('selected-graph', 'figure'), Output('selected-graph1', 'figure'), Output('selected-graph2', 'figure'), Output('selected-graph3', 'figure')],
    Input(component_id='x1', component_property='value'),
    Input(component_id='y', component_property='value'),
    Input(component_id='c', component_property='value'),
    Input(component_id='x2', component_property='value'),
    Input(component_id='x3', component_property='value'),
    Input(component_id='y2', component_property='value'),
    Input(component_id='y3', component_property='value'),
    Input(component_id='x4', component_property='value'),
    Input(component_id='c2', component_property='value')
    )
def update_figure_1(x1_name, y_name, c_name, x2_name, x3_name, y1_name, y2_name, x4_name, c2_name):
    fig = px.scatter(df, x=x1_name, y=y_name, color=c_name, log_x=False)
    fig.update_layout(transition_duration=500)
    fig1 = px.histogram(df, x=x2_name)
    fig1.update_layout(transition_duration=500)
    fig2 = px.box(df, x = x3_name, y = y1_name)
    fig2.update_layout(transition_duration=500)
    fig3 = px.bar(df, x = x4_name, y = y2_name, color = c2_name)
    fig3.update_layout(transition_duration=500)
    return fig, fig1, fig2, fig3
