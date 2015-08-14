%                                               -*- Tralics -*-
%
%  latex2html.plt
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
\ProvidesPackage{latex2html}[2011/04/11 v1.0 Latex2html: Addition to Tralics]

% Suppress some error messages about undefined stuff
\let\listoffigures\relax
\let\listoftables\relax
\let\nouppercase\relax
\let\captionfont\relax
\let\ifpdf\iffalse
\newcounter{tocdepth}

% \strut should normally only be called from math mode
% Tralics is less permissive about that than LaTeX
\let\origstrut\strut
\def\strut{\ifmmode\origstrut\fi}

% Support for \addcontentsline
\def\addcontentsline#1#2#3{\xmlelt{addcontentsline}{
  \XMLaddatt{file}{#1}
  \XMLaddatt{sec_unit}{#2}
  \XMLaddatt{entry}{#3}
}}

% Support for titlepage environment
\newenvironment{titlepage}[0]{
  \begin{xmlelement*}{titlepage}}{
  \end{xmlelement*}}

% Fix missing paragraph in commands like \cleardoublepage
% This should be fixed in tralics very soon
\def\newpage{\par\xmlemptyelt{newpage}}
\def\clearpage{\par\xmlemptyelt{clearpage}}
\def\cleardoublepage{\par\xmlemptyelt{cleardoublepage}}

