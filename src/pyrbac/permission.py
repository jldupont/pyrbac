'''
Created on Jun 14, 2015

@author: jldupont
'''


class Permission(object):
    '''
    Base class for permissions
    '''


class Read(Permission):
    '''
    'Read' Permission on a resource
    '''

class Update(Permission):
    '''
    'Update' Permission on a resource
    '''
   
class Create(Permission):
    '''
    'Create' Permission for a resource
    '''
    
class Delete(Permission):
    '''
    'Delete' Permission on a resource
    '''
    
class List(Permission):
    '''
    'List' Permission for a collection of resource
    '''
    
class Search(Permission):
    '''
    'Search' Permission on a collection of resource
    '''

    
