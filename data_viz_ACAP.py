#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.dates import DateFormatter


# In[3]:


def create_lists(file = 'ELAHackathon_Datasets_2023\ELAHackathon_Metadata_2023.csv'):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        i = 0
        for row in reader:
            i += 1
            if i >= 5 and i <= 9:
                if i == 5:
                    parameters = []
                    for j in range(len(row)):
                        if row[j] == 'Parameters':
                            for k in range(j+1, len(row)):
                                parameters.append(row[k])
                if i == 7:
                    sites = []
                    for j in range(len(row)):
                        if row[j] == 'Sites':
                            for k in range(j+1, len(row)):
                                sites.append(row[k])
    #print(len(parameters), parameters, sites)

    i = 0

    for j in range(len(parameters)):
        if  parameters[j] == '':
            i = j
            break
        #print(i, type(i))
    del parameters[i:]

    #print(len(parameters))
    
    return sites, parameters


#parameters[parameters != '']


# In[4]:


def read_data(file = 'ELAHackathon_Datasets_2023\Hackathon Datasets\ACAP-SJ Datasets\ACAP_Saint_John_Community-Based_Water_Monitoring_Program.csv'):

    df= pd.read_csv(file, delimiter = ',', dtype = 'object')
    column_names = df.columns.to_list()
#print(column_names)
    keep_cols = ['MonitoringLocationName', 'MonitoringLocationType', 'ActivityStartDate', 'ActivityEndDate', 'CharacteristicName',              'MethodSpeciation', 'ResultValue', 'ResultUnit']

    for col in column_names:
        if col not in keep_cols:
        #print(col)
            df.drop(columns = col, axis = 'columns', inplace = True)

    df[['ActivityStartDate', 'ActivityEndDate']] = df[['ActivityStartDate', 'ActivityEndDate']].apply(pd.to_datetime)
    
    return df
#print(df.dtypes)

#parameters = ["Orthophosphate"]
#sites = ["Alder Downstream"]


            
    







# In[24]:


def create_plots(df, site, param):
    sub_df = df.loc[(df['MonitoringLocationName'] == site) & (df['CharacteristicName'] == param)]
    #print(sub_df)
    if not sub_df.empty:
        #unit = sub_df['ResultUnit'].iloc[0]
        sub_df = sub_df.dropna(subset=['ResultValue'])
        sub_df['ResultValue'] = sub_df['ResultValue'].apply(pd.to_numeric)
        if not sub_df['ResultValue'].isnull().values.all():
            create_scatter(sub_df, param, site)
            create_line(sub_df, param, site)
        elif sub_df['ResultValue'].isnull().values.any():
            sub_df = sub_df['ResultValue'].dropna()
            create_scatter(sub_df, param, site)
            create_line(sub_df, param, site)
        else:
            print("No data for the current site and parameter.")
    else:
        print("No data for the current site and parameter.")
    return sub_df
        

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
    plt.show()


# In[27]:


second_file = "ELAHackathon_Datasets_2023\Hackathon Datasets\ACAP-SJ Datasets\ACAP_Saint_John_Nutrients_in_the_lower_Wolastoq_watershed.csv"
df = read_data(second_file)
#print(type(df))
create_plots(df, "Taylor's Brook", "Boron")


# In[ ]:




