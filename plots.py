#!/usr/bin/env python

import ROOT as root
from matplotlib import pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
import scipy
from matplotlib import cm

oneDFile = root.TFile("MultiDimFitGrid1000Fastneg20to20.root")
twoDFile = root.TFile("MultiDimFitGrid1000Fastneg20to20GGvQQ.root")
profileFile = root.TFile("MultiDimFitSinglesGGvQQ.root")

oneDTree = oneDFile.Get("limit")
twoDTree = twoDFile.Get("limit")
profileTree = profileFile.Get("limit")

oneDData = scipy.zeros((oneDTree.GetEntries(),2))
arrayLen = int(scipy.sqrt(twoDTree.GetEntries()-2))
print("Array Side Length: {0:.1f}".format(arrayLen))
twoDData = scipy.zeros((arrayLen,arrayLen,3))

for iEntry in range(0,oneDTree.GetEntries()):
  oneDTree.GetEntry(iEntry)
  if 2*oneDTree.deltaNLL > 10:
    continue
  oneDData[iEntry,0] = float(oneDTree.r)
  oneDData[iEntry,1] = 2*float(oneDTree.deltaNLL)

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

oneDData = scipy.ma.masked_equal(oneDData,0.)
twoDData = scipy.ma.masked_equal(twoDData,0.)
#for i in range(0,twoDData.shape[0],10):
#  print twoDData[i,:]
#for i in range(0,twoDData.shape[0],100):
#  print twoDData[i,:]

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

fig = mpl.figure()
ax = fig.add_subplot(111)
ax.plot(oneDData[:,0],oneDData[:,1],'b-')
ax.set_xlabel("$\mu$")
ax.set_ylabel("$-2\ln\Delta\mathcal{L}$")
fig.savefig("1d.png")

fig.clear()
ax = fig.add_subplot(111)
ax.pcolormesh(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
ax.set_xlabel("$\mu(ggH)$")
ax.set_ylabel("$\mu(qqH)$")
fig.savefig("2d_pcolormesh.png")

fig.clear()
ax = fig.add_subplot(111)
ct = ax.contour(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2],[1.,4.],colors=['g','y'])
ax.clabel(ct,inline=1,rightside_up=True,fontsize=20,fmt={1.0:"1$\sigma$",4.0:"2$\sigma$"})
ax.plot([bestFitXY[0]],[bestFitXY[1]],"kx")
ax.set_xlabel("$\mu(ggH)$")
ax.set_ylabel("$\mu(qqH)$")
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
fig.savefig("2d_contour.png")

fig.clear()
minZ = -5.
minmaxX = 15
minmaxY = 15
ax = fig.add_subplot(111, projection='3d')
ax.plot(profileYy,minmaxY*scipy.ones(len(profileYy)),profileY,color='b')
ax.plot(-minmaxX*scipy.ones(len(profileXx)),profileXx,profileX,color='b')
ax.scatter(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
#ax.plot_wireframe(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
#ax.plot_surface(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2])
ax.contour(twoDData[:,:,0],twoDData[:,:,1],twoDData[:,:,2],[1.,4], zdir='z', offset=minZ, colors=['g','y'])
ax.plot([bestFitXY[0]],[bestFitXY[1]],minZ,color='k',marker=".")
ax.set_xlim(-minmaxX,minmaxX)
ax.set_ylim(-minmaxY,minmaxY)
ax.set_zlim(minZ,10)
ax.set_xlabel("$\mu(ggH)$")
ax.set_ylabel("$\mu(qqH)$")
ax.set_zlabel("$-2\ln\Delta\mathcal{L}$")
fig.savefig("2d_3d.png")

print twoDData.shape
