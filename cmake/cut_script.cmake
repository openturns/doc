# script to cut python script PYTHON_SCRIPT into PART_FILE

file ( WRITE ${PART_FILE}.tmp "\\begin{lstlisting}\n")
file ( STRINGS ${PYTHON_SCRIPT} PYTHON_LINES )

# foreach does not iterate on empty list element
set ( CR_INDICATOR "-thisIsABlanLine-" )
STRING(REGEX REPLACE ";;" ";${CR_INDICATOR};" PYTHON_LINES "${PYTHON_LINES}")

set ( _TEX_BEGIN FALSE )
set ( _TEX_END FALSE )
foreach ( PYTHON_LINE ${PYTHON_LINES} )

  if ( "${PYTHON_LINE}" STREQUAL "${CR_INDICATOR}" )
    set ( PYTHON_LINE "" )
  endif ()

  # is this the beginning ?
  string ( REGEX MATCH "# BEGIN_TEX" _TEX_BEGIN_MATCH "${PYTHON_LINE}" )
  if ( _TEX_BEGIN_MATCH )
    set ( _TEX_BEGIN TRUE )
  endif ()
  
  # is this the end ?
  string ( REGEX MATCH "# END_TEX" _TEX_END_MATCH "${PYTHON_LINE}" )
  if ( _TEX_END_MATCH )
    set ( _TEX_END TRUE )
  endif ()
  
  # write the line after the beginning marker, and before the marker, and if not a keyword
  if ( NOT _TEX_BEGIN_MATCH AND NOT _TEX_END_MATCH AND _TEX_BEGIN AND NOT _TEX_END)
    file ( APPEND ${PART_FILE}.tmp "${PYTHON_LINE}\n" )
  endif ()
endforeach ()
file ( APPEND ${PART_FILE}.tmp  "\\end{lstlisting}\n")
file ( RENAME ${PART_FILE}.tmp ${PART_FILE} )
