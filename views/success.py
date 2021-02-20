import warnings
# Dash configuration
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import dash_bootstrap_components as dbc

from server import app

warnings.filterwarnings("ignore")

# Create success layout
layout = html.Div(children=[
    dcc.Location(id='url_login_success', refresh=True),
    html.Div(
        className="container",
        children=[
            html.Div(
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="ten columns",
                            children=[
                                html.Br(),
                                html.Div('Login successfull'),
                            ]
                        ),
                        html.Div(
                            className="two columns",
                            # children=html.A(html.Button('LogOut'), href='/')
                            children=[
                                html.Br(),
                                html.Button(id='back-button', children='Go back', n_clicks=0)
                            ]
                        )
                    ]
                )
            )
    # dbc.Col(html.Div([
    #     dcc.Tabs(id = 'tabs',
    #         value = 'tab-2', 
    #         children = [
    #             dcc.Tab(label='Data', value = 'tab-1'),
    #             dcc.Tab(label='Objectives', value = 'tab-2'),
    #             dcc.Tab(label='Creatives', value = 'tab-3'),
    #             dcc.Tab(label='Platforms', value = 'tab-4'),
    #             dcc.Tab(label='Plot', value = 'tab-5')
    #         ]),
    #         html.Div(id = 'tabs-content'
    #         )
    #     ]), width = 9)
        ]
    )
])


# Create callbacks
@app.callback(Output('url_login_success', 'pathname'),
              [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/dashboard'
