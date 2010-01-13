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
        self.assertEquals("Invalid Job ID: hi", x)
        
    def testProcessResultField(self):
        x = conkyhudson.processResultField({"result": "SUCCESS"}, "a,b,c")
        self.assertEquals("a", x)
        
if __name__ == "__main__":
    unittest.main()
