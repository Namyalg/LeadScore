import dash_html_components as html
from navbar import create_navbar
from dash.dependencies import Input, Output
from textbx import text_box
from password import password
import dash_core_components as dcc
nav = create_navbar()
username = text_box()
pswd = password()
header = html.H3('Enter admin credentials')


def admin_login():
    layout = html.Div([
        html.Div([
            nav
        ]),
        html.Div([
            header
        ]),
        html.Div([
            username
        ]),
        html.Div([
            pswd,
        ]),
        dcc.Link(html.Button("SUBMIT"), href="/admin_dashboard", refresh=True),
    ], style={'margin' : 'auto'}
    
    )
    return layout
