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
    
    Go through all the 'roles' assigned to a user type and
     confirm that there is at least 1 of these roles that
     list the required 'permission'. Else, raise 'PermissionError'.

    @param user: subclass of BaseUserRBAC
    @param permission: subclass of Permission  
    
    @return: None
    @raise PermissionError 
    '''
    assert isinstance(user, BaseUserRBAC) or issubclass(user, BaseUserRBAC),     "The parameter 'user' must be an instance of 'BaseUserRBAC'"
    assert isinstance(permission, Permission), "The parameter 'permission' must be an instance of 'Permission'"
    
    for role in user.roles:
        if role.has_all_permissions:
            return
        
        if has_permission(role, permission):
            return
        
    raise PermissionError('Expecting permission %s' % permission)
    

def has_permission(role, permission):
    '''
    Verifies that 'role' has 'permission'
    
    @param role: subclass of Role
    @param permission: subclass of Permission  
    
    @return True | False
    '''
    
    for _permission in role.permissions:
        if _permission == permission:
            return True

    return False
