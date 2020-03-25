import dash
import dash_core_components as dcc
import dash_html_components as html
import anapioficeandfire

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

api = anapioficeandfire.API()
houses = api.get_houses()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
  [
    html.H1('Ice and Fire Houses'),
    dcc.Graph(
      id='houses-graph',
      figure={
        'data': [
          {
            'x': [
              house.name for house in houses
            ],
            'y': [
              len(house.swornMembers) for house in houses
            ],
            'type': 'bar',
            'name': 'Sworn Members'
          }
        ],
        'layout': {
          'title': 'Houses Sworn Members'
        }
      }
    )
  ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
