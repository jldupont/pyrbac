'''
Created on Jun 15, 2015

@author: jldupont
'''
import unittest

from pyrbac import * #@UnusedWildImport



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



class Manager(Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (Domain, Create)
                                       ,(Domain, Read)
                                       ,(Domain, Update)
                                      ])

class Tester(Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (TestResource, List)
                                       ,(TestResource, Read)
                                       ,(TestResource, Update)
                                      ])


class Director(Role):
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

    def testAssignment1(self):
        '''
        A Director attempts to assign a role of 'Manager'
        '''
        
        user1 = UserRBAC([Director])
        
        self.assertTrue( can_assign(user1, Manager) )

    def testAssignment2(self):
        '''
        A Manager attempts to assign a role of 'Director'
        '''
        
        user1 = UserRBAC([Manager])
        
        self.assertFalse( can_assign(user1, Director) )

    def testAssignment3(self):
        '''
        A Manager attempts to assign a role of 'Manager'
        '''
        
        user1 = UserRBAC([Manager])
        
        self.assertFalse( can_assign(user1, Manager) )
