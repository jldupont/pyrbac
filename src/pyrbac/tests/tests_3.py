'''
Created on Jun 15, 2015

@author: jldupont
'''
import unittest

from pyrbac.user import BaseUserRBAC
from pyrbac.action import * #@UnusedWildImport

from pyrbac.user import get_user_class_from_name

#
# ==================================================================================
#
class User1(BaseUserRBAC):
    '''
    A test user
    '''

#
# ===================================================================================
#




class Test3(unittest.TestCase):
    '''
    User class related tests
    '''

    def testUser1(self):
        
        user1_class = get_user_class_from_name('User1')
        
        assert issubclass(user1_class, BaseUserRBAC)
        

