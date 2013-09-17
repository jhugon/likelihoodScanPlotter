#!/usr/bin/env python

from scipy import *
import matplotlib.pyplot as mpl
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

VEV=246.
MMU=0.1056583715
MTOP=173.07
MBOT=4.18
MTAU=1.77682
MH = 125.0


def effectiveOneOverggHAmplitude():
  """
  Approximation, valid for large m_t, of course
  http://arxiv.org/abs/hep-ph/0601212
  """
  return 2.76 - 6.37e-2 * (MH/100.)**2

def effectiveOneOvergamgamHAmplitude():
  """
  Approximation
  http://arxiv.org/abs/hep-ph/0601212
  """
  return -0.85 + 0.16 * (MH/100.)**2

def effectiveLoopggHMu(l,c=1./(16*pi**2)):
  """
  Only considering CP conserving operator
  http://arxiv.org/abs/hep-ph/0601212
  """
  result = 8.*pi**2*VEV**2*c
  result /= l**2 * effectiveOneOverggHAmplitude()
  result = 1.-result
  return abs(result)**2

def effectiveLoopggHL(mu,c=1./(16*pi**2)):
  """
  Only considering CP conserving operator
  http://arxiv.org/abs/hep-ph/0601212
  """
  result = sqrt(mu)
  result = 1.-result
  result = 1./result
  result *= 8.*pi**2*VEV**2*c
  result /= effectiveOneOverggHAmplitude()
  result = sqrt(result)
  return result

def getK(l,m):
    return 1. + VEV**3 / (sqrt(2) * m * l**2)
def getMu(l,m):
    return getK(l,m)**2
def getL(mu,m):
    result = VEV**3
    result /= m * ( mu**(0.5) - 1 ) * sqrt(2)
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

##################################################
# Axis 1 ffH


ax1.semilogy(muTest,lambdaResult,'r-')
ax1.semilogy(muTest,topLambdaResult,'g-')
ax1.semilogy(muTest,botLambdaResult,'c-')
ax1.semilogy(muTest,tauLambdaResult,'b-')
ax1.semilogy(muTest,[effectiveLoopggHL(m,-1) for m in muTest],'k--')

annoX = 5.
shiftY = 1.2
shiftY = 1.
ax1.annotate(r"$H\rightarrow\mu\mu$",xy=(annoX,getL(annoX,MMU)*shiftY),color='r',ha='left',va='bottom')
ax1.annotate(r"$H\rightarrow\tau\tau$",xy=(annoX,getL(annoX,MTAU)*shiftY),color='b',ha='left',va='bottom')
ax1.annotate(r"$H\rightarrow b\bar{b}$",xy=(annoX,getL(annoX,MBOT)*shiftY*0.8),color='c',ha='left',va='top')
ax1.annotate(r"$H\rightarrow t\bar{t}$",xy=(annoX,getL(annoX,MTOP)*shiftY),color='g',ha='left',va='bottom')
ax1.annotate(r"$gg\rightarrow H$, $\alpha=-1$",xy=(annoX+5.,effectiveLoopggHL(annoX+5.,-1.)*shiftY),color='k',ha='left',va='bottom')

##################################################
# Axis 2 ffH

ax2.semilogx(lambdaTest,muResult,'r-')
ax2.semilogx(lambdaTest,topMuResult,'g-')
ax2.semilogx(lambdaTest,botMuResult,'c-')
ax2.semilogx(lambdaTest,tauMuResult,'b-')


annoY = 1.5
ax2.annotate(r"$H\rightarrow\mu\mu$",xy=(getL(annoY+1,MMU),annoY),color='r',ha='left',va='bottom')
ax2.annotate(r"$H\rightarrow\tau\tau$",xy=(getL(annoY+1,MTAU),annoY),color='b',ha='left',va='bottom')
ax2.annotate(r"$H\rightarrow b\bar{b}$",xy=(getL(annoY+1.3,MBOT),annoY-0.1),color='c',ha='right',va='top')
ax2.annotate(r"$H\rightarrow t\bar{t}$",xy=(getL(annoY+1,MTOP),annoY),color='g',ha='left',va='bottom')

##################################################
# Axis 2 ggH

ax2.semilogx(lambdaTest,[effectiveLoopggHMu(l,-1./(16*pi**2))-1.  for l in lambdaTest],'k--')
ax2.semilogx(lambdaTest,[effectiveLoopggHMu(l,-1.)-1.  for l in lambdaTest],'k:')
#ax2.annotate(r"$gg\rightarrow H$"+"\n"+r"$\alpha=-1/16\pi^2$",xy=(effectiveLoopggHL(annoY+1.1,-1./(16*pi**2)),annoY+0.1),color='k',ha='left',va='bottom')
ax2.annotate(r"$gg\rightarrow H$"+"\n"+r"$\alpha=-\frac{1}{16\pi^2}$",xy=(effectiveLoopggHL(annoY+1.1,-1./(16*pi**2)),annoY+0.1),color='k',ha='left',va='bottom')
ax2.annotate(r"$gg\rightarrow H$"+"\n"+r"$\alpha=-1$",xy=(effectiveLoopggHL(annoY+1.1,-1.),annoY+0.1),color='k',ha='left',va='bottom')

##################################################
### Final annotations and save

ax1.add_artist(AnchoredText("Effective $\psi^2\phi^2$ Coupling\nUnit Wilson Coefficients",loc=1,frameon=False))

fig.savefig("EffectiveHiggsFermion.png")

print "for muons:"
print "For mu of 7.4: "
print "lambda = ",getL(7.4,MMU)
print "and back again = ",getMu(getL(7.4,MMU),MMU)
print
print "For mu of 7.0: "
print "lambda = ",getL(7.0,MMU)

print "From HIG-13-005:"
print "For k_b of 2.2 (My approximate CMS prelim result 95\% CL UL): "
print "  ",getL(2.2**2,MBOT)
print "For k_tau of 1.75 (My approximate CMS prelim result 95\% CL UL): "
print "  ",getL(1.75**2,MTAU)
print "For k_t of 3.0 (My approximate CMS prelim result 95\% CL UL): "
print "  ",getL(3.**2,MTOP)

print "Effective ggH:"
print "For mu of 7.0: "
print "For k_g of 1.5 (My approximate CMS prelim result 95\% CL UL): "
print "  Assuming alpha=-1:"
print "    ",effectiveLoopggHL(1.5**2,-1.)
print "  Assuming alpha=-1/16pi^2:"
print "    ",effectiveLoopggHL(1.5**2)

print "For k_gamma of 1.4 (My approximate CMS prelim result 95\% CL UL): "

