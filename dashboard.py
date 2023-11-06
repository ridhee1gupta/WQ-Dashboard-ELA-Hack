#!/usr/bin/env python
# coding: utf-8

# In[12]:


from dash import Dash, dcc, html, Input, Output, no_update
from dash.exceptions import PreventUpdate
import plotly.express as px
import data_viz_ACAP as viz


# In[13]:


data, sites, parameters = viz.read_data()
#print(data)
#if site in sites and param in parameters:
cleaned_data, param = viz.clean_data(data, "Ammonia")
site = "Caledonia Upstream"
cleaned_data = cleaned_data.loc[cleaned_data['MonitoringLocationName'] == site]
#print(cleaned_data)
if not cleaned_data.empty:
    unit = data["ResultUnit"].iloc[0]
    #param = data["CharacteristicName"].iloc[0]
    fig_scatter = px.scatter(cleaned_data, x="ActivityStartDate", y="ResultValue", \
                    labels = {"ActivityStartDate": "Date", "ResultValue": f"{param} ({unit})"})
    fig_scatter.update_layout(title_text = f"Recorded values of {param} at {site}", title_x = 0.5)
    fig_line = px.line(cleaned_data, x="ActivityStartDate", y="ResultValue", \
                        labels = {"ActivityStartDate": "Date", "ResultValue": f"{param} ({unit})"}, markers=True)
    fig_line.update_layout(title_text = f"Trend of {param} at {site}", title_x = 0.5)
    #print(type(unit), unit)

    external_stylesheets = [
        {
            "href": (
                "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap"
            ),
            "rel": "stylesheet",
        },
    ]




app = Dash(__name__, external_stylesheets = external_stylesheets)


# In[5]:
app.title = "WatQC: Find out if the watershed next to you is safe and healthy!"

app.layout = html.Div(
        children = [
            html.Div(
                children = [
                    html.Img(src = "WATQC-Favicon\android-chrome-192x192.png", alt = "WatQC Logo", className = "header-emoji"),
                    html.H1(
                        children = "WatQC Dashboard", className = "header-title"
                    ),
            html.P(
                children = (
                "Find out if the watershed next to you is safe and healthy!"
            ),
            className = "header-description",
        ),
    ],
    className = "header",
),
html.Div([
    dcc.Tabs([
        dcc.Tab(
            label = "Analyze our data!",
            children = [
                html.P(
                    id = "no-content",
                    style = {"color": "#2580C8", "text-align": "center"}
                ),
                html.Div(
                    children = [
                        html.Div(children = "Sites", className = "menu-title"),
                            dcc.Dropdown(
                                id = "site-filter",
                                options = [
                                    {"label": site, "value": site}
                                    for site in sites
                                ],
                                value = "Adam's Lake",
                                clearable = False,
                                searchable = True,
                                className = "dropdown",
                                multi = True
                            ),
                    ]
                ),
                html.Div(
                    children = [
                        html.Div(children = "Parameters", className = "menu-title"),
                            dcc.Dropdown(
                                id = "parameter-filter",
                                options = [
                                    {"label": param, "value": param}
                                    for param in parameters
                                ],
                                value = "Ammonia",
                                clearable = False,
                                searchable = True,
                                className = "dropdown",
                            ),
                    ],
                    className = "menu",
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = dcc.Graph(
                                id = "line-plot",
                                config = {"displayModeBar": False},
                                figure = fig_line
                            ),
                            className = "card",
                        ),
                    ],
                ),
                html.Div(
                    children = dcc.Graph(
                        id = "scatter-plot",
                        config = {"displayModeBar": False},
                        figure = fig_scatter
                    ),
                    className = "card",
                ),
            ],
    ), # end of first tab
    dcc.Tab(
        label = "Every season is fishing season!",
        children = [
                html.Embed(
                    src = "//leaconsulting.maps.arcgis.com/apps/Embed/index.html" \
                          "?webmap=32038bf69ed841b29d7249d4b4193290&extent=-66.0204," \
                          "45.3155,-66.0082,45.3202&zoom=true&previewImage=false&" \
                          "scale=true&search=true&searchextent=true&details=true&"
                          "legendlayers=true&active_panel=legend&disable_scroll=true&theme=dark",
                    title = "Hackathon Map - WatQC Dashboard",
                    height = "600", width = "1000"
                    #className = "embed-container"
                )
        ]
    ), # end of second tab
    dcc.Tab(
        label = "But what does it all mean?",
        children = [
            html.Button("Download our Water Quality Report Explainer", id = "wqi-explainer", className = "button"),
            dcc.Download(id = "download-explainer"),
            html.P(
                children = ("Sure, you are able to visualize this data and see " \
                              "what the trends are for your favourite watershed " \
                              "but what does this really mean? Have we ever thought " \
                              "about what it means for a waterbody to have high pH values? " \
                              "What about declining fish diversity? "
                              "We explain some of these factors below!")
            ),
            html.P(
                children = ("Key Takeaways:"),
                style = {'color': '#2580C8',
                         'margin': 10,
                         'font-size': 20,
                         'text-align': 'justify',
                         'max-width': 950,
                         'font-weight': 'bold'}
            ),
            html.Ul(
                children = [
                    html.Li(
                        ("Temperature, pH, and salinity greatly influence plant and animal survival in water bodies."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                                 #'font-weight': 'bold'}
                    ),
                    html.Li(
                        ("Ammonia, phosphate, and E. Coli, when disturbed by pollution, negatively impact water body properties."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                    ),
                    html.Li(
                        ("Fish species, including Bait, Forage, and Sport Fish, maintain ecological balance."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                    )
                ]
            ),
            html.P(
                children = ("Observations from Sites:"),
                style = {'color': '#2580C8',
                         'margin': 10,
                         'font-size': 20,
                         'text-align': 'justify',
                         'max-width': 950,
                         'font-weight': 'bold'}
            ),
            html.Ul(
                children = [
                    html.Li(
                        ("Similar water bodies can be compared despite unique baseline physical parameters."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                                 #'font-weight': 'bold'}
                    ),
                    html.Li(
                        ("Physical parameters are affected by large-scale factors such as acid rain and global warming."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                    )
                ]
            ),
            html.P(
                children = ("Water Quality Index (WQI):"),
                style = {'color': '#2580C8',
                         'margin': 10,
                         'font-size': 20,
                         'text-align': 'justify',
                         'max-width': 950,
                         'font-weight': 'bold'}
            ),
            html.Ul(
                children = [
                    html.Li(
                        ("A generalized score (0-100) assesses water quality based on parameters compared to recommended thresholds."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                                 #'font-weight': 'bold'}
                    ),
                    html.Li(
                        ("Categories include Pristine, Usually Desirable, Sometimes Desirable, Often Not Desirable, Usually Not Desirable."),
                        style = {'color': '#2580C8',
                                 'margin': 10,
                                 'font-size': 20,
                                 'text-align': 'justify',
                                 'max-width': 950}
                    )
                ]
            ),
            html.P(
                children = ("Want to learn more about the science behind water quality and what all the trends mean? " \
                            "Download our water quality report explainer and spread your newfound knowledge about everything " \
                            "water and fish quality related!")
            ),
            html.Button("Download our Water Quality Report Explainer", id = "wqi-explainer", className = "button"),
            dcc.Download(id = "download-explainer")
        ]
    ) # end of the third tab
]) # end of all tabs
],
className = "wrapper",
)
])




@app.callback(
    Output("line-plot", "figure"),
    Output("scatter-plot", "figure"),
    Output("no-content", "children"),
    Input("site-filter", "value"),
    Input("parameter-filter", "value"),
)

def update_charts(sites, param):
    locations = []
    #print(type(sites))
    if type(sites) is not list:
        sites = [sites]
        #print(sites)
    filtered_data, parameter = viz.clean_data(data, param)
    mask = filtered_data.MonitoringLocationName.isin(sites)
    #print(sites)
    if not filtered_data[mask].empty:
        line_fig, scatter_fig = create_charts(filtered_data[mask], param)
        return line_fig, scatter_fig, ""
    else:
        return no_update, no_update, f"There is no data recorded for your selections :("

def create_charts(df, param):
    unit = df["ResultUnit"].iloc[0]
    site = df["MonitoringLocationName"].iloc[0]
    line_plot_figure = px.line(df, x="ActivityStartDate", y="ResultValue", color = "MonitoringLocationName", \
                    labels = {"ActivityStartDate": "Date", "ResultValue": f"{param} ({unit})", "MonitoringLocationName": "Site"}, markers=True, \
                    title = f"Abundance of {param} over the years")
    scatter_plot_figure = px.scatter(df, x="ActivityStartDate", y="ResultValue", color = "MonitoringLocationName", \
                    labels = {"ActivityStartDate": "Date", "ResultValue": f"{param} ({unit})", "MonitoringLocationName": "Site"}, \
                    title = f"Abundance of {param} over the years")
    return line_plot_figure, scatter_plot_figure

@app.callback(
    Output("download-explainer", "data"),
    Input("wqi-explainer", "n_clicks"),
    prevent_initial_call = True,
)

def download_data(n_clicks):
    return dcc.send_file("ELA_Hackathon_WatQC.pdf")





if __name__ == "__main__":
    app.run_server(debug=True)


# In[ ]:
