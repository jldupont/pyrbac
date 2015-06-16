'''
Created on Jun 15, 2015

@author: jldupont
'''
import unittest

from pyrbac.user import UserRBAC
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
                                      ])

class Tester(mrole.Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (TestResource, List)
                                       ,(TestResource, Read)
                                       ,(TestResource, Update)
                                      ])


class Director(mrole.Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (Domain, Create)
                                       ,(Domain, Read)
                                       ,(Domain, Update)
                                       ,(Domain, Delete)
                                      ])


#
# ===================================================================================
#




class Test2(unittest.TestCase):
    '''
    Hypothetical roles tests
    '''


    def testNameProperty(self):
        '''
        Resource Property
        '''
        assert Domain.name == "Domain"
        
    
    def testPermission1a(self):
        '''
        Permission OK 2 - with user class instance
        '''
        user1 = UserRBAC([Manager])
                
        ensure(user1, Permission(Domain, Create))
        ensure(user1, Permission(Domain, Read))
        ensure(user1, Permission(Domain, Update))


    def testPermission1b(self):
        '''
        Another user class
        '''
        user2 = UserRBAC([Director])
        
        ensure(user2, Permission(Domain, Create))
        ensure(user2, Permission(Domain, Read))
        ensure(user2, Permission(Domain, Update))
        ensure(user2, Permission(Domain, Delete))  

    def testPermission1c(self):
        '''
        Multiple roles per user class
        '''
        user3 = UserRBAC([Manager, Tester])
                
        ensure(user3, Permission(Domain, Create))
        ensure(user3, Permission(Domain, Read))
        ensure(user3, Permission(Domain, Update))
        
        ensure(user3, Permission(TestResource, List))
        ensure(user3, Permission(TestResource, Read))
        ensure(user3, Permission(TestResource, Update))

    def testPermission2(self):
        '''
        Multiple roles per user class
        '''
        user3 = UserRBAC(['manager', 'tester'])
                
        ensure(user3, Permission(Domain, Create))
        ensure(user3, Permission(Domain, Read))
        ensure(user3, Permission(Domain, Update))
        
        ensure(user3, Permission(TestResource, List))
        ensure(user3, Permission(TestResource, Read))
        ensure(user3, Permission(TestResource, Update))

    def testPermission3(self):
        '''
        Missing permission
        '''        
        user1 = UserRBAC([Manager])
        
        with self.assertRaises(PermissionError):
            ensure(user1, Permission(TestResource, Create))

