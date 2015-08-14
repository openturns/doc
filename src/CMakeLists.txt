
set (PACKAGE ${CPACK_PACKAGE_NAME})
set (VERSION ${PACKAGE_VERSION})


configure_file (${CMAKE_CURRENT_SOURCE_DIR}/GenericInformation.tex.in 
                ${CMAKE_CURRENT_BINARY_DIR}/GenericInformation.tex
                @ONLY
)

# install common html files
if (TRALICS_FOUND AND XSLTPROC_EXECUTABLE)

  install (FILES OpenTURNS.css
            DESTINATION ${HTML_INSTALL_PATH}
         )
endif ()

macro (ot_add_document DOCUMENT_NAME)

  # parse arguments
  set (_CMD)
  set (_PDF_DEPENDENCIES)
  set (_PDF_BIBFILES)
  set (_PDF_IMAGE_DIRS)
  set (_XML_DEPENDENCIES)
  set (_USE_INDEX)
  set (_PARAMS)
  set (_IGNOREOUT OFF)
  foreach (_ARG ${ARGN})
    string (TOUPPER ${_ARG} ARG)
    if (${ARG} MATCHES PDF_DEPENDENCIES)
      set (_CMD PDF_DEPENDENCIES)
    elseif (${ARG} MATCHES PDF_BIBFILES)
      set (_CMD PDF_BIBFILES)
    elseif (${ARG} MATCHES PDF_IMAGE_DIRS)
      set (_CMD PDF_IMAGE_DIRS)
    elseif (${ARG} MATCHES XML_DEPENDENCIES)
      set (_CMD XML_DEPENDENCIES)
    elseif (${ARG} MATCHES USE_INDEX)
      set (_USE_INDEX "USE_INDEX")
    else ()
      if (${_CMD} MATCHES PDF_DEPENDENCIES)
        list (APPEND _PDF_DEPENDENCIES ${_ARG})
      elseif (${_CMD} MATCHES PDF_BIBFILES)
        list (APPEND _PDF_BIBFILES ${_ARG})
      elseif (${_CMD} MATCHES PDF_IMAGE_DIRS)
        list (APPEND _PDF_IMAGE_DIRS ${_ARG})
      elseif (${_CMD} MATCHES XML_DEPENDENCIES)
        list (APPEND _XML_DEPENDENCIES ${_ARG})
      endif ()
    endif ()
  endforeach (_ARG)

  # install scripts
  file (GLOB PYTHON_SCRIPTS "${CMAKE_CURRENT_SOURCE_DIR}/Scripts/*.py")
  install (FILES ${PYTHON_SCRIPTS}
            DESTINATION ${EXAMPLES_INSTALL_PATH}
         )

  # cut scripts and put them in binary dir
  set (PART_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/Scripts)
  execute_process (COMMAND ${CMAKE_COMMAND} -E make_directory ${PART_DIRECTORY})
  foreach (PYTHON_SCRIPT ${PYTHON_SCRIPTS})
    get_filename_component (BASENAME ${PYTHON_SCRIPT} NAME_WE)
    set (PART_FILE ${PART_DIRECTORY}/${BASENAME}.part)
    execute_process (COMMAND ${CMAKE_COMMAND} -DPYTHON_SCRIPT=${PYTHON_SCRIPT} -DPART_FILE=${PART_FILE} -P ${CMAKE_SOURCE_DIR}/cmake/cut_script.cmake)                    
  endforeach ()

  # find all generated part files relatively to the src dir
  file (GLOB PART_FILES RELATIVE ${CMAKE_CURRENT_BINARY_DIR} "${PART_DIRECTORY}/*.part")

  list (APPEND _PDF_DEPENDENCIES ${PART_FILES})
  list (APPEND _XML_DEPENDENCIES ${PART_FILES})

  # latex part 
  if (PDFLATEX_COMPILER AND BIBTEX_COMPILER)

    if (CMAKE_CURRENT_BINARY_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
      # in-source build
      set (LATEX_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/build)
    else ()
      # out-of-source build
      set (LATEX_OUTPUT_PATH ${CMAKE_CURRENT_BINARY_DIR})
    endif ()

    add_latex_document (OpenTURNS_${DOCUMENT_NAME}.tex 
      INPUTS ${_PDF_DEPENDENCIES}
      BIBFILES ${_PDF_BIBFILES}
      IMAGE_DIRS ${_PDF_IMAGE_DIRS}
      ${_USE_INDEX}
      DEFAULT_PDF
      MANGLE_TARGET_NAMES
   )

    execute_process (
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/Figures/logoOpenTURNS.jpg ${LATEX_OUTPUT_PATH}/logoOpenTURNS.jpg
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/latex2html/latex2html.sty ${LATEX_OUTPUT_PATH}/latex2html.sty
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/Math_Notations.sty ${LATEX_OUTPUT_PATH}/Math_Notations.sty
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/otcommon.sty ${LATEX_OUTPUT_PATH}/otcommon.sty
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_BINARY_DIR}/src/GenericInformation.tex ${LATEX_OUTPUT_PATH}/GenericInformation.tex
   )

    install (FILES ${LATEX_OUTPUT_PATH}/OpenTURNS_${DOCUMENT_NAME}.pdf DESTINATION ${PDF_INSTALL_PATH})

  endif ()

  if (TRALICS_FOUND AND XSLTPROC_EXECUTABLE)

    # list tex files
    set (_TEX_FILES)
    foreach (_PDF_DEPENDENCY ${_PDF_DEPENDENCIES})
      get_filename_component (_EXTENSION ${_PDF_DEPENDENCY} EXT)
      if (_EXTENSION STREQUAL ".tex")
        list (APPEND _TEX_FILES ${_PDF_DEPENDENCY})
      endif ()
    endforeach ()

    # link plt files
    if (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/OpenTURNS_${DOCUMENT_NAME}.sty)
      execute_process (
        COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_CURRENT_SOURCE_DIR}/OpenTURNS_${DOCUMENT_NAME}.sty ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.plt
     )
    endif ()
    execute_process (
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/Figures/logoOpenTURNS.jpg ${CMAKE_CURRENT_BINARY_DIR}/logoOpenTURNS.jpg
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/Math_Notations.sty ${CMAKE_CURRENT_BINARY_DIR}/Math_Notations.plt
      COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/src/otcommon.sty ${CMAKE_CURRENT_BINARY_DIR}/otcommon.plt
   )

    # write the tralics command in a separate file to ignore errors
    file (WRITE ${CMAKE_CURRENT_BINARY_DIR}/tralics.cmake
      "execute_process (COMMAND ${TRALICS_EXECUTABLE} -oe8 -noentnames -nozerowidthspace -confdir=${TRALICS_INCLUDE_DIR} -confdir=${CMAKE_SOURCE_DIR}/latex2html -inputdir=${CMAKE_CURRENT_SOURCE_DIR} -inputdir=${CMAKE_SOURCE_DIR}/src -outputdir=${CMAKE_CURRENT_BINARY_DIR} OpenTURNS_${DOCUMENT_NAME}.tex
                 ERROR_QUIET)"
   )

    add_custom_command (OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xml
                        COMMAND ${CMAKE_COMMAND} -P tralics.cmake
                        DEPENDS ${_TEX_FILES}
   )
    add_custom_command (OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xhtml
                        COMMAND ${XSLTPROC_EXECUTABLE} --path ${CMAKE_SOURCE_DIR}/latex2html --novalid -o ${CMAKE_CURRENT_BINARY_DIR}/cut.xml ${CMAKE_SOURCE_DIR}/latex2html/latex2html.xsl ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xml
                        COMMAND ${XSLTPROC_EXECUTABLE} --path ${CMAKE_SOURCE_DIR}/latex2html ${CMAKE_SOURCE_DIR}/latex2html/scissors.xsl ${CMAKE_CURRENT_BINARY_DIR}/cut.xml
                        COMMAND ${XSLTPROC_EXECUTABLE} --path ${CMAKE_SOURCE_DIR}/latex2html --novalid -o ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xhtml ${CMAKE_SOURCE_DIR}/latex2html/glue.xsl ${CMAKE_CURRENT_BINARY_DIR}/cut.xml
                        MAIN_DEPENDENCY ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xml
   )
    add_custom_target(OpenTURNS_${DOCUMENT_NAME}_xhtml ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/OpenTURNS_${DOCUMENT_NAME}.xhtml)

    install (FILES ${CMAKE_SOURCE_DIR}/src/Figures/logoOpenTURNS.jpg
                   ${CMAKE_SOURCE_DIR}/src/Figures/PreviousButton.png
                   ${CMAKE_SOURCE_DIR}/src/Figures/UpButton.png
                   ${CMAKE_SOURCE_DIR}/src/Figures/NextButton.png
             DESTINATION ${HTML_INSTALL_PATH}/${DOCUMENT_NAME}
            )

    # preserve directory structure when including png files
    file (GLOB_RECURSE PNG_FILES ${CMAKE_CURRENT_SOURCE_DIR}/*.png)
    foreach (PNG_FILE ${PNG_FILES})
      file (RELATIVE_PATH _RELATIVE_FILE ${CMAKE_CURRENT_SOURCE_DIR} ${PNG_FILE})
      get_filename_component (_RELATIVE_DIR ${_RELATIVE_FILE} PATH)
      install (FILES ${PNG_FILE}
                DESTINATION ${HTML_INSTALL_PATH}/${DOCUMENT_NAME}/${_RELATIVE_DIR})
    endforeach ()

    # install all html files
    file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/install_html.cmake 
      "file (GLOB HTML_FILES \"${CMAKE_CURRENT_BINARY_DIR}/*.xhtml\")
set (ABOLUTE_HTML_INSTALL_PATH \$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/${HTML_INSTALL_PATH})
execute_process (COMMAND ${CMAKE_COMMAND} -E make_directory \${ABOLUTE_HTML_INSTALL_PATH}/${DOCUMENT_NAME})
foreach (HTML_FILE \${HTML_FILES})
  get_filename_component (BASENAME \${HTML_FILE} NAME)
  execute_process (COMMAND ${CMAKE_COMMAND} -E compare_files \${HTML_FILE} \${ABOLUTE_HTML_INSTALL_PATH}/${DOCUMENT_NAME}/\${BASENAME}
                    RESULT_VARIABLE DIFFERENT
                    ERROR_QUIET)
  if (DIFFERENT)
    message (STATUS \"Installing: \${ABOLUTE_HTML_INSTALL_PATH}/${DOCUMENT_NAME}/\${BASENAME}\")
    execute_process (COMMAND ${CMAKE_COMMAND} -E copy \${HTML_FILE} \${ABOLUTE_HTML_INSTALL_PATH}/${DOCUMENT_NAME})
  else ()
    message (STATUS \"Up-to-date: \${ABOLUTE_HTML_INSTALL_PATH}/${DOCUMENT_NAME}/\${BASENAME}\")
  endif ()
endforeach ()
"
   )

    install (SCRIPT ${CMAKE_CURRENT_BINARY_DIR}/install_html.cmake)

  endif ()
endmacro ()

# recurse subdirectories
add_subdirectory (DevelopersGuide)
add_subdirectory (DocumentationGuide)
add_subdirectory (ExamplesGuide)
add_subdirectory (ReferenceGuide)
add_subdirectory (UserManual)
add_subdirectory (UseCasesGuide)

if (PDFLATEX_COMPILER AND BIBTEX_COMPILER)
  add_dependencies (OpenTURNS_UserManual_TUI_pdf OpenTURNS_ReferenceGuide_pdf)
  add_dependencies (OpenTURNS_UseCasesGuide_pdf OpenTURNS_UserManual_TUI_pdf OpenTURNS_ReferenceGuide_pdf)
endif ()
