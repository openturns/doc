<?xml version="1.0" encoding="UTF-8"?>
<!--                                            -*- Libxslt -*-
 
   latex2html.xsl
 
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

  <!-- Output type -->

  <xsl:output method="xml"
              encoding="UTF-8"
              doctype-public="-//W3C//DTD XHTML 1.1 plus MathML 2.0//EN"
              doctype-system="http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd" />

  <!-- Root element -->

  <xsl:template match="/">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <html>
          <head>
            <xsl:call-template name="root-head" />
          </head>
          <body>
            <cut:here type="container">
              <xsl:apply-templates />
            </cut:here>
          </body>
        </html>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:apply-templates>
          <xsl:with-param name="toc" select="'yes'" />
        </xsl:apply-templates>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="root-head">
    <xsl:element name="title">
      <xsl:value-of select="//headings[@type='olh']/hi" />
    </xsl:element>
    <xsl:element name="meta">
      <xsl:attribute name="http-equiv">Content-Type</xsl:attribute>
      <xsl:attribute name="content">application/xhtml+xml;charset=UTF-8</xsl:attribute>
    </xsl:element>
    <xsl:element name="link">
      <xsl:attribute name="rel">stylesheet</xsl:attribute>
      <xsl:attribute name="type">text/css</xsl:attribute>
      <xsl:attribute name="href">../OpenTURNS.css</xsl:attribute>
    </xsl:element>
  </xsl:template>

  <!-- Divisions -->

  <xsl:template match="div0">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <xsl:variable name="id">
          <xsl:call-template name="generate-id" />
        </xsl:variable>
        <cut:here filename="{$id}.xhtml" title="{head}">
          <xsl:call-template name="div-with-id">
            <xsl:with-param name="remap">h1</xsl:with-param>
          </xsl:call-template>
          <xsl:apply-templates>
            <xsl:with-param name="toc" select="'no'" />
            <xsl:with-param name="div" select="'yes'" />
          </xsl:apply-templates>
          <xsl:call-template name="div-footnotes" />
        </cut:here>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:call-template name="toc-div">
          <xsl:with-param name="class">toclevel1</xsl:with-param>
        </xsl:call-template>
        <xsl:apply-templates>
          <xsl:with-param name="toc" select="'yes'" />
          <xsl:with-param name="div" select="'yes'" />
        </xsl:apply-templates>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="div1">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <xsl:call-template name="div-with-id">
          <xsl:with-param name="remap">h2</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:call-template name="toc-div">
          <xsl:with-param name="class">toclevel2</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <xsl:apply-templates>
      <xsl:with-param name="toc" select="$toc" />
      <xsl:with-param name="div" select="'yes'" />
    </xsl:apply-templates>
    <xsl:if test="$toc = 'no'">
      <xsl:call-template name="div-footnotes" />
    </xsl:if>
  </xsl:template>

  <xsl:template match="div2">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <xsl:call-template name="div-with-id">
          <xsl:with-param name="remap">h3</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:call-template name="toc-div">
          <xsl:with-param name="class">toclevel3</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <xsl:apply-templates>
      <xsl:with-param name="toc" select="$toc" />
      <xsl:with-param name="div" select="'yes'" />
    </xsl:apply-templates>
    <xsl:if test="$toc = 'no'">
      <xsl:call-template name="div-footnotes" />
    </xsl:if>
  </xsl:template>

  <xsl:template match="div3">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <xsl:call-template name="div-with-id">
          <xsl:with-param name="remap">h4</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:call-template name="toc-div">
          <xsl:with-param name="class">toclevel4</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <xsl:apply-templates>
      <xsl:with-param name="toc" select="$toc" />
      <xsl:with-param name="div" select="'yes'" />
    </xsl:apply-templates>
    <xsl:if test="$toc = 'no'">
      <xsl:call-template name="div-footnotes" />
    </xsl:if>
  </xsl:template>

  <xsl:template match="div4">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc = 'no'">
        <xsl:call-template name="div-with-invisible-id">
          <xsl:with-param name="remap">h5</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
      <xsl:when test="$toc = 'yes'">
        <xsl:call-template name="toc-div">
          <xsl:with-param name="class">toclevel5</xsl:with-param>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <xsl:apply-templates>
      <xsl:with-param name="toc" select="$toc" />
      <xsl:with-param name="div" select="'yes'" />
    </xsl:apply-templates>
    <xsl:if test="$toc = 'no'">
      <xsl:call-template name="div-footnotes" />
    </xsl:if>
  </xsl:template>

  <xsl:template match="div5">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:call-template name="div-with-no-id">
        <xsl:with-param name="remap">h6</xsl:with-param>
      </xsl:call-template>
      <xsl:apply-templates>
        <xsl:with-param name="toc" select="$toc" />
        <xsl:with-param name="div" select="'yes'" />
      </xsl:apply-templates>
      <xsl:call-template name="div-footnotes" />
    </xsl:if>
  </xsl:template>

  <xsl:template name="div-with-id">
    <xsl:param name="remap" />
    <xsl:element name="{$remap}">
      <xsl:attribute name="id">
        <xsl:call-template name="generate-id" />
      </xsl:attribute>
      <xsl:value-of select="@id-text" />
      <xsl:text> </xsl:text>
      <xsl:value-of select="head" />
    </xsl:element>
  </xsl:template>

  <xsl:template name="div-with-invisible-id">
    <xsl:param name="remap" />
    <xsl:element name="{$remap}">
      <xsl:attribute name="id">
        <xsl:call-template name="generate-id" />
      </xsl:attribute>
      <xsl:value-of select="head" />
    </xsl:element>
  </xsl:template>

  <xsl:template name="div-with-no-id">
    <xsl:param name="remap" />
    <xsl:element name="{$remap}">
      <xsl:value-of select="head" />
    </xsl:element>
  </xsl:template>

  <xsl:template match="head" />

  <xsl:template name="div-footnotes">
    <xsl:for-each select="p//note">
      <xsl:element name="div">
        <xsl:attribute name="class">footnote</xsl:attribute>
        <xsl:attribute name="id"><xsl:value-of select="@id" /></xsl:attribute>
        <sup>
          <xsl:text>[</xsl:text>
          <xsl:value-of select="@id-text" />
          <xsl:text>]</xsl:text>
        </sup>
        <xsl:apply-templates />
      </xsl:element>
    </xsl:for-each>
  </xsl:template>

  <!-- Pages -->

  <xsl:template match="newpage">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <hr />
    </xsl:if>
  </xsl:template>

  <xsl:template match="clearpage">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <hr />
    </xsl:if>
  </xsl:template>

  <xsl:template match="cleardoublepage">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <hr />
    </xsl:if>
  </xsl:template>

  <!-- Paragraphs -->

  <xsl:template match="p">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test="@rend or @spacebefore">
          <!-- no real "paragraph", rather a layout division -->
          <xsl:call-template name="layout-division" />
        </xsl:when>
        <xsl:otherwise>
          <!-- normal paragraphs -->
          <p>
            <xsl:apply-templates />
          </p>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template name="layout-division">
    <xsl:element name="div">
      <xsl:if test="@rend = 'center'">
        <xsl:attribute name="class">centered</xsl:attribute>
      </xsl:if>
      <xsl:if test="@spacebefore">
        <xsl:attribute name="style">padding-top:<xsl:value-of select="@spacebefore" />;</xsl:attribute>
      </xsl:if>
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>

  <!-- Floats -->

  <xsl:template match="float">
    <xsl:param name="toc">no</xsl:param>
    <xsl:variable name="caption" select="p/caption|caption" />
    <xsl:if test="$toc = 'no'">
      <!-- container for tables, minipages or normal images -->
      <xsl:element name="table">
        <xsl:call-template name="optional-id" />
        <tr>
          <xsl:for-each select="p/minipage|minipage|p/figure|figure|p/table|table">
            <td>
              <xsl:apply-templates select="." />
              <xsl:if test="$caption != ''">
                <div class="centered">
                  <xsl:value-of select="$caption" />
                </div>
              </xsl:if>
            </td>
          </xsl:for-each>
        </tr>
      </xsl:element>
      <xsl:if test="@id-text">
        <div class="centered">
          <xsl:choose>
            <xsl:when test="@type = 'figure'">
              <b>Figure <xsl:value-of select="@id-text" /></b>
            </xsl:when>
            <xsl:when test="@type = 'table'">
              <b>Table <xsl:value-of select="@id-text" /></b>
            </xsl:when>
          </xsl:choose>
        </div>
      </xsl:if>
    </xsl:if>
  </xsl:template>

  <!-- Figures -->

  <xsl:template match="figure">
    <xsl:param name="toc">no</xsl:param>
    <xsl:variable name="head" select="head" />
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <!-- normal figures, referencing a file -->
        <xsl:when test="@file">
          <div class="centered">
            <xsl:call-template name="figure-image" />
          </div>
          <xsl:call-template name="figure-legend" />
        </xsl:when>
        <!-- special figures, containing minipages -->
        <xsl:otherwise>
          <xsl:element name="table">
            <xsl:call-template name="optional-id" />
            <tr>
              <xsl:for-each select="p/minipage|minipage">
                <td>
                  <xsl:apply-templates select="." />
                  <xsl:if test="position() = 1">
                    <div class="centered">
                      <xsl:value-of select="$head" />
                    </div>
                  </xsl:if>
                </td>
              </xsl:for-each>
            </tr>
          </xsl:element>
          <xsl:call-template name="figure-group-legend" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template match="caption">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:apply-templates />
    </xsl:if>
  </xsl:template>

  <xsl:template name="figure-image">
    <xsl:element name="img">
      <xsl:call-template name="optional-id" />
      <xsl:call-template name="figure-file" />
      <xsl:attribute name="width">50%</xsl:attribute>
      <xsl:attribute name="alt">
        <xsl:value-of select="head" />
      </xsl:attribute>
    </xsl:element>
  </xsl:template>

  <xsl:template name="figure-file">
    <xsl:attribute name="src">
      <xsl:value-of select="@file" />
      <xsl:text>.</xsl:text>
      <xsl:choose>
        <xsl:when test="@extension='pdf'">
          <xsl:text>png</xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="@extension" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:attribute>
  </xsl:template>

  <xsl:template name="figure-legend">
    <xsl:if test="@id-text">
      <div class="centered">
        <b>Figure <xsl:value-of select="@id-text" />: </b>
        <i><xsl:value-of select="head" /></i>
      </div>
    </xsl:if>
  </xsl:template>

  <xsl:template name="figure-group-legend">
    <xsl:if test="@id-text">
      <div class="centered">
        <b>Figure <xsl:value-of select="@id-text" /></b>
      </div>
    </xsl:if>
  </xsl:template>

  <!-- Lists -->

  <xsl:template match="list">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test="@type = 'simple'">
          <xsl:element name="ul">
            <xsl:call-template name="optional-id" />
            <xsl:apply-templates>
              <xsl:with-param name="listtype" select="@type" />
            </xsl:apply-templates>
          </xsl:element>
        </xsl:when>
        <xsl:when test="@type = 'ordered'">
          <xsl:element name="ol">
            <xsl:call-template name="optional-id" />
            <xsl:apply-templates>
              <xsl:with-param name="listtype" select="@type" />
            </xsl:apply-templates>
          </xsl:element>
        </xsl:when>
        <xsl:when test="@type = 'description'">
          <xsl:element name="dl">
            <xsl:call-template name="optional-id" />
            <xsl:apply-templates>
              <xsl:with-param name="listtype" select="@type" />
            </xsl:apply-templates>
          </xsl:element>
        </xsl:when>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template match="label">
    <xsl:param name="toc">no</xsl:param>
    <xsl:param name="listtype" />
    <xsl:if test="$toc = 'no'">
      <xsl:if test="$listtype = 'description'">
        <dt>
          <xsl:apply-templates />
        </dt>
      </xsl:if>
     </xsl:if>
  </xsl:template>

  <xsl:template match="item">
    <xsl:param name="toc">no</xsl:param>
    <xsl:param name="listtype" />
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test="$listtype = 'simple' or $listtype='ordered'">
          <xsl:call-template name="item-with-id">
            <xsl:with-param name="remap">li</xsl:with-param>
          </xsl:call-template>
        </xsl:when>
        <xsl:when test="$listtype = 'description'">
          <xsl:call-template name="item-with-id">
            <xsl:with-param name="remap">dd</xsl:with-param>
          </xsl:call-template>
        </xsl:when>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template name="item-with-id">
    <xsl:param name="remap" />
    <xsl:element name="{$remap}">
      <xsl:call-template name="optional-id" />
      <xsl:apply-templates />
    </xsl:element>
  </xsl:template>

  <!-- Tables -->

  <xsl:template match="table">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:element name="table">
        <xsl:call-template name="optional-id" />
        <xsl:attribute name="border">1</xsl:attribute>
        <xsl:call-template name="table-caption" />
        <xsl:for-each select="row">
          <tr>
            <xsl:apply-templates />
          </tr>
        </xsl:for-each>
      </xsl:element>
    </xsl:if>
  </xsl:template>

  <xsl:template name="table-caption">
    <xsl:if test="@id-text">
      <caption>
        <b>Table <xsl:value-of select="@id-text" />:</b>
        <xsl:text> </xsl:text>
        <xsl:value-of select="head" />
      </caption>
    </xsl:if>
  </xsl:template>

  <xsl:template match="cell">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <td>
        <xsl:apply-templates />
        &#xA0;
      </td>
    </xsl:if>
  </xsl:template>

  <!-- Table of contents -->

  <xsl:template match="tableofcontents">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <h1>Contents</h1>
      <xsl:apply-templates select="/">
        <xsl:with-param name="toc" select="'yes'" />
      </xsl:apply-templates>
    </xsl:if>
  </xsl:template>

  <xsl:template name="toc-div">
    <xsl:param name="class" />
    <xsl:element name="p">
      <xsl:attribute name="class">
        <xsl:value-of select="$class" />
      </xsl:attribute>
      <xsl:if test="$class != 'toclevel5'"> <!-- toc level 5 is not numbered -->
        <xsl:value-of select="@id-text" />
        <xsl:text> </xsl:text>
      </xsl:if>
      <xsl:element name="cut:link">
        <xsl:attribute name="href">
          <xsl:call-template name="generate-id" />
        </xsl:attribute>
        <xsl:value-of select="head" />
      </xsl:element>
    </xsl:element><xsl:text>
</xsl:text>
  </xsl:template>

  <xsl:template name="toc-biblio">
    <xsl:element name="p">
      <xsl:attribute name="class">toclevel1</xsl:attribute>
      <cut:link href="bibliography">Bibliography</cut:link>
    </xsl:element><xsl:text>
</xsl:text>
  </xsl:template>

  <xsl:template name="toc-index">
    <xsl:element name="p">
      <xsl:attribute name="class">toclevel1</xsl:attribute>
      <cut:link href="index">Index</cut:link>
    </xsl:element><xsl:text>
</xsl:text>
  </xsl:template>

  <!-- Bibliography -->

  <xsl:template match="biblio">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc='no'">
        <xsl:text disable-output-escaping="yes"><![CDATA[
          </cut:here>
          <cut:here xmlns:cut="http://www.openturns.org/scissors" filename="bibliography.xhtml" title="Bibliography">]]>
        </xsl:text>
        <h1 id="bibliography">Bibliography</h1>
        <table border="0">
          <xsl:apply-templates />
        </table>
      </xsl:when>
      <xsl:when test="$toc='yes'">
        <xsl:call-template name="toc-biblio" />
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="citation">
    <tr>
      <td valign="top">
        <xsl:element name="p">
          <xsl:attribute name="id">
            <xsl:value-of select="@id" />
          </xsl:attribute>
          [<xsl:value-of select="@key" />]
        </xsl:element>
      </td>
      <td>
        <xsl:apply-templates />
      </td>
    </tr>
  </xsl:template>

  <xsl:template match="bauteurs">
    <xsl:for-each select="bpers">
      <xsl:if test="position() > 1">
        <xsl:choose>
          <xsl:when test="position() &lt; last()">
            <xsl:text>, </xsl:text>
          </xsl:when>
          <xsl:otherwise>
            <xsl:choose>
              <xsl:when test="last() = 2">
                <xsl:text> and </xsl:text>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>, and </xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:if>
      <xsl:value-of select="@prenomcomplet" />
      <xsl:text> </xsl:text>
      <xsl:value-of select="@nom" />
    </xsl:for-each>.
  </xsl:template>

  <xsl:template match="btitle">
    <i>
      <xsl:apply-templates />
    </i>.
  </xsl:template>

  <xsl:template match="bpublisher">
    <xsl:apply-templates />.
  </xsl:template>

  <xsl:template match="bhowpublished">
    <xsl:apply-templates />.
  </xsl:template>

  <xsl:template match="bnote">
    <xsl:apply-templates />.
  </xsl:template>

  <!-- Index -->

  <xsl:template match="theindex">
    <xsl:param name="toc">no</xsl:param>
    <xsl:choose>
      <xsl:when test="$toc='no'">
        <xsl:text disable-output-escaping="yes"><![CDATA[
          </cut:here>
          <cut:here xmlns:cut="http://www.openturns.org/scissors" filename="theindex.xhtml" title="Index">]]>
        </xsl:text>
        <h1 id="index">
          <xsl:value-of select="@title" />
        </h1>
        <xsl:apply-templates />
      </xsl:when>
      <xsl:when test="$toc='yes'">
        <xsl:call-template name="toc-index" />
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="index">
    <xsl:if test="@level = '1'">
      <p class="primary">
        <xsl:value-of select="." />
        <xsl:call-template name="indexref">
          <xsl:with-param name="idrefs" select="@target"/>
        </xsl:call-template>
      </p>
      <xsl:if test="@target = ''">
        <xsl:for-each select="following-sibling::index[1]">
          <xsl:call-template name="index2" />
        </xsl:for-each>
      </xsl:if>
    </xsl:if>
  </xsl:template>

  <xsl:template name="index2">
    <xsl:if test="@level='2'">
      <p class="secondary">
        <xsl:value-of select="." />
        <xsl:call-template name="indexref">
          <xsl:with-param name="idrefs" select="@target"/>
        </xsl:call-template>
      </p>
      <xsl:for-each select="following-sibling::index[1]">
        <xsl:call-template name="index2" />
      </xsl:for-each>
    </xsl:if>
  </xsl:template>

  <xsl:template name="indexref">
    <xsl:param name="idrefs" />
    <xsl:variable name="string" select="concat(normalize-space($idrefs), ' ')" />
    <xsl:if test="$string != ' '">
      <xsl:variable name="before" select="substring-before($string, ' ')" />
      <xsl:variable name="after" select="substring-after($string, ' ')" />
      <xsl:text>, </xsl:text>
      <cut:link href="{$before}">here</cut:link>
      <xsl:call-template name="indexref">
        <xsl:with-param name="idrefs" select="$after" />
      </xsl:call-template>
    </xsl:if>
  </xsl:template>

  <xsl:template match="anchor">
    <xsl:param name="toc">no</xsl:param>
    <xsl:param name="div">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test="$div = 'yes'">
          <!-- block-level anchor -->
          <xsl:element name="div">
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
          </xsl:element>
        </xsl:when>
        <xsl:when test="$div = 'no'">
          <!-- inline anchor -->
          <xsl:element name="span">
            <xsl:attribute name="id">
              <xsl:value-of select="@id" />
            </xsl:attribute>
          </xsl:element>
        </xsl:when>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <!-- Maths -->

  <xsl:template match="formula">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test="@type = 'display'">
          <xsl:element name="table">
            <xsl:call-template name="optional-id" />
            <tr>
              <td class="ftext">
                <xsl:apply-templates />
              </td>
              <xsl:if test="@id-text">
                <td class="fnum">
                  (<xsl:value-of select="@id-text" />)
                </td>
              </xsl:if>
            </tr>
          </xsl:element>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template match="mathml:*|mathml:*/@*">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:copy>
        <xsl:apply-templates select="@*|node()" />
      </xsl:copy>
    </xsl:if>
  </xsl:template>

  <!-- Hyperref package -->

  <xsl:template match="hyperlink">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:element name="cut:link">
        <xsl:attribute name="href">
          <xsl:value-of select="@href" />
        </xsl:attribute>
        <xsl:apply-templates />
      </xsl:element>
    </xsl:if>
  </xsl:template>

  <xsl:template match="hypertarget">
    <xsl:element name="span">
      <xsl:attribute name="id">
        <xsl:value-of select="@name" />
      </xsl:attribute>
    </xsl:element>
  </xsl:template>

  <!-- Listings package -->

  <xsl:template match="listing">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:element name="p">
        <xsl:attribute name="class">
          <xsl:choose>
            <xsl:when test="@basicstyle = 'red'">redlisting</xsl:when>
            <xsl:when test="@basicstyle = 'blue'">bluelisting</xsl:when>
            <xsl:otherwise>listing</xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:for-each select="./p">
          <xsl:value-of select="." />
          <xsl:text>&#x0A;</xsl:text>
        </xsl:for-each>
      </xsl:element>
    </xsl:if>
  </xsl:template>

  <!-- Framed package -->

  <xsl:template match="framed">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <div class="framed">
        <xsl:apply-templates />
      </div>
    </xsl:if>
  </xsl:template>

  <!-- Inlines -->

  <xsl:template match="headings" />

  <xsl:template match="cit">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:text>[</xsl:text>
        <xsl:apply-templates />
      <xsl:text>] </xsl:text>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ref">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:variable name="target">
        <xsl:value-of select="@target" />
      </xsl:variable>
      <xsl:for-each select="//*[@id = $target]">
        <cut:link href="{$target}">
          <xsl:value-of select="@key" />      <!-- citation   -->
          <xsl:value-of select="@id-text" />  <!-- all others -->
        </cut:link>
      </xsl:for-each>
    </xsl:if>
  </xsl:template>

  <xsl:template match="xref">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:element name="a">
        <xsl:attribute name="href">
          <xsl:choose>
            <xsl:when test="contains(@url, '.pdf')">
              <xsl:value-of select="concat(substring-before(@url, '.pdf'), '.html')" />
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="@url" />
            </xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
        <xsl:apply-templates />
      </xsl:element>
    </xsl:if>
  </xsl:template>

  <xsl:template match="note">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <sup>
        <xsl:text>[</xsl:text>
        <xsl:element name="cut:link">
          <xsl:attribute name="href">
            <xsl:value-of select="@id" />
          </xsl:attribute>
          <xsl:value-of select="@id-text" />
        </xsl:element>
        <xsl:text>]</xsl:text>
      </sup>
    </xsl:if>
  </xsl:template>

  <xsl:template match="fbox">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <em class="framed">
        <xsl:apply-templates select="minipage/p/*" />
      </em>
    </xsl:if>
  </xsl:template>

  <xsl:template match="hi">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:choose>
        <xsl:when test=". != ''">
          <xsl:choose>
            <xsl:when test="@rend = 'bold'">
              <b><xsl:apply-templates /></b>
            </xsl:when>
            <xsl:when test="@rend = 'it'">
              <i><xsl:apply-templates /></i>
            </xsl:when>
            <xsl:when test="@rend = 'underline'">
              <!-- <u> is deprecated -->
              <em class="under"><xsl:apply-templates /></em>
            </xsl:when>
            <xsl:when test="@rend = 'tt'">
              <tt><xsl:apply-templates /></tt>
            </xsl:when>
            <xsl:when test="@rend = 'large'">
              <big><xsl:apply-templates /></big>
            </xsl:when>
            <xsl:when test="@rend = 'small'">
              <small><xsl:apply-templates /></small>
            </xsl:when>
            <xsl:when test="@color = 'colid5'">
              <!-- <font color="..."> is deprecated -->
              <em class="blue"><xsl:apply-templates /></em>
            </xsl:when>
            <xsl:otherwise>
              <xsl:apply-templates />
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:template>

  <xsl:template match="text()">
    <xsl:param name="toc">no</xsl:param>
    <xsl:if test="$toc = 'no'">
      <xsl:value-of select="." />
    </xsl:if>
  </xsl:template>

  <!-- Default -->

  <xsl:template match="*">
    <xsl:param name="toc">no</xsl:param>
    <xsl:apply-templates>
      <xsl:with-param name="toc" select="$toc" />
    </xsl:apply-templates>
  </xsl:template>

  <!-- Routine templates -->

  <xsl:template name="generate-id">
    <!-- ensure an id value is generated -->
    <xsl:choose>
      <xsl:when test="@id">
        <xsl:value-of select="@id" />
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>_</xsl:text>
        <xsl:value-of select="generate-id(.)" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="optional-id">
    <!-- generate an id attribute only if needed -->
    <xsl:if test="@id">
      <xsl:attribute name="id">
        <xsl:value-of select="@id" />
      </xsl:attribute>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
