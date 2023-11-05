'''
Graph functions x^a for values of a near -1,
and the antiderivatives of these functions (ln x when a=-1)
'''
import time

print ("   WC =", time.perf_counter(), "  PT = ", time.process_time())
stimeWC = time.perf_counter()   # wall clock
stimePT = time.process_time()   # processor time

import matplotlib.pyplot as plt
import numpy as np

xlo = 0.2; xhi = 8.0
xList = np.linspace(xlo,xhi,40)
#print ("xList...", xList)
pvar = 0.2     # variation from -1
pwr1 = -1 + pvar
pwr2 = -1 - pvar
#displ = 1.0**(pwr1+1) / (pwr1+1) - np.log(1.0)
displ = 1.0 / (pwr1 + 1) 
print("displ:", displ)

def antideriv(x,p):     # antiderivative of x^p
    if p == -1:
        adx = np.log(x) 
    else:    
        adx = x**(p+1) / (p+1)
        if p < -1: adx += displ
        else: adx -= displ
    return (adx)

def plotfxafx(P,clr):
    yList = (xList)**P
    plt.plot(xList,yList,'--',c=clr,label=("x^"+str(P)))
    yList = antideriv(xList,P)
    #print ("yList...", yList)
    plt.plot(xList,yList,c=clr)
    
plt.close('all')

plotfxafx(-1,'green')       # 1/x and its antideriv
plotfxafx(pwr1,'orange')    # x^p1  "       "
plotfxafx(pwr2,'red')       # x^p2  "       "

plt.legend()
plt.ylim([-6, 6])   
plt.grid() 
plt.show()

print ("   WC =", time.perf_counter(), "  PT = ", time.process_time())
etimeWC = time.perf_counter()   # wall clock
etimePT = time.process_time()   # processor time
print ("Durtn WC =", (etimeWC - stimeWC))
print ("Durtn PT =", (etimePT - stimePT))

print ("==="*18)
