import numpy as np 
import matplotlib.pyplot as plt
#from matplotlib import cm

f1 = np.genfromtxt("bob_season1.dat", 
                         delimiter=' ',
                         dtype=[('aodt', np.float64), ('aod1', np.float64), 
                                ('aod2', np.float64), ('aod3', np.float64)], 
                                usecols=(5,6,7,8))
                                
f2 = np.genfromtxt("arbsea_season1.dat", 
                         delimiter=' ',
                         dtype=[('ao_t', np.float64), ('ao1', np.float64), 
                                ('ao2', np.float64), ('ao3', np.float64)], 
                                usecols=(5,6,7,8)) 

f3 = np.genfromtxt("bob_season2.dat", 
                         delimiter=' ',
                         dtype=[('aodt', np.float64), ('aod1', np.float64), 
                                ('aod2', np.float64), ('aod3', np.float64)], 
                                usecols=(5,6,7,8))
                                
f4 = np.genfromtxt("arbsea_season2.dat", 
                         delimiter=' ',
                         dtype=[('ao_t', np.float64), ('ao1', np.float64), 
                                ('ao2', np.float64), ('ao3', np.float64)], 
                                usecols=(5,6,7,8)) 
f5 = np.genfromtxt("bob_season3.dat", 
                         delimiter=' ',
                         dtype=[('aodt', np.float64), ('aod1', np.float64), 
                                ('aod2', np.float64), ('aod3', np.float64)], 
                                usecols=(5,6,7,8))
                                
f6 = np.genfromtxt("arbsea_season3.dat", 
                         delimiter=' ',
                         dtype=[('ao_t', np.float64), ('ao1', np.float64), 
                                ('ao2', np.float64), ('ao3', np.float64)], 
                                usecols=(5,6,7,8)) 
f7 = np.genfromtxt("bob_season4.dat", 
                         delimiter=' ',
                         dtype=[('aodt', np.float64), ('aod1', np.float64), 
                                ('aod2', np.float64), ('aod3', np.float64)], 
                                usecols=(5,6,7,8))
                                
f8 = np.genfromtxt("arbsea_season4.dat", 
                         delimiter=' ',
                         dtype=[('ao_t', np.float64), ('ao1', np.float64), 
                                ('ao2', np.float64), ('ao3', np.float64)], 
                                usecols=(5,6,7,8)) 



fig1 = plt.figure()

### 
a,b,c,d= (f1['aodt'], f1['aod1'], f1['aod2'], f1['aod3']) 
e,f,g,h, = (f2['ao_t'], f2['ao1'], f2['ao2'], f2['ao3'])

avg1=b/a
avg1_n =avg1/max(avg1)
av1=f/e
av1_n =av1/max(av1)
ax = fig1.add_subplot(3,4,1)
plt.hist(avg1_n,bins=500,histtype='step')
plt.hist(av1_n,bins=500,histtype='step',label='AS')
plt.axis([0,1,0,3500])
plt.ylabel('Finefraction')
plt.title('Winter')

avg2=c/a
avg2_n =avg2/max(avg2)
av2=g/e
av2_n =av2/max(av2)
ax = fig1.add_subplot(3,4,5)
plt.hist(avg2_n,bins=500,histtype='step')
plt.hist(av2_n,bins=500,histtype='step')
plt.axis([0,1,0,5000])
plt.ylabel('coarse Spherical fraction')

avg3=d/a
avg3_n =avg3/max(avg3)
av3=h/e
av3_n =av3/max(av3)
ax = fig1.add_subplot(3,4,9)
plt.hist(avg3_n,bins=500,histtype='step')
plt.hist(av3_n,bins=500,histtype='step')
plt.axis([0,1,0,3500])
plt.ylabel('C_non sphericalfraction')
###

### 
i,j,k,l= (f3['aodt'], f3['aod1'], f3['aod2'], f3['aod3']) 
m,n,o,p, = (f4['ao_t'], f4['ao1'], f4['ao2'], f4['ao3'])

avg1=j/i
avg1_n =avg1/max(avg1)
av1=n/m
av1_n =av1/max(av1)
ax = fig1.add_subplot(3,4,2)
plt.hist(avg1_n,bins=500,histtype='step')
plt.hist(av1_n,bins=500,histtype='step')
plt.axis([0,1,0,5000])
#plt.ylabel('Fine')
plt.title('Pre Monsoon')

avg2=k/i
avg2_n =avg2/max(avg2)
av2=o/m
av2_n =av2/max(av2)
ax = fig1.add_subplot(3,4,6)
plt.hist(avg2_n,bins=500,histtype='step')
plt.hist(av2_n,bins=500,histtype='step')
plt.axis([0,1,0,10100])
#plt.ylabel('coarse Spherical')

avg3=l/i
avg3_n =avg3/max(avg3)
av3=p/m
av3_n =av3/max(av3)
ax = fig1.add_subplot(3,4,10)
plt.hist(avg3_n,bins=500,histtype='step')
plt.hist(av3_n,bins=500,histtype='step')
plt.axis([0,1,0,5000])
#plt.ylabel('coarse non spherical')
###

### 
q,r,s,t= (f5['aodt'], f5['aod1'], f5['aod2'], f5['aod3']) 
u,v,w,x, = (f6['ao_t'], f6['ao1'], f6['ao2'], f6['ao3'])

avg1=r/q
avg1_n =avg1/max(avg1)
av1=v/u
av1_n =av1/max(av1)
ax = fig1.add_subplot(3,4,3)
plt.hist(avg1_n,bins=500,histtype='step')
plt.hist(av1_n,bins=500,histtype='step')
plt.axis([0,1,0,4000])
#plt.ylabel('Fine')
plt.title('Monsoon')

avg2=s/q
avg2_n =avg2/max(avg2)
av2=w/u
av2_n =av2/max(av2)
ax = fig1.add_subplot(3,4,7)
plt.hist(avg2_n,bins=500,histtype='step')
plt.hist(av2_n,bins=500,histtype='step')
plt.axis([0,1,0,6000])
#plt.ylabel('coarse Spherical')

avg3=t/q
avg3_n =avg3/max(avg3)
av3=x/u
av3_n =av3/max(av3)
ax = fig1.add_subplot(3,4,11)
plt.hist(avg3_n,bins=500,histtype='step')
plt.hist(av3_n,bins=500,histtype='step')
plt.axis([0,1,0,3000])
#plt.ylabel('coarse non spherical')
###

### 
y,z,aa,bb= (f7['aodt'], f7['aod1'], f7['aod2'], f7['aod3']) 
cc,dd,ee,ff = (f8['ao_t'], f8['ao1'], f8['ao2'], f8['ao3'])

avg1=z/y
avg1_n =avg1/max(avg1)
av1=dd/cc
av1_n =av1/max(av1)
ax = fig1.add_subplot(3,4,4)
plt.hist(avg1_n,bins=500,histtype='step')
plt.hist(av1_n,bins=500,histtype='step')
plt.axis([0,1,0,4000])
#plt.ylabel('Fine')
plt.title('PostMonsoon')

avg2=aa/y
avg2_n =avg2/max(avg2)
av2=ee/cc
av2_n =av2/max(av2)
ax = fig1.add_subplot(3,4,8)
plt.hist(avg2_n,bins=500,histtype='step')
plt.hist(av2_n,bins=500,histtype='step')
plt.axis([0,1,0,6000])
#plt.ylabel('coarse Spherical')

avg3=bb/y
avg3_n =avg3/max(avg3)
av3=ff/cc
av3_n =av3/max(av3)
ax = fig1.add_subplot(3,4,12)
plt.hist(avg3_n,bins=500,histtype='step',label="BOB")
plt.hist(av3_n,bins=500,histtype='step',label="AS")
plt.axis([0,1,0,4500])
#plt.ylabel('coarse non spherical')
###
avg2_n.annotate('B')
av2.annotate('A')

plt.legend(loc="upper right")
plt.show()