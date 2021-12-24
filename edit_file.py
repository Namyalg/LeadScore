import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


df = pd.read_csv('test.csv')

body = dbc.Container(
    [
        dbc.Row(
            [
                dash_table.DataTable(id="dash_neu", editable=True, row_deletable=True, columns=[{'name': i, 'id': i} for i in df.columns], data=df.to_dict('records')),
                dbc.Col(html.Button('+', id='editing-rows-button', n_clicks=0)),
                dbc.Col(html.Button('update', id='btn-save', n_clicks=0))
            ]
        )])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([body])


@app.callback(
    [dash.dependencies.Output("dash_neu", "data"), dash.dependencies.Output("dash_neu", "columns")],
    [Input("btn-save", "n_clicks"), Input('editing-rows-button', 'n_clicks')],
    [State('dash_neu', 'data'), State('dash_neu', 'columns')]
)
def update(button, clicked, data, columns):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-save' in changed_id:
        df = pd.DataFrame(data)
        df.to_csv('test.csv', encoding='utf-8', index=False)
        columns = [{'name': i, 'id': i} for i in df.columns]
        data = df.to_dict('records')
        return data, columns
    if 'editing-rows-button' in changed_id:
        if clicked > 0:
             data.append({c['id']: '' for c in columns})
        return data, columns
    return data, columns

if __name__ == '__main__':
    app.run_server(debug=True)