---
logo: figures/ABARES2.png
biosphere: figures/BIOSPHERE.png
title: 'ABARESdocs test report'
subtitle: 'An open source document production system'
author:
- Neal Hughes
refauthors: 'Hughes, N.'
reporttype: 'User guide'
date: '2 December 2016'
year: 2016
month: 'December'
thanks: 'This software system uses the open source document conversion system Pandoc, as well as the Python libraries pandas, matplotlib and tabulate. The chart_builder script has been developed jointly with Orion Sanders and Mihir Gupta. '
issn: 666666
isbn: 666666
projectno: 666666
bibliography: References.bib  
csl: style-manual-australian-government.csl
figPrefix: 'Figure'
tblPrefix: 'Table'
eqPrefix: 'Equation'
---

# Introduction {#intro}

This document serves as both a user guide and demonstration of 'ABARESdocs' or at least it will if I ever get around to finishing it.

# Text {#text}

## Dot points

-  Dot points look like this
    -  and also like this
    -  and this

## Linked statistics

- ABARESdocs allows the author insert in-text references to statistics, linked to an underlying data file. Here are some examples:
    - Winter crop production in Victoria in 2014-15 was 5,531.7 kilotonnes.
    - Summer crop area planted in Queensland in 2015-16 was 1,417.0 '000 Ha. 
    
## References

ABARESdocs (via Pandoc) supports citations / referencing linked to Endnote or Bibtex libraries. Here is an example:

Climatic conditions are the single most important factor affecting the productivity of Australian cropping farms [@Kokic2006; @Hughes2011]. Australia's climate is highly variable, with lower mean rainfall and higher rainfall variability than other comparable regions [@Peel2004]. As a result, Australian agriculture is subject to more revenue volatility than almost any other country in the world [@Keogh2012].

A bibliography is then automatically inserted at the end of the document.

## External links

ABARESdocs allows for external references. Check out this cool football team, the [Geelong Cats](http://www.geelongcats.com.au).

## Internal links

ABARESdocs also supports internal document links. For example, the [Charts](#charts) section below shows how insert charts with ABARESdocs. 

## Math

ABARESdocs (via Pandocs) supports mathematical notation using Latex syntax:

To control for the effect of climate on productivity we estimate a regression of the form:

$$ Y_{it} = g(Z_{it}, X_{it}, t) $$

where $Y_{it}$ is the farm performance measure (i.e., *TFP* or *W_YIELD*) for farm $i$ in period $t$, $Z_{it}$  is a vector of farm specific climate variables, $X_{it}$ a vector of farm characteristics and $g$ is an unknown function. Here  $Z_{it}$ is a subset of the 60 climate variables defined in section 3 and $X_{it}$ includes *LAT*, *LONG*, *AREA*, *LIVESTOCK*, *AGE*, *IRRIG2*, *FLOOD20*, *FLOOD5* and *FLOOD1_5* (and *W_AREA* in the wheat yield model).

Equation numbering is also supported, check out @eq:model:

$$ Y_{it} = g(Z_{it}, X_{it}, t) $$ {#eq:model}

# Charts {#charts}

ABARESdocs uses some Python scripts to generate nicely formated chart images. For more information on how this works see the charts folder.

Once chart image files and table text files have been generated they can be inserted as below. Pandoc supports numbering and cross-referencing of tables and charts. 

## Simple charts

Here is a line chart (@fig:line_chart) 

![Line chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/line_chart){#fig:line_chart}

Here is an area chart (@fig:area_chart) 

![Area chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/area_chart){#fig:area_chart}

Here is a bar chart (@fig:bar_chart) 

![Bar chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/bar_chart){#fig:bar_chart}

Here is a horizontal bar chart (@fig:bar_chart_h) 

![Horizontal Bar chart showing winter crop production in Australia, 2012-13 to 2014-15](figures/bar_chart_h){#fig:bar_chart_h}

Here is a stacked bar chart (@fig:bar_chart_s) 

![Stacked bar chart showing winter crop production in Australia, 2012-13 to 2014-15](figures/bar_chart_s){#fig:bar_chart_s}

Here is a scatter chart (@fig:scatter_chart) 

![Scatter chart showing winter crop production in Australia against area, 2004-05 to 2014-15](figures/scatter_chart){#fig:scatter_chart}

Here is a multi-scatter chart (@fig:scatter_chart_b) 

![Multi-scatter chart showing winter crop production in Australia against area, 2004-05 to 2014-15](figures/scatter_chart_b){#fig:scatter_chart_b}

## Combo charts

Here is a line chart with secondary y-axis (@fig:combo_chart_a) 

![Line chart with secondary y-axis showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_a){#fig:combo_chart_a}

Here is a bar and line chart with secondary y-axis (@fig:combo_chart_b) 

![Bar and line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_b){#fig:combo_chart_b}

Here is an area and line chart with secondary y-axis (@fig:combo_chart_c) 

![Area and line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_c){#fig:combo_chart_c}

## Panel charts

Here is a panel line chart (@fig:panel_chart) 

![Panel chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/panel_chart){#fig:panel_chart}

Here is a panel bar chart (@fig:panel_chart_b) 

![Panel bar chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/panel_chart_b){#fig:panel_chart_b}

Here is a multi-panel chart (@fig:multi_panel_chart_a) 

![Multi panel chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/multi_panel_chart_a){#fig:multi_panel_chart_a}

Here is a multi-panel bar / line chart (@fig:multi_panel_chart_b) 

![Multi panel bar/line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/multi_panel_chart_b){#fig:multi_panel_chart_b}

# Tables {#tables}

ABARESdocs allows report tables to be linked to csv files. Here are some examples (@tbl:prod_table, @tbl:area_table).

------------------------------------------------------
              NSW      VIC      QLD       SA        WA
-------  --------  -------  -------  -------  --------
2005     10,712.2  4,214.4  1,391.2  5,297.5  12,977.8

2006     11,981.3  6,266.8  1,433.4  7,517.9  13,944.6

2007      3,794.1  1,747.9    924.2  2,793.1   8,278.1

2008      3,999.2  4,691.7  1,194.1  4,705.7  10,760.5

2009      9,438.4  3,887.4  2,325.6  4,863.4  13,784.6

2010      7,787.0  5,889.1  1,616.9  7,035.5  12,943.0

2011     14,783.6  7,625.2  1,820.6  9,316.1   8,044.1

2012     11,952.1  7,352.0  2,328.7  7,371.5  16,600.0

2013     11,123.4  6,885.6  2,156.0  6,469.7  11,243.1

2014      9,773.0  6,774.6  1,516.2  7,221.3  16,509.8

2015      9,230.0  5,531.7  1,417.0  7,574.4  14,550.7

------------------------------------------------------

Table: winter crop production in Australia, 2004-05 to 2014-15 {#tbl:prod_table}

----------------------------------------------------
             NSW      VIC      QLD       SA       WA
-------  -------  -------  -------  -------  -------
2005     6,438.8  3,191.5    856.9  3,964.5  7,932.2

2006     5,592.9  2,969.2    965.6  3,868.2  7,406.7

2007     5,671.1  3,081.9    808.1  4,140.7  6,477.2

2008     6,312.0  3,375.0    872.6  4,130.8  7,264.6

2009     6,295.0  3,491.6  1,208.5  3,978.7  7,899.3

2010     6,106.0  3,488.4  1,173.0  3,782.9  8,270.6

2011     6,157.6  3,456.8  1,216.7  3,821.1  7,715.1

2012     5,969.1  3,410.5  1,205.0  3,837.8  8,252.2

2013     5,852.2  3,457.0  1,222.3  3,776.3  8,097.2

2014     5,313.9  3,284.1  1,105.3  3,448.3  8,248.9

2015     5,840.5  3,384.9  1,129.5  3,986.0  8,271.5

----------------------------------------------------

Table: winter crop area in Australia, 2004-05 to 2014-15 {#tbl:area_table}

You can also insert static tables directly with markdown syntax.


|                             | TFP          |  W_YIELD     |
|-----------------------------|--------------|--------------|
| Number of samples per split | 50           | 5            |
| Number of trees             | 1175         | 1475         |
| Learning rate               | 0.045        | 0.032        |

Table: Final meta-parameter values {#tbl:meta}

# Appendix A: Tips and tricks {#tips} 

# References {-}
