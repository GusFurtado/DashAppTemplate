import logging

import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug import run_simple

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL, MATCH
from dash.exceptions import PreventUpdate

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import pandas as pd

import utils
from utils import fonts
from layouts import menu, app1, app2



server = flask.Flask(__name__)
server.config['PORT'] = 2000
server.secret_key = 'SECRET_KEY'

file_handler = logging.FileHandler('data/errorlog.log')
file_handler.setLevel(logging.WARNING)
server.logger.addHandler(file_handler)



menu_app = dash.Dash(
    __name__,
    server = server,
    url_base_pathname = '/menu/',
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        fonts.FONTAWESOME,
        fonts.MONTSERRAT,
        fonts.NUNITO
    ]
)
menu_app.title = 'Menu'
menu_app.layout = menu.layout


app1_app = dash.Dash(
    __name__,
    server = server,
    url_base_pathname = '/app1/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)
app1_app.title = 'Dash App 1'
app1_app.layout = app1.layout


app2_app = dash.Dash(
    __name__,
    server = server,
    url_base_pathname = '/app2/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)
app2_app.title = 'Dash App 2'
app2_app.layout = app2.layout


pio.templates.default = 'plotly_white'



@server.route('/')
def redirect_menu():
    return flask.redirect('/menu/')

@server.route('/menu/')
def render_menu():
    return flask.redirect('/PyMenu')

@server.route('/app1/')
def render_app1():
    return flask.redirect('/PyApp1')

@server.route('/app2/')
def render_app2():
    return flask.redirect('/PyApp2')



def pop_user():
    flask.session.pop('autenticado', None)
    flask.session.pop('user', None)
    
def user_auth(user, password):
    # Auth process
    return user == 'test'


@menu_app.callback(
    [Output('user_alert', 'children'),
    Output('user_alert', 'is_open'),
    Output('formulario_collapse', 'is_open'),
    Output('atalho_collapse', 'is_open')],
    [Input('login_button', 'n_clicks')],
    [State('user_input', 'value'),
    State('password_input', 'value')])
def autenticar_usuario(click, user, password):

    
    if click == 0:
        if 'autenticado' in flask.session:
            return None, False, False, True
        else:
            raise PreventUpdate

    else:
        if user_auth(user, password):
            flask.session['autenticado'] = True
            flask.session['user'] = user
            return None, False, False, True
        else:
            pop_user()
            return f"Acesso negado ao usuário '{user}'", True, True, False



@app1_app.callback(
    Output('location', 'pathname'),
    [Input('footer', 'n_clicks')])
def validate_user_app1(click):
    if 'autenticado' not in flask.session:
        return '/menu'
    raise PreventUpdate

@app2_app.callback(
    Output('location', 'pathname'),
    [Input('footer', 'n_clicks')])
def validate_user_app2(click):
    if 'autenticado' not in flask.session:
        return '/menu'
    raise PreventUpdate



app = DispatcherMiddleware(server, {
    '/PyMenu': menu_app.server,
    '/PyApp1': app1_app.server,
    '/PyApp2': app2_app.server
})

run_simple(
    hostname = '0.0.0.0',
    port = server.config['PORT'],
    application = app,
    use_reloader = True,
    use_debugger = True
)