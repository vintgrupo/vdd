import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output

df = pd.read_csv('HIST_PAINEL_COVIDBR_20ago2020_MT.csv')

# print(df.columns)
df_semana = df.groupby(['semanaEpi']).sum()

# fig_scatter_acumulados = px.scatter(df, x='data', y='casosAcumulado', title='Casos Acumulados')
# fig_line_semana = px.line(df_semana, x=df_semana.index, y='casosAcumulado', title='Semana Epidemiológica')

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Dropdown(
            id='dd_situacao',
            options=[
                {'label': 'Casos Acumulados', 'value': 'casosAcumulado'},
                {'label': 'Casos Novos', 'value': 'casosNovos'},
                {'label': 'Óbitos Acumulados', 'value': 'obitosAcumulado'},
                {'label': 'Óbitos Novos', 'value': 'obitosNovos'}
            ],
            value='casosAcumulado',
            multi=False
        ),
        dcc.Graph(
            id='fig_situacao'
        ),
        html.Br(),
        dcc.Dropdown(
            id='dd_semana',
            options=[
                {'label': 'Casos Acumulados', 'value': 'casosAcumulado'},
                {'label': 'Casos Novos', 'value': 'casosNovos'},
                {'label': 'Óbitos Acumulados', 'value': 'obitosAcumulado'},
                {'label': 'Óbitos Novos', 'value': 'obitosNovos'}
            ],
            value=['casosAcumulado'],
            multi=True
        ),
        dcc.Graph(
            id='fig_semana'
        )
    ]
)

@app.callback(
    Output(component_id='fig_situacao', component_property='figure'),
    [Input(component_id='dd_situacao', component_property='value')]
)
def graf_situacao(dd_scatter_situacao):
    # print('dd: ', dd_scatter_situacao)
    # fig = px.scatter(df, x='data', y=dd_scatter_situacao, title='Casos em Mato Grosso')
    fig = px.line(df, x='data', y=dd_scatter_situacao, title='Casos em Mato Grosso')
    return fig


@app.callback(
    Output(component_id='fig_semana', component_property='figure'),
    [Input(component_id='dd_semana', component_property='value')]
)
def graf_semana(dd_semana):
    return px.line(df_semana, x=df_semana.index, y=dd_semana, title='Semana Epidemiológica')


app.run_server(debug=True, use_reloader=True)
