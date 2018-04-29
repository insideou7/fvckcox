# fvckcox

Attempts to detect network packet loss and log it to the specified log folder. Logs are grouped by month and year. The goal is to log every 'outage event' so I can contact my service provider (guess who) and get money back on my bill. I have the script scheduled to run every hour, so an outage event is any packet loss when the script is run. 

## Usage
It's written in Python 2.7. 

You mainly just need to set the log folder location and the test IPs. In this case the log folder is adjacent to the Main.py file. The dns (outbound IP) should work for most people, but you may need to change your router IP depending on your router. The script does a small check on your router to see if it is working before trying to test outbound connectivity.

    routerIp = 'http://192.168.1.1'
    dnsIp = 'https://1.1.1.1'
    logFolder = path.dirname(path.realpath(__file__))
    logFolder = path.join(logFolder, 'logs')  #changeme
