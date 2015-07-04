'''

Exporting to JSON model for integration with client side javascript
 e.g. https://github.com/jldupont/jsrbac

Created on Jul 4, 2015

@author: jldupont
'''
import json
import role

__all__ = [ 'export' ]

def export(tojson=True):
    '''
    Export to JSON representation compatible with 
     https://github.com/jldupont/jsrbac
     
    @param tojson: if True, returns JSON string representation
                   if False, returns a python dict ready for json.dumps
    '''
    
    roles = role.get_roles()
    
    edict = {}
    
    for one_role in roles:
        
        edict[one_role.name.lower()] = _export_role(one_role)
        
    if tojson:
        return json.dumps( edict )
    
    return edict

def _export_role(r):
    '''
    Exports a role
    '''
    def fn(x):
        return repr(x).lower()
    
    perms = map(fn, r.permissions)
    
    return {
             'a': r.has_all_permissions
            ,'p': perms
            }