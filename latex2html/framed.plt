%                                               -*- Tralics -*-
%
%  framed.plt
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
\ProvidesPackage{framed}[2011/04/07 v1.0 Framed: Addition to Tralics]

\newenvironment{framed}[0]{
  \begin{xmlelement*}{framed}}{
  \end{xmlelement*}}
