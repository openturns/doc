

set ( COMMON_INPUT 
  OpenTURNS_DevelopersGuide.tex
  introduction.tex
  architecture.tex
  platform_development.tex
  documentation_development.tex
  module_development.tex
  wrapper_development.tex
  coding_rules.tex
  coding_rules_introduction.tex
  Package.tex
  FileNames.tex
  Cpp.tex
  Python.tex
  version_control.tex
  windows_port.tex
  windows_native_port.tex
)

set (PDF_INPUT ${COMMON_INPUT})

set (XML_INPUT ${COMMON_INPUT})

ot_add_document ( DevelopersGuide 
                  PDF_DEPENDENCIES ${PDF_INPUT}
                  PDF_IMAGE_DIRS Figures Figures/design Figures/modeling_notions Figures/win_native
                  XML_DEPENDENCIES ${XML_INPUT}
                  USE_INDEX
)
