'''
Access Control

Created on Jun 14, 2015

@author: jldupont
'''

from .user import BaseUserRBAC
from .permission import Permission, PermissionError

def ensure(user, permission):
    '''
    Ensures that 'user' has 'permission'
    
    @return: None
    @raise PermissionError 
    '''
    assert issubclass(user, BaseUserRBAC),     "The parameter 'user' must be of subclass 'BaseUserRBAC'"
    assert issubclass(permission, Permission), "The parameter 'permission' must be of subclass 'Permission'"
    
    if user.has_all_permissions:
        return
    