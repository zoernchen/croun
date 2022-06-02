# csv file to LaTeX table

import numpy as np
import pandas as pd
import math
from decimal import *
import csv

name= "A04_ergebnisse"
path = f"K:/work/Physikpraktikum/A02/{name}_rounded"
df = pd.read_csv(f"{path}.csv", header=None) #set header to None if data starts in first line of document
data = df.to_numpy() #convert pandas data frame to numpy array

x = data[:,0]
y1 = data[:,1]

xerr = data[:,2]
y1err = data[:,3]

for i in range(0, len(x)):
    s = f"{x[i]} & {y1[i]} & {xerr[i]} & {y1err[i]} //"
    print(s)