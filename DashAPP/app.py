
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from helper_data import match_options_week1
from helper_func import data_per_week, data_pie_per_match, bar_passRes_match
import dash_bootstrap_components as dbc

df_plays = pd.read_csv('dash_plays.csv')
#df_dash_week1 = pd.read_csv('matches_week1_pie.csv')
#df_pie = df_dash_week1.groupby(['matches', 'possessionTeam', 'passResult'])[['passResult']].count()
#df_pie = df_pie.add_suffix('_Count').reset_index()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


#.................................................HTML LAYOUT.............................................

# 1st row showing pass results of whole game with pie chart and then each team with barchart
app.layout = html.Div([ 
    #The 1st row is regarding the title of dashboard
    dbc.Row(dbc.Col(html.H3("NFL Big Data Bowl 2021"), width = {'size':6, 'offset': 3}),),
    #to create a drop down for picking the week number
    #it will be in the same row as graphs
    dbc.Row([
            dbc.Col(dcc.Dropdown( id = 'week_match', options = match_options_week1,
                                        value = '[PHI , ATL]', multi = False, clearable = False),
                                        width = { 'size': 2, 'offset': 1, 'order':2}), 
            
            dbc.Col(dcc.Graph( id = 'pie_match_pass_result' , figure ={}),
                    width= 6, lg = {'size': 4, 'offset': 0, 'order': 1}),

            dbc.Col(dcc.Graph( id = 'bar', figure={}),
            width = 6, lg={'size':4, 'offset': 1, 'order': 3}), ])
        

])


#.......................................................call back functions

@app.callback(
    Output(component_id = 'pie_match_pass_result', component_property= 'figure'),
    Output(component_id = 'bar', component_property= 'figure'),
    [Input(component_id='week_match', component_property='value')]
)
#define a function that can update the figure that is going to be shown as graph
def pie_match_pass_fig(week_match):
    week_match = week_match
    week1 = data_per_week(df_plays, 1)
    week1_pie = data_pie_per_match(week1)
    week1_bar = bar_passRes_match(week1, week_match)
    #df_new = df_pie.loc[df_pie['matches']== week_match]
    pasRes_pichart = px.pie(
    data_frame = week1_pie,  values= week_match, color = 'passResult',
 hole = 0.3)
    barchart_match = px.bar(
    data_frame = week1_bar,
    x = 'passResult', y = week_match,
    color = 'passResult', opacity = 0.9,
    orientation = 'v', facet_row = 'possessionTeam')
    return (pasRes_pichart, barchart_match)








#..........................................................................................
if __name__ =='__main__':
    app.run_server(debug=True)