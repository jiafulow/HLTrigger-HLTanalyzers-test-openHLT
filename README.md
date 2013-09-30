HLTrigger-HLTanalyzers-test-openHLT
===================================

CMSSW NewOpenHLT + PF2PAT workflow https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers

## openHLT2PAT

This allows a job to produce trigger primitives and offline objects together in one single run. Trigger primitives are produced by STEAM's new openHLT (https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT); offline objects are produced using standard PF2PAT. They are joined together using SubProcess and two-file solution.


### Setup environment

See the file `addpkg_5_3_11.csh` to setup environment for CMSSW_5_3_11.


### Checkout

```
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not, 
# check out the package by git cms-addpkg HLTrigger/HLTanalyzers .
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
```

### Run

For openHLT-only:
```
# Producer step
python openHLT.py -p -i /store/data/Run2012D/MET/RAW/v1/000/208/307/F4F98F29-9E3A-E211-8A78-003048F1C420.root -o MyProducts.MET.root -t hlt_MET.py -n 100
cmsRun openhlt_go.py
# Filter step
python openHLT.py -i MyProducts.MET.root -o MyFilters.MET.root -t hlt_MET.py -n 100
cmsRun openhlt_go.py
```

For openHLT2PAT (by default only the final products are stored):
```
# Producer step
python openHLT2PAT.py -p -i ifiles_MET_RAWAOD_208307.py -o MyProducts.MET.root -t hlt_MET.py -n 100
cmsRun openhlt_go.py
# Filter step is disabled
```

#### Nota Bene

- FastTimerService clashes with SubProcess, so it is disabled from `setup_cff.py`.
- Global tags for MC are hardcoded in `openHLT.TEMPLATE`, `openHLT2PAT.TEMPLATE`.
- Global tag for PAT is hardcoded in `openHLT2PAT.TEMPLATE`.
- Global tag for HLT is provided by default by `setup_cff.py` and can be overwritten by input HLT config file.
- To run CRAB jobs, it's easiest to use the `dump.py` file that is produced when `cmsRun openhlt_go.py` is executed successfully.
- Currently, openHLT intermediate products are not saved for openHLT2PAT (in order to reduce disk usage), so it's not possible to do the filter step.

### Useful Links

- https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers
- https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
