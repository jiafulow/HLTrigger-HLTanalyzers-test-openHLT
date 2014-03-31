source /uscmst1/prod/sw/cms/cshrc prod  # only at FNAL
setenv SCRAM_ARCH slc5_amd64_gcc462

## Prepare working area
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
addpkg HLTrigger/HLTanalyzers V03-10-20
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
# TobTecFakesFilter
# ------------------------------------------------------------------------------
cvs co -d KStenson/TrackingFilters UserCode/KStenson/TrackingFilters
cp KStenson/TrackingFilters/plugins/TobTecFakesFilter.cc RecoMET/METFilters/plugins/
cp KStenson/TrackingFilters/python/tobtecfakesfilter_cfi.py RecoMET/METFilters/python/
rm -rf KStenson/TrackingFilters

# ------------------------------------------------------------------------------
# PAT recipe V08-09-62
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X
# ------------------------------------------------------------------------------
addpkg DataFormats/PatCandidates V06-05-06-12
addpkg PhysicsTools/PatAlgos     V08-09-62
#addpkg PhysicsTools/PatUtils
addpkg PhysicsTools/PatUtils     V03-09-28

# ------------------------------------------------------------------------------
# MET recipe for CMSSW_5_3_11 (till patch 3)
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMETRecipe53X
# ------------------------------------------------------------------------------
#addpkg RecoMET/METAnalyzers V00-00-08  
addpkg DataFormats/METReco V03-03-11-01
addpkg JetMETCorrections/Type1MET V04-06-09-02


# ------------------------------------------------------------------------------
# Type-0+1 MET
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis
# https://github.com/TaiSakuma/WorkBookMet
# ------------------------------------------------------------------------------
## git-less solution :(
mkdir TaiSakuma_53X-met-130910-01
cd TaiSakuma_53X-met-130910-01
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/MetType1Corrections_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/TauMetCorrections_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/caloMETCorrections_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctedMet_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctionTermsCaloMet_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctionTermsPfMetShiftXY_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctionTermsPfMetType0PFCandidate_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctionTermsPfMetType0RecoTrack_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/correctionTermsPfMetType1Type2_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/pfMETCorrectionType0_cfi.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/pfMETCorrections_cff.py
wget --no-check-certificate https://github.com/TaiSakuma/cmssw/raw/53X-met-130910-01/JetMETCorrections/Type1MET/python/pfMETsysShiftCorrections_cfi.py
cp *.py ../JetMETCorrections/Type1MET/python/
cd ..
rm -rf TaiSakuma_53X-met-130910-01


# ------------------------------------------------------------------------------
# MVA MET
# https://twiki.cern.ch/twiki/bin/view/CMS/MVAMet
# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID
# ------------------------------------------------------------------------------
#cvs co -r METPU_5_3_X_v10 JetMETCorrections/METPUSubtraction
#cvs co -r HEAD -d pharrisTmp UserCode/pharris/MVAMet/data
#cp  -d pharrisTmp/*June2013*.root          JetMETCorrections/METPUSubtraction/data/
#cp  -d pharrisTmp/*Dec2012*.root           JetMETCorrections/METPUSubtraction/data/
##cp  -d pharrisTmp/*53_UnityResponse.root  JetMETCorrections/METPUSubtraction/data/
#rm -rf pharrisTmp
#
### Micro-managing :(
### 1. Get PU jet id stuff
#addpkg DataFormats/JetReco  # refer V05-00-16
#cd DataFormats/JetReco
#cvs up -r 1.1 interface/PileupJetIdentifier.h
#cvs up -r 1.1 src/PileupJetIdentifier.cc
#cvs up -r 1.67 src/classes.h
#cvs up -r 1.71 src/classes_def.xml
#cd -
#
#addpkg RecoJets/JetProducers  # refer METPU_5_3_X_v4
#cvs co -r HEAD RecoJets/JetProducers/data
#cd RecoJets/JetProducers
#cvs up -r 1.4 BuildFile.xml
#cvs up -r 1.2 interface/PileupJetIdAlgo.h
#cvs up -r 1.1 src/PileupJetIdAlgo.cc
#cvs up -r 1.2 plugins/BuildFile.xml
#cvs up -r 1.2 plugins/PileupJetIdProducer.cc
#cvs up -r HEAD python/PileupJetIDCutParams_cfi.py
#cvs up -r HEAD python/PileupJetIDParams_cfi.py
#cvs up -r HEAD python/PileupJetID_cfi.py
#cd -
#
### 2. Get MVA MET stuff
##addpkg DataFormats/METReco  # refer b5_3_X_cvMEtCorr_2013Feb22
#cd DataFormats/METReco
#cvs up -r 1.2 interface/MVAMEtData.h
#cvs up -r 1.1 interface/MVAMEtDataFwd.h
#cvs up -r 1.2 interface/SigInputObj.h
#cvs up -r 1.3 interface/PFMEtSignCovMatrix.h
#cvs up -r 1.1 src/MVAMEtData.cc
#cvs up -r 1.2 src/SigInputObj.cc
#cvs up -r 1.36 src/classes.h
#cvs up -r 1.41 src/classes_def.xml
#sed -i 's@class name="HcalNoiseSummary" ClassVersion="14"@class name="HcalNoiseSummary" ClassVersion="11"@' src/classes_def.xml
#cd -
#
#addpkg RecoMET/METAlgorithms  # refer V03-04-07
#cd RecoMET/METAlgorithms
#rm interface/SigInputObj.h
#rm src/SigInputObj.cc
#cvs up -r 1.6 interface/SignAlgoResolutions.h
#cvs up -r 1.7 interface/SignCaloSpecificAlgo.h
#cvs up -r 1.3 interface/significanceAlgo.h
#cvs up -r 1.11 src/SignCaloSpecificAlgo.cc
#cd -
#
#addpkg RecoTauTag/RecoTau V01-05-07-00
#
### 3. Get noPU MET stuff
#cd JetMETCorrections/METPUSubtraction
#cvs up -r 1.2 interface/noPileUpMEtAuxFunctions.h
#cvs up -r 1.2 src/noPileUpMEtAuxFunctions.cc
#cd -


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

