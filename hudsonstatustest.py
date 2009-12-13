#!/usr/bin/python

import pythonhudson
import unittest

class TestUsage(unittest.TestCase):
    def testGetUrlString(self):
        self.assertEqual("http://somewhere/hudson/job/somejob/lastBuild/api/python",
                         pythonhudson.getUrl("somewhere", "somejob"))
        
        
if __name__ == "__main__":
    unittest.main()
