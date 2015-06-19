'''
Created on Jun 15, 2015

@author: jldupont
'''

class MetaAction(type):
    
    actions = []
    
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        newclass=super(MetaAction, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)
        
        if newclass.__name__ != 'Action':
            cls.actions.append(newclass)
            newclass.name = newclass.__name__
    
        return newclass
    

class Action(object):
    '''
    Base class for Actions
    '''
    
    __metaclass__ = MetaAction

    def __repr__(self, *args, **kwargs):
        return self.__class__.__name__



class Read(Action):
    '''
    'Read' Action on a resource
    '''

class Update(Action):
    '''
    'Update' Action on a resource
    '''
   
class Create(Action):
    '''
    'Create' Action for a resource
    '''
    
class Delete(Action):
    '''
    'Delete' Action on a resource
    '''
    
class List(Action):
    '''
    'List' Action for a collection of resource
    '''
    
class Search(Action):
    '''
    'Search' Action on a collection of resource
    '''

    
