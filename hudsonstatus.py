#!/usr/bin/python

import urllib
import sys
import getopt
class HudsonStatus:
    
    urlString = 'http://%s/hudson/job/%s/lastBuild/api/python'

   
    def getUrl(server,job):
        return urlString % (server, job)
        
    def getBuildStatus(server, job):
        
        url = getUrl(server,job)
        print "URL:" + url
        hudsonJob = eval(urllib.urlopen(url).read())
        print hudsonJob
        print hudsonJob['result']
        print hudsonJob['culprits']
        for culprit in hudsonJob['culprits']:
            print culprit['fullName']
        return hudsonJob
        
        
    
    
