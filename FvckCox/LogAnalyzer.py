from __future__ import division
import urllib2
import ssl
import json
from os import path,makedirs
from datetime import datetime
from calendar import monthrange

from Utils import read_file, get_logfile_path

class LogAnalyzer:
    def __init__(self, logFolder):
        self.logFolder = logFolder
        
    def AddMonths(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day,monthrange(year,month)[1])
        return datetime(year,month,day)
        
    def GetPreviousMonthsLog(self):
        lastMonth = self.AddMonths(datetime.now(), -1)
        logFilePath = get_logfile_path(self.logFolder, lastMonth.year, lastMonth.month)
        
        if path.exists(logFilePath):
            with open(logFilePath, 'r') as f:
                data = read_file(logFilePath)
                jsonData = json.loads(data)
                return jsonData['results']
        else:
            return None
        
    def AnalyzeLogs(self, logs):
        lastMonth = self.AddMonths(datetime.now(), -1)
        numDrops = len(logs)
        datesOut = set()
        
        for log in logs:
            _date = datetime.strptime(log['timestamp'], '%Y-%m-%d %H:%M')
            datesOut.add(_date.strftime("%Y-%m-%d"))
            
        daysInLastMonth = monthrange(lastMonth.year, lastMonth.month)[1]
        numDaysOut = len(datesOut)
        
        output  = '=================================================\n'
        output += '%s Report\n' % lastMonth.strftime("%Y-%m")
        output += '=================================================\n'
        output += 'Days dropped: %2s/%s (%1.2f%%)\n' % (numDaysOut, daysInLastMonth, (numDaysOut * 100) / daysInLastMonth)
        output += '   Hours out: %5s (%1.2f%%)\n\n' % (numDrops, (numDrops * 100) / (daysInLastMonth * 24))
        
        return output
        
    def WriteAnalysis(self, analysis):
        logFilePath = path.join(self.logFolder, 'analysis.txt')
        
        with open(logFilePath, 'a+') as f:
            f.write(analysis)
            
    def AnalyzeAndWritePreviousMonth(self):
        logs = self.GetPreviousMonthsLog()
        analysis = self.AnalyzeLogs(logs)
        self.WriteAnalysis(analysis)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        