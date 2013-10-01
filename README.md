HLTrigger-HLTanalyzers-test-openHLT
===================================

CMSSW NewOpenHLT + PF2PAT workflow https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers

## openHLT2PAT

This produces trigger primitives and offline objects together in one single run to facilitates comparison between online vs. offline objects.

Trigger primitives are produced by STEAM's new openHLT (https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT); offline objects are produced using standard PF2PAT (https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT). They are joined together using SubProcess (https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses) and two-file solution.


### Setup environment

See the file `addpkg_5_3_11.csh` to setup environment for CMSSW_5_3_11.


### Checkout

```sh
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not, 
# check out the package by git cms-addpkg HLTrigger/HLTanalyzers .
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
```

### Run

For openHLT-only:
```sh
# Producer step
python openHLT.py -p -i /store/data/Run2012D/MET/RAW/v1/000/208/307/F4F98F29-9E3A-E211-8A78-003048F1C420.root -o MyProducts.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
# Filter step
python openHLT.py -i MyProducts.MET.root -o MyFilters.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
```

For openHLT2PAT:
```sh
# Producer step
python openHLT2PAT.py -p -i ifiles_MET_RAWAOD_208307.py -o MyProducts.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
# Filter step (note: use openHLT.py)
python openHLT.py -i MyProducts.MET.root -o MyFilters.MET.root -t hlt_MET.py -n 1000
```

#### Nota Bene

- FastTimerService clashes with SubProcess, so it is disabled in `setup_cff.py` and has to be disabled in any input HLT ocnfig file.
- Global tag for MC is hardcoded in both `openHLT.TEMPLATE`, `openHLT2PAT.TEMPLATE`.
- Global tag for PAT is hardcoded in `openHLT2PAT.TEMPLATE`.
- Global tag for HLT is provided by default by `setup_cff.py` and can be overwritten by input HLT config file.
- To run CRAB jobs, it's easiest to use the `dump.py` file that is produced when `cmsRun openhlt_go.py` is executed successfully.

### Useful Links

- https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers
- https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses
