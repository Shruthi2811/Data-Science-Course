# -*- coding: utf-8 -*-
"""
Name: Anirudh K Muralidhar
Masters in Data Science, Indiana University
start date: 15th Oct, 2016
Objective: Plot various graphs in order to 
analyse the perform of Kobe Bryant.
"""

import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from sys import argv

def hit_and_miss_data_plot(df):
    """
    This function helps to plot the
    hit and miss percentage data across
    various seasons.
    """
    
    sub_df = df[['hits', 'misses', 'total_shots']]
    # get the subset required to plot data
    sub_df.drop_duplicates(inplace = True)
    # drop the duplicate values
    x = sub_df.index
    # get the x-axis of the plots
    trace0 = go.Scatter(
    x = x,
    # seasons
    y = sub_df['hits']*100/sub_df['total_shots'],
    # hit percent in each season
    mode = 'lines+markers',
    # define the scatter mode
    name = 'Shots made(%)',
    # define name
    text = 'Shot played: ' + sub_df['total_shots'].astype(str),
    # add text hover
    marker = dict(size = 10, color = 'rgba(0, 255, 0, 1)', line = {'width':2})
    # customize the lines and marker
    )
    
    trace1 = go.Scatter(
    x = x,
    # seasons
    y = sub_df['misses']*100/sub_df['total_shots'],
    # miss percent in each season
    mode = 'lines+markers',
    # define the scatter mode
    name = 'Shots missed(%)',
    # define name
    text = 'Shot played: ' + sub_df['total_shots'].astype(str),
    # add text hover
    marker = dict(size = 10, color = 'rgba(255, 0, 0, 1)', line = {'width':2})
    # customize the lines and marker
    )

    layout = go.Layout(
    title = "Kobe Bryant's accuracy trend Analysis",
    titlefont = dict(family = 'Arial, sans-serif', size = 30, color = 'black'),
    autosize = False,
    width = 20,
    height = 20,
    # add plot title
    hovermode = 'closest',
    xaxis = dict(title = 'Seasons', 
                 ticklen = 5,
                 zeroline = False,
                 titlefont = dict(family = 'Arial, sans-serif', size = 25,
                                  color = 'black'),
                 tickangle = 55,
                 tickfont = dict(family = 'Old Standard TT, serif', size = 12, color = 'black')),
    # customize x-axis
    yaxis = dict(title = 'Percentage values',
                 ticklen = 10,
                 zeroline = False,
                 titlefont = dict(family = 'Arial, sans-serif', size = 25,
                                  color = 'black'),
                 tickfont = dict(family = 'Old Standard TT, serif', size = 12, color = 'black'))
    # customize y-axis
    )
    
    data = [trace0, trace1]
    # data to be plotted
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename = 'hit')
    
    
def main(inp_file):
    """
    This function serves as the heart of the 
    program.
    Arguments:
    1. inp_file: The input file name in string.
    """
    
    df = pd.read_csv(inp_file, index_col = 'season')
    # read the input file in pandas dataframe
    hit_and_miss_data_plot(df)
    # func call to plot hit and miss data
    

if __name__ == '__main__':
    # start of main program
    inp_file =  'data_two.csv'
    # get the input file as a sys argv
    main(inp_file)
    # main func call

