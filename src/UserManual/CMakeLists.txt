
set ( COMMON_INPUT
  OpenTURNS_UserManual_TUI.tex
  OpenTURNS_UserManual_TUI.sty
  BaseObjects_UserManual.tex
  DistFunc_UserManual.tex
  ExperimentPlane_UserManual.tex
  CombinatorialGenerator_UserManual.tex
  FFT_UserManual.tex
  Function_UserManual.tex
  Graphs_UserManual.tex
  Integration_UserManual.tex
  NonParametricResponseSurfaceApproximation_FCE_UserManual.tex
  NonParametricResponseSurfaceApproximation_Kriging_UserManual.tex
  OpenTURNS_UserManual_TUI.tex
  Optimization_UserManual.tex
  ParametricResponseSurfaceApproximation_UserManual.tex
  Polynomials_UserManual.tex
  ProbabilisticModeling_UserManual.tex
  QuadraticCumul_UserManual.tex
  ResourceMap_UserManual.tex
  SpecFunc_UserManual.tex
  Statistics_UserManual.tex
  Stochastic_Process_UserManual.tex
  ThresholdProbabilityReliabilityAlgorithm_UserManual.tex
  ThresholdProbabilitySimulationAlgorithm_UserManual.tex
  user_manual_title.tex
)

set ( PDF_INPUT ${COMMON_INPUT}
)

set ( XML_INPUT ${COMMON_INPUT}
)
      
ot_add_document ( UserManual_TUI 
                  PDF_DEPENDENCIES ${PDF_INPUT}
                  XML_DEPENDENCIES ${XML_INPUT}
                  USE_INDEX
)  
