import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# df = pd.DataFrame(px.data.iris())
df = pd.read_csv('HIST_PAINEL_COVIDBR_20ago2020_MT.csv')
# print(df.columns)
df_mes = df.groupby(['semanaEpi']).sum()

print(df_mes.columns)

fig_scatter_acumulados = px.scatter(df, x='data', y='casosAcumulado', color='data', title='Casos Acumulados')
fig_line_acumulados = px.line(df_mes, x=df_mes.index, y='casosAcumulado', title='Semana Epidemiológica')

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(figure=fig_scatter_acumulados),
        html.Br(),
        dcc.Graph(figure=fig_line_acumulados)
    ]
)

app.run_server(debug=True, use_reloader=True)
