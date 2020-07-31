# -*- coding: utf-8 -*-
"""Application index.

This is the first page users will see when they visit your app.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.express as px


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
five different machine learning classifiers are implemented to classify a multi-class target label. The classification techniques are evaluated on the forest cover type dataset provided by Jock A. Blackard and Colorado State University.

> Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science
            """
        ),
        dcc.Link(
            dbc.Button("Evaluation Metrics", color="primary"), href="/predictions"
        ),
    ],
    md=4,
)


column2 = dbc.Col([dbc.Row(html.Img(src= 'post2_pairplot2.png',style={'height': '50%','width': '50%'})),
                   dbc.Row(html.Img(src= 'post2_countplot1.png',style={'height': '50%','width': '50%'}))])

layout = dbc.Row([column1, column2])
