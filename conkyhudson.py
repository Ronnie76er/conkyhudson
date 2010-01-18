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


    statusValue = job["result"]
    building = job["building"]
    if(outputOptions == None):
        if(statusValue == None):
            if(building == True):
                return "Building..."
            else:
                return "No status"
        return statusValue
    
    outputStrings = outputOptions.split(",")
    #print outputStrings
    if(statusValue == "SUCCESS"):
        return outputStrings[0]
    elif(statusValue == "FAILURE"):
        return outputStrings[1]
    elif(statusValue == None and building == True):
        return outputStrings[2]
    else:
        return "Error"
        
def processCulpritField(job, outputOptions):
    """Process the 'culprit' field"""
    
    culprits = job["culprits"]
    if(culprits == None):
        return outputOptions
    
    culpritsString = ''
    
    for culprit in culprits:
        if(culpritsString != ''):
            culpritsString += ", "
        culpritsString += culprit["fullName"]
        
    return culpritsString
    
    
    

    
def parseResultFields(hudsonStatus, jobs):
    """
    Taking in the input from the template, in the form of [job;field;output values]
    and taking in the data from the jobs, return an appropriate string for the output.
    
    This will depend on the type of field in hudsonStatus.
    """
        
    fieldValues = hudsonStatus.split(";")
    
    jobId = fieldValues[0]
    job = {}
    if jobId in jobs:
        job = jobs[jobId]
    else:
        return "No Data" 
    
    fieldName = fieldValues[1]
    options = None
    
    if(len(fieldValues) > 2):
        options = fieldValues[2]
    
    
    
    retVal = ''
    statusValue = None
    
    if(fieldName == "result"):
        retVal = processResultField(job, options)
    elif(fieldName == "culprit"):
        retVal = processCulpritField(job, options)
    else: #if it doesn't match anything, just attempt to return it's value
        retVal = job[fieldName]
    
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
