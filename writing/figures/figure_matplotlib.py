################################################################################
# PLOTS DATA USING MATPLOTLIB
# Ludovic.charleux@univ-smb.fr june 2020
################################################################################

import numpy as np 
from matplotlib import pyplot as plt  
import pandas as pd 
import os
# Please install: pip install pdfcropmargins 

# MATPLOTLIB / LaTeX SETUP
# FIGURE CONFIGURATION
import matplotlib as mpl
from rcparams import RCPARAMS
mpl.use("pgf")
mpl.rcParams.update(RCPARAMS)
#mpl.style.use('classic')



# FIGURE SIZING
full_width = 190. * 0.0393700787 #6.69 # fig width in inches
full_size_fig = (full_width, full_width /2)
path = "figure_matplotlib"



# DATA 
data = pd.read_csv("../../data/data.csv")
x = data.x.values
ya = data.ya.values
yb = data.yb.values

fig = plt.figure(figsize = full_size_fig)
ax = fig.add_subplot(1,1,1)
ax.minorticks_on()
plt.plot(x, ya, "r-",label = r"$y_a$")
plt.plot(x, yb, "b-", label = r"$y_b$")
plt.fill_between(x, ya, yb, where = ya >= yb, 
                 label = "$y_a \geq y_b$", 
                 alpha = .5, 
                 facecolor = "magenta")
plt.fill_between(x, ya, yb, where = ya < yb, 
                 label = "$y_a < y_b$", 
                 alpha = .5, 
                 facecolor = "green")
ax.grid(which='major', linestyle='--', linewidth='.5', color='gray')
plt.xlim(x.min(), x.max())
plt.legend(loc = "best")
plt.xlabel("Time, $t$ [s]")
plt.ylabel("Amplitude, $y$ [V]")
plt.title(r"Some useless maths: $\zeta = \sum_{i=0}^{+\infty} \kappa_i$")
plt.ylim(-20., 20.)
plt.xlim(5., 10.)
plt.tight_layout() 
plt.savefig(path + "_full.pdf", bbox_inches='tight')
os.system("pdf-crop-margins -mo {0}".format(path + "_full.pdf"))
os.remove(path + "_full_uncropped.pdf")

# SMALL VERSION
fig.set_figwidth(full_width / 2)
fig.set_figheight(full_width / 3)
plt.savefig(path + "_half.pdf", bbox_inches='tight')
os.system("pdf-crop-margins -mo {0}".format(path + "_half.pdf"))
os.remove(path + "_half_uncropped.pdf")
plt.close("all")
