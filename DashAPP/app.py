import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from iexfinance.stocks import get_historical_data
import plotly.graph_objs as go
from helper_data import options_list
from dash.dependencies import Input, Output, State


#df = get_historical_data('GE', start = strat, end=end, output_format= 'pandas')
#print(df.head())

#define my application
app = dash.Dash()

# define my html component
app.layout = html.Div(children = [  html.Div("NFL Offense Analytics", 
                                            style = {"color": "red",
                                                    "text-align": "center",
                                                    "border-style" : "dotted",
                                                    "background-color": "lightblue",
                                                    "display": "inline-block",
                                                    "width": "80%"}), 
                                    # to have a drop down on each college number of players and their role(off/Def)
                                    html.Div( children=[     
                                                            html.Div(dcc.Dropdown(id = 'team_roles', options = options_list, value = 'Offense'),
                                                            style = {   "color": "red",
                                                                        "text-align": "center",
                                                                        "border-style" : "dotted",
                                                                        "background-color": "lightblue",
                                                                        "display": "inline-block",
                                                                        "width": "80%"}),
                                                            html.Div(dcc.Graph(id = 'top_universities', figure = {data = [], layout = []}))
                                                                            ]),
                                    # to have a drop down on each role based on offene defense
                                    html.Div( children = [ html.Div(" Drop Button Off-Def"), 
                                                            html.Div("role of players")])

    
])



## creating callbacks
@app.callback ([
    output =(

    )
])




if __name__ =='__main__':
    app.run_server(debug=True) 