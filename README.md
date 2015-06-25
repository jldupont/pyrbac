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
```