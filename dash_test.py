import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.H1("hello dash")

if __name__ == '__main__':
    app.run_server(debug=True, port=8080, host='127.0.0.1')
