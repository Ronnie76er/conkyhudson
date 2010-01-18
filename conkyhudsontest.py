#!/usr/bin/python

import conkyhudson
import unittest

class TestUsage(unittest.TestCase):
    #def testParseTemplate(self):
    #    x = conkyhudson.parseTemplate("{x}[x]adfjalkf()[y]")
    #    self.assertEqual(2, len(x))
    #    
    def testParseResultFieldsBadJobId(self):
        x = conkyhudson.parseResultFields("hi;hi", {"jobId1":"job"})
        self.assertEquals("No Data", x)
        
    def testParseResultFieldsUnhandledField(self):
        x = conkyhudson.parseResultFields("jobId1;field", {"jobId1":{"field":"Some value in a field"}})
        self.assertEquals("Some value in a field", x)
        
    def testProcessResultField(self):
        x = conkyhudson.processResultField({"result": "SUCCESS",
                                            "building":"false"}, "a,b,c")
        self.assertEquals("a", x)
        
    def testProcessResultFieldNoOutputOptions(self):
        x = conkyhudson.processResultField({"result": "SUCCESS",
                                            "building":"false"}, None)
        self.assertEquals("SUCCESS", x)
        x = conkyhudson.processResultField({"result": "FAILURE",
                                            "building":False}, None)
        self.assertEquals("FAILURE", x)
        x = conkyhudson.processResultField({"result": None,
                                            "building":True}, None)
        self.assertEquals("Building...", x)
        x = conkyhudson.processResultField({"result": None,
                                            "building":False}, None)
        self.assertEquals("No status", x)
        
    def testProcessCulpritField(self):
        x = conkyhudson.processCulpritField({
            "culprits":[
                {"fullName":"name1"},
                {"fullName": "name2"},
                {"fullName": "name3"}
            ]}, "None")
        self.assertEquals("name1, name2, name3", x)
    
    def testParseResultFieldsWithResultNoOptions(self):
        x = conkyhudson.parseResultFields("jobId1;result", {"jobId1":{"result":"SUCCESS",
                                                                      "building":False}})
        self.assertEquals("SUCCESS", x)
if __name__ == "__main__":
    unittest.main()
