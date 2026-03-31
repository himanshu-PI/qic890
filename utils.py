import stim 
import pymatching
import numpy as np
from gates import * 

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Google Sans'
plt.rcParams['text.color'] = 'k'
plt.rcParams['axes.labelcolor'] = 'k'
plt.rcParams['text.usetex'] = False
google = ["#0077b6","#34a853","#fbbc04","#ea4335","#9aa0a6"]


marks = [
    '.',  # point
    ',',  # pixel
    'o',  # circle
    'v',  # triangle_down
    '^',  # triangle_up
    '<',  # triangle_left
    '>',  # triangle_right
    '1',  # tri_down
    '2',  # tri_up
    '3',  # tri_left
    '4',  # tri_right
    '8',  # octagon
    's',  # square
    'p',  # pentagon
    'P',  # plus (filled)
    '*',  # star
    'h',  # hexagon1
    'H',  # hexagon2
    '+',  # plus
    'x',  # x
    'X',  # x (filled)
    'D',  # diamond
    'd',  # thin_diamond
    '|',  # vline
    '_',  # hline
]
