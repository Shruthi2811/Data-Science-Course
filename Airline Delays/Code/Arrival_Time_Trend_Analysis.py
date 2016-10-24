import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('darkgrid')
f1=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1987.csv',nrows=400000)
f2=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1988.csv',nrows=400000)
f3=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1989.csv',nrows=400000)
f4=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1990.csv',nrows=400000)
f5=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1991.csv',nrows=400000)
f6=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1992.csv',nrows=400000)
f7=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1993.csv',nrows=400000)
f8=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1994.csv',nrows=400000)
f9=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1995.csv',nrows=400000)
f10=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1996.csv',nrows=400000)
f11=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1997.csv',nrows=400000)
f12=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1998.csv',nrows=400000)
f13=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1999.csv',nrows=400000)
f14=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2000.csv',nrows=400000)
f15=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2001.csv',nrows=400000)
f16=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2002.csv',nrows=400000)
f17=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2003.csv',nrows=400000)
f18=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2004.csv',nrows=400000)
f19=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2005.csv',nrows=400000)
f20=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2006.csv',nrows=400000)
f21=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2007.csv',nrows=400000)
f22=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2008.csv',nrows=400000)
md=0
me=0
x=0
y=0
for i in f1.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf1=(1.0*md)/x
mef1=(1.0*me)/y
md=0
me=0
x=0
y=0
for i in f2.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf2=(1.0*md)/x
mef2=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f3.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf3=(1.0*md)/x
mef3=(1.0*me)/y
md=0
me=0
x=0
y=0
for i in f4.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf4=(1.0*md)/x
mef4=(1.0*me)/y
md=0
me=0
x=0
y=0
for i in f5.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf5=(1.0*md)/x
mef5=(1.0*me)/y
md=0
me=0
x=0
y=0
for i in f6.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf6=(1.0*md)/x
mef6=(1.0*me)/y
md=0
me=0
x=0
y=0
for i in f7.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf7=(1.0*md)/x
mef7=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f8.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf8=(1.0*md)/x
mef8=(1.0*me)/y 
md=0
me=0
x=0
y=0
for i in f9.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf9=(1.0*md)/x
mef9=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f10.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf10=(1.0*md)/x
mef10=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f11.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf11=(1.0*md)/x
mef11=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f12.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf12=(1.0*md)/x
mef12=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f13.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf13=(1.0*md)/x
mef13=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f14.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf14=(1.0*md)/x
mef14=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f15.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf15=(1.0*md)/x
mef15=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f16.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf16=(1.0*md)/x
mef16=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f17.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf17=(1.0*md)/x
mef17=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f18.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf18=(1.0*md)/x
mef18=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f19.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf19=(1.0*md)/x
mef19=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f20.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf20=(1.0*md)/x
mef20=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f21.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf21=(1.0*md)/x
mef21=(1.0*me)/y  
md=0
me=0
x=0
y=0
for i in f22.ArrDelay.values:
    if i>0:
        md=md+i
        x=x+1
    elif i<0:
        me=me+i
        y=y+1
mdf22=(1.0*md)/x
mef22=(1.0*me)/y  
year=[1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008]
ticks=['1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008']
mef=[mef1,mef2,mef3,mef4,mef5,mef6,mef7,mef8,mef9,mef10,mef11,mef12,mef13,mef14,mef15,mef16,mef17,mef18,mef19,mef20,mef21,mef22]
mdf=[mdf1,mdf2,mdf3,mdf4,mdf5,mdf6,mdf7,mdf8,mdf9,mdf10,mdf11,mdf12,mdf13,mdf14,mdf15,mdf16,mdf17,mdf18,mdf19,mdf20,mdf21,mdf22]
plt.ylabel('Time(mins)')
plt.xlabel('Years')
plt.title('1987-2008: Arrival Time Trend Analysis')
plt.xlim(1987,2009)
plt.ylim(-30,50)
plt.xticks(year,ticks,rotation=90)
plt.text(2008,mef22+5,'Early arrival')
plt.text(2008,mdf22+5,'Delayed arrival')
plt.plot(year,mdf)
plt.plot(year,mef)
plt.show()