import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from home import create_page_home
from admin import admin_login
from admin_dashboard import admin_dashboard
from guest_dashboard import guest_dashboard
from guest import guest_login
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/admin':
        return admin_login()
    if pathname == '/guest':
        return guest_login()
    if pathname == "/admin_dashboard":
        return admin_dashboard()
    if pathname == "/guest_dashboard":
        return guest_dashboard()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
