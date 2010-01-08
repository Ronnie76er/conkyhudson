#!/usr/bin/python

import urllib
import sys
import getopt
class HudsonStatus:
    
    urlString = 'http://%s/hudson/job/%s/lastBuild/api/python'

   
    def getUrl(self,server,job):
        return self.urlString % (server, job)
        
    def getBuildStatus(self,server, job):
        url = self.getUrl(server,job)
        print "URL:" + url
        hudsonJob = eval(urllib.urlopen(url).read())
        return hudsonJob
        
        
    
    
