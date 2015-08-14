
set ( COMMON_INPUT 
  OpenTURNS_DocumentationGuide.tex 
)

set ( PDF_INPUT ${COMMON_INPUT}
)

set ( XML_INPUT ${COMMON_INPUT}
)

ot_add_document ( DocumentationGuide
                  PDF_DEPENDENCIES ${PDF_INPUT}
                  XML_DEPENDENCIES ${XML_INPUT}
)
