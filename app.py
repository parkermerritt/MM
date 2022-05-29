import dash
import dash_core_components as dcc
import dash_html_components as html

import colorlover as cl
import datetime as dt
import flask
import os
import pandas as pd
import time

app = dash.Dash(
    __name__, 
    title="Mesh Methods",
    #assets_external_scripts='https://cdn.plot.ly/plotly-finance-1.28.0.min.js'
)
app._favicon = ("./assets/favicon.ico")
server = app.server

#app.scripts.config.serve_locally = False

colorscale = cl.scales['9']['qual']['Paired']

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv')

app.layout = html.Div([
    
    html.Div([
        html.Img(src="./assets/MeshMethodsLogo-v1.png",
                style={
                    'margin-right': '2em',
                    'height': '400px',
                    'text-align':'center'
                },
        ),
        html.H2('Mesh Methods LLC',style={'text-align':'center','font-family': 'Trebuchet MS','font-size':30}),
        html.H3('contact@meshmethods.com',style={'text-align':'center','font-family': 'Trebuchet MS','font-size':20}),

        ],style={'textAlign': 'center'}
    ),
    
])



#@app.callback(
    #dash.dependencies.Output('graphs','children'),
    #[dash.dependencies.Input('stock-ticker-input', 'value')])
#def update_graph(tickers):
#    graphs = []
#
#    if not tickers:
#        graphs.append(html.H3(
#            "Select a stock ticker.",
#            style={'marginTop': 20, 'marginBottom': 20}
#        ))
#    else:
#        for i, ticker in enumerate(tickers):
#
#            dff = df[df['Stock'] == ticker]
#
#            candlestick = {
#                'x': dff['Date'],
#                'open': dff['Open'],
#                'high': dff['High'],
#                'low': dff['Low'],
#                'close': dff['Close'],
#                'type': 'candlestick',
#                'name': ticker,
#                'legendgroup': ticker,
#                'increasing': {'line': {'color': colorscale[0]}},
#                'decreasing': {'line': {'color': colorscale[1]}}
#            }
#            bb_bands = bbands(dff.Close)
#            bollinger_traces = [{
#                'x': dff['Date'], 'y': y,
#                'type': 'scatter', 'mode': 'lines',
#                'line': {'width': 1, 'color': colorscale[(i*2) % len(colorscale)]},
#                'hoverinfo': 'none',
#                'legendgroup': ticker,
#                'showlegend': True if i == 0 else False,
#                'name': '{} - bollinger bands'.format(ticker)
#            } for i, y in enumerate(bb_bands)]
#            graphs.append(dcc.Graph(
#                id=ticker,
#                figure={
#                    'data': [candlestick] + bollinger_traces,
#                    'layout': {
#                        'margin': {'b': 0, 'r': 10, 'l': 60, 't': 0},
#                        'legend': {'x': 0}
#                    }
#                }
#            ))
#    return graphs


if __name__ == '__main__':
    #app.run_server(debug=False)
    app.run_server(port=5000,host='0.0.0.0',debug=False,dev_tools_hot_reload=True)