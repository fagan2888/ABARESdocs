# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:14:12 2016

@author: DAUser
"""

import pandas as pd
import tabulate as tab
    
def find_between( s, first, last ):
    try:
        start = s.index(first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
      
def find_between_multi(s, first, last, idx):
    try:
        start = s.index(first, idx ) + len( first )
        end = s.index( last, start )
        return [s[start:end], start]
    except ValueError:
        return ""      
      
def double_space(s):
    idx= 0
    end = False    
    n = len(s) 
    
    while not(end):    
        
        try:
            idx = s.index('\n', idx) + 1
        except ValueError:
            end = True
        if not(end):    
            if s[idx-2] == '-' or s[idx+2] == '-':
                s = s
            else:
                s = s[0:idx] + '\n' + s[idx::]
            idx += 1
            if idx > n:
                end = True
    return s

def format_table(folder, fname, format_str=",0.2f"):
    
    data = pd.read_csv(folder + fname + '.csv', index_col=0)
    data.index = data.index.map(str)
    cols = data.index

    out = tab.tabulate(data, headers="keys", floatfmt=format_str, numalign="right", stralign="left") 
    n = len(find_between(out, '\n', '\n'))
    line1 = n*'-' +'\n'
    
    out = line1 + out     
    out = double_space(out)
    line2 = '\n\n'+ n*'-'     
    out = out + line2        

    out = '---' + out
    out = out.replace('\n-', '\n----')
    out = out.replace('\n ', '\n    ')
     
    for col in cols:
        out = out.replace(col, col + "   ")

    
    textfile = open(folder + fname + '.txt', "w")
    textfile.write(out)
    textfile.close()
    
    
class ReportBuilder:
    
    def __init__(self, tfolder, rfolder, reportname):
        
        self.tfolder = tfolder
        self.rfolder = rfolder
        self.reportname = reportname
        

    def insert_tables_stats(self, tablelist, tableformat, stats):

        i = 0        
        for tablename in tablelist:
            t_format = tableformat[i]

            format_table(self.tfolder, tablename, t_format)
            i+=1
            
        with open(self.rfolder + 'source\\' + self.reportname + '.md', 'r') as outfile:
            report = outfile.read()
            outfile.close()    
    
        for tablename in tablelist:
                
            with open(self.tfolder + tablename + '.txt', 'r') as tfile:
                table = tfile.read()
                tfile.close()
            
            report = report.replace('~' + tablename + '~', table)
        
        for stat in stats:
            report = report.replace('**' + stat + "**", stats[stat])
            
        with open(self.rfolder + self.reportname + '.md', 'w') as outfile:
            outfile.write(report)
            outfile.close()
    
    def make_chart_index(self, chartfile, chapters):
        
        chart_index = pd.DataFrame({'name' : {}, 'type' : {},  'number' : {}, 'caption' : {}, 'source' : {}})        
        chart_number = 1
        table_number = 1

        for chfile in chapters:

            with open(self.rfolder + 'source\\' + chfile, 'r') as outfile:
                report = outfile.read()
                outfile.close()  
        
            #chap_name, _ = find_between_multi(report, '# ' , ' {', 0)

            n = len(report)
            idx = 0
            caption = ''
            
            while idx < n:
                
                try:
                    caption, idx = find_between_multi(report, '![' , '](', idx)
                    name, idx = find_between_multi(report, '(figures/' , ')', idx)
                    chart_index = chart_index.append({'name' : name, 'type' : 'chart',  'number' : chart_number, 'caption' : caption}, ignore_index=True)
                    chart_number += 1       
                except ValueError:
                    idx = n + 1
                 

            idx = 0
            caption = ''
            
            while idx < n:
                
                try:
                    name, idx = find_between_multi(report, '~' , '~', idx)
                    caption, idx = find_between_multi(report, 'Table: ' , ' {#', idx)
                    chart_index = chart_index.append({'name' : name, 'type' : 'table', 'number' : table_number, 'caption' : caption}, ignore_index=True)
                    table_number += 1            
                except ValueError:
                    idx = n + 1

        chart_index.to_csv(chartfile)
