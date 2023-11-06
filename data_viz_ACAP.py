#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.dates import DateFormatter


# In[15]:





#parameters[parameters != '']


# In[16]:


def read_data(file = 'ELAHackathon_Datasets_2023\Hackathon Datasets\ACAP-SJ Datasets\ACAP_Saint_John_Community-Based_Water_Monitoring_Program.csv'):

    df= pd.read_csv(file, delimiter = ',', dtype = 'object')
    column_names = df.columns.to_list()
#print(column_names)
    keep_cols = ['MonitoringLocationName', 'MonitoringLocationType', 'ActivityStartDate', 'ActivityEndDate', 'CharacteristicName', 'MethodSpeciation', 'ResultValue', 'ResultUnit']

    for col in column_names:
        if col not in keep_cols:
        #print(col)
            df.drop(columns = col, axis = 'columns', inplace = True)

    df[['ActivityStartDate', 'ActivityEndDate']] = df[['ActivityStartDate', 'ActivityEndDate']].apply(pd.to_datetime)
    sites = df["MonitoringLocationName"].sort_values().unique()
    parameters = df["CharacteristicName"].sort_values().unique()

    return df, sites, parameters
#print(df.dtypes)

#parameters = ["Orthophosphate"]
#sites = ["Alder Downstream"]











# In[17]:


def clean_data(df, param):
    sub_df = df.loc[(df['CharacteristicName'] == param)]
    #print(sub_df)
    if not sub_df.empty:
        #unit = sub_df['ResultUnit'].iloc[0]
        sub_df = sub_df.dropna(subset=['ResultValue'])
        sub_df['ResultValue'] = sub_df['ResultValue'].apply(pd.to_numeric)
        return sub_df, param
        #if not sub_df['ResultValue'].isnull().values.all():
        #    create_scatter(sub_df, param, site)
        #    create_line(sub_df, param, site)
        #elif sub_df['ResultValue'].isnull().values.any():
        #    sub_df = sub_df['ResultValue'].dropna()
        #    create_scatter(sub_df, param, site)
        #    create_line(sub_df, param, site)
        #else:
        #    print("No data for the current site and parameter.")
    #else:
    #    print("No data for the current site and parameter.")
    #    return sub_df, site, param
    else:
        #print("No data for the current site and parameter.")
        return sub_df, param

'''
def create_scatter(df, param, site):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(df['ActivityStartDate'], df['ResultValue'])
    unit = df['ResultUnit'].iloc[0]
    if unit != 'None':
        ax.set(xlabel="Date",
               ylabel= f"{param} ({unit})",
               title=f"Plot of data over time for {param} at {site}")
    else:
        ax.set(xlabel="Date",
               ylabel= f"{param}",
               title=f"Plot of data over time for {param} at {site}")

    ax.grid()

    date_form = DateFormatter("%Y-%m")
    ax.xaxis.set_major_formatter(date_form)
    plt.savefig(f"Record of data for {param} at {site}")
    plt.show()

def create_line(df, param, site):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(df['ActivityStartDate'], df['ResultValue'], '-o')
    unit = df['ResultUnit'].iloc[0]
    if unit != 'None':
        ax.set(xlabel="Date",
               ylabel= f"{param} ({unit})",
               title=f"Trend over time for {param} at {site}")
    else:
        ax.set(xlabel="Date",
               ylabel= f"{param}",
               title=f"Trend over time for {param} at {site}")
    ax.grid()

    date_form = DateFormatter("%Y-%m")
    ax.xaxis.set_major_formatter(date_form)
    plt.savefig(f"Trend of data for {param} at {site}")
    plt.show()


# In[12]:
'''

second_file = "ELAHackathon_Datasets_2023\Hackathon Datasets\ACAP-SJ Datasets\ACAP_Saint_John_Nutrients_in_the_lower_Wolastoq_watershed.csv"
#sites, parameters = create_lists()
#print(sites, parameters)
#df = read_data()
#print(df.to_string())
#print(type(df))
#create_plots(df, "Taylor's Brook", "Boron")
#for site in sites:
#    print(site)
#    for param in parameters:
#        print(param)
#        sub_df, watershed, parameter = clean_data(df, site, param)


# In[ ]:
