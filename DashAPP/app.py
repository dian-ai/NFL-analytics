import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from helper_data import match_options_week1


df_plays = pd.read_csv('dash_plays.csv')
df_dash_week1 = pd.read_csv('matches_week1_pie.csv')
#df_pie = df_dash_week1.groupby(['matches', 'possessionTeam', 'passResult'])[['passResult']].count()
#df_pie = df_pie.add_suffix('_Count').reset_index()

app = dash.Dash(__name__)


#.................................................HTML LAYOUT.............................................

# 1st row showing pass results of whole game with pie chart and then each team with barchart
app.layout = html.Div(children = [ 
    #to create a drop down for picking the week number
    html.Div([
        html.Label([' Match analysis']), 
                                    dcc.Dropdown(
                                        id = 'week_match',
                                        options = match_options_week1,
                                        value = '[PHI , ATL]',
                                        multi = False,
                                        clearable = False,
                                        style = {'width': '50%'}
                                    )

]), 
# bellow the drop down of week number present the graph of pass result for the selected match
html.Div([
    dcc.Graph(
        id = 'pie_match_pass_result'
    )
]),

])


#.......................................................call back functions

@app.callback(
    Output(component_id = 'pie_match_pass_result', component_property= 'figure'),
    [Input(component_id='week_match', component_property='value')]
)
#define a function that can update the figure that is going to be shown as graph
def pie_match_pass_fig(week_match):

    #df_new = df_pie.loc[df_pie['matches']== week_match]
    pasRes_pichart = px.pie(
    data_frame = df_dash_week1,  values= week_match, color = 'passResult',
 hole = 0.3)

    return (pasRes_pichart)








#..........................................................................................
if __name__ =='__main__':
    app.run_server(debug=True) 