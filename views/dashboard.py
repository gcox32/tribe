import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

layout = dbc.Col(html.Div([
        dcc.Tabs(id = 'tabs',
            value = 'tab-2', 
            children = [
                dcc.Tab(label='Data', value = 'tab-1'),
                dcc.Tab(label='Scores Summary', value = 'tab-2'),
                dcc.Tab(label='Compare Sites', value = 'tab-3'),
                dcc.Tab(label='Compare Workouts', value = 'tab-4'),
                dcc.Tab(label='Plot', value = 'tab-5')
            ]),
            html.Div(id = 'tabs-content'
            )
        ]), width = 9)