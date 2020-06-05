################################################################################
# CREATE DUMMY DATA
# Ludovic.charleux@univ-smb.fr june 2020
################################################################################

# PACKAGES
import numpy as np
import pandas as pd

# DATA
x = np.linspace(5., 10., 1000)   
ya = np.sin(np.pi/2. * x**2) * x**1.3
yb = np.cos(np.pi * x /5.) * ya
data = pd.DataFrame()
data["x"] = x
data["ya"] = ya
data["yb"] = yb
data.to_csv("../data/data.csv", index= False)
 

