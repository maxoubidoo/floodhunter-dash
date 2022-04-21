#
# Imports================================================================================================
#

import plotly_express as px
import pandas as pd
import numpy as np

import dash
from dash import dcc , html , dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from datetime import date
from PIL import Image
import json
import base64


import init

import pymongo
from pymongo import MongoClient

#
# Recuperation/Traitement des données================================================================================================
#


client = pymongo.MongoClient("mongodb+srv://Maxoubioo:FloodHunter@floodhunter.bl1w5.mongodb.net/FloodHunter?retryWrites=true&w=majority")


db = client.FloodHunter
collection = db['Submits'] 


#
# Main================================================================================================
#

wh2015 , fig , styles = init.setup()

external_stylesheets = [
    './style.css',
    {
        'href': './style.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


colors = {
    'background': '#ffffff',
    'text': '#111111'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 


axis_template = {
    "showbackground": True,
    "backgroundcolor": "#141414",
    "gridcolor": "rgb(255, 255, 255)",
    "zerolinecolor": "rgb(255, 255, 255)",
}

plot_layout = {
    "title": "",
    "margin": {"t": 0, "b": 0, "l": 0, "r": 0},
    "font": {"size": 12, "color": "white"},
    "showlegend": False,
    "plot_bgcolor": "#141414",
    "paper_bgcolor": "#141414",
    "scene": {
        "xaxis": axis_template,
        "yaxis": axis_template,
        "zaxis": axis_template,
        "aspectratio": {"x": 1, "y": 1.2, "z": 1},
        "camera": {"eye": {"x": 1.25, "y": 1.25, "z": 1.25}},
        "annotations": [],
    },
}

server = app.server


image_filename = 'FloodHunterN.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())




app.layout = html.Div(style={'backgroundColor': colors['background']}, 
children=[

    html.Div(style={'backgroundColor': '#ffffff'}, children=[
        html.Div([
        html.Img(  src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'height': '40%', 'width': '40%', }) ,
        ], style={'textAlign': 'center'}),


        html.Div( style={'textAlign': 'left','color': colors['text'], 'width': '49%', 'display': 'inline-block', 'textAlign': 'center'},
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
            ],
        ),


        html.Div( style={'textAlign': 'left','color': colors['text'],'width': '49%', 'display': 'inline-block', 'textAlign': 'center' },
            children=[ 
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
        ),],),

    #html.Label('Source'),

    # dcc.Checklist(
    #     id = "Drop_Source",
    #     options=[
    #     {'label': 'FloodHunter', 'value': 'FloodHunter'},
    #     {'label': 'Twitter', 'value': 'Twitter'},
    #     {'label': 'Tik Tok', 'value': 'TikTok'},
    #     {'label': 'Facebook', 'value': 'Facebook'}
    #     ],
    #     value=['FloodHunter', 'Twitter' , 'TikTok', 'Facebook'],
    #     labelStyle={'display': 'inline-block'}
    # ),#CheckList 

    #html.Div(id='Drop_Source_output'),#Confirmation du menu déroulant

    dcc.Graph(id='graph1',figure={'layout': {
                "showbackground": True,
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']}
                }}),

    html.Div([
        dcc.Markdown("""
            **Click Data**

            Click on points in the graph.
        """),
        html.Pre(id='click-data', style=styles['pre']),
    ], className='three columns'),

    dcc.Graph(id='image', figure = fig), 



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

) #Elements interactifs


def update_output_div(Date_Start, Date_End): # ,  Drop_Source):


    data = init.read_mongo(collection)

    graph1 = px.scatter_mapbox(data, lat="Latitude", lon="Longitude", hover_name="Date", hover_data=["Username"],
                    color_discrete_sequence=["fuchsia"], zoom=1, height=800 )

    # datageo = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

    # graph1 = px.scatter_mapbox(datageo, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
    #                 color_discrete_sequence=["fuchsia"], zoom=1, height=800)

    graph1.update_layout(
        clickmode='event+select',
        mapbox_style="open-street-map",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSHydroCached/MapServer/tile/{z}/{y}/{x}"
                ]}],
        paper_bgcolor='rgba(23,61,124,255)',
        plot_bgcolor='rgba(23,61,124,255)'
        )



    try:
        img = np.array(Image.open(f"plouf2.JPG"))              #f"assets/{input}"))
    except OSError:
        raise PreventUpdate

    fig = px.imshow(img, color_continuous_scale="gray")
    fig.update_layout(coloraxis_showscale=False, paper_bgcolor='rgba(23,61,124,255)',plot_bgcolor='rgba(23,61,124,255)')
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
if __name__ == '__main__':
    app.run_server(debug=True) # app.run_server = local / app.run = server

