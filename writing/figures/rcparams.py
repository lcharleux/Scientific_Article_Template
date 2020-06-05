################################################################################
# CUSTOMIZATION OF MATPLOTLIB FIGURE FOR QUALITY PRINTING
# Ludovic.charleux@univ-smb.fr june 2017-2020
################################################################################

RCPARAMS = {
  "pgf.texsystem": "xelatex",
  "font.family": "serif", # use serif/main font for text elements
  "text.usetex": True,    # use inline math for ticks
  "pgf.rcfonts": False,   # don't setup fonts from rc parameters
  "pgf.preamble": [
       r"\usepackage{fontspec}",
       r"\usepackage{amsmath}",
       r"\setmainfont{XCharter}", # Charter BT
       ],
  "font.size"       : 10,
  "xtick.labelsize" : 8,
  "ytick.labelsize" : 8,
  "figure.titlesize": "large",
  "axes.labelsize"  : 10,
  "axes.titlesize"  : "large",  # fontsize of the axes title
  "axes.labelpad"   : 0.01,     # space between label and axis
  "axes.labelweight": "normal",  # weight of the x and y labels
  "axes.labelcolor" : "black",
  "axes.xmargin"    : 0.01, #.05,  # x margin.  
  "axes.ymargin"    : 0.05, #.05,  # y margin 
  "axes.spines.left"   : True,   # display axis spines
  "axes.spines.bottom" : True,
  "axes.spines.top"    : True,
  "axes.spines.right"  : True,
}

