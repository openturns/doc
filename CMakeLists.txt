cmake_minimum_required (VERSION 2.8)

project (OpenTURNS-doc NONE)

list (APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

option (USE_LATEX "Use LaTeX for PDF output" ON)
option (USE_TRALICS "Use Tralics for HTML output" ON)

if (USE_LATEX)
  find_package (LATEX)
  include (UseLATEX)
endif ()

if (USE_TRALICS)
  find_program (XSLTPROC_EXECUTABLE xsltproc)
  find_package (Tralics)
endif ()

set (CMAKE_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}")
set (CPACK_SOURCE_IGNORE_FILES "/.git;/build;.*~;${CPACK_SOURCE_IGNORE_FILES};/_CPack_Packages;.*bz2;.*gz")
set (CPACK_PACKAGE_NAME openturns-doc)
set (OPENTURNS_VERSION 1.6) # default ot version
set (CPACK_PACKAGE_VERSION_MAJOR 2015) # YY
set (CPACK_PACKAGE_VERSION_MINOR 02) # MM
set (CPACK_PACKAGE_VERSION_PATCH  )
set (CPACK_SOURCE_GENERATOR      "TGZ;TBZ2"    )
set (CPACK_GENERATOR             "TGZ;TBZ2"    )
set (CPACK_BINARY_STGZ           "OFF"         )
set (CPACK_BINARY_TBZ2           "ON"          )
set (CPACK_BINARY_TGZ            "ON"          )
set (CPACK_BINARY_TZ             "OFF"         )
set (PACKAGE_NAME           ${CPACK_PACKAGE_NAME})
set (PACKAGE_VERSION        ${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR})
if (CPACK_PACKAGE_VERSION_PATCH)
  set (PACKAGE_VERSION      ${PACKAGE_VERSION}.${CPACK_PACKAGE_VERSION_PATCH})
endif (CPACK_PACKAGE_VERSION_PATCH)
set (CPACK_PACKAGE_VERSION ${PACKAGE_VERSION})
set (PACKAGE_BUGREPORT      bugs@openturns.org)
set (CPACK_COMPONENTS_ALL_IN_ONE_PACKAGE 1)
set (CPACK_SOURCE_PACKAGE_FILE_NAME ${PACKAGE_NAME}-${PACKAGE_VERSION})
set (CPACK_SYSTEM_NAME "any")
include (CPack)

find_package (PythonInterp)
if (CMAKE_VERSION VERSION_LESS "2.8.6")
  execute_process (COMMAND ${PYTHON_EXECUTABLE} -c "import sys; print(sys.version_info[0])"
                    OUTPUT_VARIABLE PYTHON_VERSION_MAJOR
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
endif ()

# Required to set the lib suffix of the config search path without enabling any language
if (CMAKE_SYSTEM_NAME MATCHES "Linux")
  execute_process (COMMAND uname -m
                    OUTPUT_VARIABLE _ARCH 
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
  if (_ARCH STREQUAL "x86_64")
    set (CMAKE_SIZEOF_VOID_P 8)
  endif ()
endif ()
find_package (OpenTURNS NO_MODULE)
if (OPENTURNS_FOUND)
  message(STATUS "Found OpenTURNS: ${OPENTURNS_ROOT_DIR}")
  set (OPENTURNS_VERSION ${OPENTURNS_VERSION_STRING})
endif ()

set (DOC_INSTALL_PATH share/doc/openturns-doc CACHE PATH "doc directory" )
set (HTML_INSTALL_PATH ${DOC_INSTALL_PATH}/html CACHE PATH "HTML directory")
set (PDF_INSTALL_PATH ${DOC_INSTALL_PATH}/pdf CACHE PATH "PDF directory")
set (EXAMPLES_INSTALL_PATH ${DOC_INSTALL_PATH}/examples CACHE PATH "examples directory")

# subdirectories
add_subdirectory (src)
enable_testing ()

add_subdirectory (test)
