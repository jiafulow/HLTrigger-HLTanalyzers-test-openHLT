source /uscmst1/prod/sw/cms/cshrc prod  # only at FNAL
setenv SCRAM_ARCH slc5_amd64_gcc462

# Prepare working area
cmsrel CMSSW_5_3_11
cd CMSSW_5_3_11/src
cmsenv

#kserver_init  # only at FNAL

# ------------------------------------------------------------------------------
# for HLT
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT
# ------------------------------------------------------------------------------
addpkg HLTrigger/Configuration

# ------------------------------------------------------------------------------
# for NewOpenHLT
# https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
# ------------------------------------------------------------------------------
addpkg HLTrigger/btau V04-01-16
addpkg HLTrigger/HLTanalyzers
#cp /afs/cern.ch/user/h/halil/public/openHLT/* .

# ------------------------------------------------------------------------------
# for MET filters
# https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
# ------------------------------------------------------------------------------
# Current configuration of the tracking POG filters in V00-00-13 only works on AOD for releases >=53X
cvs co -r V00-00-13-01 RecoMET/METFilters
# For CSC Beam Halo filter
cvs co -r V00-00-08 RecoMET/METAnalyzers
# For the HBHE filter
# For 52x release, please check out the following branch since it fixes a compiling issue
# cvs co -r BV00-03-20_HBHEfor52X CommonTools/RecoAlgos
cvs co -r V00-03-23 CommonTools/RecoAlgos
# Additional packages for the tracking POG filters
cvs co -r V01-00-11-01 DPGAnalysis/Skims
cvs co -r V00-11-17 DPGAnalysis/SiStripTools
cvs co -r V00-00-08 DataFormats/TrackerCommon
cvs co -r V01-09-05 RecoLocalTracker/SubCollectionProducers

# ------------------------------------------------------------------------------
# PAT recipe V08-09-62
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X
# ------------------------------------------------------------------------------
addpkg DataFormats/PatCandidates V06-05-06-12
addpkg PhysicsTools/PatAlgos     V08-09-62
addpkg PhysicsTools/PatUtils

# ------------------------------------------------------------------------------
# MET recipe for CMSSW_5_3_11
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMETRecipe53X
# ------------------------------------------------------------------------------
#addpkg RecoMET/METAnalyzers V00-00-08  
addpkg DataFormats/METReco V03-03-11-01
addpkg JetMETCorrections/Type1MET V04-06-09-02


# ------------------------------------------------------------------------------
# MVA Met
# https://twiki.cern.ch/twiki/bin/view/CMS/MVAMet
# ------------------------------------------------------------------------------
#cvs co -r METPU_5_3_X_v12 JetMETCorrections/METPUSubtraction 
##cd JetMETCorrections/METPUSubtraction/test/
##./setup.sh 
##cd ../../../
#
#cvs co -r HEAD -d pharrisTmp UserCode/pharris/MVAMet/data
#cp  -d pharrisTmp/*June2013*.root           JetMETCorrections/METPUSubtraction/data/
##cp  -d pharrisTmp/*53_UnityResponse.root  JetMETCorrections/METPUSubtraction/data/
#rm -rf pharrisTmp
##cvs co -r METPU_5_3_X_v12 RecoJets/JetProducers
##cvs up -r HEAD RecoJets/JetProducers/data/
##cvs up -r HEAD RecoJets/JetProducers/python/PileupJetIDCutParams_cfi.py                     
##cvs up -r HEAD RecoJets/JetProducers/python/PileupJetIDParams_cfi.py                     
##cvs up -r HEAD RecoJets/JetProducers/python/PileupJetID_cfi.py                     
###cvs up -r CMSSW_5_3_3 RecoJets/JetProducers/src/JetSpecific.cc
##cvs co -r b5_3_X_cvMEtCorr_2013Feb22            DataFormats/METReco
##cvs co -r V05-00-16                             DataFormats/JetReco
##cvs co -r V01-04-25                             RecoTauTag/RecoTau 
##cvs co -r V03-04-07                             RecoMET/METAlgorithms
##cvs co -r V01-04-13                             RecoTauTag/Configuration


checkdeps -a
scram b -j4
rehash
