
set ( COMMON_INPUT
  OpenTURNS_ExamplesGuide.tex
  resultatExampleBeam.tex
  scriptExample_beam.py
  scriptExample_Truss_mainSparsePolyChaos.py
  scriptExample_Truss_PhysicalModel.py
  scriptExample_Truss_ProbaModel.py
  Figures/Truss_histo.png 
)

set ( PDF_INPUT ${COMMON_INPUT}
  Figures/convergenceGrapheDS.pdf
  Figures/convergenceGrapheIS.pdf
  Figures/convergenceGrapheMonteCarlo.pdf
  Figures/distributionE_pdf.pdf
  Figures/distributionF_pdf.pdf
  Figures/distributionI_pdf.pdf
  Figures/distributionL_pdf.pdf
  Figures/ImportanceFactorsDrawingFORM.pdf
  Figures/PCE_LaguerrePolynomials_VariableF.pdf
  Figures/PCE_JacobiPolynomials_VariableI.pdf
  Figures/PCE_JacobiPolynomials_VariableE.pdf
  Figures/PCE_LegendrePolynomials_VariableL.pdf
  Figures/PCE_comparisonModels.pdf
  Figures/poutre.pdf
  Figures/smoothedCDF.pdf
  Figures/smoothedPDF.pdf
  Figures/smoothedPDF_and_GaussianPDF.pdf
  Figures/Treillis.pdf
  Figures/Truss_errors.pdf
  Figures/Truss_SA.pdf
  Figures/Truss_histo.pdf
)

set ( XML_INPUT ${COMMON_INPUT}
  Figures/convergenceGrapheDS.png
  Figures/convergenceGrapheIS.png
  Figures/convergenceGrapheMonteCarlo.png
  Figures/distributionE_pdf.png
  Figures/distributionF_pdf.png
  Figures/distributionI_pdf.png
  Figures/distributionL_pdf.png
  Figures/ImportanceFactorsDrawingFORM.png
  Figures/PCE_LaguerrePolynomials_VariableF.png
  Figures/PCE_JacobiPolynomials_VariableI.png
  Figures/PCE_JacobiPolynomials_VariableE.png
  Figures/PCE_LegendrePolynomials_VariableL.png
  Figures/PCE_comparisonModels.png
  Figures/poutre.png
  Figures/smoothedCDF.png
  Figures/smoothedPDF.png
  Figures/smoothedPDF_and_GaussianPDF.png
  Figures/Treillis.png
  Figures/Truss_errors.png
  Figures/Truss_SA.png
)

ot_add_document ( ExamplesGuide                  
                  PDF_DEPENDENCIES ${PDF_INPUT}
                  XML_DEPENDENCIES ${XML_INPUT}
)
