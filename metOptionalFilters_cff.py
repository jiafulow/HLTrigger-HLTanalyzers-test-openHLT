import FWCore.ParameterSet.Config as cms

## The good vertices filter __________________________________________________||
goodVerticesFilter = cms.EDFilter(
    "VertexSelector",
    filter = cms.bool(True),
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)

## The beam scraping filter __________________________________________________||
noscraping = cms.EDFilter(
    "FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
    )

## The HCAL laser filter (Nov 2012) __________________________________________||
from EventFilter.HcalRawToDigi.hcallasereventfilter2012_cfi import *

## The ECAL dead cell boundary energy filter _________________________________||
# The section below is for the filter on Boundary Energy. Available in AOD in CMSSW>44x
# For releases earlier than 44x, one should make the following changes
# process.EcalDeadCellBoundaryEnergyFilter.recHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB")
# process.EcalDeadCellBoundaryEnergyFilter.recHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE")
from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import *
EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(False)
EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyDeadCellsEB=cms.untracked.double(10)
EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyDeadCellsEE=cms.untracked.double(10)
EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyGapEB=cms.untracked.double(100)
EcalDeadCellBoundaryEnergyFilter.cutBoundEnergyGapEE=cms.untracked.double(100)
EcalDeadCellBoundaryEnergyFilter.enableGap=cms.untracked.bool(False)
EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB = cms.vint32(12,14)
EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE = cms.vint32(12,14)

## Tracking TOBTEC fakes filter ______________________________________________||
# The following should already be loaded. If not, uncomment the following.
from RecoMET.METFilters.trackingPOGFilters_cfi import tobtecfakesfilter

tobtecfakesFilters = cms.Sequence( ~tobtecfakesfilter )

