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
            
    def testRoleSerialization(self):
        
        roles_list = [mrole.Admin, mrole.Guest]
        
        names_list = mrole.roles_class_to_name_list(roles_list)
        
        self.assertTrue('Admin' in names_list, 'Expected Admin in list, got %s' % repr(names_list))
        self.assertTrue('Guest' in names_list, 'Expected Guest in list, got %s' % repr(names_list))
        
            
    def testRoleDeserialization(self):
        
        names_list = ['Admin', 'Guest']
        
        roles_list = mrole.roles_class_from_name_list(names_list)
        self.assertTrue(mrole.Admin in roles_list, 'Expected role Admin in result list')
        self.assertTrue(mrole.Guest in roles_list, 'Expected role Guest in result list')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()