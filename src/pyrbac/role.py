'''
Created on Jun 14, 2015

@author: jldupont
'''

class MetaRole(type):
    '''
    Metaclass for Role
    
    Collects all subsclasses of Role
    '''
    
    roles = []
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaRole, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'Role':
            cls.roles.append(newclass)
    
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

