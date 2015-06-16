'''
Created on Jun 14, 2015

@author: jldupont
'''
from _pyio import __metaclass__

class MetaResource(type):
    '''
    Metaclass for Resource
    
    Collects all subsclasses of Role
    '''
    
    resources = []
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaResource, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'Resource':
            cls.resources.append(newclass)
            newclass.name = newclass.__name__
    
        return newclass


def get_resources():
    '''
    Returns the list of resource classes 
    '''
    return MetaResource.resources

#
#
#

class Resource(object):
    '''
    Base class for a Resource
    '''
    
    __metaclass__ = MetaResource
    