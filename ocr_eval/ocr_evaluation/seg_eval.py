
# coding: utf-8

# In[75]:

from numpy import *
import sys
#Import the data from the user
ev = loadtxt(sys.argv[1])
#Import the data from the ground truth
gt = loadtxt(sys.argv[2])
#print(gt)
#print(ev)
su=size(ev)/4
sg=size(gt)/4


# In[76]:

A=zeros((sg,su))
i=0
for x1,y1,w1,h1 in gt:
    j=0
    for x2,y2,w2,h2 in ev:
        xa=x1+w1
        xb=x2+w2
        ya=y1-h1
        yb=y2-h2
        t1=max(x1,x2)
        t2=min(xa,xb)
        r1=min(y1,y2)
        r2=max(ya,yb)
        if(t1<xa and t1<xb and r1>ya and r1>yb):
            area=(t1-t2)*(r2-r1)
        else:
            area=0
        if (area>0.25*min(w1*h1,w2*h2)):
            A[i][j]=1;
        j+=1
    i+=1
A


# In[78]:

#fd=false detection
#miss=missed detection
#us=total under-segmentations
#usc=total under-segmented components
#os=total over-segmentations
#osc=total over-segmented components
#cs=correct segmentations
fd=miss=us=usc=os=osc=cs=0
if(su==0):
    miss=sg
elif(sg==0):
    fd=su
else:
    fd=sum(sum(A,axis=0)==0)
    miss=sum(sum(A,axis=1)==0)
    
    temp=sum(A,axis=0)-1
    usc=sum(temp>0)
    us=sum(temp*(temp>0))
    
    temp=sum(A,axis=1)-1
    osc=sum(temp>0)
    os=sum(temp*(temp>0))
    
    t1=(sum(A,axis=0)==1).astype(int).reshape(1,su)
    t2=(sum(A,axis=1)==1).astype(int).reshape(sg,1)
    cs=sum(A*t1*t2)
    print fd,miss,usc,us,osc,os,cs


# In[ ]:



