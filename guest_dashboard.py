import dash_html_components as html
from navbar import create_navbar
from dash.dependencies import Input, Output
from textbx import text_box
from get_table  import get_table
import dash_core_components as dcc
header = html.H3('This is the GUEST dashboard')

tab = get_table()

def guest_dashboard():
    layout = html.Div([
        header,
        get_table
    ])
    return layout
