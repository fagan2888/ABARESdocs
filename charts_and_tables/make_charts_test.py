"""
Test of ABARES chart_builder script
"""

#%load_ext autoreload
#%autoreload 2
#%cd "J:\ProductivityAndWaterAndSocial\Water\_Resources\ABARESdocs\\charts_and_tables"

import pandas as pd
import chart_builder
import numpy as np
import os

# =============================
#
# Create chart builder instance
#
# =============================

home = os.getcwd() 
dataout = home + "\\output\\"
datain = home + "\\input\\"
home_1 = os.path.dirname(home)
images = home_1 + "\\report\\figures\\"

cb = chart_builder.ChartBuilder(dataout, images)

# =============================
#
# Read in some data
#
# =============================

data = pd.read_csv(datain + "raw_crop_data.csv")
data = data.set_index(['YEAR', 'SEASON', 'UNIT'])

table1 = data.xs(('winter', 'production'), level=('SEASON', 'UNIT'))
table1 = table1.drop(['TAS', 'AUS'], 1)

temp1 = data['AUS'].xs(('winter', 'area'), level=('SEASON', 'UNIT'))
temp1.name= 'Area'
temp2 = data['AUS'].xs(('winter', 'production'), level=('SEASON', 'UNIT'))
temp2.name='Production'
table2 = pd.concat([temp1, temp2], axis=1)

table3 = data.xs(('winter', 'area'), level=('SEASON', 'UNIT'))
table3 = table3.drop(['TAS', 'AUS'], 1)

# =============================
#
# Chart type 1: Line chart
#
# =============================

chartdata = table1.copy()
chartdata.to_csv(dataout + "line_chart.csv")

fig = cb.make_chart(chartdata, kind='line',  legend=True, date=True, unit_label = 'kt')
cb.save_chart(fig, "line_chart")

# =============================
#
# Chart type 2: Area chart
#
# =============================

chartdata = table1.copy()
chartdata.to_csv(dataout + "area_chart.csv")

fig = cb.make_chart(chartdata, kind='area',  legend=True, date=True, unit_label = 'kt')
cb.save_chart(fig, "area_chart")

# =============================
#
# Chart type 3a: Bar chart (time series)
#
# =============================

chartdata = table1.copy()
chartdata = chartdata.drop(['QLD', 'SA', 'WA'], 1)
chartdata.to_csv(dataout + "bar_chart.csv")

fig = cb.make_chart(chartdata, kind='bar',  legend=True, date=True, unit_label = 'kt', date_n=2)
cb.save_chart(fig, "bar_chart")

# =============================
#
# Chart type 3b: Bar chart (cross section)
#
# =============================

chartdata = table1.copy()
chartdata = chartdata.transpose()
chartdata = chartdata[[2013, 2014, 2015]]
chartdata.to_csv(dataout + "bar_chart_g.csv")

fig = cb.make_chart(chartdata, kind='bar',  legend=True, date=False, unit_label = 'kt' )
cb.save_chart(fig, "bar_chart_g")

# =============================
#
# Chart type 4: Horizontal bar chart
#
# =============================

chartdata = table1.copy()
chartdata = chartdata.transpose()
chartdata = chartdata[[2013, 2014, 2015]]
chartdata.to_csv(dataout + "bar_chart_h.csv")

fig = cb.make_chart(chartdata, kind='barh',  legend=True, date=False, unit_label = 'kt' )
cb.save_chart(fig, "bar_chart_h")

# =============================
#
# Chart type 5: Stacked bar chart
#
# =============================

chartdata = table1.copy()
chartdata = chartdata.transpose()
chartdata = chartdata[[2013, 2014, 2015]]
chartdata = chartdata.transpose()
chartdata.to_csv(dataout + "bar_chart_s.csv")

fig = cb.make_chart(chartdata, kind='bar',  legend=True, date=False, unit_label = 'kt' , stacked=True)
cb.save_chart(fig, "bar_chart_s")


# =============================
#
# Chart type 6a: Scatter chart 
#
# =============================

chartdata = table2.copy()
chartdata.to_csv(dataout + "scatter_chart.csv")

fig = cb.make_chart(chartdata, kind='scatter', msize=10, unit_label='kt', xunit_label='000 Ha')
cb.save_chart(fig, "scatter_chart")


# =============================
#
# Chart type 6b: Scatter chart (multiple series with labels)  - LABELS NOT WORKING CURRENTLY
#
# =============================

chartdata = table2.copy()
chartdata.to_csv(dataout + "scatter_chart_b.csv")
offset = chartdata.copy()

fig = cb.make_chart(chartdata, kind='multiscatter', msize=10, legend=True, unit_label='kt', xunit_label='000 Ha', scatlabel=['2004-05 to 2010-11','2011-12 to 2014-15'], scatindex = [np.arange(0,6), np.arange(6,10)], label=True, offset=offset, ylim=(15000,50000), date=True)
cb.save_chart(fig, "scatter_chart_b")

# ==============================
#
# Chart type 7a: Combo chart - Secondary axis
#
# ==============================

chartdata = table2.copy()
chartdata.to_csv(dataout + "combo_chart_a.csv")

fig = cb.make_combo_chart(chartdata, kind='line', date=True, unit_label='000 Ha', unit_label2='kt', primary=['Area'], secondary=['Production'], date_n=3)
cb.save_chart(fig, "combo_chart_a")

# ==============================
#
# Chart type 7b: Combo chart - Bar and line
#
# ==============================

chartdata = table2.copy()
chartdata.to_csv(dataout + "combo_chart_b.csv")

fig = cb.make_combo_chart(chartdata, kind='bar', date=True, unit_label='000 Ha', unit_label2='kt', primary=['Area'], secondary=['Production'], date_n=1, ylim=(20000, 23000))
cb.save_chart(fig, "combo_chart_b", scale=False)

# ==============================
#
# Chart type 7c: Combo chart - Area and line 
#
# ==============================

chartdata = table2.copy()
chartdata.to_csv(dataout + "combo_chart_c.csv")

fig = cb.make_combo_chart(chartdata, kind='area', date=True, unit_label='000 Ha', unit_label2='kt', primary=['Area'], secondary=['Production'], date_n=1, ylim=(20000, 23000), secondary_y=True)
cb.save_chart(fig, "combo_chart_c", scale=False)

# =============================
#
# Chart type 8a: Panel chart (single series per panel) - line
#
# =============================

chartdata = table1.copy()
chartdata = chartdata / 1000
chartdata.to_csv(dataout + "panel_chart.csv")
chartdata = chartdata.drop(['WA'] ,1)

fig = cb.make_chart(chartdata, kind='line',  legend=False, date=True, unit_label = 'Mt', multi=True, layout=(2,2), figsize = (5, 5))
cb.save_chart(fig, "panel_chart", scale=False)

# =============================
#
# Chart type 8b: Panel chart (single series per panel) - bar
#
# =============================

chartdata = table1.copy()
chartdata = chartdata / 1000
chartdata.to_csv(dataout + "panel_chart_b.csv")
chartdata = chartdata.drop(['WA'] ,1)

fig = cb.make_chart(chartdata, kind='bar',  legend=False, date=True, unit_label = 'Mt', multi=True, layout=(2,2), figsize = (5, 5), colors=cb.abares_colors[0], date_n=2)
cb.save_chart(fig, "panel_chart_b", scale=False)

# =============================
#
# Chart type 9a Multi-series panel chart (two lines per panel)
#
# =============================

temp = table3.copy()
temp.columns = [s + "_AREA" for s in temp.columns]
prim = list(table1.columns[0:4])
sec = list(temp.columns[0:4])
chartdata = pd.concat([table1.copy(), temp ], axis=1)
chartdata = chartdata.drop(['WA', 'WA_AREA'] ,1)
chartdata.to_csv(dataout + "multi_panel_chart_a.csv")
temp = chartdata.copy()

fig = cb.make_combo_chart(chartdata, kind='line',  legend=False, date=True, unit_label = 'Kt', unit_label2 = '000 HA', primary = prim, secondary = sec, multi=True, layout=(2,2), secondary_y=True, figsize = (7, 5), colors=[cb.abares_colors[0], cb.abares_colors[1]], leglabel=['Production', 'Area'], hspace=0.2, wspace=0.4, ytickformat=',g', ytickformat2=',.0f')
cb.save_chart(fig, "multi_panel_chart_a", scale=False)

# =============================
#
# Chart type 9b Multi-series panel chart (two lines per panel)
#
# =============================

chartdata = temp
chartdata.to_csv(dataout + "multi_panel_chart_b.csv")

fig = cb.make_combo_chart(chartdata, kind='bar',  legend=False, date=True, unit_label = 'Kt', unit_label2 = '000 HA', primary = prim, secondary = sec, multi=True, layout=(2,2), secondary_y=True, figsize = (7, 5), colors=[cb.abares_colors[0], cb.abares_colors[1]], leglabel=['Production', 'Area'], hspace=0.2, wspace=0.4, ytickformat=',g', ytickformat2=',.0f')
cb.save_chart(fig, "multi_panel_chart_b", scale=False)


# =============================
#
# Make excel file
#
# =============================

cb.make_excel('chart_table_index.csv', 'Report_chart_table_data.xlsx', 'ABARESdocs test report')
