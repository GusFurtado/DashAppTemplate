import dash_html_components as html
import dash_bootstrap_components as dbc



titulo = dbc.Row(
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
    header = 'Usuário não validado',
    is_open = False,
    dismissable = True,
    icon = 'danger',
    style = {
        'margin-left': 15,
        'margin-right': 15
    }
)



formulario = dbc.Col([

    dbc.Form([

        # Usuário
        dbc.FormGroup(
            [
                dbc.Label(
                    'Usuário',
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
                    placeholder = 'Usuário de rede',
                    autoComplete = True
                )
            ]
        ),          

        # Password
        dbc.FormGroup(
            [
                dbc.Label(
                    'Senha',
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
                    placeholder = "Senha da rede",
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



atalhos = dbc.Col([
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
        titulo,
        dbc.Row([
            dbc.Collapse(
                formulario,
                id = 'formulario_collapse',
                is_open = True,
                style = {
                    'width': 400
                }
            ),
            dbc.Collapse(
                atalhos,
                id = 'atalho_collapse',
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