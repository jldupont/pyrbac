'''
Created on Jun 14, 2015

@author: jldupont
'''
import unittest

import pyrbac.role as mrole


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRoleAccumulation(self):
        '''
        There should only be 2 roles defined in the library
        '''
        assert len(mrole.get_roles()) == 2

    def testRoleAdmin1(self):
        '''
        Existence
        '''
        assert mrole.Admin in mrole.get_roles()





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()