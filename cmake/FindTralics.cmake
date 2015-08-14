# - Find Tralics
# Tralics is a free software whose purpose is to convert a LaTeX document into an XML file.
# www-sop.inria.fr/marelle/tralics
#
# The module defines the following variables:
#  TRALICS_FOUND        - True if Tralics found.
#  TRALICS_INCLUDE_DIR  - where to find latex.plt
#  TRALICS_EXECUTABLE   - Tralics executable
#
#=============================================================================
# Copyright 2005-2012 EDF-EADS-Phimeca
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distributed this file outside of CMake, substitute the full
#  License text for the above reference.)

if ( TRALICS_INCLUDE_DIR )
   # in cache already
   set( Tralics_FIND_QUIETLY TRUE )
endif ( TRALICS_INCLUDE_DIR )


find_program( TRALICS_EXECUTABLE
              NAMES tralics
)


find_path ( TRALICS_INCLUDE_DIR
            NAMES
              latex.plt 
            HINTS
              /usr/share/tralics
)

include ( FindPackageHandleStandardArgs )

find_package_handle_standard_args ( Tralics DEFAULT_MSG TRALICS_EXECUTABLE TRALICS_INCLUDE_DIR )

mark_as_advanced ( TRALICS_INCLUDE_DIR TRALICS_EXECUTABLE )

