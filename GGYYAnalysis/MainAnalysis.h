#ifndef GGYYAnalysis_MainAnalysis_H
#define GGYYAnalysis_MainAnalysis_H

#include "xAODRootAccess/TEvent.h"
#include <EventLoop/Algorithm.h>

#include <TH1.h>
#include <TTree.h>

class MainAnalysis : public EL::Algorithm
{
  // put your configuration variables here as public variables.
  // that way they can be set directly from CINT and python.
public:
  // float cutValue;

  bool isMC;
  // variables that don't get filled at submission time should be
  // protected from being send from the submission node to the worker
  // node (done by the //!)
public:
  xAOD::TEvent* m_event; //!
  TTree *m_tree; //!
  int m_eventnumber; //!
  int m_eventweight; //!

  std::vector<float> m_j0pt; //!
  std::vector<float> m_j0eta; //!
  std::vector<float> m_j0phi; //!
  std::vector<float> m_j0m; //!

  std::vector<float> m_gammapt; //!
  std::vector<float> m_gammaeta; //!
  std::vector<float> m_gammaphi; //!
  std::vector<float> m_gammam; //!

  // this is a standard constructor
  MainAnalysis ();

  // these are the functions inherited from Algorithm
  virtual EL::StatusCode setupJob (EL::Job& job);
  virtual EL::StatusCode fileExecute ();
  virtual EL::StatusCode histInitialize ();
  virtual EL::StatusCode changeInput (bool firstFile);
  virtual EL::StatusCode initialize ();
  virtual EL::StatusCode execute ();
  virtual EL::StatusCode postExecute ();
  virtual EL::StatusCode finalize ();
  virtual EL::StatusCode histFinalize ();

  // this is needed to distribute the algorithm to the workers
  ClassDef(MainAnalysis, 1);
};

#endif
