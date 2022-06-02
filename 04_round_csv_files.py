# rounding data in .csv files correctly
import numpy as np
import pandas as pd
import math
from decimal import *
import csv

#import custom rounding file croun
import croun as cr

name= "A04_ergebnisse"
path = f"K:/work/Physikpraktikum/A02/{name}"
df = pd.read_csv(f"{path}.csv", header=None) #set header to None if data starts in first line of document
data = df.to_numpy() #convert pandas data frame to numpy array
#print(data)

# this assumes the first column is the x- data followed by the y1, y2, ... data
# in the same scheme in the same row follow the errors: xerr, y1err, y2err ....

#number of columns c
c = 4

x = data[:,0]
y1 = data[:,1]

print(x)

xerr = data[:,2]
y1err = data[:,3]

rxerr=([])
ry1err=([])
for i in range(0, len(xerr)):
    r = cr.prnd(xerr[i])
    t = cr.prnd(y1err[i])
    rxerr.append(r)
    ry1err.append(t)

xk =([])
y1k = ([])
for n in range(0, len(rxerr)):
    k = cr.getk(rxerr[n])
    l = cr.getk(ry1err[n])
    xk.append(k)
    y1k.append(l)

rx = ([])
ry1 = ([])
for s in range(0,len(x)):
    a = cr.rnd(x[s], xk[s])
    b = cr.rnd(y1[s], y1k[s])
    rx.append(a)
    ry1.append(b)


rdata = np.stack((rx, ry1, rxerr, ry1err), axis=1)

fields = (["frequency", "amplitude", "f-err", "amp-err"])

filename= f"{path}{name}_rounded.csv"



# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields as header
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rdata)
