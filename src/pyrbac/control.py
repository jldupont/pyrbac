'''
Access Control

Created on Jun 14, 2015

@author: jldupont
'''

from .user import UserRBAC
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
    assert isinstance(user, UserRBAC) or issubclass(user, UserRBAC), "The parameter 'user' must be an instance of 'BaseUserRBAC'"
    assert isinstance(permission, Permission), "The parameter 'permission' must be an instance of 'Permission'"
    
    for role in user.roles:
        if role.has_all_permissions:
            return
        
        if has_permission(role, permission):
            return
        
    raise PermissionError('Expecting %s on User %s' % (permission, user))
    

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

def can_assign(user_source, target_role):
    '''
    Can the 'user_source' assign 'target_role' to another user ?
    
    For 'user_source' to be able to assign 'target_role' to another user,
     'user_source' must have all the permissions assigned to 'target_role' *and* more.
    
    @return True | False
    '''
    
    target_permission_set = set(target_role.permissions)
    
    src_permissions_set = set()
    
    for role in user_source.roles:
        
        ##
        ## It only takes 1 admin (or equivalent) role
        ##
        if role.has_all_permissions:
            return True
        
        src_permissions_set.update(role.permissions)

    ##
    ## Must be a strict subset (i.e. not equal)
    ##        
    return target_permission_set < src_permissions_set
