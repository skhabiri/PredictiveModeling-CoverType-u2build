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

est_list = [lr, rc, rfc, gbc, xgbc]
style_list = ["primary","secondary","info"]

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
            return "Not clicked."
        else:
            my_list=[]
            for i in dropval:
                for j in boxval:
                    my_list.append(est_list[i][j])
            return str(my_list)
            # return str(est_list[dropval[0]][boxval[0]])
            # return f"Clicked {n_clicks} times."
            # card_content = [
            # dbc.CardHeader("Card header"),
            # dbc.CardBody(
            #     [
            #         html.H5("Card title", className="card-title"),
            #         html.P(
            #             "This is some card content that we'll reuse",
            #             className="card-text",
            #         ),
            #     ]
            # )]

            # rows = []
            # for i in dropval:
            #     columns = []
            #     for j in boxval:
            #         card_content = [
            #                 dbc.CardHeader("Card header"),
            #                 dbc.CardBody(
            #                     [
            #                         html.H5("Card title", className="card-title"),
            #                         html.P(
            #                             str(est_list[i][j]),
            #                             className="card-text",
            #                         ),
            #                     ]
            #                 )
            #         ]
            #         columns.append(dbc.Col(dbc.Card(card_content, color=style_list[j], inverse=True)))
            #     rows.append(dbc.Row(columns, className="mb-4",))
            # return rows;

# app.layout = html.Div([
#     dcc.Dropdown(
#         id='countries-dropdown',
#         options=[{'label': k, 'value': k} for k in all_options.keys()],
#         value='America',  #default value to show
#         multi=True,
#         searchable=False
#     ),
#
#     dcc.Dropdown(id='cities-dropdown', multi=True, searchable=False, placeholder="Select a city"),
#
#     html.Div(id='display-selected-values')
# ])
#
# @app.callback(
#     dash.dependencies.Output('cities-dropdown', 'options'),
#     [dash.dependencies.Input('countries-dropdown', 'value')])
# def set_cities_options(selected_country):
#     if type(selected_country) == 'str':
#         return [{'label': i, 'value': i} for i in all_options[selected_country]]
#     else:
#         return [{'label': i, 'value': i} for country in selected_country for i in all_options[country]]
