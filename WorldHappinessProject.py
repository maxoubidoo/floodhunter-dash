# filename = 'dash-01.py'

#
# Imports================================================================================================
#

import plotly_express as px

import dash

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import pandas as pd

from datetime import date

from PIL import Image

import json

import numpy as np


#
# Data Treatment==========================================================================================
#

wh2015 = pd.read_csv ("./2015.csv")
wh2016 = pd.read_csv ("./2016.csv")
wh2017 = pd.read_csv ("./2017.csv")
wh2018 = pd.read_csv ("./2018.csv")
wh2019 = pd.read_csv ("./2019.csv")
wh2020 = pd.read_csv ("./2020.csv")


#Renaming to have common names
wh2017.rename(columns={'Happiness.Rank': 'Happiness Rank', 'Happiness.Score': 'Happiness Score',
                        "Economy..GDP.per.Capita." : "Economy (GDP per Capita)","Health..Life.Expectancy.":"Health (Life Expectancy)",
                        "Trust..Government.Corruption.":"Trust (Government Corruption)", "Dystopia.Residual" : "Dystopia Residual"}, inplace=True)

wh2018.rename(columns={ "Overall rank" : "Happiness Rank" ,  "Country or region" : "Country" , "Score" : "Happiness Score",
                        "GDP per capita" : "Economy (GDP per Capita)", "Healthy life expectancy" : "Health (Life Expectancy)",
                        "Freedom to make life choices" : "Freedom", "Perceptions of corruption" : "Trust (Government Corruption)",
                        "Social support" : "Family" }, inplace=True)

wh2019.rename(columns={ "Overall rank" : "Happiness Rank" ,  "Country or region" : "Country" , "Score" : "Happiness Score",
                        "GDP per capita" : "Economy (GDP per Capita)", "Healthy life expectancy" : "Health (Life Expectancy)",
                        "Freedom to make life choices" : "Freedom", "Perceptions of corruption" : "Trust (Government Corruption)",
                        "Social support" : "Family" }, inplace=True)

wh2020.rename(columns={ "Country name" : "Country", "Regional indicator" : "Region", "Ladder score" : "Happiness Score",
                         "Freedom to make life choices" : "Freedom","Logged GDP per capita" : "Economy (GDP per Capita)", 
                         "Healthy life expectancy" : "Health (Life Expectancy)", "Perceptions of corruption" : "Trust (Government Corruption)",
                         "Social support" : "Family", "Dystopia + residual" : "Dystopia Residual"},inplace=True)


#
#Function definition================================================================================================
#

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


try:
    img = np.array(Image.open(f"plouf.jpg"))              #f"assets/{input}"))
except OSError:
    raise PreventUpdate

fig = px.imshow(img, color_continuous_scale="gray")
fig.update_layout(coloraxis_showscale=False)
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

#
# Main================================================================================================
#

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


if __name__ == '__main__':

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets) # (3)


    app.layout = html.Div(
    children=[

        html.H1(children="FloodHunter", style={'textAlign': 'center', 'color': '#7FDBFF'}), #tittle
        
        html.P(
            children="FLowHunter visual reprsentation"
        ),    #subtittle


        html.Div(
            className="row",
            children=[ 

                html.Label('Start'),

                dcc.DatePickerSingle(
                    id='Date_Start',
                    min_date_allowed=date(2000, 1, 1),
                    max_date_allowed=date(2030, 12, 12),
                    initial_visible_month=date(2008, 1, 1),
                    display_format='D/M/Y' ,
                    date=date(2008, 1, 1)
                ),

                html.Div(id='output_Date_Start'),

                html.Label('End'),

                dcc.DatePickerSingle(
                    id='Date_End',
                    min_date_allowed=date(2000, 1, 1),
                    max_date_allowed=date(2030, 12, 12),
                    initial_visible_month=date(2018, 1, 1),
                    display_format='D/M/Y' ,
                    date=date(2018, 1, 1)
                ),

                html.Div(id='output_Date_End'),

            ],
        ),

        #html.Label('Source'),

        # dcc.Checklist(
        #     id = "Drop_Source",
        #     options=[
        #     {'label': 'NOTREAPPLI', 'value': '???'},
        #     {'label': 'Twitter', 'value': 'Twitter'},
        #     {'label': 'Tik Tok', 'value': 'TikTok'},
        #     {'label': 'Facebook', 'value': 'Facebook'}
        #     ],
        #     value=['???', 'Twitter' , 'TikTok', 'Facebook'],
        #     labelStyle={'display': 'inline-block'}
        # ),#CheckList 

        #html.Div(id='Drop_Source_output'),#Confirmation du menu déroulant

        dcc.Graph(id='graph1'), #bubble map

        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),

        dcc.Graph(id='image', figure = fig), #bubble map



])


#
#Interactions ================================================================================================
#


    @app.callback(
    Output('click-data', 'children'),
    Input('graph1', 'clickData'))
    def display_click_data(clickData):
        return json.dumps(clickData, indent=2)


    @app.callback(
    #Output(component_id='Drop_Source_output',component_property='children'),
    Output("graph1" , "figure"),
    Output('output_Date_Start', 'children'),
    Output('output_Date_End', 'children'),
    
    Input('Date_Start', 'date') ,
    Input('Date_End', 'date'),
    #Input('Drop_Source', 'value'),
    
    ) #Elements interactifs


    def update_output_div(Date_Start, Date_End): # ,  Drop_Source):


        data = wh2015

        datageo = pd.DataFrame()

        datageo = data.copy()

        datageo["Happiness Score"] = datageo['Happiness Score'].apply(lambda x: x**3)


        # graph1 = px.scatter_geo(datageo, locations="Country", color="Region",locationmode="country names",
        #         hover_name="Country", size="Happiness Score",
        #         projection="natural earth")

        # graph1.update_layout(
        #     geo = dict(
        #         showland = True,
        #         landcolor = "rgb(212, 212, 212)",
        #         showsubunits = True,
        #         subunitcolor = "rgb(000, 255, 000)",
        #         showcountries = True,                
        #         countrycolor = "rgb(255, 255, 255)",
        #         showlakes = True,
        #         lakecolor = "rgb(000, 000, 255)",
        #         showrivers=True,
        #         rivercolor="Blue" , 
        #         #resolution=50,

                
        #     )
        #     )

        datageo = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

        graph1 = px.scatter_mapbox(datageo, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=1, height=800)

        graph1.update_layout(
            clickmode='event+select',
            mapbox_style="open-street-map",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSHydroCached/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])

        #graph1.update_traces(marker_size=15)   

        # graph1.add_layout_image(
        # dict(
        #     source=Image.open(f"plouf.jpg"),
        #     xref= "x" ,
        #     yref= "y" ,
        #     xanchor="center",
        #     yanchor="middle",
        #     x= 10 ,
        #     y= 10 ,
        #     sizex= 50 ,
        #     sizey= 50 ,
        #     sizing="contain",
        #     opacity=0.8,
        #     layer="above"
        # )),

        try:
            img = np.array(Image.open(f"plouf.jpg"))              #f"assets/{input}"))
        except OSError:
            raise PreventUpdate

        fig = px.imshow(img, color_continuous_scale="gray")
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)



        string_prefix = 'You have selected: '

        if Date_Start is not None:
            date_object = date.fromisoformat(Date_Start)
            date_string = date_object.strftime('%B %d, %Y')
            output_Date_Start =  string_prefix + date_string

        if Date_End is not None:
                    date_object = date.fromisoformat(Date_End)
                    date_string = date_object.strftime('%B %d, %Y')
                    output_Date_End =  string_prefix + date_string

        #Drop_Source_output =     Drop_Source       


        return     graph1 , output_Date_Start , output_Date_End #Drop_Source_output,


    #
    # RUN APP================================================================================================
    #

    app.run_server(debug=True) # (8)

