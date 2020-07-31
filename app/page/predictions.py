# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# import pickle
#
# lr = pickle.load(open('LogisticRegression.pkl', 'rb'))
# rc = pickle.load(open('RidgeClassifier.pkl', 'rb'))
# rfc = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
# gbc = pickle.load(open('GradientBoostingClassifier.pkl', 'rb'))
# xgbc = pickle.load(open('XGBClassifier.pkl', 'rb'))

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


layout = html.Div([
                dbc.Row([dbc.Col(
                                dbc.Card([
                                        dbc.CardHeader("CLasssification Scores"),
                                        dbc.CardBody([
                                                    # html.H5("Card title", className="card-title"),
                                                    html.P("The target label of the Covertype datset is 'Cover_Type'. The target label has 7 classes. Here we can compare accuracy, precision, and recall scores of the listed classifiers. "
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
                                                {'label': 'LogisticRegression', 'value': 'LogisticRegression'},
                                                {'label': 'RidgeClassifier', 'value': 'RidgeClassifier'},
                                                {'label': 'RandomForestClassifier', 'value': 'RandomForestClassifier'},
                                                {'label': 'GradientBoostingClassifier', 'value': 'GradientBoostingClassifier'},
                                                {'label': 'XGBClassifier', 'value': 'XGBClassifier'}
                                                ],
                                        value= ['LogisticRegression', 'RandomForestClassifier' ],
                                        placeholder= "Select an Estimator",
                                        multi=True
                                            )
                            ),
                        dbc.Col([
                                dcc.Checklist(
                                        id="checkbox1",
                                        options=[
                                                {'label': 'Accuracy', 'value': 'Accuracy'},
                                                {'label': 'Precision', 'value': 'Precision'},
                                                {'label': 'Recall', 'value': 'Recall'}
                                                ],
                                        value=['Accuracy']
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
                                        style={"width": "100%", 'height': 300}
                                            )
                                )
                        ],
                        className="mb-4"
                        )
                # html.Div()
                ])
