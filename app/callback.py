# -*- coding: utf-8 -*-
"""app/callback.py

Define application callbacks here.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app.page import index, predictions, insights, process

import pickle

lr = pickle.load(open('LogisticRegression.pkl', 'rb'))
rc = pickle.load(open('RidgeClassifier.pkl', 'rb'))
rfc = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
gbc = pickle.load(open('GradientBoostingClassifier.pkl', 'rb'))
xgbc = pickle.load(open('XGBClassifier.pkl', 'rb'))

# est_list = [lr, rc, rfc, gbc, xgbc]
estdict = {"LogisticRegression": lr,
            "RidgeClassifier": rc,
            "RandomForestClassifier": rfc,
            "GradientBoostingClassifier": gbc,
            "XGBClassifier": xgbc}

scoredict = {"Accuracy": 0,
            "Precision":1,
            "Recall":2}

# style_list = ["primary","secondary","info"]

def register_callbacks(app):
    """Wrap the main application function with the application callbacks.

    Multipage apps:
    URL Routing for Multi-Page Apps: https://dash.plot.ly/urls

    """

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        """
        To add a page to the list of registered callbacks add the page
        to the imports above, then follow the convention below.

        Example:

            elif pathname == "/newUrlPath":
                return new_page_module.layout
        """
        if pathname == "/":
            return index.layout
        elif pathname == "/predictions":
            return predictions.layout
        elif pathname == "/insights":
            return insights.layout
        elif pathname == "/process":
            return process.layout
        else:
            return dcc.Markdown("## Page not found")


    @app.callback(
        Output("example-output", "value"),
        [Input("Estimator metrics", "n_clicks")],
        [State('dropdown1', 'value'), State('checkbox1', 'value')]
    )
    def update_output(n_clicks,dropval,boxval):
        if n_clicks is None:
            return "Compare the Metrics"
        # else:
        #     my_list=[]
        #     for i in dropval:
        #         for j in boxval:
        #             my_list.append(est_list[i][j])
        #     return ' '.join([str(elem) for elem in my_list])
        else:
            my_string=''
            for est in dropval:
                my_string += "\n***** " + est + " *****\n"
                for scr in boxval:
                    my_string = my_string + scr + " score is:\n"
                    try: iter(estdict[est][scoredict[scr]])
                    except Exception: my_string = my_string + " " + str(round(estdict[est][scoredict[scr]],3)) +"\n"
                    else:
                        my_string = my_string + ', '.join([str(round(item, 3)) for item in estdict[est][scoredict[scr]]]) +"\n"
            return my_string
