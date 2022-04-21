import pandas as pd
import numpy as np
from PIL import Image
import plotly_express as px
from dash.exceptions import PreventUpdate


def read_mongo(collection, query={}, no_id=True):
    """ Read from Mongo and Store into DataFrame """


    # Make a query to the specific DB and Collection
    cursor = collection.find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df


def setup():
        #
    # Data Treatment==========================================================================================
    #

    wh2015 = pd.read_csv ("./2015.csv")


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
        img = np.array(Image.open(f"plouf2.jpg"))              #f"assets/{input}"))
    except OSError:
        raise PreventUpdate



    fig = px.imshow(img, color_continuous_scale="gray")
    fig.update_layout(coloraxis_showscale=False,  paper_bgcolor='rgba(23,61,124,255)', plot_bgcolor='rgba(23,61,124,255)')
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return wh2015 , fig , styles