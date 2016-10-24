import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f1=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2004.csv')
f2=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2005.csv')
f3=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2006.csv')
f4=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2007.csv')
f5=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2008.csv')
cc=[]
a=0
b=0
c=0
d=0
for i in f1.CancellationCode.values:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    elif i=='D':
        d+=1

for i in f2.CancellationCode.values:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    elif i=='D':
        d+=1
for i in f3.CancellationCode.values:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    elif i=='D':
        d+=1
for i in f4.CancellationCode.values:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    elif i=='D':
        d+=1               
for i in f5.CancellationCode.values:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    elif i=='D':
        d+=1                         
t=a+b+c+d
ap=(1.0*a/t)*100
bp=(1.0*b/t)*100
cp=(1.0*c/t)*100
dp=(1.0*d/t)*100
plt.pie([ap,bp,cp,dp],labels=["Carrier","Weather","NAS","Security"],autopct='%0.2f%%')
plt.show()