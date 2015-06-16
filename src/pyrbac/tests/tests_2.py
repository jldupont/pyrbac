'''
Created on Jun 15, 2015

@author: jldupont
'''
import unittest

from pyrbac.user import BaseUserRBAC
from pyrbac.action import * #@UnusedWildImport
import pyrbac.role as mrole
from pyrbac.resource import Resource
from pyrbac.permission import define_permissions, Permission, PermissionError
from pyrbac.control import ensure

#
# ==================================================================================
#

class Domain(Resource):
    '''
    A test resource
    '''

class TestResource(Resource):
    '''
    A test resource
    '''



class Manager(mrole.Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (Domain, Create)
                                       ,(Domain, Read)
                                       ,(Domain, Update)
                                       ,(Domain, Delete)
                                      ])


class User1(BaseUserRBAC):
    '''
    A test user
    '''
    roles = [Manager]

#
# ===================================================================================
#




class Test2(unittest.TestCase):
    '''
    Hypothetical role 'Manager' tests
    '''

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNameProperty(self):
        assert Domain.name == "Domain"
        
    
    def testPermission1(self):
        
        ensure(User1, Permission(Domain, Create))  

    def testPermission2(self):
        
        user1 = User1()
        ensure(user1, Permission(Domain, Create))  
        

    def testPermission3(self):
        
        user1 = User1()
        
        with self.assertRaises(PermissionError):
            ensure(user1, Permission(TestResource, Create))

