#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:04:30 2020

@author: laura.gf
"""

import pandas as pd
import plotly.express as px
from plotly.io import write_image
# Main script here
# Read the data
all_of_gp = pd.read_csv("data/gapminder_all.csv")

# subset to get data on America
america_data = all_of_gp[all_of_gp['continent']=="Americas"]

# Define a dictionary of labels
label_dictionary = labels={
                    "lifeExp_2007": "Life Expectancy 2007",
                    "gdpPercap_2007":"GDP Per Capita 2007"}
                    
# Create plot
fig = px.scatter(america_data,
                 x="lifeExp_2007",
           y="gdpPercap_2007",
           color='country',
           title='Life expectancy vs GDP Per Capita (2007, America)',
                labels=label_dictionary)
                


fig.html("scatter_plot.png")
