import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df.to_csv('test.csv')

nmb_clicks = 0
app.layout = html.Div([
    dcc.Store(id='click-memory', data = {'nmb_clicks': nmb_clicks}),
    html.Div([
        dcc.Input(
            id='adding-rows-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-columns-button', n_clicks=nmb_clicks)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='adding-rows-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        editable=True,
        row_deletable=True
    ),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
])

@app.callback(dash.dependencies.Output('adding-rows-table', 'columns'),
             [dash.dependencies.Input('adding-columns-button', 'n_clicks'),
              dash.dependencies.Input('adding-rows-name', 'value')],
             [dash.dependencies.State('click-memory', 'data')])
def update_dropdown(click, name, data):
    if click != data['nmb_clicks']:
        if name not in df.columns:
            df[name] = [float('nan')] * len(df.index)
    print(df['State'])
    df.to_csv('test.csv')
    return [{"name": i, "id": i} for i in df.columns]

@app.callback(dash.dependencies.Output('click-memory', 'data'),
             [dash.dependencies.Input('adding-columns-button', 'n_clicks')],
             [dash.dependencies.State('click-memory', 'data')])
def on_data(click, data):
    if click != nmb_clicks:
        data['nmb_clicks'] = data['nmb_clicks'] + 1
    print(df['State'])
    df.to_csv('test.csv')
    return data

if __name__ == '__main__':
    app.run_server(debug=True)