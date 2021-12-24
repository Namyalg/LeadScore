import dash_html_components as html
from navbar import create_navbar
import dash_core_components as dcc

def password():
    input_u = dcc.Input(
            id="password",
            type="password",
            placeholder="password",
        )
    return input_u
