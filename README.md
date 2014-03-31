HLTrigger-HLTanalyzers-test-openHLT
===================================

![CMS](http://jiafulow.github.io/VHbbAnalysis/css/CMS-BW-128x128.gif)

CMSSW NewOpenHLT + PF2PAT workflow used in [Jet/MET Trigger subgroup](https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers).

This produces trigger primitives and offline objects together in one single run to facilitates comparison between online vs. offline objects. Trigger primitives are produced by TSG's [new openHLT](https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT); offline objects are produced using standard [PF2PAT](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT). They are joined together using [SubProcess](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses) and [two-file solution](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePoolInputSources#Example_5_Merging_files_with_dif).


openHLT2PAT (CMSSW_5_3_X)
-------------------------
![CMSSW_5_3_14_patch2](http://img.shields.io/badge/cmssw-v5.3.14--patch.2-blue.svg)

### Setup environment

See the file [addpkg_5_3_14.csh](addpkg_5_3_14.csh) to setup environment for `CMSSW_5_3_14_patch2`.

2014-02-25: updated from `CMSSW_5_3_11` to `CMSSW_5_3_14_patch2`.

### Checkout

```sh
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not,
# check out the package by `git cms-addpkg HLTrigger/HLTanalyzers`
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
cd HLTrigger/HLTanalyzers/test/openHLT
```

### Run

Before the first run (on Data):
```sh
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

To run on MC, add argument `--mc`.


openHLT2PAT (CMSSW_7_1_X)
-------------------------
![CMSSW_7_1_0_pre4](http://img.shields.io/badge/cmssw-v7.1.0--pre.4-blue.svg)

### Setup environment

See the file [addpkg_7_1_0.csh](addpkg_7_1_0.csh) to setup environment for `CMSSW_7_1_0_pre4`.

2014-02-25: Updated both [openHLT.py](openHLT.py) and [openHLT.TEMPLATE](openHLT.TEMPLATE) to work in `CMSSW_7_X_Y`.

### Checkout

```sh
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not,
# check out the package by `git cms-addpkg HLTrigger/HLTanalyzers`
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
cd HLTrigger/HLTanalyzers/test/openHLT
```

### Run

  **Under Construction**


## Nota Bene

- **Important**: Please edit [openHLT2PAT.TEMPLATE](openHLT2PAT.TEMPLATE) and disable the lines under the comment block "User stuff". These are stuff that is interesting to the author, but probably not to anyone else.
- FastTimerService clashes with SubProcess, so it has to be disabled in any input HLT config file.
- To do a skim, append `-s skimfiles/skimHLTPFMET150_cfi.py` as an argument to [openHLT2PAT.py](openHLT2PAT.py).
- Global tags are hardcoded in both [openHLT.TEMPLATE](openHLT.TEMPLATE) and [openHLT2PAT.TEMPLATE](openHLT2PAT.TEMPLATE).
- To run CRAB jobs, it's easiest to use the [dump.py](dump.py) file that is produced when `cmsRun openhlt_go.py` is executed successfully.
- To run only offline reconstruction, substitute `openHLT2PAT` by `onlyPAT` everywhere.

### Useful Links

- https://twiki.cern.ch/twiki/bin/view/CMS/JetMETTriggers
- https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePF2PAT
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubProcesses

