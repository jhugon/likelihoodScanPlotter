#!/bin/bash
echo "Sourcing cmsset_default.sh"
cd /afs/cern.ch/cms
source cmsset_default.sh
export SCRAM_ARCH=slc5_amd64_gcc472
echo "SCRAM_ARCH is $SCRAM_ARCH"
cd $LS_SUBCWD
echo "In Directory: "
pwd
eval `scramv1 runtime -sh`
echo "cmsenv success!"
date

inputCard=hmm_$1
datacard=ws_$inputCard
datacardGGvQQ=wsGGvQQ_$inputCard
echo $1
echo $inputCard
echo $datacard
echo $datacardGGvQQ

cp $1 $inputCard

text2workspace.py $inputCard -m 125 -D data_obs -o $datacard
text2workspace.py $inputCard -m 125 -D data_obs -P HiggsAnalysis.CombinedLimit.PhysicsModel:floatingXSHiggs --PO modes=ggH,qqH --PO ggHRange=-20:20 --PO qqHRange=-30:30  -o $datacardGGvQQ

combine -M MultiDimFit --algo=singles --cl=0.68 $datacardGGvQQ >& logSinglesQQvGG
mv higgs*.root GGvQQSingles_$1.root

combine -M MultiDimFit --algo=grid --points=1000 --fastScan --rMin=-20 --rMax=20 $datacard >& logGrid
mv higgs*.root MuGrid_$1.root

combine -M MultiDimFit --algo=grid --points=5000 --fastScan  $datacardGGvQQ >& logGridQQvGG
mv higgs*.root GGvQQGrid_$1.root

echo "done"
date

