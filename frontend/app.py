import sys, os
import dash
from dash import Dash, html, dcc, callback, Input, Output, State, no_update
#from pages import login, signup

# Initialize Dash app
app = Dash(__name__, 
          update_title='', 
          suppress_callback_exceptions=True,
          use_pages=True
        )

app.layout = html.Div(
    dash.page_container
)

# This was provided by the Dash documentation
#
# @callback(Output('page-content', 'children'),
#               Input('url', 'pathname'))
# def display_page(pathname):
#     if pathname == '/login':
#         return login.layout
#     elif pathname == '/signup':
#         return signup.layout
#     else:
#         return '404'

if __name__ == "__main__":
    app.run_server(debug=True)


# Initial app layout
# - The login page will always be first
# - TODO: Cookies/Session?
# app.layout = login