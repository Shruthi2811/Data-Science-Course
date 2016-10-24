import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('darkgrid')
f1=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1998.csv',nrows=400000)
f2=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\1999.csv',nrows=400000)
f3=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2000.csv',nrows=400000)
f4=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2001.csv',nrows=400000)
f5=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2002.csv',nrows=400000)
f6=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2003.csv',nrows=400000)
f7=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2004.csv',nrows=400000)
f8=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2005.csv',nrows=400000)
f9=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2006.csv',nrows=400000)
f10=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2007.csv',nrows=400000)
f11=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2008.csv',nrows=400000)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f1.ArrDelay.values,f1.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo=[(1.0*md1)/x1]
tu=[(1.0*md2)/x2]
we=[(1.0*md3)/x3]
th=[(1.0*md4)/x4]
fr=[(1.0*md5)/x5]
sa=[(1.0*md6)/x6]
su=[(1.0*md7)/x7]
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f2.ArrDelay.values,f2.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f3.ArrDelay.values,f3.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f4.ArrDelay.values,f4.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f5.ArrDelay.values,f5.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f6.ArrDelay.values,f6.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f7.ArrDelay.values,f7.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f8.ArrDelay.values,f8.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f9.ArrDelay.values,f9.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f10.ArrDelay.values,f10.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
md1=0
md2=0
md3=0
md4=0
md5=0
md6=0
md7=0
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
for i,j in zip(f11.ArrDelay.values,f11.DayOfWeek.values):
    if i>0:
        if j==1:
            md1=md1+i
            x1=x1+1
        elif j==2:
            md2=md2+i
            x2=x2+1
        elif j==3:
            md3=md3+i
            x3=x3+1
        elif j==4:
            md4=md4+i
            x4=x4+1
        elif j==5:
            md5=md5+i
            x5=x5+1
        elif j==6:
            md6=md6+i
            x6=x6+1
        elif j==7:
            md7=md7+i
            x7=x7+1
if x1==0:
    x1=1
if x2==0:
    x2=1
if x3==0:
    x3=1
if x4==0:
    x4=1
if x5==0:
    x5=1
if x6==0:
    x6=1
if x7==0:
    x7=1
mo.append((1.0*md1)/x1)
tu.append((1.0*md2)/x2)
we.append((1.0*md3)/x3)
th.append((1.0*md4)/x4)
fr.append((1.0*md5)/x5)
sa.append((1.0*md6)/x6)
su.append((1.0*md7)/x7)
year=[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008]
ticks=['1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008']
plt.ylabel('Delay Time(mins)')
plt.xlabel('Years')
plt.title('Delay analysis over 10 years for each day of the week')
plt.xlim(1997,2009)
plt.xticks(year,ticks)
plt.text(2008,mo[10],'Monday')
plt.text(2008,tu[10],'Tuesday')
plt.text(2008,we[10],'Wednesday')
plt.text(2008,th[10],'Thursday')
plt.text(2008,fr[10],'Friday')
plt.text(2008,sa[10],'Saturday')
plt.text(2008,su[10],'Sunday')
plt.plot(year,mo)
plt.plot(year,tu)
plt.plot(year,we)
plt.plot(year,th)
plt.plot(year,fr)
plt.plot(year,sa)
plt.plot(year,su)
plt.show()