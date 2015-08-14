<?xml version="1.0" encoding="UTF-8"?>
<!--                                            -*- Libxslt -*-
 
   glue.xsl
 
   (C) Copyright 2005-2012 EDF-EADS-Phimeca
 
   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License.
 
   This library is distributed in the hope that it will be useful
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.
 
   You should have received a copy of the GNU Lesser General Public
   License along with this library; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
 
   @author: $LastChangedBy$
   @date:   $LastChangedDate$
   Id:      $Id$

-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns="http://www.w3.org/1999/xhtml"
                xmlns:mathml="http://www.w3.org/1998/Math/MathML"
                xmlns:cut="http://www.openturns.org/scissors"
                version="1.0">

  <xsl:output method="xml"
              encoding="UTF-8"
              doctype-public="-//W3C//DTD XHTML 1.1 plus MathML 2.0//EN"
              doctype-system="http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd" />

  <xsl:template match="cut:here">
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template match="cut:link">
    <xsl:element name="a">
      <xsl:attribute name="href">
        <xsl:text>#</xsl:text>
        <xsl:value-of select="@href" />
      </xsl:attribute>
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>

  <xsl:template match="*|@*">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
