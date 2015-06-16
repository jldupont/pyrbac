'''
Created on Jun 14, 2015

@author: jldupont
'''
import unittest

from pyrbac.permission import * #@UnusedWildImport
import pyrbac.role as mrole

#
# ==================================================================================
#

class Test1(unittest.TestCase):
    '''
    Very basic tests
    '''

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRoleAdmin1(self):
        '''
        Existence
        '''
        assert mrole.Admin in mrole.get_roles()

    def testRoleAdmin2(self):
        '''
        Name property
        '''
        assert (mrole.Admin).name == 'Admin'






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()