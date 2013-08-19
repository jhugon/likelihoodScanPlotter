#!/usr/bin/env python

import ROOT as root
from matplotlib import pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.interpolate import interp1d,splrep, UnivariateSpline, InterpolatedUnivariateSpline
from matplotlib import cm

savePrefixes = [
"current",
"real125p0",
"real125p7",
#"snowmassUnc1_300",
#"snowmassUnc1_3000",
#"snowmassUnc2_300",
#"snowmassUnc2_3000"
]

annotation1List = [
"$\sqrt{s}=7$ TeV, $\mathcal{L} = 5.0$ fb$^{-1}$",
"$\sqrt{s}=7$ TeV, $\mathcal{L} = 5.0$ fb$^{-1}$",
"$\sqrt{s}=7$ TeV, $\mathcal{L} = 5.0$ fb$^{-1}$",
#"$\sqrt{s}=14$ TeV, $\mathcal{L} = 300$ fb$^{-1}$",
#"$\sqrt{s}=14$ TeV, $\mathcal{L} = 3000$ fb$^{-1}$",
#"$\sqrt{s}=14$ TeV, $\mathcal{L} = 300$ fb$^{-1}$",
#"$\sqrt{s}=14$ TeV, $\mathcal{L} = 3000$ fb$^{-1}$",
]

annotation2List = [
"$\sqrt{s}=8$ TeV, $\mathcal{L} = 19.8$ fb$^{-1}$",
"$\sqrt{s}=8$ TeV, $\mathcal{L} = 19.8$ fb$^{-1}$",
"$\sqrt{s}=8$ TeV, $\mathcal{L} = 19.8$ fb$^{-1}$",
#"Uncertainty Scenario 1",
#"Uncertainty Scenario 1",
#"Uncertainty Scenario 2",
#"Uncertainty Scenario 2",
]

oneDFileList = [
"MultiDimFitGrid1000Fastneg20to20.root",
"params125.7/CombSplitAll_7P8TeV_125.0.txt.lhGridR.root",
"params125.7/CombSplitAll_7P8TeV_125.7.txt.lhGridR.root",
#"conservative/MultiDimFitGridR1000Fast_300.root",
#"conservative/MultiDimFitGridR1000Fast_3000.root",
#"optimistic/MultiDimFitGridR1000Fast_300.root",
#"optimistic/MultiDimFitGridR1000Fast_3000.root",
]

twoDFileList = [
"MultiDimFitGrid1000Fastneg20to20GGvQQ.root",
"params125.7/CombSplitAll_7P8TeV_125.0.txt.lhGridQQvGG.root",
"params125.7/CombSplitAll_7P8TeV_125.7.txt.lhGridQQvGG.root",
#"conservative/MultiDimFitGrid1000Fastneg20to20GGvQQ_300.root",
#"conservative/MultiDimFitGrid1000Fastneg20to20GGvQQ_3000.root",
#"optimistic/MultiDimFitGrid1000Fastneg20to20GGvQQ_300.root",
#"optimistic/MultiDimFitGrid1000Fastneg20to20GGvQQ_3000.root",
]

profile1DFileList = [
"MultiDimFitSingles.root",
"params125.7/CombSplitAll_7P8TeV_125.0.txt.profileR.root",
"params125.7/CombSplitAll_7P8TeV_125.7.txt.profileR.root",
#"conservative/MultiDimFitSinglesR_300.root",
#"conservative/MultiDimFitSinglesR_3000.root",
#"optimistic/MultiDimFitSinglesR_300.root",
#"optimistic/MultiDimFitSinglesR_3000.root",
]

profile2DFileList = [
"MultiDimFitSinglesGGvQQ.root",
"params125.7/CombSplitAll_7P8TeV_125.0.txt.profileQQvGG.root",
"params125.7/CombSplitAll_7P8TeV_125.7.txt.profileQQvGG.root",
#"conservative/MultiDimFitSinglesGGvQQ_300.root",
#"conservative/MultiDimFitSinglesGGvQQ_3000.root",
#"optimistic/MultiDimFitSinglesGGvQQ_300.root",
#"optimistic/MultiDimFitSinglesGGvQQ_3000.root",
]

labelList = [
"Current Analysis",
"Current Analysis 125.",
"Current Analysis 125.7",
#"S1, 300 fb$^{-1}$",
#"S1, 3000 fb$^{-1}$",
#"S2, 300 fb$^{-1}$",
#"S2, 3000 fb$^{-1}$",
]

annotation3List = [
  "$m_H=125$ GeV/c$^2$",
  "$m_H=125$ GeV/c$^2$",
  "$m_H=125.7$ GeV/c$^2$",
  #"$m_H=125$ GeV/c$^2$",
  #"$m_H=125$ GeV/c$^2$",
  #"$m_H=125$ GeV/c$^2$",
  #"$m_H=125$ GeV/c$^2$",
]

def drawAnnotations(fig,title,annotation1=None,annotation2=None,annotation3=None,
                    annotation1r=None,annotation2r=None,annotation3r=None,
                    annotation1c=None,annotation2c=None,annotation3c=None,
                    annotationSize="medium", titleSize='large'
                    ):
  fig.text(0.13,0.905,"CMS Preliminary",va='bottom',ha='left',size=titleSize)
  fig.text(0.89,0.905,title,va='bottom',ha='right',size=titleSize)
  if annotation1:
    fig.text(0.14,0.88,annotation1,va='top',ha='left',size=annotationSize)
  if annotation2:
    fig.text(0.14,0.83,annotation2,va='top',ha='left',size=annotationSize)
  if annotation3:
    fig.text(0.14,0.78,annotation3,va='top',ha='left',size=annotationSize)
  if annotation1r:
    fig.text(0.875,0.88,annotation1r,va='top',ha='right',size=annotationSize)
  if annotation2r:
    fig.text(0.875,0.83,annotation2r,va='top',ha='right',size=annotationSize)
  if annotation3r:
    fig.text(0.875,0.78,annotation3r,va='top',ha='right',size=annotationSize)
  if annotation1c:
    fig.text(0.5,0.88,annotation1c,va='top',ha='center',size=annotationSize)
  if annotation2c:
    fig.text(0.5,0.83,annotation2c,va='top',ha='center',size=annotationSize)
  if annotation3c:
    fig.text(0.5,0.78,annotation3c,va='top',ha='center',size=annotationSize)

def saveAs(fig,name):
  fig.savefig(name+".png",format="png")
  fig.savefig(name+".pdf",format="pdf")
  fig.savefig(name+".eps",format="eps")
  fig.savefig(name+".svg",format="svg")

oneDLikelihoods = []
oneDLikelihoodLabels = []
twoDLikelihoods = []
twoDLikelihoodLabels = []
fig = mpl.figure()

for savePrefix,oneDFN,twoDFN,profile1DFN,profile2DFN,annotation1,annotation2,annotation3,label in zip(savePrefixes,oneDFileList,twoDFileList,profile1DFileList,profile2DFileList,annotation1List,annotation2List,annotation3List,labelList):

  print("#################################################\nRunning for savePrefix: {0}...".format(savePrefix))

  minX = -15
  minY = -15
  maxX = 15
  maxY = 15
  if "300" in savePrefix:
    minX = -1
    minY = -1
    maxX = 3.5
    maxY = 3.5
  if "3000" in savePrefix:
    minX = 0
    minY = 0
    maxX = 2
    maxY = 2

  if profile1DFN:
    profileFile = root.TFile(profile1DFN)
    profileTree = profileFile.Get("limit")
    profileR = []
    for iEntry in range(0,3):
      profileTree.GetEntry(iEntry)
      r = float(profileTree.r)
      profileR.append(r)
    profileR.sort()
    print profileR
    print("Profiled mu values:")
    print("mu: {0:.2f} +{1:.2f} -{2:.2f}".format(profileR[1],profileR[2]-profileR[1],profileR[1]-profileR[0]))
    print("Relative Uncertainty: {0:.2f}".format((profileR[2]-profileR[1])/profileR[1]))
  if profile2DFN:
    profileFile = root.TFile(profile2DFN)
    profileTree = profileFile.Get("limit")
    profileGG = []
    profileQQ = []
    for iEntry in range(0,6):
      profileTree.GetEntry(iEntry)
      ggH = float(profileTree.r_ggH)
      qqH = float(profileTree.r_qqH)
      if iEntry <3:
        profileGG.append(ggH)
      else:
        profileQQ.append(qqH)
      #print("ggH: {0:10.2f} qqH: {1:10.2f}".format(ggH,qqH))
    profileGG.sort()
    profileQQ.sort()
    #print profileGG
    #print profileQQ
    print("Profiled mu values:")
    print("GG: {0:.2f} +{1:.2f} -{2:.2f}".format(profileGG[1],profileGG[2]-profileGG[1],profileGG[1]-profileGG[0]))
    print("QQ: {0:.2f} +{1:.2f} -{2:.2f}".format(profileQQ[1],profileQQ[2]-profileQQ[1],profileQQ[1]-profileQQ[0]))
    print("Relative Uncertainty: GG: {0:.2f} QQ: {1:.2f}".format((profileGG[2]-profileGG[1])/profileGG[1],
          (profileQQ[2]-profileQQ[1])/profileQQ[1]))

  if oneDFN:
    oneDFile = root.TFile(oneDFN)
    oneDTree = oneDFile.Get("limit")
    oneDData = scipy.zeros((oneDTree.GetEntries(),2))
    for iEntry in range(0,oneDTree.GetEntries()):
      oneDTree.GetEntry(iEntry)
      if 2*oneDTree.deltaNLL > 10:
        continue
      oneDData[iEntry,0] = float(oneDTree.r)
      oneDData[iEntry,1] = 2*float(oneDTree.deltaNLL)
    oneDDataUnmasked = scipy.copy(oneDData)
    oneDData = scipy.ma.masked_equal(oneDData,0.)

    minimumIndex = scipy.argmin(oneDData[:,1])
    #lowInterp = UnivariateSpline(oneDDataUnmasked[:minimumIndex,1],oneDDataUnmasked[:minimumIndex,0])
    #highInterp = UnivariateSpline(oneDDataUnmasked[minimumIndex:,1],oneDDataUnmasked[minimumIndex:,0])
    #lowInterp = InterpolatedUnivariateSpline(oneDDataUnmasked[:minimumIndex,1],oneDDataUnmasked[:minimumIndex,0])
    #highInterp = InterpolatedUnivariateSpline(oneDDataUnmasked[minimumIndex:,1],oneDDataUnmasked[minimumIndex:,0])
    low1SigI = scipy.argmin(scipy.fabs(oneDData[:minimumIndex,1.]-1.0))
    high1SigI = scipy.argmin(scipy.fabs(oneDData[minimumIndex:,1.]-1.0))
    low1Sig = oneDData[low1SigI,0]
    high1Sig = oneDData[minimumIndex:,0][high1SigI]
    low2SigI = scipy.argmin(scipy.fabs(oneDData[:minimumIndex,1.]-4.0))
    high2SigI = scipy.argmin(scipy.fabs(oneDData[minimumIndex:,1.]-4.0))
    low2Sig = oneDData[low2SigI,0]
    high2Sig = oneDData[minimumIndex:,0][high2SigI]

    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(oneDData[:,0],oneDData[:,1],'b-')
    #ax.plot(lowInterp(oneDData[:minimumIndex,1]),oneDData[:minimumIndex,1],'r.')
    #ax.plot(highInterp(oneDData[minimumIndex:,1]),oneDData[minimumIndex:,1],'g.')
    #for nsig in [1.,4.]:
    #  print lowInterp(nsig), highInterp(nsig)
    #  ax.axhline(nsig,linestyle='--')
    #  ax.axvline(lowInterp(nsig),linestyle='--')
    #  ax.axvline(highInterp(nsig),linestyle='--')
    ax.axhline(1.,linestyle=':',color='r')
    ax.plot([low1Sig,low1Sig],[0.,1.],linestyle=':',color='r')
    ax.plot([high1Sig,high1Sig],[0.,1.],linestyle=':',color='r')
    ax.axhline(4.,linestyle=':',color='r')
    ax.plot([low2Sig,low2Sig],[0.,4.],linestyle=':',color='r')
    ax.plot([high2Sig,high2Sig],[0.,4.],linestyle=':',color='r')
    print("rBF: {0:10.2f} 1sigma contours found on scan: {1:10.2f} {2:10.2f}".format(oneDData[minimumIndex,0],low1Sig,high1Sig))

    ax.set_xlabel("$\mu$")
    ax.set_ylabel("$-2\Delta\ln\mathcal{L}$")
    drawAnnotations(fig,r"$H\rightarrow\mu\mu$",annotation1c=annotation1,annotation2c=annotation2,annotation3c=annotation3)
    saveAs(fig,savePrefix+"_1d")
    if "300" in savePrefix:
      oneDLikelihoods.append(oneDData)
      oneDLikelihoodLabels.append(label)
  
  twoDFile = root.TFile(twoDFN)
  twoDTree = twoDFile.Get("limit")
  
  arrayLen = int(scipy.sqrt(twoDTree.GetEntries()-2))
  twoDData = scipy.zeros((arrayLen,arrayLen,3))
  
  bestFitXY = [0.,0.]
  twoDTree.GetEntry(0)
  bestFitXY[0] = float(twoDTree.r_ggH)
  bestFitXY[1] = float(twoDTree.r_qqH)
  for iX in range(0,arrayLen):
    for iY in range(0,arrayLen):
      iEntry = iX + arrayLen*iY + 1
      twoDTree.GetEntry(iEntry)
    
      m2Nll = float(2*twoDTree.deltaNLL)
      twoDData[iX,iY,0] = float(twoDTree.r_ggH)+1e-6
      twoDData[iX,iY,1] = float(twoDTree.r_qqH)+1e-6
      if m2Nll > 10.:
        m2Nll = 0.
      twoDData[iX,iY,2] = m2Nll
  
  #twoDData = twoDData[30:twoDData.shape[0]-30,30:twoDData.shape[1]-30,:]
  #print twoDData.shape
  #print "x:"
  #print twoDData[:,:,0]
  #print "y:"
  #print twoDData[:,:,1]
  #print "Z:"
  #print twoDData[:,:,2]
  
  #X,Y,Z = convertData(twoDData)
  
  twoDData = scipy.ma.masked_equal(twoDData,0.)
  #for i in range(0,twoDData.shape[0],10):
  #  print twoDData[i,:]
  #for i in range(0,twoDData.shape[0],100):
  #  print twoDData[i,:]
  if "300" in savePrefix:
    twoDLikelihoods.append(twoDData)
    twoDLikelihoodLabels.append(label)
    
  
  profileXraw = scipy.amin(twoDData[:,:,2],axis=1)
  profileYraw = scipy.amin(twoDData[:,:,2],axis=0)
  profileXx = []
  profileX = []
  profileY = []
  profileYy = []
  for x,lnn in zip(twoDData[:,0,1],profileXraw):
    if lnn:
      profileX.append(lnn)
      profileXx.append(x)
  for y,lnn in zip(twoDData[0,:,0],profileYraw):
    if lnn:
      profileY.append(lnn)
      profileYy.append(y)
  
  #fig.clear()
  #ax = fig.add_subplot(111)
  #ax.contourf(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2],[1.,4.],colors=['g','y'])
  #ax.set_xlabel("$\mu_{GF}$")
  #ax.set_ylabel("$\mu_{VBF}$")
  #ax.set_xlim(minX,maxX)
  #ax.set_ylim(minY,maxY)
  #drawAnnotations(fig,r"$H\rightarrow\mu\mu$",annotation1=annotation1,annotation2=annotation2,annotation3=annotation3)
  #saveAs(fig,savePrefix+"_2d_contourColor")
  
  fig.clear()
  ax = fig.add_subplot(111)
  ct = ax.contour(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2],[1.,4.],colors=['g','y'])
  ax.clabel(ct,inline=1,rightside_up=True,fontsize=20,fmt={1.0:"1$\sigma$",4.0:"2$\sigma$"})
  ax.plot([bestFitXY[0]],[bestFitXY[1]],"kx")
  ax.set_xlabel("$\mu_{GF}$")
  ax.set_ylabel("$\mu_{VBF}$")
  ax.set_xlim(minX,maxX)
  ax.set_ylim(minY,maxY)
  drawAnnotations(fig,r"$H\rightarrow\mu\mu$",annotation1=annotation1,annotation2=annotation2,annotation3=annotation3)
  saveAs(fig,savePrefix+"_2d_contour")
  
  fig.clear()
  minZ = -5.
  ax = fig.add_subplot(111, projection='3d')
  #ax.plot(profileYy,maxY*scipy.ones(len(profileYy)),profileY,color='b')
  #ax.plot(minX*scipy.ones(len(profileXx)),profileXx,profileX,color='b')
  ax.scatter(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
  #ax.plot_wireframe(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
  #ax.plot_surface(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
  ax.contour(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2],[1.,4], zdir='z', offset=minZ, colors=['g','y'])
  ax.plot([bestFitXY[0]],[bestFitXY[1]],minZ,color='k',marker=".")
  ax.set_xlim(minX,maxX)
  ax.set_ylim(minY,maxY)
  ax.set_zlim(minZ,10)
  ax.set_xlabel("$\mu_{GF}$")
  ax.set_ylabel("$\mu_{VBF}$")
  ax.set_zlabel("$-2\Delta\ln\mathcal{L}$")
  drawAnnotations(fig,r"$H\rightarrow\mu\mu$",annotation1=annotation1,annotation1r=annotation2,annotation2=annotation3,annotationSize='small')
  saveAs(fig,savePrefix+"_2d_3d")
  
  print twoDData.shape

if len(oneDLikelihoods)>1:
  fig.clear()
  ax = fig.add_subplot(111)
  for l,label in zip(oneDLikelihoods,oneDLikelihoodLabels):
    ax.plot(l[:,0],l[:,1],label=label)
  ax.set_xlabel("$\mu$")
  ax.set_ylabel("$-2\Delta\ln\mathcal{L}$")
  drawAnnotations(fig,r"$H\rightarrow\mu\mu$","$\sqrt{s}=14$ TeV Projection")
  leg = ax.legend(loc='best', fontsize="x-small")
  leg.get_frame().set_alpha(0.5)
  saveAs(fig,"1d_AllTogether")
  oneDLikelihoods.append(oneDData)

if len(twoDLikelihoods)>1:
  fig.clear()
  ax = fig.add_subplot(111)
  twoDColors = ['k','b','r','m','g','y']
  minX = 0
  minY = 0
  maxX = 2.5
  maxY = 2.5
  for l,label,c in zip(twoDLikelihoods,twoDLikelihoodLabels,twoDColors[:len(twoDLikelihoodLabels)]):
    ct = ax.contour(l[:,:,0],l[:,:,1],l[:,:,2],[1.],colors=[c])
    #ax.clabel(ct,inline=1,rightside_up=True,fontsize=15,fmt={1.0:label})
  proxyArtistList = []
  for label,c in zip(twoDLikelihoodLabels,twoDColors[:len(twoDLikelihoodLabels)]):
    proxyArtistList.append(mpl.Line2D([0,0],[1,1],label=label,color=c))
  ax.set_xlim(minX,maxX)
  ax.set_ylim(minY,maxY)
  ax.set_xlabel("$\mu_{GF}$")
  ax.set_ylabel("$\mu_{VBF}$")
  drawAnnotations(fig,r"$H\rightarrow\mu\mu$","$\sqrt{s}=14$ TeV Projection","1$\sigma$ Contours")
  leg = ax.legend(proxyArtistList,twoDLikelihoodLabels,loc='best', fontsize="x-small")
  leg.get_frame().set_alpha(0.5)
  saveAs(fig,"2d_AllTogether")
  oneDLikelihoods.append(oneDData)

print "Done."
