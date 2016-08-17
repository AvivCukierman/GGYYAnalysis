import ROOT
from xAH_config import xAH_config
import sys, os

import shlex

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/GGYYAnalysis/")

c = xAH_config()

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

c.setalg("JetHistsAlgo", {
  "m_name":"Jets_Uncalib/",
  "m_inContainerName":"AntiKt4LCTopoJets", 
  "m_detailStr" : "kinematic energy NLeading4"
} )
