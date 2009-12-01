#!/usr/bin/python

import urllib
import sys
import getopt

urlString = 'http://%s/hudson/job/%s/lastBuild/api/python'

def usage():
    print "You're an idiot"
    return 1

def getUrl(server,job):
    return urlString % (server, job)
    
def getBuildStatus(server, job):
    
    url = getUrl(server,job)
    print "URL:" + url
    hudsonJob = eval(urllib.urlopen(url).read())
    print hudsonJob
    print hudsonJob['result']
    

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:j:", ["help", "server", "job"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        
        elif opt in ("-s", "--server"):
            server = arg
            
        elif opt in ("-j", "--job"):
            job = arg
            
    
    getBuildStatus(server, job)    
        
if __name__ == "__main__":
    main(sys.argv[1:])
    
