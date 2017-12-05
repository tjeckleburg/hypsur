#! /home/hda/anaconda3/bin/python
import scipy as sp
from matplotlib import pyplot as plt
import grid  as grid

grid1 = grid.Grid()

print(grid1.jmax_ind)

grid1.defineBoundary(boundary='kmin_cur')

print(grid1.kmin_cur)

