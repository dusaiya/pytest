#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年10月23日

@author: alibaba
'''
import myclass1
import unittest

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEqual(myclass1.sum(1, 2), 3, 'sum fail')
    def testsub(self):
        self.assertEqual(myclass1.sub(2, 1), 1, 'sub fail') 
    
if __name__=='__main__':
    unittest.main()
    