'''
Created on Jun 14, 2015

@author: jldupont
'''

from .permission import Permission


class MetaRole(type):
    '''
    Metaclass for Role
    
    Collects all subclasses of Role
    '''
    
    roles = []
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaRole, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'Role':
            cls.roles.append(newclass)
            newclass.name = newclass.__name__
            
            newclass._validate()
    
        return newclass
    

def get_roles():
    '''
    Return all Role subclasses
    '''
    return MetaRole.roles



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

