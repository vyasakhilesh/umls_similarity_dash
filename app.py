import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd


# Initialise App
app = dash.Dash(__name__)

# Loading Data
# df = 

# create figure
# fig = 

# colors
colors = {'background': '#111111', 'text': '#7FDBFF'}

#Markdown text
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash App [Link](http://127.0.0.1:8050/)
'''

# Create table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div(style={'backgroundColor': colors['background']}, 
    children = [
        html.H1(children='Dash: UMLS SIMILARITY', style={'textAlign': 'center','color': colors['text']}),
        html.Div(children='''Visualising Dash''', style={'textAlign': 'center','color': colors['text']}),
    # html.P('''Pick one UMLS concept from the dropdown below.'''),
    # dcc.Graph(id='', figure=fig)   # Put your figure here
    # generate_table(df) # to generate table
     dcc.Markdown(children=markdown_text),
     html.Label('Dropdown'),
     dcc.Dropdown()
    ])

# Final Running the App
if __name__ == '__main__':
    app.run_server(debug=True) # For reloading