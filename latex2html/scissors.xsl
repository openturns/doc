<?xml version="1.0" encoding="UTF-8"?>
<!--                                            -*- Libxslt -*-
 
   scissors.xsl
 
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
                xmlns:exsl="http://exslt.org/common"
                extension-element-prefixes="exsl"
                xmlns="http://www.w3.org/1999/xhtml"
                xmlns:mathml="http://www.w3.org/1998/Math/MathML"
                xmlns:cut="http://www.openturns.org/scissors"
                version="1.0">

  <xsl:output method="xml" encoding="UTF-8" />

  <xsl:template match="/">
    <xsl:message>index.xhtml</xsl:message>
    <exsl:document href="index.xhtml"
                   encoding="UTF-8"
                   method="xml"
                   doctype-public="-//W3C//DTD XHTML 1.1 plus MathML 2.0//EN"
                   doctype-system="http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd">
      <xsl:apply-templates />
    </exsl:document>
  </xsl:template>

  <xsl:template match="cut:here">
    <xsl:choose>
      <xsl:when test="@type = 'container'">
        <xsl:apply-templates />
      </xsl:when>
      <xsl:otherwise>
        <xsl:message>
          <xsl:value-of select="@filename" />
        </xsl:message>
        <xsl:call-template name="document" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="cut:link">
    <xsl:element name="a">
      <xsl:attribute name="href">
        <xsl:value-of select="id(@href)/ancestor::cut:here[1]/@filename" />
        <xsl:text>#</xsl:text>
        <xsl:value-of select="@href" />
      </xsl:attribute>
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>

  <xsl:template name="document">
    <exsl:document href="{@filename}"
                   encoding="UTF-8"
                   method="xml"
                   doctype-public="-//W3C//DTD XHTML 1.1 plus MathML 2.0//EN"
                   doctype-system="http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd">
      <html>
        <head>
          <title>
            <xsl:value-of select="@title" />
          </title>
          <meta http-equiv="Content-Type" content="application/xhtml+xml;charset=UTF-8" />
          <link rel="stylesheet" type="text/css" href="../OpenTURNS.css" />
        </head>
        <body>
          <xsl:apply-templates />
          <xsl:call-template name="buttons" />
        </body>
      </html>
    </exsl:document>
  </xsl:template>

  <xsl:template name="buttons">
    <xsl:variable name="preceding" select="count(preceding::cut:here)" />
    <xsl:variable name="following" select="count(following::cut:here)" />
    <table>
      <tr>
        <td>
          <xsl:if test="$preceding">
            <div class ="centered"> 
              <a href="{preceding::cut:here[1]/@filename}">
                <img src="PreviousButton.png" />
              </a>
            </div>
          </xsl:if>
        </td>
        <td>
          <div class ="centered"> 
            <a href="index.xhtml">
              <img src="UpButton.png" />
            </a>
          </div>
        </td>
        <td>
          <xsl:if test="$following">
            <div class ="centered"> 
              <a href="{following::cut:here[1]/@filename}">
                <img src="NextButton.png" />
              </a>
            </div>
          </xsl:if>
        </td>
      </tr>
      <tr>
        <td>
          <div class ="centered"> 
            <xsl:if test="$preceding">
              <xsl:value-of select="preceding::cut:here[1]/@title" />
            </xsl:if>
            &#xA0;
          </div>
        </td>
        <td>
          <div class ="centered"> 
            Table of contents
          </div>
        </td>
        <td>
          <div class ="centered"> 
            <xsl:if test="$following">
              <xsl:value-of select="following::cut:here[1]/@title" />
            </xsl:if>
            &#xA0;
          </div>
        </td>
      </tr>
    </table>
  </xsl:template>

  <xsl:template match="*|@*">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()" />
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
