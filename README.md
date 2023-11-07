# WatQC Water Quality Dashboard
## Description
This code creates a dashboard where users are able to visualize data from ACAP-St. John's Community-Based Water Monitoring Program Dataset. It allows users to visualize trends for 
multiple sites in the Water Monitoring Program per parameter. Users get to choose the parameter and the sites they want to visualize. Additionally, users can also access the ArcGIS 
embeddment of this data which shows fish species sightings for most of the sites from the Program and heatmaps for the water quality parameters. The last functionality of this dashboard 
explains scientific terms and the evaluation of various visualizations for one site (Cold Brook) in the dataset. 

The code is written in Python, with implementation from the Plotly library for graphical implementation and Dash for HTML/CSS bindings through Python. 

We hope to incorporate further graphical visualizations, especially for fish data, and have record counts shown for each site and parameter. We also hope to be able to give access to 
data from specific sites and parameters that are chosen by users. We also want to connect our platform with DataStream and other datahubs so users are able to pull data from these sites
and visualize them on our platform. We also hope to have Water Quality Reports generated for all sites and show data pulled from other datahubs on our ArcGIS feature. 

## Running the Project
To start this dashboard, clone or download this repository as is and run the dashboard.py file in the terminal. A local version of the dashboard will open on your localhost:8050, which 
can be copied to your browser's search tab and used. This dashboard is also hosted to be publicly available at [site]. 

## Demo of the Dashboard
To know how to use this dashboard, please follow this video link that gives a detailed demo: 

https://github.com/ridhee1gupta/WQ-Dashboard-ELA-Hack/assets/56942399/6589f63f-d43c-47f1-aa25-792111bd5dcd

## Credits
This project was created by Nick Cheng, Ridhee Gupta, and Manuel Ron Lleras as part of IISD-ELA's Hackathon: Hacking the World's Freshwater Laboratory. 
The following website, titled, **Develop Data Visualization Interfaces in Python with Dash**, by Real Python, was also used as a reference to build the dashboard: 
https://realpython.com/python-dash/

## License
This project is covered under MIT Open License. 
