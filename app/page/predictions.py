# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


import pickle

lr = pickle.load(open('LogisticRegression.pkl', 'rb'))
rc = pickle.load(open('RidgeClassifier.pkl', 'rb'))
rfc = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
gbc = pickle.load(open('GradientBoostingClassifier.pkl', 'rb'))
xgbc = pickle.load(open('XGBClassifier.pkl', 'rb'))

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# dcc.Dropdown(
#                 id='your-dropdown-id',
#                 options=[{'label': i, 'value': i} for i in variable_name],
#                 value= variable_name,
#                 multi=True,
#             ),
# #
# layout = dbc.Row([column1, column2])



layout = html.Div([
                dbc.Row([dbc.Col(
                                dbc.Card([
                                        dbc.CardHeader("Estimator Metrics"),
                                        dbc.CardBody([
                                                    # html.H5("Card title", className="card-title"),
                                                    html.P("The performance of different classifiers are comapred for the Forest Cover-Type dataset. The target label in this dataset has 7 classes."
                                                    ,className="card-text"),
                                                    ])
                                        ],
                                        color="primary", inverse=True
                                        )
                                ),
                        dbc.Col(
                                dcc.Dropdown(
                                        id="dropdown1",
                                        options=[
                                                {'label': 'LogisticRegression', 'value': 0},
                                                {'label': 'RidgeClassifier', 'value': 1},
                                                {'label': 'RandomForestClassifier', 'value': 2},
                                                {'label': 'GradientBoostingClassifier', 'value': 3},
                                                {'label': 'XGBClassifier', 'value': 4}
                                                ],
                                        value= [0, 2],
                                        placeholder= "Select an Estimator",
                                        multi=True
                                            )
                            ),
                        dbc.Col([
                                dcc.Checklist(
                                        id="checkbox1",
                                        options=[
                                                {'label': 'Accuracy', 'value': 0},
                                                {'label': 'Precision', 'value': 1},
                                                {'label': 'Recall', 'value': 2}
                                                ],
                                        value=[0]
                                            ),
                                dbc.Button("Estimator metrics", id="Estimator metrics", className="mr-1")
                                ])
                        ],
                        className="mb-4",
                        ),
                dbc.Row([dbc.Col(dcc.Textarea(
                                        id="example-output",
                                        placeholder="Enter a value...",
                                        # value="This is a TextArea component",
                                        style={"width": "100%"}
                                            )
                                )
                        ],
                        className="mb-4"
                        )
                # html.Div()
                ])
