#!/usr/bin/python

import urllib
import sys
import getopt
class HudsonStatus:
    
    urlString = 'http://%s/hudson/job/%s/lastBuild/api/python'

   
    def getUrl(self,server,job):
        return self.urlString % (server, job)
        
    def getBuildStatus(self,entry):
        
        entryContents = entry.split(";")
        
        server = entryContents[0]
        job = entryContents[1]
        field = entryContents[2]
        
        
        url = self.getUrl(server,job)
        print "URL:" + url
        hudsonJob = eval(urllib.urlopen(url).read())
        print field + ":" + hudsonJob[field]
        return hudsonJob
        
        
    
    
