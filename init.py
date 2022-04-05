import pandas as pd
import numpy as np
from PIL import Image
import plotly_express as px
from dash.exceptions import PreventUpdate



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
        img = np.array(Image.open(f"plouf.jpg"))              #f"assets/{input}"))
    except OSError:
        raise PreventUpdate

    fig = px.imshow(img, color_continuous_scale="gray")
    fig.update_layout(coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return wh2015 , fig , styles