import dash
from dash import html, dcc, callback, Input, Output, State, no_update
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util import *

dash.register_page(
    __name__, 
    title='Sign Up', 
    path='/signup'
)

# Layout: Signup Form
signupform = [
    html.Img(src=format_img('logo.png'), 
            style={'margin': '30px auto', 'display': 'block'}),
    html.Div('Username', className='label'),
    dcc.Input('', className='input', id='user'),
    html.Div('E-Mail', className='label'),
    dcc.Input('', className='input', id='email', type='email'),
    html.Div('Password', className='label'),
    dcc.Input('', className='input', id='pw', type='password'),
    html.Div(
        dcc.Link(
            "Already have an account?", 
            href='/login'
        ), 
        id='signin-toggle', 
        className='login-signup-toggle'
    ),
    html.Button('Continue', id='submit', className='loginbutton'),
]

# Layout: Signup page
signuppage = html.Div([
        #Login form (with logo)
        html.Div(children=signupform, id='form-area', className='form-area'),

        #Empty Div for logic reasons
        html.Div(id='hidden-signin-div', style={'display': 'none'}),

        #Console shit
        html.Div([
            html.Div(
                html.Div('Console', className='consoletitle'), 
                            className='consoletitlecontainer'),
            html.Div('Welcome!', id='result', 
                        className='consoleoutput'),
        ], className='console'),
    ], 
    id='layout', 
    className='layout'
)

@dash.callback(
    Output('hidden-signin-div', 'children'),
    Input('submit', 'n_clicks'),
    State('user', 'value'),
    State('pw', 'value'),
    prevent_initial_call=True
)
def authenticate(_, username, password):
    # Guard against empty inputs
    if ((username == '') and (password == '')):
        return html.Div('Enter a username and password')
    elif (username == ''):
        return html.Div('Username is empty, try again')
    elif (password == ''):
        return html.Div('Password is empty, try again')

    try:
        auth_response = int(run_php_script('loginRequest.php',
                                            [username, password]))
    except:
        return html.Div('An error occurred while running the login script')
   
    # Return the response in HTML
    if auth_response == 1:
        return dcc.Location(pathname='/logSucc', id='redirect')
    if auth_response == 2:
        return html.Div('Invalid login, try again',
                         style={'color': 'red'})
    else:
        return html.Div('Unhandled error',
                         style={'color': 'red'})

def layout():
    return signuppage