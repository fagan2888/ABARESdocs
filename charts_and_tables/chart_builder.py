#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#from matplotlib import dates as dt 
#import plotly
#import plotly.graph_objs as go
import matplotlib as mpl
import shutil
import os

#plotly.plotly.sign_in("nealbob", "zlb6t6yxll")
#layout = go.Layout(autosize=False, width=1000, height=500, margin=go.Margin(l=70, r=50, b=50, t=50, pad=5), font=dict(size=14))

def get_col_widths(dataframe):
    # First we find the maximum length of the index column   
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

def label_point(a, ax, c):
   
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], point['val'],  fontproperties= mpl.font_manager.FontProperties(size=7.5), color='gray')
      
        
class ChartBuilder:
    
    def __init__(self, infolder, outfolder):
        
        self.infolder = infolder
        self.outfolder = outfolder

        home = os.getcwd() 
        plt.style.use(home + "\\abares.mplstyle")
        self.abares_colors = ['#ff7900', '#96172e', '#00505c', '#d5d2ca', '#80ded6', '#eed6a5', '#512B1B', '#F2AF00', '#DE3831']
        self.counter = 0
        
        mpl.rcParams['axes.color_cycle'] = self.abares_colors   

    def build_contents(self):
    
        self.excelfile.book.add_worksheet('Contents')
        contents = self.excelfile.book.worksheets_objs[0]
        contents.write(1, 0, "                 " + self.title)
        contents.insert_image(0, 0, self.outfolder + "DAWR_ABARES.jpg", {'url' : 'internal:Contents!A1'})

        xlformat = self.excelfile.book.add_format()
        xlformat.set_bg_color('white')
        xlformat2 = self.excelfile.book.add_format()
        xlformat2.set_bg_color('white')
        xlformat2.set_bottom()
        xlformat2.set_bold()
        xlformat2.set_font_size(15)
        xlformat3 = self.excelfile.book.add_format()
        xlformat3.set_bg_color('white')
        xlformat3.set_bold()
        xlformat3.set_font_size(15)
        xlformat4 = self.excelfile.book.add_format()
        xlformat4.set_bg_color('white')
        xlformat4.set_font_size(13)
        xlformat4.set_bold()
        xlformat5 = self.excelfile.book.add_format({
            'font_color': 'blue',
            'underline':  1,
            'bg_color': 'white'
            })
        xlformat6 = self.excelfile.book.add_format()
        xlformat6.set_bg_color('white')
        xlformat6.set_font_size(13)
        
        formats = [xlformat, xlformat2, xlformat3, xlformat4, xlformat5, xlformat6]
        
        contents.set_row(0, 70, xlformat)   
        contents.set_row(1,18, xlformat2)
        contents.set_column('A:AD', 8.43, xlformat)
        contents.insert_image(2, 0, self.outfolder + "BIOSPHERE.png", {'url' : 'http://www.agriculture.gov.au/abares', 'x_scale' : 0.5, 'y_scale' : 0.5, 'y_offset' : 2, 'x_offset' : 15})
        contents.write(22, 0, 'For more information download the report at:')
        contents.write_url(23, 0, 'http://www.agriculture.gov.au/abares/publications', string='agriculture.gov.au/abares/publications')
        contents.write(25, 0, 'Australian Bureau of Agricultural and Resource Economics and Sciences')
        contents.write(26, 0, 'Postal address GPO Box 858 Canberra ACT 2601')
        contents.write(27, 0, 'Switchboard +61 2 6272 3933')
        contents.write_url(28, 0, 'mailto:info.abares@agriculture.gov.au', string='info.abares@agriculture.gov.au')
        contents.write_url(29, 0, 'http://www.agriculture.gov.au/abares', string='agriculture.gov.au/abares' )
        contents.write(4, 7, 'Contents', xlformat3)
    
        return [contents, formats]

    def start_section(self, section_name):
        
        self.contents.write(self.counter + 6, 9, section_name, self.formats[3])
        self.counter +=2
        
    def start_subsection(self, section_name):
        
        self.contents.write(self.counter + 5, 9, section_name, self.formats[5])
        self.counter +=1
        
    
    def save_excel(self):
    
        self.contents.set_column('I:J', 5, self.formats[0])
        self.contents.set_column('K:K', 150, self.formats[0])
        self.excelfile.save()

    def chart_to_excel(self, data, idx, imagelink=False):
    
        fname = self.meta.iloc[idx]['name']
        figurenum = int(self.meta.iloc[idx]['number'])
        sname = 'Figure ' + str(figurenum)
        
        data.to_excel(self.excelfile, sheet_name=sname, startrow=5) 
        sheet = self.excelfile.sheets[sname]
    
        col = data.shape[1]
        row = data.shape[0]
        sheet.insert_image(5, col+2, self.outfolder + fname + ".png", {'x_scale' : 0.85, 'y_scale' : 0.85})    

        for i, width in enumerate(get_col_widths(data)):
            sheet.set_column(i, i, width*1.05)
        
        sheet.write(row + 8, 0, 'Source: ' + str(self.meta.iloc[idx]['source']))
        figure_caption = 'Figure ' + str(figurenum) + ": " + self.meta.iloc[idx]['caption']        
        sheet.write(3, 0, figure_caption)
        print(figure_caption)
        
        #sheet.write_url(row + 10, 0, '.\images\\' + fname + '.pdf', string='Vector image (pdf file)', cell_format=self.formats[4])
        #sheet.write_url(row + 11, 0, '.\images\\' + fname+ '.png', string='Hi-res image (png file)', cell_format=self.formats[4])
        #sheet.write_url(row + 12, 0, '.\images\\' + fname+ '.jpg', string='Low-res image (jpg file)', cell_format=self.formats[4])
    
        sheet.write(1, 0, "                 " + self.title)
        sheet.insert_image(0, 0, self.outfolder + "DAWR_ABARES.jpg", {'url' : 'internal:Contents!A1'})
        sheet.set_row(0, 70, self.formats[0])
        sheet.set_row(1,18, self.formats[1])
    
        #contents =  self.excelfile.book.worksheets_objs[0]
        self.contents.write_url(5 + self.counter,10, 'internal:\'' + sname +'\'!A1', string = 'Figure ' + str(figurenum) + ": " + self.meta.iloc[idx]['caption'], cell_format=self.formats[4])
        
        shutil.copy(self.outfolder + fname + ".pdf", self.outfolder + '\\final\\' + 'Figure ' + str(figurenum) + ".pdf")
        
    def table_to_excel(self, data, idx):
    
        fname = self.meta.iloc[idx]['name']
        figurenum = int(self.meta.iloc[idx]['number'])
        sname = 'Table ' + str(figurenum)
        
        data.to_excel(self.excelfile, sheet_name=sname, startrow=5) 
        sheet = self.excelfile.sheets[sname]
    
        col = data.shape[1]
        row = data.shape[0]

        for i, width in enumerate(get_col_widths(data)):
            sheet.set_column(i, i, width*1.05)
        
        sheet.write(row + 8, 0, 'Source: ' + str(self.meta.iloc[idx]['source']))
        figure_caption = 'Table ' + str(figurenum) + ": " + self.meta.iloc[idx]['caption']        
        sheet.write(3, 0, figure_caption)
        print(figure_caption)
        
        sheet.write(1, 0, "                 " + self.title)
        sheet.insert_image(0, 0, self.outfolder + "DAWR_ABARES.jpg", {'url' : 'internal:Contents!A1'})
        sheet.set_row(0, 70, self.formats[0])
        sheet.set_row(1,18, self.formats[1])
    
        self.contents.write_url(5 + self.counter,10, 'internal:\'' + sname +'\'!A1', string = 'Table ' + str(figurenum) + ": " + self.meta.iloc[idx]['caption'], cell_format=self.formats[4])
        
    
    def make_excel(self, metafile, excelfile, title, imagelink=False):
      
        self.title = title
        self.meta = pd.read_csv(metafile)
        self.excelfile = pd.ExcelWriter(excelfile, engine='xlsxwriter', datetime_format='dd/mm/yyyy')
        self.contents, self.formats = self.build_contents()

        old_section_name = 'none'

        for i in range(self.meta.shape[0]):
            chart = self.meta.iloc[i]
            fname = chart['name']
            
            if chart.chapter != old_section_name:
                self.start_section(chart.chapter)
                old_section_name = chart.chapter
                
            data = pd.read_csv(self.infolder + fname + '.csv', index_col=0, encoding = 'cp1252')
            if chart['type'] == 'chart':     
                self.chart_to_excel(data, i, imagelink=imagelink)
            else:
                self.table_to_excel(data, i)

            self.counter +=1
        
        self.counter = 0
        
        self.save_excel()

    def make_forpubs(self, forpubsf):

        
        for i in range(self.meta.shape[0]):
            chart = self.meta.iloc[i]
            fname = chart['name']
            number = chart['number']
            
            outf = forpubsf + 'Figure ' + str(number) + '.pdf'
            inf = self.outfolder + fname + '.pdf'     
            print(outf)
            print(inf)
            shutil.copy2(inf, outf)
        
    
    def read_csv(self, idx):
        
        chart = self.meta.iloc[idx]
        fname = chart['name']
                
        data = pd.read_csv(self.infolder + fname + '.csv', index_col=0, encoding = 'cp1252')
        
        return data

    def save_chart(self, fig, fname, scale=True, size=(6.1, 3.1), figsize=(4.3, 2.8)):
        
        if scale:
            fig.set_size_inches(size[0], size[1], forward=True)
            scalex = figsize[0] / size[0]
            scaley = (figsize[1] + 0.3) / size[1]           
            fig.tight_layout(rect=(0,0,scalex,scaley), )        
            fig.savefig((self.outfolder + fname + ".png"), dpi=300)        
            fig.savefig((self.outfolder + fname + ".jpg"), dpi=75) 
            fig.savefig((self.outfolder + fname + ".pdf"), dpi=300)  
        else:
            fig.savefig((self.outfolder + fname + ".png"), bbox_inches='tight', dpi=300)        
            fig.savefig((self.outfolder + fname + ".jpg"), bbox_inches='tight', dpi=75) 
            fig.savefig((self.outfolder + fname + ".pdf"), bbox_inches='tight', dpi=300)  
            
    def make_chart(self, data, kind='line', unit_label='none', xunit_label='none', legend=True, no_xlabel=True, ytickformat=',g', xtickformat=',g', stacked=False, fig='none', date=False, makefig=True, xlfile = 'none', title='none', xlformats='none', multi=False, figsize=(4.3,2.8), addtoexcel=True, primary='none', colors='none', layout=(1,3), scatindex='none', scatlabel='none', label=False, combo=False, ylim=None, ylim_min=None, builddate=True, offset='none', date_n=1, linewidth=2.1, legdown=False, msize=0.35, fitline=None):
        
        if colors != 'none':
            mpl.rcParams['axes.color_cycle'] = colors

        mpl.rcParams['axes.color_cycle']
        
        if primary != 'none':        
            data = pd.DataFrame(data[primary])
                    
        if date:
            if type(data.index) == pd.core.index.Int64Index:
                data.index = np.array([str(d-1) + "–" + str(d)[-2:] for d in data.index])
            elif builddate:
                data.index = pd.to_datetime(data.index, format='%d/%m/%Y')      
            
        if kind=='multiscatter' and label:
            offset.index = data.index
            
        if makefig:
            fig, ax = self.matplotlib_chart(data, kind=kind, unit_label=unit_label, xunit_label=xunit_label, legend=legend, no_xlabel=no_xlabel, ytickformat=ytickformat, xtickformat=xtickformat, stacked=stacked, fig=fig, date=date, subplot=multi, layout=layout, scatindex=scatindex, scatlabel=scatlabel, label=label, offset=offset, ylim=ylim, ylim_min=ylim_min, date_n=date_n, colors=colors, figsize=figsize, linewidth=linewidth, legdown=legdown, msize=msize, fitline=fitline)                        
            if figsize != 'none':        
                fig.set_figheight(figsize[1])
                fig.set_figwidth(figsize[0])      
        
        if colors != 'none':
            mpl.rcParams['axes.color_cycle'] = self.abares_colors   
        
        if not(combo):
            plt.show()
        
        self.ax = ax

        return fig

    def abares_style(self, ax, data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, ylim=None, date_n=1, legdown=False):
     
        if legend:
                       
            if legdown:
                ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), borderaxespad=0., ncol=4)
            else:
                ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_color('black')
    
        if kind == 'barh':
            ax.spines['left'].set_color('black')
            ax.spines['top'].set_color('black')
            ax.xaxis.grid(True, clip_on=False)
            ax.yaxis.grid(False)
        else:
            ax.spines['left'].set_color('none')
            ax.xaxis.grid(False)
            ax.yaxis.grid(True, clip_on=False)
   
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.get_yaxis().set_tick_params(direction='out')

        if kind == 'barh':
            labels = ax.xaxis.get_majorticklocs()
            labels = [format(s, xtickformat) for s in labels]
            #labels = [s.replace(",", " ") for s in labels]
            if unit_label != 'none':
                labels[0] = unit_label
                ax.set_xticklabels(labels)
                ax.spines['top'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                #idx = ax.yaxis.get_majorticklocs().astype(int)
                #labels = data.index[idx]
                #labels = [(ytickformat % s) for s in labels]
                #ax.set_yticklabels(labels)
        else:
            if kind == 'bar':
                idx = ax.xaxis.get_majorticklocs().astype(int)
                labels  = data.index[idx]
                
                if date:
                     
                    n = date_n           
                    ticks = [i for i in range(len(data.index))]
                    ticklabels = [l.decode('utf-8') for l in data.index]
 
                    ax.xaxis.set_ticks(ticks[::n])
 
                    if not(type(data.index[0]) == str):
                        temp = pd.to_datetime(ticklabels[::n])
                        temp = [item.strftime('%b %Y') for item in temp]
                    else:
                         temp = ticklabels[::n]
                  
                    ax.xaxis.set_ticklabels(temp)
                  
            else:
                labels = ax.xaxis.get_majorticklocs()
                labels = [(format(s, xtickformat)) for s in labels]
                #labels = [s.replace(",", " ") for s in labels]
            if xunit_label != 'none':
                labels[0] = xunit_label              
            if not(date) or (kind=='scatter' or kind=='multiscatter'):
                ax.set_xticklabels(labels)
            else:                
                labels = ax.get_xticklabels()
                plt.setp(labels, rotation=90)
                
            labels = ax.yaxis.get_majorticklocs()
           
            #ylim = ax.get_ylim()
            
            ax.set_ylim(labels[0], labels[len(labels)-1])
            labels = [format(s, ytickformat) for s in labels]
            #labels = [s.replace(",", " ") for s in labels]
            if unit_label != 'none':
                labels[0] = unit_label
            ax.set_yticklabels(labels)
            
        
        

        if legend:
            
            if kind == 'area' or kind =='noline':
                if legdown:
                    for legobj in plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), borderaxespad=0., ncol=4).legendHandles:
                        legobj.set_linewidth(2.0)  
                else:               
                    for legobj in plt.legend(loc='upper left', bbox_to_anchor=(1, 1)).legendHandles:
                        legobj.set_linewidth(2.0)  
            if kind != 'scatter' :  
                plt.setp(plt.gca().get_legend().get_texts(), fontsize='8.3')
                plt.gca().get_legend().get_frame().set_alpha(0)
       
                
 
            
            
    def matplotlib_chart(self, data, kind='line', unit_label='none', xunit_label='none', legend=True, no_xlabel=True, ytickformat=',g', xtickformat=',g', stacked=False, fig='none', scatlabel='none', scatindex = 'none', date=False, axnum=0, subplot=False, layout=(1,3), label=False, offset='none', ylim=None, ylim_min=None, date_n=0, colors='none', figsize=(3,3), linewidth=2.1, legdown=False, msize=0.35, fitline=None):
                
        
        if fig == 'none':
            plt.close('all')
            fig = plt.figure()       
            ax = fig.gca() 
        else:
            ax = fig.axes[axnum]
            n = len(fig.axes)
        if subplot:
            fig.set_tight_layout(True)
    
        if (kind == 'bar'):
            ax = data.plot(kind=kind, edgecolor='none', stacked=stacked, legend=legend, subplots=subplot, layout=layout, ax=ax, ylim=ylim)
            
            #if subplot:
            #    n = ax.shape[0]                
            #    for i in range(n):
             #       for a in ax[i]:
             #           a.get_lines()[0].set_visible(False)
            #else:
                #ax.get_lines().set_visible(False)
                
        elif (kind == 'barh'):
            if (colors != 'none'):
                ax = data.plot(kind=kind, edgecolor='none', stacked=stacked, legend=legend, subplots=subplot, layout=layout, ax=ax, colors=colors, figsize=figsize)
            else:
                ax = data.plot(kind=kind, edgecolor='none', stacked=stacked, legend=legend, subplots=subplot, layout=layout, ax=ax)
            #if subplot:
                #n = ax.shape[0]                
                #for i in range(n):
                    #for a in ax[i]:
                        #a.get_lines()[0].set_visible(False)
            #else:
                #ax.get_lines().set_visible(False)
        elif kind =='scatter':
            n = 0            
            if scatlabel != 'none':
                ax = data.plot(kind=kind, x=data.columns[0], y=data.columns[1], color=self.abares_colors[n], edgecolor='none', s=msize, ax=ax, label=scatlabel)
            else:
                ax = data.plot(kind=kind, x=data.columns[0], y=data.columns[1], color=self.abares_colors[n], edgecolor='none', s=msize, ax=ax)
        elif kind =='multiscatter':
            for i in range(len(scatindex)):
                d = data.iloc[scatindex[i]]
                if ylim != None:
                    ax = d.plot(kind='scatter', x=d.columns[0], y=d.columns[1], color=self.abares_colors[i], edgecolor='none', s=msize, ax=ax, label=scatlabel[i], ylim=ylim)        
                else:
                    ax = d.plot(kind='scatter', x=d.columns[0], y=d.columns[1], color=self.abares_colors[i], edgecolor='none', s=msize, ax=ax, label=scatlabel[i], xlim=(0,8000), ylim=(0,1000))        
        elif kind == 'area':
            ax = data.plot(kind=kind, ax = ax, legend=legend, subplots=subplot, layout=layout, linewidth=0)
        elif subplot:
            ax = data.plot(kind=kind, ax = ax, legend=legend, subplots=subplot, layout=layout, color = self.abares_colors[0])    
            
            fig = ax[0][0].get_figure()
            axes = fig.get_axes()     
            m = len(axes)
            for i in range(m):
                axes[i].set_title(data.columns[i])
        elif kind == 'noline':
            ms = 'o'
            lw = 0
            for i in range(len(scatindex)):
                d = data.iloc[scatindex[i]]
                
                d.columns = [scatlabel[i]]
                c = colors[i]
                if fitline[i]:
                    lw = 1.75
                    ms = None
                    
                ax = d.plot(kind='line', ax = ax, legend=legend, subplots=subplot, layout=layout, linewidth=lw, marker=ms, markersize=msize, color=c, fillstyle='full', markeredgecolor=c, markeredgewidth=0.0)
                
        else:
            ax = data.plot(kind=kind, ax = ax, legend=legend, subplots=subplot, layout=layout, linewidth=linewidth)
        
        if (kind !='scatter') and (kind != 'multiscatter'):
            if kind=='barh':
                plt.ylabel('')
            else:
                plt.xlabel('')
        
        if ylim != None:            
            plt.ylim(ylim)
        elif ylim_min != None:
            plt.ylim(ymin=ylim_min)

        if subplot:
            if len(ax.shape) == 1:
                for a in ax:
                    self.abares_style(a, data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, date_n=date_n)
                    if ylim!= None:
                        a.set_ylim(ylim)
                    elif ylim_min != None:
                        plt.ylim(ymin=ylim_min)
            else:
                n = ax.shape[0]
                for i in range(n):
                    for a in ax[i]:
                        self.abares_style(a, data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, date_n=date_n)
                        if ylim!= None:
                            a.set_ylim(ylim)
                        elif ylim_min != None:
                            plt.ylim(ymin=ylim_min)
            
                    
        else:
            
            self.abares_style(ax, data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, date_n=date_n, legdown=legdown)
            
            if label:
                temp = data + offset            
                temp['val'] = [s.decode('utf-8') for s in data.index]
                temp.columns = ['x', 'y', 'val']
                label_point(temp, ax, self.abares_colors[3])
        
        #fig.tight_layout() 
    
        return fig, ax

    def make_combo_chart(self, data, kind='line', unit_label='none', unit_label2 = 'none', xunit_label='none', legend=True, no_xlabel=True, ytickformat=',g', ytickformat2=',.0f', xtickformat=',g', stacked=False,  date=False, figsize=(4.3,2.8), primary='none', secondary='none', colors='none', manual=False, builddate=True, ylim=None, scatlabel='none', scatindex='none', label=False, secondary_y=True, newindex=False, multi=False, layout=(1,1), leglabel='none', date_n=1, clean_secondary=None, legdown=False, hspace=0.2, wspace=0.2):
    
        if multi:
            c = [colors[0]]
        else:
            c = colors
        
        
        fig = self.make_chart(data, kind=kind, unit_label=unit_label, xunit_label=xunit_label, legend=legend, no_xlabel=no_xlabel, ytickformat=ytickformat, xtickformat=xtickformat, stacked=stacked,  date=date, figsize=figsize, primary=primary, addtoexcel=False, combo=True, colors=c, builddate=builddate, ylim=ylim, scatlabel=scatlabel, scatindex=scatindex, label = label, multi=multi, layout=layout, date_n=date_n, legdown=legdown)
                
        
        if multi:
            axes, data, fig = self.plot_multi_secondary(data, fig, primary, secondary, unit_label2=unit_label2, ytickformat2=ytickformat2, date=date, colors=colors[1], manual=manual, builddate=builddate, secondary_y=secondary_y, newindex=newindex, leglabel=leglabel, kind=kind, clean_secondary=clean_secondary)
            
            #for a in axes:
            #    self.abares_style(a, data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, date_n = date_n)
            fig.subplots_adjust(wspace=wspace, hspace=hspace) 
        else:
            fig = self.plot_secondary(data, fig.gca(), primary, secondary, unit_label2=unit_label2, ytickformat2=ytickformat2, date=date, colors=colors, builddate=builddate, secondary_y=secondary_y, multi=multi, kind=kind, clean_secondary=clean_secondary)        
            
            #if kind=='area':
            #    self.abares_style(fig.gca(), data, kind, legend, unit_label, xtickformat, ytickformat, xunit_label, date, date_n = date_n, legdown=legdown)
           
        plt.show()
        
        return fig
        
        
    def plot_secondary(self, data, ax, primary, secondary, unit_label2='none',  ytickformat2=',g', date=False, colors='none', kind='none', builddate=True, secondary_y=True, multi=False, clean_secondary=None):
        
        data = data[secondary]            

        n = len(primary)  
        
        if colors == 'none':
            colors = self.abares_colors[n::]
        else:
            colors = colors[n::]
         
        if date:   
            if type(data.index) == pd.core.index.Int64Index:
                data.index = np.array([str(d-1) + "–" + str(d)[-2:] for d in data.index])
            elif builddate:
                data.index = pd.to_datetime(data.index, format='%d/%m/%Y')
        
        if kind=='bar' or kind=='area':
            if secondary_y:
                ax2 = ax.twinx()
                i = 0
                for col in secondary:        
                    c = colors[i] 
                    temp = data[col]
                    temp.index = range(data.shape[0])
                    ax2.plot(data[col], label=col, color=c)
                    i += 1
            else:
                i = 0
                for col in secondary:        
                    c = colors[i]         
                    ax.plot(data[col], label=col, color=c)
                    i += 1
        else:
            i = 0
            for col in secondary:            
                c = colors[i]     
                temp = pd.DataFrame(data[col])
                ax2 = temp.plot(kind='line', ax = ax, secondary_y = secondary_y, color = c, legend=False)   
                i += 1
                ax2.xaxis.grid(True)
                ax.yaxis.grid(True)
               
      
                
        fig = ax.get_figure()
        if secondary_y:
            ax.tick_params(axis='y',which='major',left='off') 
            axes = [ax, ax2] 
        else:
            axes = [ax]
            
        if secondary_y:  
            if not(multi):
                handles0, labels0 = axes[0].get_legend_handles_labels()            
                handles1, labels1 = axes[1].get_legend_handles_labels()            
                handles = handles0 + handles1
                labels = [lab + ' (left axis)' for lab in labels0] + [lab + ' (right axis)' for lab in labels1]
                axes[0].legend(handles, labels, bbox_to_anchor=(1.12, 1), loc='upper left', borderaxespad=0., framealpha=0)
                
            if clean_secondary != None and not np.isnan(data[secondary[0]].max(skipna=True)):
                inc = clean_secondary[0]
                btop = clean_secondary[1]
                bbot = clean_secondary[2]
                bzero = clean_secondary[3]
                ymax = clean_secondary[4]
                if ymax == None:
                    ymax = data[secondary[0]].max(skipna=True)                    
                                    
                nticks = len(axes[0].get_yticks())                
                
                if bzero != None:
                    tick_size = (int(ymax / (nticks-1-btop) / inc) + 1)*inc
                    axes[1].set_yticks(np.linspace(0,tick_size*(nticks-1),len(axes[0].get_yticks())))
                else:
                    tick_size = (int( (data[secondary[0]].max(skipna=True) - data[secondary[0]].min(skipna=True) ) / (nticks-2-btop-bbot) / inc) + 1)*inc
                    m = int(data[secondary[0]].min(skipna=True)/tick_size - bbot)*tick_size
                    axes[1].set_yticks(np.linspace(m,m+tick_size*(nticks-1),len(axes[0].get_yticks())))   

            else:
                axes[1].set_yticks(np.linspace(axes[1].get_yticks()[0],axes[1].get_yticks()[-1],len(axes[0].get_yticks())))
            axes[1].tick_params(length=0)
            labels = axes[1].yaxis.get_majorticklocs()
            labels = [format(s, ytickformat2) for s in labels]
            #labels = [s.replace(",", " ") for s in labels]
            if unit_label2 != 'none':
                labels[0] = unit_label2
                axes[1].set_yticklabels(labels)
        
            plt.setp(axes[0].get_legend().get_texts(), fontsize='8.3')        
        
            for a in axes:
                a.spines['top'].set_color('none')
                a.spines['bottom'].set_color('black')   
            
            if kind == 'area':
                for legobj in axes[0].get_legend().legendHandles:
                    legobj.set_linewidth(2.0) 
        else:
            for legobj in axes[0].get_legend().legendHandles:
                legobj.set_linewidth(2.0) 
            axes[0].legend(bbox_to_anchor=(1.12, 1), loc='upper left', borderaxespad=0., framealpha=0)
            plt.setp(axes[0].get_legend().get_texts(), fontsize='8.3')
            
            
            
        mpl.rcParams['axes.color_cycle'] = self.abares_colors    
    
        return fig

    def plot_multi_secondary(self, data, fig, primary, secondary, unit_label2='none',  ytickformat2=',.0f', date=False, colors='none', manual=False, builddate=True, secondary_y=True, newindex=False, leglabel = 'none', kind='none', clean_secondary=None):
    
        #d = len(primary)
        fig.set_tight_layout(True)
        if newindex:
            data = data[secondary]
            data.index = data[secondary[0]]
            secondary = secondary[1::]
        else:
            data = data[secondary]            

        m = len(secondary)        
         
        if date and not(newindex):   
            if type(data.index) == pd.core.index.Int64Index:
                data.index = np.array([str(d-1) + "–" + str(d)[-2:] for d in data.index])
            elif builddate:
                data.index = pd.to_datetime(data.index, format='%d/%m/%Y')
     
        axes = fig.axes
        for i in range(m):    
            if secondary_y:
                axc = axes[i].twinx()
            else:
                axc = axes[i]     
            
            axc.plot(data[secondary[i]].values, label=secondary[i], color=colors)
            if not(kind=='bar'):
                axc.set_title(primary[i])
            
            if clean_secondary != None and not np.isnan(data[secondary[i]].max(skipna=True)):
                
                inc = clean_secondary[0]
                btop = clean_secondary[1]
                bbot = clean_secondary[2]
                bzero = clean_secondary[3]
                nticks = len(axes[i].get_yticks())                
                ymax = clean_secondary[4]
                if ymax == None:
                    ymax = data[secondary[0]].max(skipna=True)   
                    
                if bzero != None:
                    tick_size = (int(ymax / (nticks-1-btop) / inc) )*inc
                    axc.set_yticks(np.linspace(0,tick_size*(nticks-1),len(axes[i].get_yticks())))
                else:
                    tick_size = (int( (data[secondary[i]].max(skipna=True) - data[secondary[0]].min(skipna=True) ) / (nticks-2-btop-bbot) / inc) + 1)*inc
                    m = int(data[secondary[i]].min(skipna=True)/tick_size - bbot)*tick_size
                    axc.set_yticks(np.linspace(m,m+tick_size*(nticks-1),len(axes[i].get_yticks())))   
            else:
                axc.set_yticks(np.linspace(axc.get_yticks()[0], axc.get_yticks()[-1],len(axes[i].get_yticks())))              

            axc.tick_params(length=0)
            labels = axc.yaxis.get_majorticklocs()
            
            labels = [format(s, ytickformat2) for s in labels]
            #labels = [s.replace(",", " ") for s in labels]
            
            if unit_label2 != 'none':
                labels[0] = unit_label2
                axc.set_yticklabels(labels)
            
            axes[i].spines['bottom'].set_color('black')
            axes[i].spines['top'].set_color('none')    
            axc.spines['bottom'].set_color('black')
            axc.spines['top'].set_color('none')   
                
            #plt.tight_layout()
        fig.set_tight_layout(True)
        fig = axc.get_figure()

        handles, labels = axes[0].get_legend_handles_labels()
        if secondary_y:
            axc.tick_params(axis='y',which='major',left='off') 
            h, l = axc.get_legend_handles_labels()
            labels = labels + l
            handles = handles + h
        axes[0].legend(handles, leglabel, bbox_to_anchor=(1.1, 1.25), loc='upper center', borderaxespad=0., ncol=2, framealpha=0)
        
        mpl.rcParams['axes.color_cycle'] = self.abares_colors    
    
    
        return [axes, data, fig]

        
        

#def plotly_chart(ax, folder, fname, units=True, unit_label, legend=True):
#
#    fig = ax.get_figure()
#
#    if legend:
#        ax.legend().set_visible(False)
#        plotly_fig = plotly.tools.mpl_to_plotly(fig)
#        plotly_fig['layout']['margin'] = go.Margin(l=70, r=200, b=50, t=50, pad=5)
#        plotly_fig['layout']['width'] = plotly_fig['layout']['width'] + 150
#        plotly_fig['layout']['showlegend'] = True
#    else:
#        plotly_fig = plotly.tools.mpl_to_plotly(fig)

#    if units:
#        plotly_fig['layout']['yaxis']['title'] = unit_label
#
#    plotly_fig['layout']['yaxis']['range'] = (ax.get_ylim()[0], ax.get_ylim()[1]*1.01)
#    plotly_fig['layout']['xaxis']['range'] = ax.get_xlim()
#    plotly_fig['layout']['yaxis']['zeroline'] = True
#    plotly_fig['layout']['yaxis']['gridcolor'] = 'black'
#    plotly_fig['layout']['xaxis']['gridcolor'] = 'white'

#    plotly.offline.plot(plotly_fig, filename= (folder + fname + ".html"))
#    #plotly.plotly.image.save_as(plotly_fig, filename=(folder + fname + '.png'))

#infolder = "J:\ProductivityAndWaterAndSocial\Water\_Projects\SMDB_water_market\_Data\charts\data\\"
#outfolder = "J:\ProductivityAndWaterAndSocial\Water\_Projects\SMDB_water_market\_Data\charts\images\\"

#excelfile = pd.ExcelWriter("J:\ProductivityAndWaterAndSocial\Water\_Projects\SMDB_water_market\_Data\charts\\" + "ABARES_SMDB_Water_Market_chart_data.xlsx",  engine='xlsxwriter') 
#meta = pd.read_csv("J:\ProductivityAndWaterAndSocial\Water\_Projects\SMDB_water_market\_Data\charts\chart_index.csv")
#book = excelfile.book
#title = 'Lessons from the water market: The southern Murray Darling Basin water allocation market 2000 to 2016'
#contents, formats = build_contents(excelfile, title)

#contents.write(5, 9, 'Section 2: The southern Murray-Darling Basin water market', formats[3])
#make_chart(infolder, outfolder, meta.iloc[0], xlfile=excelfile, xlformats=formats, title=title, makefig=False)
#make_chart(infolder, outfolder, meta.iloc[1], unit_label="GL", kind='barh', stacked=True, xlfile=excelfile, xlformats=formats, title=title)
#make_chart(infolder, outfolder, meta.iloc[2], unit_label="GL", kind='line', stacked=True, date=True, xlfile=excelfile, xlformats=formats, title=title)
#make_chart(infolder, outfolder, meta.iloc[3], unit_label="%", kind='line',  date=True, xlfile=excelfile, xlformats=formats, title=title)
#make_chart(infolder, outfolder, meta.iloc[4], unit_label="no.", kind='line',  date=True, xlfile=excelfile, xlformats=formats, title=title)
#make_chart(infolder, outfolder, meta.iloc[5], unit_label="ML", kind='bar',  multi=True, legend=False, date=True, xlfile=excelfile, xlformats=formats, title=title, figsize=(7.5,3.5))

#fig = make_chart(infolder, outfolder, meta.iloc[6], unit_label="GL", kind='bar',  date=True, addtoexcel=False, primary=['Allocation trade vol', 'Entitlement trade vol'])
#fig = plot_secondary(infolder, outfolder, meta.iloc[6], fig, ['Allocation trade vol', 'Entitlement trade vol'], ['Allocation trade no', 'Entitlement trade no'], unit_label2='no.', ytickformat2=',g')


#make_chart(infolder, outfolder, "trade_vol_bar", unit_label="GL", kind='bar')
#make_chart(infolder, outfolder, "trade_vol_area", unit_label="GL", kind='area')
#make_chart(infolder, outfolder, "trade_vol_barh", unit_label="GL", kind='barh')
#make_chart(infolder, outfolder, "trade_vol_scatter", unit_label="GL", xunit_label='GL', kind='scatter')
#make_chart(infolder, outfolder, "trade_vol_hist", unit_label="GL", xunit_label='GL', kind='hist')
#make_chart(infolder, outfolder, "trade_vol_bar_s", unit_label="GL", kind='bar', stacked=True)
#make_chart(infolder, outfolder, "trade_vol_barh_s", unit_label="GL", kind='barh', stacked=True)

# combo bar and line chart
#bar_line_chart(infolder, outfolder, "trade_vol_line", unit_label="GL", unit_label2='test')

#Multi scatter chart
#data = pd.read_csv(infolder +  "trade_vol_scatter.csv", index_col=0)
#data_list = [data[0:10], data[10::]]
#multi_scatter_chart(data_list, ['Pre 1993', 'Post 1993'], outfolder, "trade_vol_multi_scatter", unit_label='GL', xunit_label='GL')

#Multi-panel chart
#fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True, figsize=(11,7))
#data = pd.read_csv(infolder +  "trade_vol_scatter.csv", index_col=0)
#data.index.names = [' ']
#matplotlib_chart(data, unit_label="GL", kind='line', ax=axes[0,0], legend=False, no_xlabel=True)
#matplotlib_chart(data, unit_label="GL", kind='line', ax=axes[0,1], legend=False, no_xlabel=True)
#matplotlib_chart(data, unit_label="GL", kind='line', ax=axes[1,0], legend=False, no_xlabel=True)
#matplotlib_chart(data, unit_label="GL", kind='line', ax=axes[1,1], legend=False, no_xlabel=True)
#axes[0,0].legend(loc = 'lower center', bbox_to_anchor = (0,-0.1,1,1),
#            bbox_transform = plt.gcf().transFigure, ncol=4, )




