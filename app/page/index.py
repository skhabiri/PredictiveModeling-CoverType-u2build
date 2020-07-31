# -*- coding: utf-8 -*-
"""Application index.

This is the first page users will see when they visit your app.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.express as px
import base64
from textwrap import dedent



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(dedent('''
Machine learning modeling techniques are applied to classify a multi-class dataset.
For this purpose we use the [Covertype](https://archive.ics.uci.edu/ml/datasets/covertype) 
dataset available on UCI Machine Learning Repository.

The following classifiers were evaluated and compared for accuracy, precision and recall scores.
* LogisticRegression
* RidgeClassifier
* RandomForestClassifier
* GradientBoostingClassifier
* XGBClassifier


_Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository.
Irvine, CA: University of California, School of Information and Computer Science_


        ''')),
        dcc.Link(
            dbc.Button("Evaluation Metrics", color="primary"), href="/predictions"
        ),
    ],
    md=4,
)

pairplot_png = 'post2_pairplot2.png'
pair_base64 = base64.b64encode(open(pairplot_png, 'rb').read()).decode('ascii')
countplot_png = 'post2_countplot1.png'
count_base64 = base64.b64encode(open(countplot_png, 'rb').read()).decode('ascii')

column2 = dbc.Col([dbc.Row(html.Img(src= 'data:image/png;base64,{}'.format(pair_base64),style={'height': '50%','width': '70%'})),
                   dbc.Row(html.Img(src= 'data:image/png;base64,{}'.format(count_base64),style={'height': '50%','width': '70%'}))])

layout = dbc.Row([column1, column2])
