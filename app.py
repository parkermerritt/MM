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
    #assets_external_scripts='https://cdn.plot.ly/plotly-finance-1.28.0.min.js'
)
server = app.server

#app.scripts.config.serve_locally = False

colorscale = cl.scales['9']['qual']['Paired']

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv')

app.layout = html.Div([
    
    html.Div([
        html.H2('Mesh Methods',
                style={'display': 'inline',
                       'float': 'left',
                       'font-size': '2.66em',
                       'margin-left': '2em',
                       'font-weight': 'bolder',
                       'font-family': 'Product Sans',
                       'color': "rgba(117, 117, 117, 0.95)",
                       'margin-top': '40px',
                       'margin-bottom': '0'
                       }),
        html.Img(src="./assets/MeshMethodsLogo-v1.png",
                style={
                    'margin-right': '2em',
                    'height': '120px',
                    'float': 'right'
                },
        ),
    ]),
    
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
    app.run_server(debug=False)
    app.run_server(port=5000,host='0.0.0.0',debug=True)