import csv
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm 
import pylab as py
import scipy
from scipy.stats import kstest
from statsmodels.tsa.stattools import acf
dane = []
zmiana = []
zmiana_licz = []
dane = []
zmiana = []
zmiana_licz = []
data = []
cena_otw = []
with open('prezentacja2\USD_YUAN.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
      dane.append(lines[1])
      cena_otw.append(lines[1])
      data.append(lines[0])
data = data[1:]
dane = dane [1:] # lista z datami
cena_otw = cena_otw[1:]
cena_otw_l = []
for z in cena_otw:
    cena_otw_l.append(float(z))
   

for i in dane:
    zmiana.append(float(i))

for k in range(len(zmiana)-1):
        zmiana_licz.append( (zmiana[k+1]/zmiana[k]) - 1 )
plt.plot(data,cena_otw_l)
plt.title("Kurs wlutowy USD/CNY")
plt.ylabel("Cena otwarcia")
plt.show()

args = scipy.stats.laplace.fit(zmiana_licz[0:310])
print(kstest(zmiana_licz[0:310],'laplace',args=args))
print(len(zmiana_licz))
print(args)
