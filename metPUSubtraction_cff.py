import FWCore.ParameterSet.Config as cms


full_met_53x = cms.PSet(
    impactParTkThreshold = cms.double(1.),
    cutBased = cms.bool(False),
    tmvaWeights = cms.string("RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml"),
    tmvaMethod = cms.string("JetID"),
    version = cms.int32(-1),
    tmvaVariables = cms.vstring(
        "nvtx",
        "jetPt",
        "jetEta",
        "jetPhi",
        "dZ",
        "beta",
        "betaStar",
        "nCharged",
        "nNeutrals",
        "dR2Mean",
        "ptD",
        "frac01",
        "frac02",
        "frac03",
        "frac04",
        "frac05",
    ),
    tmvaSpectators = cms.vstring(),
    label = cms.string("full"),

    # the cut values are hardcoded in JetMETCorrections/METPUSubtraction/src/mvaMEtUtilities.cc
    JetIdParams = cms.PSet(
        #4 Eta Categories  0-2.5 2.5-2.75 2.75-3.0 3.0-5.0

        #Tight Id
        Pt010_Tight    = cms.vdouble( 0.5,0.6,0.6,0.9),
        Pt1020_Tight   = cms.vdouble(-0.2,0.2,0.2,0.6),
        Pt2030_Tight   = cms.vdouble( 0.3,0.4,0.7,0.8),
        Pt3050_Tight   = cms.vdouble( 0.5,0.4,0.8,0.9),

        #Medium Id
        Pt010_Medium   = cms.vdouble( 0.2,0.4,0.2,0.6),
        Pt1020_Medium  = cms.vdouble(-0.3,0. ,0. ,0.5),
        Pt2030_Medium  = cms.vdouble( 0.2,0.2,0.5,0.7),
        Pt3050_Medium  = cms.vdouble( 0.3,0.2,0.7,0.8),

        #Loose Id
        Pt010_Loose    = cms.vdouble(-0.2,-0.3,-0.5,-0.5),
        Pt1020_Loose   = cms.vdouble(-0.2,-0.2,-0.5,-0.3),
        Pt2030_Loose   = cms.vdouble(-0.2,-0.2,-0.2, 0.1),
        Pt3050_Loose   = cms.vdouble(-0.2,-0.2, 0. , 0.2)
    ),
)

from RecoJets.JetProducers.PileupJetID_53x_cfi import pileupJetIdProducer
from RecoJets.JetProducers.PileupJetIDParams_cfi import full_53x
pileupJetIdProducerForPFMEtMVA = pileupJetIdProducer.clone(
    jets = cms.InputTag("calibratedAK5PFJetsForPFMEtMVA"),
    algos = cms.VPSet(full_met_53x),
)
pileupJetIdProducerForNoPileUpPFMEt = pileupJetIdProducer.clone(
    jets = cms.InputTag("calibratedAK5PFJetsForNoPileUpPFMEt"),
    algos = cms.VPSet(full_53x),
)


#from RecoMET.METPUSubtraction.mvaPFMET_leptons_cff import pfMEtMVAsequence
from RecoMET.METPUSubtraction.mvaPFMET_leptons_cff import isomuons, hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits, hpsPFTauDiscriminationAgainstMuon2, isotaus, isoelectrons, calibratedAK5PFJetsForPFMEtMVA, pfMEtMVA, pfMEtMVAsequence
pfMEtMVAsequence2 = pfMEtMVAsequence
pfMEtMVAsequence2 += pileupJetIdProducerForPFMEtMVA

#from RecoMET.METPUSubtraction.noPileUpPFMET_cff import noPileUpPFMEtSequence
from RecoMET.METPUSubtraction.noPileUpPFMET_cff import calibratedAK5PFJetsForNoPileUpPFMEt, puJetIdForNoPileUpPFMEt, selectedVerticesForPFMEtCorrType0, selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0, particleFlowDisplacedVertex, trackToVertexAssociation, pfCandidateToVertexAssociation, pfMETcorrType0, pfCandidateToVertexAssociationForNoPileUpPFMEt, pfMETcorrType0ForNoPileUpPFMEt, jvfJetIdForNoPileUpPFMEt, noPileUpPFMEtData, noPileUpPFMEt, noPileUpPFMEtSequence
noPileUpPFMEtData.srcJetIds = cms.InputTag('pileupJetIdProducerForNoPileUpPFMEt', 'fullId')
noPileUpPFMEtSequence2 = noPileUpPFMEtSequence
noPileUpPFMEtSequence2.replace(puJetIdForNoPileUpPFMEt, pileupJetIdProducerForNoPileUpPFMEt)
noPileUpPFMEtSequence2.remove(pfCandidateToVertexAssociation)
noPileUpPFMEtSequence2.remove(pfMETcorrType0)
noPileUpPFMEtSequence2.remove(jvfJetIdForNoPileUpPFMEt)

