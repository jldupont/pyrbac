'''
Created on July 4, 2015

@author: jldupont
'''
import unittest

from pyrbac import export


#
# ===================================================================================
#
class Test4(unittest.TestCase):
    '''
    Export
    
    The relevant Role classes are defined in tests_2
    '''
    def testExport1(self):
        
        edict = export(tojson=False)
        
        self.assertEqual(edict['admin']['a'], True, "Expecting 'all permission' from Admin")
        self.assertEqual('domain:create' in edict['manager']['p'], True, "Expecting 'Domain:Create' from Manager")