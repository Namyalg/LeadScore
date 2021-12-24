import dash_html_components as html
from navbar import create_navbar
import dash_core_components as dcc



def text_box():
    input_u = dcc.Input(
            id="username",
            type="text",
            placeholder="username",
        )
    return input_u
