'''
Created on Jun 14, 2015

@author: jldupont
'''

from .resource import Resource
from .action import Action

class PermissionError(Exception):
    '''
    The exception class for Permission access control
    '''


class Permission(object):
    '''
    Base class for permissions
    '''

    def __init__(self, resource, action):

        assert issubclass(resource, Resource), "Expecting subclass of Resource"
        assert issubclass(action,   Action),   "Expecting subclass of Action"

        self.for_resource = resource
        self.for_action   = action
    
    def __repr__(self, *args, **kwargs):
        return "%s:%s" % (self.for_resource.__name__, self.for_action.__name__)

    def __eq__(self, other):
        return self.for_resource == other.for_resource and self.for_action == other.for_action

    def __hash__(self):
        '''
        Useful in set() operations
        '''
        return hash(self.__repr__())

    
def define_permissions(tuples_resource_action):
    '''
    Helper function for defining Permissions
    
    @return [Permission] 
    '''
    permissions = []
    
    for resource, action in tuples_resource_action:
        assert issubclass(resource, Resource), "expecting Resource in tuple (Resource, Action)"
        assert issubclass(action,   Action),   "expecting Action in tuple (Resource, Action)"
        
        permissions.append(Permission(resource, action))
        
    return permissions