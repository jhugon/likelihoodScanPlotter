#!/usr/bin/env python

from scipy import *
import matplotlib.pyplot as mpl
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

VEV=246.
MMU=0.1056583715
MTOP=173.07
MBOT=4.18
MTAU=1.77682

def getK(l,m):
    return 1. + 2 * VEV**3 / (m * l**2)
def getMu(l,m):
    return getK(l,m)**2
def getL(mu,m):
    result = 2 * VEV**3
    result /= m * ( mu**(0.5) - 1 )
    return sqrt(result)

lambdaTest = logspace(2.,6.,num=10000)
muTest = linspace(1.02,20,num=200)

muResult = [getMu(i,MMU)-1. for i in lambdaTest]
topMuResult = [getMu(i,MTOP)-1. for i in lambdaTest]
botMuResult = [getMu(i,MBOT)-1. for i in lambdaTest]
tauMuResult = [getMu(i,MTAU)-1. for i in lambdaTest]

lambdaResult = [getL(i,MMU) for i in muTest]
topLambdaResult = [getL(i,MTOP) for i in muTest]
botLambdaResult = [getL(i,MBOT) for i in muTest]
tauLambdaResult = [getL(i,MTAU) for i in muTest]

fig = mpl.figure(figsize=(16,8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_xlabel("$\mu$")
ax1.set_ylabel("$\Lambda$ [GeV/c$^2$]")
ax2.set_xlabel("$\Lambda$ [GeV/c$^2$]")
ax2.set_ylabel("$\mu-1$")
ax2.set_xlim(1e2,1e5)
ax2.set_ylim(0.0,2.)
#ax2.ticklabel_format(style='sci',scilimits=(-3,4),axis='x')

ax1.semilogy(muTest,lambdaResult,'r-')
ax1.semilogy(muTest,topLambdaResult,'g-')
ax1.semilogy(muTest,botLambdaResult,'c-')
ax1.semilogy(muTest,tauLambdaResult,'b-')

annoX = 5.
shiftY = 1.2
shiftY = 1.
ax1.annotate(r"$H\rightarrow\mu\mu$",xy=(annoX,getL(annoX,MMU)*shiftY),color='r',ha='left',va='bottom')
ax1.annotate(r"$H\rightarrow\tau\tau$",xy=(annoX,getL(annoX,MTAU)*shiftY),color='b',ha='left',va='bottom')
ax1.annotate(r"$H\rightarrow b\bar{b}$",xy=(annoX,getL(annoX,MBOT)*shiftY*0.8),color='c',ha='left',va='top')
ax1.annotate(r"$H\rightarrow t\bar{t}$",xy=(annoX,getL(annoX,MTOP)*shiftY),color='g',ha='left',va='bottom')


ax2.semilogx(lambdaTest,muResult,'r-')
ax2.semilogx(lambdaTest,topMuResult,'g-')
ax2.semilogx(lambdaTest,botMuResult,'c-')
ax2.semilogx(lambdaTest,tauMuResult,'b-')


annoY = 1.5
ax2.annotate(r"$H\rightarrow\mu\mu$",xy=(getL(annoY+1,MMU),annoY),color='r',ha='left',va='bottom')
ax2.annotate(r"$H\rightarrow\tau\tau$",xy=(getL(annoY+1,MTAU),annoY),color='b',ha='left',va='bottom')
ax2.annotate(r"$H\rightarrow b\bar{b}$",xy=(getL(annoY+1.3,MBOT),annoY-0.1),color='c',ha='right',va='top')
ax2.annotate(r"$H\rightarrow t\bar{t}$",xy=(getL(annoY+1,MTOP),annoY),color='g',ha='left',va='bottom')

ax1.add_artist(AnchoredText("Effective $\psi^2\phi^2$ Coupling",loc=1,frameon=False))
ax1.add_artist(AnchoredText(r"$\alpha=1$",loc=2,frameon=False))

fig.savefig("EffectiveHiggsFermion.png")

print "for muons:"
print "For mu of 10: "
print "lambda = ",getL(1.5,MMU)
print "and back again = ",getMu(getL(1.5,MMU),MMU)
print "for mu of 7: ", getL(7.,MMU)
