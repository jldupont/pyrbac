#!/usr/bin/env python
"""
    Jean-Lou Dupont's Python RBAC (Role Based Access Control)
    
    Created on 2015-06-14
    @author: jldupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.4"

DESC="""
RBAC (Role Based Access Control) library loosely based on NIST model (see http://csrc.nist.gov/groups/SNS/rbac/ ).
"""


from distutils.core import setup
from setuptools import find_packages


setup(name=         'pyrbac',
      version=      __version__,
      description=  'RBAC (Role Based Access Control) library',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'https://github.com/jldupont/pyrbac',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      scripts=      [
                     ]
      ,zip_safe=True
      ,long_description=DESC
      ,install_requires=[
                         ]
      ,test_suite="tests"
      ,use_2to3 = True
      )

#############################################

f=open("latest", "w")
f.write(str(__version__)+"\n")
f.close()

