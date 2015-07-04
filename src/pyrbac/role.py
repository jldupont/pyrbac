'''
Created on Jun 14, 2015

@author: jldupont
'''

from .permission import Permission


class RoleUnknownError(Exception): pass


class MetaRole(type):
    '''
    Metaclass for Role
    
    Collects all subclasses of Role
    '''
    
    roles = {}
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaRole, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'Role':
            
            name = newclass.__name__
            newclass.name = name
            cls.roles[name.lower()] = newclass
            newclass._validate()
    
        return newclass
    

def get_roles():
    '''
    Return all Role subclasses
    '''
    return MetaRole.roles.values()


def get_role_from_name(name):
    '''
    Return a Role class given the name of a role
    
    @raise RoleUnknownError 
    '''
    try:
        return MetaRole.roles[name.lower()]
    except:
        RoleUnknownError(str(name))


def get_role_from_name_or_class(name_or_class):
    '''
    Return a Role class based on either a role name
     or pass-through the Role class
     
    @return Role class
    @raise RoleUnknownError
    '''
    if isinstance(name_or_class, basestring):
        role_class = get_role_from_name(name_or_class)
        return role_class
    
    elif issubclass(name_or_class, Role):
        return name_or_class
    
    raise RoleUnknownError(str())
    
def roles_class_from_name_list(names_list):
    '''
    Construct [Role] from [string]
    
    @return [Role]
    @raise RoleUnknownError
    '''
    assert isinstance(names_list, list), 'Expecting [string], got %s' % repr(names_list)
    
    roles = []
    
    for name in names_list:
        roles.append( get_role_from_name(name) )
    
    return roles
    
def roles_class_to_name_list(roles_class):
    '''
    Return a list of role names given a list of role classes
    
    @return [string]
    @raise RoleUnknownError 
    '''
    assert isinstance(roles_class, list), 'Expecting list of Role class'
    
    roles_name = []
    for role_class in roles_class:
        assert issubclass(role_class, Role), 'expecting Role subsclass'
        roles_name.append( role_class.name )
        
    return roles_name

class Role(object):
    '''
    Base class for all Role
    '''

    __metaclass__ = MetaRole
    
    permissions = []
    has_all_permissions = False
    
    @classmethod
    def _validate(cls):
        '''
        Validate the permissions list
        '''
        for permission in cls.permissions:
            assert isinstance(permission, Permission), "got: %s" % repr(permission)
            
#
# ========================================================================= The basic roles
#
    
class Admin(Role):
    '''
    The most privileged role
    '''

    has_all_permissions = True
    

class Guest(Role):
    '''
    The least privileged role
    '''

