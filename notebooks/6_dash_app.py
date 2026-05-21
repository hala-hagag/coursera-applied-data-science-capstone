"""
Plotly Dash dashboard for SpaceX launch records.
Run with:  python dash_app.py
"""
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('../data/spacex_launch_dash.csv')
min_p, max_p = df['Payload Mass (kg)'].min(), df['Payload Mass (kg)'].max()
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign':'center','color':'#503D36'}),
    dcc.Dropdown(id='site-dropdown',
        options=[{'label':'All Sites','value':'ALL'}]+[{'label':s,'value':s} for s in df['Launch Site'].unique()],
        value='ALL', placeholder='Select a Launch Site'),
    html.Br(),
    dcc.Graph(id='success-pie-chart'),
    html.P('Payload range (kg):'),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    marks={i:str(i) for i in range(0,10001,2000)},
                    value=[min_p, max_p]),
    dcc.Graph(id='success-payload-scatter-chart'),
])

@app.callback(Output('success-pie-chart','figure'), Input('site-dropdown','value'))
def pie(site):
    if site=='ALL':
        d = df[df['class']==1].groupby('Launch Site').size().reset_index(name='count')
        return px.pie(d, values='count', names='Launch Site', title='Total successful launches by site')
    sub = df[df['Launch Site']==site]['class'].value_counts().rename({1:'Success',0:'Failure'}).reset_index()
    sub.columns=['outcome','count']
    return px.pie(sub, values='count', names='outcome', title=f'Outcome distribution at {site}')

@app.callback(Output('success-payload-scatter-chart','figure'),
              [Input('site-dropdown','value'), Input('payload-slider','value')])
def scatter(site, prange):
    lo, hi = prange
    d = df[(df['Payload Mass (kg)']>=lo) & (df['Payload Mass (kg)']<=hi)]
    if site!='ALL': d = d[d['Launch Site']==site]
    return px.scatter(d, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                      title=f'Payload vs Outcome ({site})')

if __name__ == '__main__':
    app.run_server(debug=False)
