#!/usr/bin/python

import sys
import getopt
import hudsonstatus
import re


def usage(argv):
    print "DUMB"
    
def parseTemplateEntry(entry):
    x = hudsonstatus.HudsonStatus()
    x.getBuildStatus(entry)
    
def parseAllTemplateValues(templateValues):
    for templateValue in templateValues:
        fieldValues = templateValue.split(";")
        if(fieldValues[0] == "job"):
            print 'Its a job: ' + fieldValues[2] + ', ' + fieldValues[3] + ', id = ' + fieldValues[1]
        else:
            print "Field: " + fieldValues[1] + ", " + fieldValues[2]
    
    
def parseTemplate(contents):
    print "HERE"
    contents.find
    thing = re.findall("\[(.*?)\]", contents)
    return thing
#    for thingything in thing:
#        parseTemplateEntry(thingything)

def outputBuildStatus(template):
    f=open(template)
    contents = f.read()
    templateValues = parseTemplate(contents)
    parseAllTemplateValues(templateValues)

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
