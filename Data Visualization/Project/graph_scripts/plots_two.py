# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:40:50 2016

@author: anirudhkm
"""

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import court
from sys import argv

def get_plot_traces_by_season(df, trace_list, season = 'all'):
    """
    This function returns the traces for 
    plots hits and misses for the given
    season.
    Argument:
    1. df: The input dataframe.
    2. trace_list: To keep track of traces.
    2. season: The season defaulted to "all".
    """
    
    if season == 'all':
        sub_df = df
    else:
        sub_df = df[df.index == season]
        # get the subset
    
    trace0 = go.Scatter(
    x = sub_df['loc_x'][sub_df['shot_made_flag'] == 1],
    y = sub_df['loc_y'][sub_df['shot_made_flag'] == 1],
    mode = 'markers',
    name = 'Hit',
    marker = dict(size = 15, color = 'rgba(22, 161, 6, 0.9)')
    )
    
    trace1 = go.Scatter(
    x = sub_df['loc_x'][sub_df['shot_made_flag'] == 0],
    y = sub_df['loc_y'][sub_df['shot_made_flag'] == 0],
    mode = 'markers',
    name = 'Miss',
    marker = dict(size = 15, color = 'rgba(210, 0, 50, 0.9)')
    )
    
    trace_list.append(trace0)
    trace_list.append(trace1)
    # append traces to list
    
def scatter_plot_location(df):
    """
    This function helps to plot the 
    scatter plot of the location played
    by Kobe Bryant.
    Argument:
    1. df: The pandas dataframe.
    """
    
    trace_list = []
    # empty list to add traces
    get_plot_traces_by_season(df, trace_list)
    # get traces for all seasons
    get_plot_traces_by_season(df, trace_list, '1996/97')
    # get data for season 1996-97
    get_plot_traces_by_season(df, trace_list, '1997/98')
    # get data for season 1997-98
    get_plot_traces_by_season(df, trace_list, '1998/99')
    # get data for season 1998-99
    get_plot_traces_by_season(df, trace_list, '1999/00')
    # get data for season 1999-00
    get_plot_traces_by_season(df, trace_list, '2000/01')
    # get data for season 2000-01
    get_plot_traces_by_season(df, trace_list, '2001/02')
    # get data for season 2001-02
    get_plot_traces_by_season(df, trace_list, '2002/03')
    # get data for season 2002-03
    get_plot_traces_by_season(df, trace_list, '2003/04')
    # get data for season 2003-04
    get_plot_traces_by_season(df, trace_list, '2004/05')
    # get data for season 2004-05
    get_plot_traces_by_season(df, trace_list, '2005/06')
    # get data for season 2005-06
    get_plot_traces_by_season(df, trace_list, '2006/07')
    # get data for season 2006-07
    get_plot_traces_by_season(df, trace_list, '2007/08')
    # get data for season 2007-08
    get_plot_traces_by_season(df, trace_list, '2008/09')
    # get data for season 2008-09
    get_plot_traces_by_season(df, trace_list, '2009/10')
    # get data for season 2009-10
    get_plot_traces_by_season(df, trace_list, '2010/11')
    # get data for season 2010-11
    get_plot_traces_by_season(df, trace_list, '2011/12')
    # get data for season 2011-12
    get_plot_traces_by_season(df, trace_list, '2012/13')
    # get data for season 2012-13
    get_plot_traces_by_season(df, trace_list, '2013/14')
    # get data for season 2013-14
    get_plot_traces_by_season(df, trace_list, '2014/15')
    # get data for season 2014-15
    get_plot_traces_by_season(df, trace_list, '2015/16')
    # get data for season 2015-16
    data = go.Data(trace_list)
    # data to be plotted
    layout = go.Layout(
    xaxis = dict(showgrid = False, range = [-300, 300]),
    # define the xaxis ranges
    yaxis = dict(showgrid = False, range = [-100, 500]),
    # define the yaxis ranges
    height = 600,
    width = 650,
    plot_bgcolor = 'rgba(182, 144, 77, 1)',
    showlegend = False,
    title = 'Shot location of Kobe Bryant',
    titlefont = dict(family = 'Arial, sans-serif', size = 45, color = 'black'),
    shapes = court.main(),
    updatemenus = list([
                  dict(
                      x = -250,
                      y = 400,
                      buttons = list([
                                      dict(
                                      args = ['invisible', [False]*2 + [False]*40],
                                      label = 'All seasons',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*2 + [True]*2 + [False]*38],
                                      label = '1996-97',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*4 + [True]*2 + [False]*36],
                                      label = '1997-98',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*6 + [True]*2 + [False]*34],
                                      label = '1998-99',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*8 + [True]*2 + [False]*32],
                                      label = '1999-00',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*10 + [True]*2 + [False]*30],
                                      label = '2000-01',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*12 + [True]*2 + [False]*28],
                                      label = '2001-02',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*14 + [True]*2 + [False]*26],
                                      label = '2002-03',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*16 + [True]*2 + [False]*24],
                                      label = '2003-04',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*18 + [True]*2 + [False]*22],
                                      label = '2004-05',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*20 + [True]*2 + [False]*20],
                                      label = '2005-06',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*22 + [True]*2 + [False]*18],
                                      label = '2006-07',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*24 + [True]*2 + [False]*16],
                                      label = '2007-08',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*26 + [True]*2 + [False]*14],
                                      label = '2008-09',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*28 + [True]*2 + [False]*12],
                                      label = '2009-10',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*30 + [True]*2 + [False]*10],
                                      label = '2010-11',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*32 + [True]*2 + [False]*8],
                                      label = '2011-12',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*34 + [True]*2 + [False]*6],
                                      label = '2012-13',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*36 + [True]*2 + [False]*4],
                                      label = '2013-14',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*38 + [True]*2 + [False]*2],
                                      label = '2014-15',
                                      method = 'restyle'
                                      ),
                                      dict(
                                      args = ['visible', [False]*40 + [False]*2],
                                      label = '2015-16',
                                      method = 'restyle'
                                      ),
                                      ]))]))
    # define the layout
    fig = go.Figure(data = data, layout = layout)
    # fig to be plotted
    py.plot(fig, filename = 'scatter')
    
    
def main(inp_file):
    """
    This function serves as the 
    heart of the program.
    Argument:
    1. inp_file: Input file name as a string.
    """
    
    df = pd.read_csv(inp_file, index_col = 'season')
    # read the input file as pandas dataframe
    scatter_plot_location(df)
    # func call to plot data

if __name__ == '__main__':
    # start of main program
    inp_file = 'data_two.csv'
    # get the input file as sys argv
    main(inp_file)
    # main function call
