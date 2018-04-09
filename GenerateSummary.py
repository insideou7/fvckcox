#!/usr/bin/env python

from os import path

from FvckCox import LogAnalyzer

if __name__ == '__main__':
    logFolder = path.dirname(path.realpath(__file__))
    logFolder = path.join(logFolder, 'logs')

    analyzer = LogAnalyzer(logFolder)
    
    analyzer.AnalyzeAndWritePreviousMonth()