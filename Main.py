from os import path

from FvckCox import ConnectionTester

if __name__ == '__main__':
    routerIp = 'http://192.168.1.1'
    dnsIp = 'https://1.1.1.1'
    logFolder = path.dirname(path.realpath(__file__))
    logFolder = path.join(logFolder, 'logs')

    tester = ConnectionTester(logFolder, routerIp, dnsIp)
    
    tester.TestAndLogConnection()