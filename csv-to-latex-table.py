# csv file to LaTeX table
# you can copy the printed table and insert it in your LaTeX document

import numpy as np
import pandas as pd

#import data
name= "A04_ergebnisse"
path = f"K:/work/Physikpraktikum/A02/{name}_rounded"
df = pd.read_csv(f"{path}.csv", header=None) #set header to None if data starts in first line of document
data = df.to_numpy() #convert pandas data frame to numpy array

#data
x = data[:,0]
y1 = data[:,1]
#errors
xerr = data[:,2]
y1err = data[:,3]

#print data and errors in right order with LaTeX-ready syntax
for i in range(0, len(x)):
    s = f"{x[i]} & {y1[i]} & {xerr[i]} & {y1err[i]} //"
    print(s)
