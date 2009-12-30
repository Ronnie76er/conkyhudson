#!/usr/bin/python

import sys
import getopt
import hudsonstatus
import re


def usage(argv):
    print "DUMB"
    
def parseTemplate(contents):
    print "HERE"
    contents.find
    thing = re.findall("\[*\]", contents)
    print thing

def outputBuildStatus(template):
    print template
    f=open(template)
    contents = f.read()
    print contents
    parseTemplate(contents)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:j:t:", ["help", "server", "jobs","template"])
    except:
        usage(argv)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
            
        elif opt in ("-s", "--server"):
            server = arg
            
        elif opt in ("-j", "--jobs"):
            jobs = arg
            
        elif opt in ("-t", "--template"):
            template = arg
            
    outputBuildStatus(template)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
