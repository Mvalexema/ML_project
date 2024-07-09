# Import required libraries
import pandas as pd
import dash
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',  options=[{'label':'All Sites', 'value':'ALL'},
                                                                           {'label':'CCAFS LC-40', 'value':'CCAFS LC-40'},
                                                                           {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'},
                                                                           {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
                                                                           {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},
                                                                           ], value='ALL', placeholder='Select a Launch Site here', searchable=True),
                                html.Br(),
                                #html.Br(),
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),
                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                # dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider', min=min_payload, max=max_payload, step=1000, value=[min_payload, max_payload]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart'),),
                            ])
# add callback decorator



# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'), Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', names=filtered_df['Launch Site'], title='Total success launches by site')
    else:
        # all below is added
        # chosen launch site
        filtered_df = spacex_df[spacex_df['Launch Site']==str(entered_site)]
        # class_data = filtered_df["class"].value_counts()
        # class_data = pd.DataFrame([[n_success, len(filtered_df)-n_success]])
        # print(class_data)
        n_success = filtered_df['class'].sum()
        fig = go.Figure(go.Pie(values=[n_success, len(filtered_df)-n_success],labels=['Success', 'Failure']),
                        go.Layout(title='Total success launches by site: {}'.format(entered_site),))
        # fig = px.pie(filtered_df, values="class", names="class", title='Total success launches by site: {}'.format(entered_site))
    # return the outcomes piechart for a selected site
    return fig



@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, payload_slider):
    print(payload_slider)
    filtered_df = spacex_df[(payload_slider[0] <= spacex_df['Payload Mass (kg)']) & (spacex_df['Payload Mass (kg)'] <= payload_slider[1])]
    # filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x="Payload Mass (kg)", y='class', color="Booster Version Category", title='Correlation between Payload and Success')
    else:#all below is added
        filtered_df = spacex_df[spacex_df['Launch Site']==(entered_site)]#chosen launch site
        class_data = filtered_df[filtered_df['Launch Site']==str(entered_site)]
        fig = px.scatter(class_data, x='Payload Mass (kg)', y='class', title='Correlation between Payload and Success')
    return fig

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()


