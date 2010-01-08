#!/usr/bin/python

import sys
import getopt
import hudsonstatus
import re


def usage(argv):
    print "DUMB"
    
def getJobStatus(server, job):
    x = hudsonstatus.HudsonStatus()
    return x.getBuildStatus(server, job)
    
def parseAllTemplateValues(templateValues):
    jobs = {}
    fields = {}
    
    
    for templateValue in templateValues:
        fieldValues = templateValue.split(";")
        if(fieldValues[0] == "job"):
            print 'Its a job: ' + fieldValues[2] + ', ' + fieldValues[3] + ', id = ' + fieldValues[1]
            status = getJobStatus(fieldValues[2],fieldValues[3])
            jobs[fieldValues[1]] = status
            
        else:
            if fieldValues[0] not in fields:
                fields[fieldValues[0]] = []
            fields[fieldValues[0]].append({"field": fieldValues[1], "letters": fieldValues[2]})
    
    for jobKey, job in jobs.iteritems():
        print "Job ID: ", jobKey, "\n", job
        
    for fieldKey, field in fields.iteritems():
        print "Field ID: ", fieldKey, " , field: ", field
    
    
def parseTemplate(contents):
    contents.find
    thing = re.findall("\[(.*?)\]", contents)
    return thing

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
