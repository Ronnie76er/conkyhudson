#!/usr/bin/python

import conkyhudson
import unittest

class TestUsage(unittest.TestCase):
    def testParseTemplate(self):
        x = conkyhudson.parseTemplate("{x}[x]adfjalkf()[y]")
        self.assertEqual(2, len(x))
        
        
        
if __name__ == "__main__":
    unittest.main()
