import dash_bootstrap_components as dbc
import dash_core_components as dcc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="LOGIN",
                children=[
                    #dbc.DropdownMenuItem("LOGIN", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("ADMIN", href='/admin'),
                    dbc.DropdownMenuItem("GUEST", href='/guest'),
                ],
            ),
        ],
        brand="Home",
        brand_href="/",
        sticky="top",
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
