'''
Created on Jun 14, 2015

@author: jldupont
'''

from role import Admin

class BaseUserRBAC(object):
    '''
    The base definition of a User
    '''


class UserAdmin(BaseUserRBAC):
    '''
    The Admin user
    '''
    roles = [Admin]
    