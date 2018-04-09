import traceback
import string
import os
from datetime import datetime



def format_to_printable(s):
    return filter(lambda x: x in string.printable, s)

def get_logfile_path(logRoot, year, month):
    currentLogFolder = os.path.join(logRoot, str(year))
    logFileName = '%s_%02d.txt' % (year, month)
    logFilePath = os.path.join(currentLogFolder, logFileName)
    
    return logFilePath
        

def read_file(filename):
    file = ''
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                file += line
    return file
                

def write_error(path, error): 
    #for some reason 'with open...' won't work??
    _d = '=' * 50 + '\n'
    _d += '=' * 24 + '%s\n' % datetime.now()
    _d += '=' * 50 + '\n'
    filepath = os.path.join(path, 'errors.txt')
    f = open(filepath, 'a')
    f.write('%s' % _d)
    traceback.print_exc(file=f)
    f.write('\n')
    f.close()
    






