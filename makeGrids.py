#! /home/hda/anaconda3/bin/python
import scipy as sp
from matplotlib import pyplot as plt
import grid  as grid


grid1 = grid.sGrid()

print(grid1.jmax)

grid1.initKminCurve()

print(grid1.KminCurve)

grid1.redist()

print(grid1.KminCurve)


