HLTrigger-HLTanalyzers-test-openHLT
===================================

CMSSW NewOpenHLT + PF2PAT workflow used in Jet/MET Trigger subgroup (https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers).

This produces trigger primitives and offline objects together in one single run to facilitates comparison between online vs. offline objects. Trigger primitives are produced by STEAM's new openHLT (https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT); offline objects are produced using standard PF2PAT (https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT). They are joined together using SubProcess (https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses) and two-file solution.


openHLT2PAT (CMSSW_5_3_14_patch2)
---------------------------------
### Setup environment

See the file `addpkg_5_3_14.csh` to setup environment for CMSSW_5_3_14_patch2.

2014-02-25: updated from CMSSW_5_3_11 to CMSSW_5_3_14_patch2

### Checkout

```sh
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not,
# check out the package by git cms-addpkg HLTrigger/HLTanalyzers .
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
cd HLTrigger/HLTanalyzers/test/openHLT
```

### Run

Before the first run (on Data):
```sh
# Setup conditions
edmConfigFromDB --cff --orcoff --configName /cdaq/physics/Run2012/8e33/v2.1/HLT/V7 --nopaths > setup_cff.py
# To get the full menu
#hltGetConfiguration orcoff:/cdaq/physics/Run2012/8e33/v2.1/HLT/V7 --full --offline --data --no-output --process TEST --globaltag auto:hltonline > hlt.py
# To get a menu with selected paths
#hltGetConfiguration orcoff:/cdaq/physics/Run2012/8e33/v2.1/HLT/V7 --full --offline --data --no-output --process TEST --globaltag auto:hltonline --path HLT_PFMET150_v7 > hlt_PFMET150.py
# Or just take one of the menus available in this repository
#ls hlt*py
```

To run on MC, change `--globaltag auto:hltonline` to `--globaltag auto:startup`.

For openHLT only (on Data):
```sh
# Producer step
python openHLT.py -p -i /store/data/Run2012D/MET/RAW/v1/000/208/307/F4F98F29-9E3A-E211-8A78-003048F1C420.root -o MyProducts.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
# Filter step
python openHLT.py -i MyProducts.MET.root -o MyFilters.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
```

For openHLT2PAT (on Data):
```sh
# Producer step
python openHLT2PAT.py -p -i inputfiles/ifiles_MET_RAWAOD_208307.py -o MyProducts.MET.root -t hlt_MET.py -n 1000
cmsRun openhlt_go.py
# Filter step (note: use openHLT.py)
python openHLT.py -i MyProducts.MET.root -o MyFilters.MET.root -t hlt_MET.py -n 1000
```

To run on MC, add `--mc` argument to `openHLT.py` or `openHLT2PAT.py`.


openHLT2PAT (CMSSW_7_1_0_pre4)
------------------------------
**Under construction**

Both `openHLT.py` and `openHLT.TEMPLATE` have been updated to work in CMSSW_7_X_Y. Try running with `-t hlt_7XY.py -u setup_7XY_cff.py` for example.


## Nota Bene

- **Important**: Please edit `openHLT2PAT.TEMPLATE` and disable the lines under the comment block "User stuff". These are stuff that is interesting to the author, but probably not to anyone else.
- FastTimerService clashes with SubProcess, so it is disabled in `setup_cff.py` and has to be disabled in any input HLT config file.
- To do a skim, append `-s skimfiles/skimHLTPFMET150_cfi.py` as an argument to `openHLT2PAT.py`.
- Global tag for MC is hardcoded in both `openHLT.TEMPLATE`, `openHLT2PAT.TEMPLATE`.
- Global tag for PAT is hardcoded in `openHLT2PAT.TEMPLATE`.
- Global tag for HLT is provided by default by `setup_cff.py` and can be overwritten by input HLT config file.
- To run CRAB jobs, it's easiest to use the `dump.py` file that is produced when `cmsRun openhlt_go.py` is executed successfully.
- To run only offline reconstruction, substitute `openHLT2PAT` by `onlyPAT` everywhere.

### Useful Links

- https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers
- https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses

