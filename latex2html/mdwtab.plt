%                                               -*- Tralics -*-
%
%  mdwtab.plt
%
%  (C) Copyright 2005-2012 EDF-EADS-Phimeca
%
%  This library is free software; you can redistribute it and/or
%  modify it under the terms of the GNU Lesser General Public
%  License as published by the Free Software Foundation; either
%  version 2.1 of the License.
%
%  This library is distributed in the hope that it will be useful
%  but WITHOUT ANY WARRANTY; without even the implied warranty of
%  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
%  Lesser General Public License for more details.
%
%  You should have received a copy of the GNU Lesser General Public
%  License along with this library; if not, write to the Free Software
%  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
%
%  @author: $LastChangedBy$
%  @date:   $LastChangedDate$
%  Id:      $Id$
%
\ProvidesPackage{mdwtab}[2011/04/10 v1.0 Mdwtab: Addition to Tralics]

\def\hlx#1{\hlx@loop#1\q@delim}
\def\hlx@loop#1{%
  \ifx#1\q@delim\else%
    \@ifundefined{hlx@cmd@\string#1}{%
      \expandafter\hlx@loop%
    }{%
      \csname hlx@cmd@\string#1\expandafter\endcsname%
    }%
  \fi%
}
