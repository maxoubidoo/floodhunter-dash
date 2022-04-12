# filename = 'dash-01.py'

#
# Imports================================================================================================
#

import plotly_express as px

import dash
from dash import dcc , html , dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import pandas as pd

from datetime import date

from PIL import Image

import json

import numpy as np

import init

import base64




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
    'background': '#111111',
    'text': '#7FDBFF'
}

#if __name__ == '__main__':

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


image_filename = 'FloodHunter.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())




app.layout = html.Div(style={'backgroundColor': colors['background']}, 
children=[

    #html.H1(children="FloodHunter", style={'textAlign': 'center', 'color': '#7FDBFF'}), #tittle

    html.Img(  src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'height':'100%'}) ,

    
    
    html.P(
        children="FLoodHunter visual reprsentation"
    ),    #subtittle


    html.Div( style={'textAlign': 'center','color': colors['text']},
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


    html.Div( style={'textAlign': 'center','color': colors['text']},
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
    ),

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
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }}}),

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
if __name__ == '__main__':
    app.run_server(debug=True) # app.run_server = local / app.run = server

