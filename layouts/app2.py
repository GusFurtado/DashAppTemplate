"""
App 2 Layout
"""



import dash_html_components as html
import dash_bootstrap_components as dbc


layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.B(
                    'APP 2',
                    style = {
                        'font-size': 32,
                        'color': 'blue'
                    }
                )    
            )
        )    
    ])    
],
    className = 'fullscreen'
)