HLTrigger-HLTanalyzers-test-openHLT
===================================

CMSSW NewOpenHLT https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT

## openHLT2PAT

Join STEAM's new openHLT and offline PF2PAT together using SubProcess and two-file solution

### Checkout

```
cd $CMSSW_BASE/src
# The following assumes HLTrigger/HLTanalyzers already exists. If not, 
# check out the package by git cms-addpkg HLTrigger/HLTanalyzers .
# (see http://cms-sw.github.io/cmssw/git-cms-addpkg.html )
git clone git@github.com:jiafulow/HLTrigger-HLTanalyzers-test-openHLT.git HLTrigger/HLTanalyzers/test/openHLT
```

### Get Dependencies

See the file `addpkg_5_3_11.csh` to setup environment for CMSSW_5_3_11.

### Run

```
python openHLT2PAT.py -p -i NOT_USED -o MyProducts.MET.root -t hlt_MET_skimHLTPFMET150.py -n 100
cmsRun openhlt_go.py
```

#### Nota Bene

- `openHLT.TEMPLATE` has been modified and that has broken the compatibility with original `openHLT.py` #TODO
- FastTimerService clashes with SubProcess, so it is disabled from `setup_cff.py`.
- `isData` switch is hardcoded in `openHLT.TEMPLATE`.
- Global tags for MC are hardcoded in `openHLT.TEMPLATE`, `openHLT2PAT.TEMPLATE`.
- Global tag for PAT is hardcoded in `openHLT2PAT.TEMPLATE`.
- Global tag for HLT is provided by default by `setup_cff.py` and can be overwritten by input HLT config file.
- To run CRAB jobs, it's easiest to use the `dump.py` file that is produced when `cmsRun openhlt_go.py` is executed successfully.

### Useful Links

- https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT

