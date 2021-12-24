import dash_html_components as html
from navbar import create_navbar
from dash.dependencies import Input, Output
from textbx import text_box

import dash_core_components as dcc
header = html.H3('This is the ADMIN dashboard')


def admin_dashboard():
    layout = html.Div([ 
        header,
    ])
    return layout
