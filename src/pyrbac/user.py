'''
Created on Jun 14, 2015

@author: jldupont
'''

from role import Admin
from _pyio import __metaclass__


class UserUnknownError(Exception):
    '''
    An unknown user class
    '''


class MetaUser(type):
    '''
    Metaclass for User
    '''
    
    users = {}
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaUser, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'BaseUserRBAC':
            
            name = newclass.name = newclass.__name__            
            cls.users[name.lower()] = newclass 
    
        return newclass


class BaseUserRBAC(object):
    '''
    The base definition of a User
    '''
    
    __metaclass__ = MetaUser
    
    roles = []
    

class UserAdmin(BaseUserRBAC):
    '''
    The Admin user
    '''
    roles = [Admin]
    
    
def get_user_class_from_name(name):
    '''
    Return a BaseUserRBAC subclass corresponding to 'name' string
    
    @raise UserUnknownError    
    '''
    assert isinstance(name, basestring), "Expecting a string for 'name'" 
    
    try:
        return MetaUser.users[name.lower()]
    except:
        raise UserUnknownError()
    