source /uscmst1/prod/sw/cms/cshrc prod  # only at FNAL
setenv SCRAM_ARCH slc5_amd64_gcc462

## Prepare working area
cmsrel CMSSW_5_3_14_patch2
cd CMSSW_5_3_14_patch2/src
cmsenv

# ------------------------------------------------------------------------------
# for HLT
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT
# ------------------------------------------------------------------------------
git cms-addpkg HLTrigger/Configuration

# ------------------------------------------------------------------------------
# for NewOpenHLT
# https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
# ------------------------------------------------------------------------------
git cms-addpkg HLTrigger/HLTanalyzers

# ------------------------------------------------------------------------------
# PAT recipe
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X
# ------------------------------------------------------------------------------
git cms-addpkg PhysicsTools/PatAlgos

# ------------------------------------------------------------------------------
# MET recipe
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMETRecipe53X
# ------------------------------------------------------------------------------
git cms-merge-topic -u TaiSakuma:53X-met-131120-01

# ------------------------------------------------------------------------------
# for MET filters
# https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
# ------------------------------------------------------------------------------
# I believe it is all updated using TaiSakuma:53X-met-131120-01

# ------------------------------------------------------------------------------
# TobTecFakesFilter
# ------------------------------------------------------------------------------
#cvs co -d KStenson/TrackingFilters UserCode/KStenson/TrackingFilters
#cp KStenson/TrackingFilters/plugins/TobTecFakesFilter.cc RecoMET/METFilters/plugins/
#cp KStenson/TrackingFilters/python/tobtecfakesfilter_cfi.py RecoMET/METFilters/python/
#rm -rf KStenson/TrackingFilters
git cms-addpkg RecoMET/METFilters
wget --no-check-certificate https://gist.githubusercontent.com/jiafulow/1cecbd551b4075219af4/raw/d7fb810e20a18330be8de0e00bb127878f1573a6/TobTecFakesFilter.cc -O RecoMET/METFilters/plugins/TobTecFakesFilter.cc

# ------------------------------------------------------------------------------
# MVA and No-PU MET
# https://twiki.cern.ch/twiki/bin/view/CMS/MVAMet
# https://twiki.cern.ch/twiki/bin/view/CMS/NoPileUpMet
# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID
# ------------------------------------------------------------------------------
git-cms-merge-topic -v -u cms-met:53X-MVaNoPuMET-20131217-01

# ------------------------------------------------------------------------------
# LumiCalc (note: using GIT)
# https://twiki.cern.ch/twiki/bin/view/CMS/LumiCalc
# ------------------------------------------------------------------------------
#git clone https://github.com/cms-sw/RecoLuminosity-LumiDB.git RecoLuminosity/LumiDB
#cd RecoLuminosity/LumiDB
#git checkout V04-02-10
#cd -


## Finish up
#checkdeps -a
scram b -j4
rehash

