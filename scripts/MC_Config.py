import ROOT
from xAH_config import xAH_config
import sys, os

import shlex

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/GGYYAnalysis/")

c = xAH_config()

#
# Triggers
#
triggersList = [
  'L1_4J20',
  'L1_J100',
  'L1_3J25.0ETA23',
  'L1_4J15.0ETA25',
  'L1_J75_3J20',
  'HLT_.*bmv2c20.*',
  'HLT_ht.*',
  'HLT_j65_bt.*',
  'HLT_j70_bt.*',
  'HLT_j75_bt.*',
  'HLT_j175_bt.*',
  'HLT_2j35_bt.*',
  'HLT_2j45_bt.*',
  'HLT_2j55_bt.*',
  'HLT_2j65_bt.*',
  'HLT_2j70_bt.*',
  'HLT_2j75_bt.*',
  'HLT_j65_bm.*',
  'HLT_j70_bm.*',
  'HLT_j75_bm.*',
  'HLT_j175_bm.*',
  'HLT_2j35_bm.*',
  'HLT_2j45_bm.*',
  'HLT_2j55_bm.*',
  'HLT_2j65_bm.*',
  'HLT_2j70_bm.*',
  'HLT_2j75_bm.*',
  'HLT_j225_bl.*',
  'HLT_j300_bl.*',
  'HLT_j420.*',
  'HLT_j440.*',
  'HLT_j400.*',
  'HLT_j360.*',
  'HLT_j380.*',
  'HLT_j100',
  'HLT_j110',
  'HLT_j150',
  'HLT_j175',
  'HLT_j200',
  'HLT_j260',
  'HLT_.*bperf.*',
  'HLT_.*boffperf.*',
  'HLT_3j.*',
  'HLT_4j.*',
  'HLT_j3.*a10.*',
  'HLT_j4.*a10.*',
  'HLT_j100_2j55_bmedium',
  'HLT_e24_lhtight_iloose',
  'HLT_.*bmv2c20.*',
  'HLT_mu26_imedium'
]

#
# Event Selection
#
triggers = ",".join(triggersList)
c.setalg("BasicEventSelection", {
  "m_name"                  : "basicEventSel",
  "m_debug"                 : False,
  "m_derivationName"        : "HIGG5D3",
  "m_applyGRLCut"           : False,
  "m_doPUreweighting"       : False, 
  "m_vertexContainerName"   : "PrimaryVertices",
  "m_PVNTrack"              : 2,
  "m_truthLevelOnly"        : False,
  "m_applyPrimaryVertexCut" : True,
  "m_applyEventCleaningCut" : True,
  "m_applyCoreFlagsCut"     : True,
  "m_triggerSelection"      : triggers, 
  "m_storeTrigDecisions"    : True,
  "m_useMetaData"           : False,
  "m_applyTriggerCut"       : False,
  "m_storePassL1"           : True,
  "m_storePassHLT"          : True,
  "m_storeTrigKeys"         : True,
} )

#
# Uncalibrated Jets
#
c.setalg("JetHistsAlgo", {
  "m_name":"Jets_Uncalib/",
  "m_inContainerName":"AntiKt4LCTopoJets", 
  "m_detailStr" : "kinematic energy"
} )

#
#  Jet Calibration
#
c.setalg("JetCalibrator", {
  "m_name"                   : "AntiKt4TopoEM", 
  "m_inContainerName"        : "AntiKt4EMTopoJets",
  "m_outContainerName"       : "AntiKt4EMTopoJets_Calib", 
  "m_sort"                   : True,
  "m_jetAlgo"                : "AntiKt4EMTopo",
  "m_outputAlgo"             : "AntiKt4EMTopoJets_Calib_Algo",
  "m_calibSequence"          : "JetArea_Residual_Origin_EtaJES_GSC",
  "m_calibConfigFullSim"     : "JES_MC15cRecommendation_May2016.config",
  "m_calibConfigData"        : "JES_MC15cRecommendation_May2016.config",
  "m_calibConfigAFII"        : "JES_MC15Prerecommendation_AFII_June2015.config",
  "m_jetCleanCutLevel"       : "LooseBad",
  "m_JESUncertConfig"        : "$ROOTCOREBIN/data/JetUncertainties/JES_2015/ICHEP2016/JES2015_AllNuisanceParameters.config",
  "m_JESUncertMCType"        : "MC15",
  "m_saveAllCleanDecisions"  : True,                         
  "m_setAFII"                : False,
  "m_JERUncertConfig"        : "JetResolution/Prerec2015_xCalib_2012JER_ReducedTo9NP_Plots_v2.root",
  "m_JERApplyNominal"        : False,
  "m_redoJVT"                : True,
  "m_systName"               : "All",
  "m_systVal"                : 1
} )

#
# Calibrated Jets
#
c.setalg("JetHistsAlgo", {
  "m_name":"Jets_Calib/",
  "m_inContainerName":"AntiKt4EMTopoJets_Calib", 
  "m_detailStr" : "kinematic energy NLeading1"
} )

#
#  Jet Selection
#
c.setalg("JetSelector", {
  "m_name"                    :  "preSelJetsEMTopoJets",
  "m_inContainerName"         :  "AntiKt4EMTopoJets_Calib",
  "m_inputAlgo"               :  "AntiKt4EMTopoJets_Calib_Algo",
  "m_outContainerName"        :  "AntiKt4EMTopoJets_Calib_preSel",
  "m_outputAlgo"              :  "AntiKt4EMTopoJets_Calib_preSel_Algo",
  "m_decorateSelectedObjects" :  False, 
  "m_createSelectedContainer" :  True, 
  "m_cleanJets"               :  True, 
  "m_cleanEvtLeadJets"        :  99,
  "m_pT_min"                  :  20e3,
  "m_eta_max"                 :  4.9,
  "m_useCutFlow"              :  True,
  "m_doJVT"                   :  True,
  "m_pt_max_JVT"              :  60e3,
  "m_eta_max_JVT"             :  2.4,
  "m_WorkingPointJVT"         :  "Medium",
  "m_jetScaleType"            :  "JetConstitScaleMomentum",
  "m_debug"                   :  False
} )
