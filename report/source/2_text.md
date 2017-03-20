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
