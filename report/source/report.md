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
    - Winter crop production in Victoria in 2014-15 was **win_prod_vic** kilotonnes.
    - Summer crop area planted in Queensland in 2015-16 was **sum_crop_area** '000 Ha. 
    
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

\clearpage

Here is an area chart (@fig:area_chart) 

![Area chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/area_chart){#fig:area_chart}

\clearpage

Here is a bar chart (@fig:bar_chart) 

![Bar chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/bar_chart){#fig:bar_chart}

\clearpage

Here is a horizontal bar chart (@fig:bar_chart_h) 

![Horizontal Bar chart showing winter crop production in Australia, 2012-13 to 2014-15](figures/bar_chart_h){#fig:bar_chart_h}

\clearpage

Here is a stacked bar chart (@fig:bar_chart_s) 

![Stacked bar chart showing winter crop production in Australia, 2012-13 to 2014-15](figures/bar_chart_s){#fig:bar_chart_s}

\clearpage

Here is a scatter chart (@fig:scatter_chart) 

![Scatter chart showing winter crop production in Australia against area, 2004-05 to 2014-15](figures/scatter_chart){#fig:scatter_chart}

\clearpage

Here is a multi-scatter chart (@fig:scatter_chart_b) 

![Multi-scatter chart showing winter crop production in Australia against area, 2004-05 to 2014-15](figures/scatter_chart_b){#fig:scatter_chart_b}

\clearpage

## Combo charts

Here is a line chart with secondary y-axis (@fig:combo_chart_a) 

![Line chart with secondary y-axis showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_a){#fig:combo_chart_a}

\clearpage

Here is a bar and line chart with secondary y-axis (@fig:combo_chart_b) 

![Bar and line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_b){#fig:combo_chart_b}

\clearpage

Here is an area and line chart with secondary y-axis (@fig:combo_chart_c) 

![Area and line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/combo_chart_c){#fig:combo_chart_c}

\clearpage

## Panel charts

Here is a panel line chart (@fig:panel_chart) 

![Panel chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/panel_chart){#fig:panel_chart}

\clearpage

Here is a panel bar chart (@fig:panel_chart_b) 

![Panel bar chart showing winter crop production in Australia, 2004-05 to 2014-15](figures/panel_chart_b){#fig:panel_chart_b}

\clearpage

Here is a multi-panel chart (@fig:multi_panel_chart_a) 

![Multi panel chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/multi_panel_chart_a){#fig:multi_panel_chart_a}

\clearpage

Here is a multi-panel bar / line chart (@fig:multi_panel_chart_b) 

![Multi panel bar/line chart showing winter crop production and area in Australia, 2004-05 to 2014-15](figures/multi_panel_chart_b){#fig:multi_panel_chart_b}

\clearpage

# Tables {#tables}

ABARESdocs allows report tables to be linked to csv files. Here are some examples (@tbl:prod_table, @tbl:area_table).

~winter_crop_prod_aus~

Table: winter crop production in Australia, 2004-05 to 2014-15 {#tbl:prod_table}

~winter_crop_area_aus~

Table: winter crop area in Australia, 2004-05 to 2014-15 {#tbl:area_table}

You can also insert static tables directly with markdown syntax.


|                             | TFP          |  W_YIELD     |
|-----------------------------|--------------|--------------|
| Number of samples per split | 50           | 5            |
| Number of trees             | 1175         | 1475         |
| Learning rate               | 0.045        | 0.032        |

Table: Final meta-parameter values {#tbl:meta}

# Appendix A: Tips and tricks {#tips} 

\clearpage

# References {-}
