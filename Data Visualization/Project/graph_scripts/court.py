# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:49:54 2016
@author: anirudhkm, Indiana University
Objective: To create a basketball court which helps
us in enhanced visualization

"""

import plotly.plotly as py
import plotly.graph_objs as go

def draw_outer_boundary():
    """
    This function helps to design the 
    outer boundary of the basketball court.
    The values are stored in a dictionary and
    returned.
    """
    
    outer_bound_dict = {
    'type' : 'rect',
    'xref' : 'x',
    'yref' : 'y',
    'x0' : -250,
    'y0' : -50,
    'x1' : 250,
    'y1' : 470,
    'line' : {'color' : 'rgba(255,255,255,1)', 'width' : 5}
    }
    
    return outer_bound_dict
    
def draw_basket_hoop():
    """
    This function helps to design the
    basketball hoop circle. The values
    are stored in a dictionary and returned.
    """
    
    hoop = {
    'type':'circle',
    'xref':'x',
    'yref':'y',
    'x0':7.5,
    'y0':7.5,
    'x1':-7.5,
    'y1':-7.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}}
    return hoop
    
def draw_basket_backboard():
    """
    This function helps to design the
    basketball backboard. The values
    are stored in a dictionary and returned.
    """
    
    backboard = {
    'type':'rect',
    'xref':'x',
    'yref':'y',
    'x0':-30,
    'y0':-7.5,
    'x1':30,
    'y1':-6.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5},
    'fillcolor':'rgba(255,255,255,1)'
    }
    
    return backboard

def draw_outer_three_sec_area():
    """
    This function helps to design the
    outer three second area. The values
    are stored in a dictionary and returned.
    """
    
    outer_three_sec_area = {
    'type':'rect',
    'xref':'x',
    'yref':'y',
    'x0':-80,
    'y0':-47.5,
    'x1':80,
    'y1':143.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5},
    
    }
    
    return outer_three_sec_area
    
def draw_inner_three_sec_area():
    """
    This function helps to design the
    inner three second area. The values
    are stored in a dictionary and returned.
    """
    
    inner_three_sec_area = {
    'type':'rect',
    'xref':'x',
    'yref':'y',
    'x0':-60,
    'y0':-47.5,
    'x1':60,
    'y1':143.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5},
    }
    
    return inner_three_sec_area

def draw_left_line():
    """
    This function helps to design the
    left line. The values
    are stored in a dictionary and returned.
    """
    
    left_line = {
    'type':'rect',
    'xref':'x',
    'yref':'y',
    'x0':-220,
    'y0':-47.5,
    'x1':-220,
    'y1':92.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}
    }
    
    return left_line

def draw_right_line():
    """
    This function helps to design the
    right line. The values
    are stored in a dictionary and returned.
    """
    
    right_line = {
    'type':'rect',
    'xref':'x',
    'yref':'y',
    'x0':220,
    'y0':-47.5,
    'x1':220,
    'y1':92.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}
    }
    
    return right_line

def draw_three_point_arc():
    """
    This function helps to design the
    three point arc. The values
    are stored in a dictionary and returned.
    """
    
    three_point_arc = {
    'type':'path',
    'xref':'x',
    'yref':'y',
    'path':'M -220 92.5 C -70 300, 70 300, 220 92.5',
    'line':{'color':'rgba(255,255,255,1)', 'width':5},
    }
    
    return three_point_arc

def draw_center_cirle():
    """
    This function helps to design the
    center circle. The values
    are stored in a dictionary and returned.
    """
    
    center_circle = {
    'type':'circle',
    'xref':'x',
    'yref':'y',
    'x0':60,
    'y0':482.5,
    'x1':-60,
    'y1':362.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}
    }
    
    return center_circle
    
def draw_restraining_cirle():
    """
    This function helps to design the
    restraining circle. The values
    are stored in a dictionary and returned.
    """
    
    rest_circle = {
    'type':'circle',
    'xref':'x',
    'yref':'y',
    'x0':20,
    'y0':442.5,
    'x1':-20,
    'y1':402.5,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}
    }
    
    return rest_circle
    
def draw_free_throw_circle():
    """
    This function helps to design the
    free throw circle. The values
    are stored in a dictionary and returned.
    """
    
    free_throw_circle = {
    'type':'circle',
    'xref':'x',
    'yref':'y',
    'x0':60,
    'y0':200,
    'x1':-60,
    'y1':80,
    'line':{'color':'rgba(255,255,255,1)', 'width':5}
    }
    
    return free_throw_circle
    
def draw_restricted_circle():
    """
    This function helps to design the
    restricted area circle. The values
    are stored in a dictionary and returned.
    """
    
    restrict_circle = {
    'type':'circle',
    'xref':'x',
    'yref':'y',
    'x0':40,
    'y0':40,
    'x1':-40,
    'y1':-40,
    'line':{'color':'rgba(255,255,255,1)', 'width':5, 'dash':'dot'}
    }
    
    return restrict_circle
    
    
def main():
    """
    This function serves as the
    heart of the program.
    """
    
    obj_list = []
    # empty list which holds various items
    outer_boundary = draw_outer_boundary()
    # function call to draw outer boundary
    obj_list.append(outer_boundary)
    # append object to list
    hoop = draw_basket_hoop()
    # function call to draw basket hoop
    obj_list.append(hoop)
    # append object to list
    backboard = draw_basket_backboard()
    # func call to draw basket backboard
    obj_list.append(backboard)
    # add object to list
    outer_three_sec_area = draw_outer_three_sec_area()
    # func call to draw outer three second area
    obj_list.append(outer_three_sec_area)
    # append object to the list
    inner_three_sec_area = draw_inner_three_sec_area()
    # func call to draw inner three second area
    obj_list.append(inner_three_sec_area)
    # append object to list
    left_line = draw_left_line()
    # func call to draw left line
    obj_list.append(left_line)
    # append object to list
    right_line = draw_right_line()
    # func call to draw left line
    obj_list.append(right_line)
    # append object to list
    three_point_arc = draw_three_point_arc()
    # func call to draw the three point arc
    obj_list.append(three_point_arc)
    # add object to list
    center_circle = draw_center_cirle()
    # func call to draw center circle
    obj_list.append(center_circle)
    # append object to list
    restraining_cirle = draw_restraining_cirle()
    # func call to draw restraining circle
    obj_list.append(restraining_cirle)
    # append object to list
    free_throw_circle = draw_free_throw_circle()
    # func call to draw free throw circle
    obj_list.append(free_throw_circle)
    # add object to list
    restricted_area = draw_restricted_circle()
    # func call to draw restricted area
    obj_list.append(restricted_area)
    # add obj to list
    return obj_list
