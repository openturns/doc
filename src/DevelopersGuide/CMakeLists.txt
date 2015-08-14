

set ( COMMON_INPUT 
  OpenTURNS_DevelopersGuide.tex
  introduction.tex
  architecture.tex
  platform_development.tex
  documentation_development.tex
  module_development.tex
  wrapper_development.tex
  ExternalCodeInterface.tex
  FunctionTypes.tex
  FutureDevelopments.tex
  library_wrapper_introduction.tex
  WrapperStructure.tex
  Wrapper.tex
  coding_rules.tex
  coding_rules_introduction.tex
  Package.tex
  FileNames.tex
  Cpp.tex
  Python.tex
  version_control.tex
  windows_port.tex
  windows_native_port.tex
  library_wrapper.tex
)

set ( PDF_INPUT ${COMMON_INPUT}
  Figures/wrapper/Figure1.pdf
  Figures/wrapper/Figure2.pdf
  Figures/wrapper/Figure3.pdf
  Figures/wrapper/Figure4.pdf
  Figures/wrapper/Figure5.pdf
  Figures/wrapper/Figure6.pdf
  Figures/wrapper/Figure7.pdf
  Figures/wrapper/Figure8.pdf
)

set ( XML_INPUT ${COMMON_INPUT}
  Figures/wrapper/Figure1.png
  Figures/wrapper/Figure2.png
  Figures/wrapper/Figure3.png
  Figures/wrapper/Figure4.png
  Figures/wrapper/Figure5.png
  Figures/wrapper/Figure6.png
  Figures/wrapper/Figure7.png
  Figures/wrapper/Figure8.png
)

ot_add_document ( DevelopersGuide 
                  PDF_DEPENDENCIES ${PDF_INPUT}
                  PDF_IMAGE_DIRS Figures Figures/design Figures/modeling_notions Figures/win_native
                  XML_DEPENDENCIES ${XML_INPUT}
                  USE_INDEX
)
