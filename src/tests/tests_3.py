'''
Created on Jun 15, 2015

@author: jldupont
'''
import unittest

from pyrbac.user import UserRBAC
from pyrbac.action import * #@UnusedWildImport
from pyrbac.role import Admin, Guest


#
# ==================================================================================
#
class User1(UserRBAC):
    '''
    A test user
    '''
    def __init__(self, roles_name):
        super(User1, self).__init__(roles_name)


#
# ===================================================================================
#




class Test3(unittest.TestCase):
    '''
    User class related tests
    '''
    
    roles1 = ['Admin']
    
    def setUp(self):
        self.user1 = User1(self.roles1)

    def testUser1(self):
        
        assert isinstance(self.user1, UserRBAC)
        
    def testUser2(self):
        
        user = User1([Admin, Guest])
        
        roles = user.serialize_roles()
        
        self.assertTrue('Admin' in roles, 'Expecting to find string Admin')
        self.assertTrue('Guest' in roles, 'Expecting to find string Guest')

