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

class DummyClass(object): pass



class Test1(unittest.TestCase):
    '''
    Very basic tests
    '''

    def testRoleAdmin1(self):
        '''
        Existence
        '''
        self.assertTrue(mrole.Admin in mrole.get_roles(), 'Expecting Admin role')
        
    def testRoleAdmin2(self):
        '''
        Name property
        '''
        self.assertEqual((mrole.Admin).name, 'Admin', 'Expecting Admin class to have string name Admin')


    def testPermissionCreation1(self):
        '''
        Invalid creation 1
        '''
        with self.assertRaises(TypeError):
            Permission(None, None)


    def testPermissionCreation2(self):
        '''
        Invalid creation 2
        '''        
        with self.assertRaises(AssertionError):
            Permission(DummyClass, DummyClass)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()