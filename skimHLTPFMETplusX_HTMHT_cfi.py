import FWCore.ParameterSet.Config as cms

hlt_MET_ = [
        'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v*',
        'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v*',
        'HLT_DiCentralPFJet30_PFMET80_v*',
        'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v*',
        'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v*',
        'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v*',
       #'HLT_L1ETM100_v*',
        'HLT_L1ETM30_v*',
        'HLT_L1ETM40_v*',
       #'HLT_L1ETM70_v*',
       #'HLT_MET120_HBHENoiseCleaned_v*',
       #'HLT_MET120_v*',
       #'HLT_MET200_HBHENoiseCleaned_v*',
       #'HLT_MET200_v*',
       #'HLT_MET300_HBHENoiseCleaned_v*',
       #'HLT_MET300_v*',
       #'HLT_MET400_HBHENoiseCleaned_v*',
       #'HLT_MET400_v*',
        'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v*',
        'HLT_PFMET150_v*',
        'HLT_PFMET180_v*'
        ]

hlt_MET = " OR ".join(hlt_MET_)

skimHLTPFMETplusX_HTMHT = cms.EDFilter("TriggerResultsFilter",
    hltResults            = cms.InputTag('TriggerResults', '', 'HLT'),  # HLT results   - set to empty to ignore HLT
    l1tResults            = cms.InputTag(''),                 # L1 GT results - set to empty to ignore L1
    l1tIgnoreMask         = cms.bool(False),                  # use L1 mask
    l1techIgnorePrescales = cms.bool(False),                  # read L1 technical bits from PSB#9, bypassing the prescales
    daqPartitions         = cms.uint32(0x01),                 # used by the definition of the L1 mask
    throw                 = cms.bool(True),                   # throw exception on unknown trigger names
    triggerConditions     = cms.vstring(
        '(HLT_PFNoPUHT350_PFMET100_v* OR HLT_PFNoPUHT400_PFMET100_v*) AND NOT (%s)' % hlt_MET
        )
    )

