import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f1=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2004.csv')
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
t=a+b+c+d
ap=(1.0*a/t)*100
bp=(1.0*b/t)*100
cp=(1.0*c/t)*100
dp=(1.0*d/t)*100
carr=[ap]
weath=[bp]
nas=[cp]
sec=[dp]
f2=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2005.csv')
a=0
b=0
c=0
d=0
for i in f2.CancellationCode.values:
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
carr.append(ap)
weath.append(bp)
nas.append(cp)
sec.append(dp)
f3=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2006.csv')
a=0
b=0
c=0
d=0
for i in f3.CancellationCode.values:
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
carr.append(ap)
weath.append(bp)
nas.append(cp)
sec.append(dp)
f4=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2007.csv')
a=0
b=0
c=0
d=0
for i in f4.CancellationCode.values:
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
carr.append(ap)
weath.append(bp)
nas.append(cp)
sec.append(dp)
f5=pd.read_csv(r'C:\Users\Disha\Documents\Big Data Analytics and Applications\project\2008.csv')
a=0
b=0
c=0
d=0
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
carr.append(ap)
weath.append(bp)
nas.append(cp)
sec.append(dp)
N=5
ind = np.arange(N)  
width = 0.1  
p = plt.subplot()
b1=p.bar(ind, carr, width, color='r')
b2 = p.bar(ind+width, weath, width, color='y')
b3=p.bar(ind+width+width, nas, width, color='b')
b4 = p.bar(ind+width+width+width, sec, width, color='g')
p.set_ylabel('Flight cancellations made(%)')
p.set_title('Flight cancellation reasons')
p.set_xticks(ind + width)
p.set_xticklabels(('2004', '2005', '2006', '2007', '2008'))
p.legend((b1[0], b2[0],b3[0],b4[0]), ('Carrier', 'Weather','NAS','Security'))
def autolabel(bp):
    for l in bp:
        height = l.get_height()
        p.text(l.get_x() + l.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(b1)
autolabel(b2)
autolabel(b3)
autolabel(b4)
plt.show()