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
    
    
def getOutput(template, jobs):
    output = u""
    end = False
    a = 0
        
    # a and b are indexes in the template string
    # moving from left to right the string is processed
    # b is index of the opening bracket and a of the closing bracket
    # everything between b and a is a template that needs to be parsed
    while not end:
        b = template.find('[', a)
        
        if b == -1:
            b = len(template)
            end = True            
        # if there is something between a and b, append it straight to output
        if b > a:
            output += template[a : b]
            # check for the escape char (if we are not at the end)
            if template[b - 1] == '\\' and not end:
                # if its there, replace it by the bracket
                output = output[:-1] + '['
                # skip the bracket in the input string and continue from the beginning
                a = b + 1
                continue
                    
        if end:
            break
            
        a = template.find(']', b)
            
        if a == -1:
            self.logError("Missing terminal bracket (]) for a template item")
            return u""
            
        # if there is some template text...
        if a > b + 1:
            output += parseResultFields(template[b + 1 : a], jobs)
            
        a = a + 1

    return output

    
def getAndRemoveJobs(templateIter, contents):
    """Removes the jobs from the template and gets the info from hudson
    on the job"""
    
    jobs = {}
    charsRemoved = 0
    
    for templateValue in templateIter:
        theString = templateValue.group(1)
        fieldValues = theString.split(";")
        if(fieldValues[0] == "job"):
            status = getJobStatus(fieldValues[2],fieldValues[3])
            jobs[fieldValues[1]] = status
            contents = contents[0:templateValue.start() - charsRemoved] + contents[templateValue.end()- charsRemoved+1:]
            charsRemoved += templateValue.end() - templateValue.start()+1;
            
    return [jobs, contents]
    
def processResultField(job, outputOptions):
    """Process the 'result' field """


    if fieldValues[1] in jobs[fieldValues[0]]:
        statusValue = jobs[fieldValues[0]][fieldValues[1]]


    outputStrings = outputOptions.split(",")
    #print outputStrings
    if(fieldValue == "SUCCESS"):
        return outputStrings[0]
    elif(fieldValue == "FAILURE"):
        return outputStrings[1]
    elif(fieldValue == None):
        return "Null value"
    else:
        return "I DON'T KNOW WHAT "+ fieldValue+ " SHOULD DO"
        
def processCulpritField(fieldValue, outputOptions):
    """Process the 'culprit' field"""
    print fieldValue, outputOptions
    return "None"
    
    
    

    
def parseResultFields(hudsonStatus, jobs):
    #print hudsonStatus
    
    fieldValues = hudsonStatus.split(";")
    
    jobId = fieldValues[0]
    job = {}
    if jobId in jobs:
        job = jobs[jobId]
    else:
        return "Invalid Job ID: " + jobId
    
    fieldName = fieldValues[1]
    
    retVal = ''
    statusValue = None
    
    if(fieldName == "result"):
        processResultField(job, fieldValues[2])
    
    #if len(fieldValues) == 3:
    #    retVal = getOutputByField(fieldValues[1], statusValue, fieldValues[2])
    #else:
    #    retVal = jobs[fieldValues[0]][fieldValues[1]]
    #        
    #        
    return retVal
    
    
def parseTemplate(contents):
    thing = re.finditer("\[(.*?)\]", contents)
    jobData = getAndRemoveJobs(thing,contents)
    
    final = getOutput(jobData[1], jobData[0])
    
    #print "FINAL CONTENTS ====================\n",final
    #print "DONE =============================="

    return final

def outputBuildStatus(template):
    f=open(template)
    contents = f.read()
    templateValues = parseTemplate(contents)
    
    print templateValues
    
    #parseAllTemplateValues(templateValues)

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
