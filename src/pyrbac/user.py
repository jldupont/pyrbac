'''
Created on Jun 14, 2015

@author: jldupont
'''

from role import get_role_from_name, get_role_from_name_or_class, roles_class_to_name_list


class UserRBAC(object):
    '''
    The base definition of a User
    '''

    def __init__(self, roles_name_or_classes = []):
        
        self.init_roles_from_names_or_classes(roles_name_or_classes)
        
        
    def init_roles_from_names_or_classes(self, names_or_classes):
        '''
        Initialize the user roles from a list of role names
         or a list of classes
        
        @raise RoleUnknownError
        '''
        self.roles = []        
        for name_or_class in names_or_classes:
            
            role_class = get_role_from_name_or_class(name_or_class)
            self.roles.append( role_class )
            
    def serialize_roles(self):
        '''
        Return a structure representing the roles 
         of the user. This structure can be persisted easily through
         a representation such as JSON.
         
        @return [string]
        '''
        return roles_class_to_name_list(self.roles)
             

    def init_roles_from_names(self, roles_name = []):
        '''
        Initialize the user roles from a list of role names
        
        @raise RoleUnknownError
        '''
        assert isinstance(roles_name, list)
        
        self.roles = []
         
        for role_name in roles_name:
            role_class = get_role_from_name(role_name)
            self.roles.append(role_class)
    
    def __repr__(self):
        return "User Roles: %s" % repr(self.roles)
