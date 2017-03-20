"""
Test of ABARES report_builder script
"""

#%load_ext autoreload
#%autoreload 2
#%cd "J:\ProductivityAndWaterAndSocial\Water\_Resources\ABARESdocs\\charts_and_tables"

import pandas as pd
import report_builder
import numpy as np
import os

home = os.getcwd() 
tablesf = home + "\\output\\"
home_1 = os.path.dirname(home)
reportf = home_1 + "\\report\\"
datain = home + "\\input\\"

# =============================
#
# Create report builder instance for any chapter that has linked data
#
# =============================

rb2 = report_builder.ReportBuilder(tablesf, reportf, "2_text")
rb4 = report_builder.ReportBuilder(tablesf, reportf, "4_tables")

# =============================
#
# Read in some data
#
# =============================

data = pd.read_csv(datain + "raw_crop_data.csv")
data = data.set_index(['YEAR', 'SEASON', 'UNIT'])


# =============================
#
# Create some tables and stats
#
# =============================

table1 = data.xs(('winter', 'production'), level=('SEASON', 'UNIT'))
table1 = table1.drop(['TAS', 'AUS'], 1)
table1.to_csv(tablesf + 'winter_crop_prod_aus.csv')


table3 = data.xs(('winter', 'area'), level=('SEASON', 'UNIT'))
table3 = table3.drop(['TAS', 'AUS'], 1)
table3.to_csv(tablesf + 'winter_crop_area_aus.csv')

stats = {}

stats['win_prod_vic'] = format(table1.ix[2015]['VIC'], ',.1f')
stats['sum_crop_area'] = format(table1.ix[2015]['QLD'], ',.1f') 

# =============================
#
# Write tables and stats to chapters
#
# =============================

rb2.insert_tables_stats(['winter_crop_prod_aus', 'winter_crop_area_aus'], [',.1f', ',.1f'], stats)
rb4.insert_tables_stats(['winter_crop_prod_aus', 'winter_crop_area_aus'], [',.1f', ',.1f'], stats)

# =============================
#
# Create chart and table index file 
#
# =============================

rb2.make_chart_index('chart_table_index.csv', ['2_text.md', '3_charts.md', '4_tables.md'])

