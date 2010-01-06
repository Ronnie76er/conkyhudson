#!/usr/bin/python

import hudsonstatus
import unittest

class TestUsage(unittest.TestCase):
    def testGetUrlString(self):
        x = hudsonstatus.HudsonStatus()
        self.assertEqual("http://somewhere/hudson/job/somejob/lastBuild/api/python",
                         x.getUrl("somewhere", "somejob"))
        
        
if __name__ == "__main__":
    unittest.main()
