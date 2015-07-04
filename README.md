### Status
[![Build Status](https://travis-ci.org/jldupont/pyrbac.svg?branch=master)](https://travis-ci.org/jldupont/pyrbac)

pyrbac
======

Role Based Access Control in Python loosely based on the NIST model (see http://csrc.nist.gov/groups/SNS/rbac/ ).

Example Usage
=============

```python
from pyrbac import *

# Define a resource to police
#
class Domain(Resource):
    '''
    A test resource
    '''

# Define a Role
#
class Manager(Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (Domain, Create)
                                       ,(Domain, Read)
                                       ,(Domain, Update)
                                      ])

# Instantiate a User with a role
#
user1 = UserRBAC([Manager])

# Check for permission - throws an exception upon restriction
#                
ensure(user1, Permission(Domain, Create))

#
# Another role with more permissions
#
class Director(Role):
    '''
    A test role
    '''
    permissions = define_permissions([
                                        (Domain, Create)
                                       ,(Domain, Read)
                                       ,(Domain, Update)
                                       ,(Domain, Delete)
                                      ])
user2 = UserRBAC([Director])

#  A Director can assign the role of 'Manager'
#   because Director has strictly more rights than a 'Manager'
can_assign(user2, Manager) == True

#  But a Manager can't even assign a role of Manager
can_assign(user1, Manager) == False
```

Client Side
===========

The following javascript client side library can be useful: https://github.com/jldupont/jsrbac