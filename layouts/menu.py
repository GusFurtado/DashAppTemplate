import dash_html_components as html
import dash_bootstrap_components as dbc



title = dbc.Row(
    html.H1(
        'App',
        className = "display-3",
        style = {
            'color': 'blue',
            'font-family': 'Nunito'
        }
    ),
    justify = 'center'
)



user_alert = dbc.Toast(
    id = 'user_alert',
    header = 'User not authenticated',
    is_open = False,
    dismissable = True,
    icon = 'danger',
    style = {
        'margin-left': 15,
        'margin-right': 15
    }
)



form = dbc.Col([

    dbc.Form([

        # Username
        dbc.FormGroup(
            [
                dbc.Label(
                    'Username',
                    html_for = 'user_input',
                    style = {
                        'font-size': 14,
                        'font-weight': 'bold',
                        'color': 'blue'
                    }
                ),
                dbc.Input(
                    type = 'text',
                    id = 'user_input',
                    placeholder = 'Username',
                    autoComplete = True
                )
            ]
        ),          

        # Password
        dbc.FormGroup(
            [
                dbc.Label(
                    'Password',
                    html_for = 'password_input',
                    style = {
                        'font-size': 14,
                        'font-weight': 'bold',
                        'color': 'blue'
                    }
                ),
                dbc.Input(
                    type = "password",
                    id = 'password_input',
                    placeholder = "Password",
                ),
            ]
        ),

        dbc.Row(
            dbc.Col(
                dbc.Button(
                    'Log in',
                    id = 'login_button',
                    color = 'primary',
                    n_clicks = 0
                ),
                width = 'auto'
            ),
            justify = 'center'
        ),
        
    ]),
    user_alert
])



links = dbc.Col([
    dbc.Button(
        [html.I(className="fa fa-flask mr-2"), html.Span('App 1')],
        color = 'primary',
        href = 'http://localhost:2000/app1/'
    ),
    dbc.Button(
        [html.I(className="fa fa-fire mr-2"), html.Span('App 2')],
        color = 'primary',
        href = 'http://localhost:2000/app2/',
        className = 'ml-2'
    )
])



layout = html.Div(
    dbc.Container([
        title,
        dbc.Row([
            dbc.Collapse(
                form,
                id = 'form_collapse',
                is_open = True,
                style = {
                    'width': 400
                }
            ),
            dbc.Collapse(
                links,
                id = 'links_collapse',
                is_open = False
            )
        ],
            justify = 'center'
        )
    ],
        style = {
            'margin': 0,
            'position': 'absolute',
            'top': '50%',
            'left': '50%',
            'margin-right': '-50%',
            'transform': 'translate(-50%, -50%)'
        }
    ),
    className = 'fullscreen'
)