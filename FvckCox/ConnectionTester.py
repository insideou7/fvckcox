import urllib2
import ssl
import json
from os import path,makedirs
from datetime import datetime

from Utils import read_file, get_logfile_path

class ConnectionTester:
    def __init__(self, logFolder, inNetworkUrl, outNetworkUrl):
        self.logFolder = logFolder
        self.inNetworkUrl = inNetworkUrl
        self.outNetworkUrl = outNetworkUrl
        
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        
    def IsConnectionWorking(self, ip):
        #todo find a faster way to do this
        try:
            urllib2.urlopen(ip, context = self.ctx, timeout=1)
            return True
        except:
            return False
    
    def GetPacketLossPercentage(self, ip):
        numTries = 25
        packetsLost = 0.0
        
        for i in xrange(numTries):
            if not self.IsConnectionWorking(ip):
                packetsLost = packetsLost + 1
        percentage = packetsLost / numTries
        
        return int(round(percentage))
        
    def TestAndLogConnection(self):
        if not self.IsConnectionWorking(self.inNetworkUrl):
            return
        
        packetLoss = self.GetPacketLossPercentage(self.outNetworkUrl)
        
        if packetLoss > 0:
            results = self.FormatResults(packetLoss)
            self.LogResultsToFile(results)
        
    def FormatResults(self, packetLoss):
        now = datetime.now()
        packetLoss = packetLoss * 100
                
        out = {
            'timestamp' : '%s-%02d-%02d %02d:%02d' % (now.year, now.month, now.day, now.hour, now.minute),
            'percentPacketLoss' : packetLoss
        }
        
        return out
        
    def LogResultsToFile(self, results):
        now = datetime.now()
        currentLogFolder = path.join(self.logFolder, str(now.year))
        logFilePath = get_logfile_path(self.logFolder, now.year, now.month)
        
        if not path.exists(currentLogFolder):
            makedirs(currentLogFolder)
        
        if path.exists(logFilePath):
            with open(logFilePath, 'r') as f:
                data = read_file(logFilePath)
                jsonData = json.loads(data)
                jsonData['results'] += [results]
        else:
            jsonData = {
                'results' : [results]
            }
        
        with open(logFilePath, 'w+') as f:
            f.write(json.dumps(jsonData))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        