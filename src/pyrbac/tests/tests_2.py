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


class User1(BaseUserRBAC):
    '''
    A test user
    '''
    roles = [Manager]


class User2(BaseUserRBAC):
    '''
    A test user
    '''
    roles = [Director]


class User3(BaseUserRBAC):
    '''
    A test user
    '''
    roles = [Manager, Tester]

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
        
    
    def testPermission1(self):
        '''
        Permission OK 1 - with user class
        '''
        ensure(User1, Permission(Domain, Create))  

    def testPermission2a(self):
        '''
        Permission OK 2 - with user class instance
        '''        
        user1 = User1()
        ensure(user1, Permission(Domain, Create))
        ensure(user1, Permission(Domain, Read))
        ensure(user1, Permission(Domain, Update))


    def testPermission2b(self):
        '''
        Another user class
        '''
        user2 = User2()
        ensure(user2, Permission(Domain, Create))
        ensure(user2, Permission(Domain, Read))
        ensure(user2, Permission(Domain, Update))
        ensure(user2, Permission(Domain, Delete))  

    def testPermission2c(self):
        '''
        Multiple roles per user class
        '''        
        user3 = User3()
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
        user1 = User1()
        
        with self.assertRaises(PermissionError):
            ensure(user1, Permission(TestResource, Create))

