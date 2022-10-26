from dash import Dash, dcc, html
import dash_vtk
from responsiveTank import *
from dash.dependencies import Input, State, Output
import os
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)

app = Dash(__name__)

logoPath = 'assets/logo.png'

obj_file = dirName + '/export.obj'
txt_content = None
with open(obj_file, 'r') as file:
  txt_content = file.read()

content = dash_vtk.View(
    [
    dash_vtk.GeometryRepresentation([
        dash_vtk.Reader(
            vtkClass="vtkOBJReader",
            parseAsText=txt_content),])
    ],
    cameraPosition=[0, -1, -1],
    background=[255,255,255],
)

result = html.H2(id='stressResult',
                children=['Enter values and press Calculate'],
                className='result')

app.layout = html.Div(children=[

    html.Div(children=[

        html.Img(src=logoPath, style={'display':'inline-block','margin-left':50, 'margin-right': 20}),

        html.H1("Steel Storage Tank Calculator", className="headerText", style={'display':'inline-block'}),

    ], className='headerDiv'),

    html.Div(children=[

        html.Div(children=[

            html.H5("Tank Wall Height (m)",
                    className='heightLabel'),

            dcc.Input(
                id = 'heightInput',
                className ='heightBox',
                type = 'number'
            ),

            html.Br(),
            html.Br(),

            html.H5("Tank Diameter (m)",
                    className='diameterLabel'),

            dcc.Input(
                id = 'diameterInput',
                className ='diameterBox',
                type ='number',
            ),

            html.Br(),
            html.Br(),

            html.H5("Utilization (%)",
                    className='sliderLabel'),

            dcc.Slider(
                min=0,
                max=100,
                step=10,
                value = 80,
                id = 'utilSlider',
                className="utilSlider"
            ),

            html.Br(),

            html.Button(
                'Calculate',
                id='calculateButton',
                n_clicks=0,
                className='calculateButton',
                style={'display':'inline-block'}
            ),
            html.Br(),
            html.Br(),

            dcc.Loading(
                id="loading",
                className= "loading_output",
                type="default",
                children=[html.Div(id="loading_output")],
            ),
            html.Br(),

            result,


        ], className='inputDiv'),

        html.Div(children=[

            html.Div(
            style={"width": "80%", "height": "800px", 'margin-right': '2000'},
            children=[content],
            id="threeVis")

        ], className='threeDiv')


    ], className='containerDiv'),

])

@app.callback(
    [Output('loading_output', 'children'),
     Output('stressResult', 'children'),
     Output('threeVis', 'children')],
    Input('calculateButton', 'n_clicks'),
    [State('heightInput', 'value'),
     State('diameterInput', 'value'),
     State('utilSlider','value')]
)
def update(value, height, diameter, uti):


    if height == None:
        result = html.P(id='stressResult1',
                children=['Enter values and press Calculate'],
                className='enter')
    else:
        stress = round(calculateTank(diameter,height,uti/100),2)

        result = html.P(id='stressResult',
                        children=[html.H5('The maximum stress:'), html.H2(' {} MPa'.format(stress))])
        print(stress)

    obj_file = dirName + '/export.obj'

    txt_content = None
    with open(obj_file, 'r') as file:
        txt_content = file.read()

    content = dash_vtk.View([
        dash_vtk.GeometryRepresentation([
            dash_vtk.Reader(
                vtkClass="vtkOBJReader",
                parseAsText=txt_content,
            ),
        ]),
    ],
    cameraPosition=[0, -1, -1],
    background=[255,255,255])

    return html.P(), result, content


if __name__ == "__main__":
    app.run_server(debug=True)

