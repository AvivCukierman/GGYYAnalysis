#!/bin/bash
python GGYYAnalysis/scripts/Run.py \
    --submitDir "Test" \
    -w \
    --inputFiles "/nfs/slac/g/atlas/u01/users/acukierm/VBF_Analysis/Test_Sample" \
    --isMC 1 \
    --nevents 10 \
    --mode "class" \
    --driver "direct"
exit 0

#--inputFiles "/atlas/dq2/user/bnachman/" \
    #--inputFiles "/nfs/slac/g/atlas/u01/users/acukierm/VBF/mc_sample/" \
