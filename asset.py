# ----------------------------------------------------
# Class file for env_separation.py
#
# BDD Feature: env_separation.feature
# ----------------------------------------------------

from hamcrest import *
import unittest


class Asset():

    def __init__(self, asset_env):
        self.environment = asset_env
        self.env_prod = ['prod', 'dr']
        self.env_nonprod = ['non-prod', 'uat', 'dev', 'qa', 'lab']
        assert_that(self.environment, is_not(None), 'Environment variable is not defined')

    def environment_compare(self, e1, e2, e3):
        self.e1, self.e2, self.e3 = e1, e2, e3
        self.e1x, self.e2x, self.e3x = None, None, None
        self.env_pair = [self.e1, self.e2]

        if (self.e1 in self.env_prod):
            self.e1x = 'PROD'
        else:
            self.e1x = 'non-PROD'

        if (self.e2 in self.env_prod):
            self.e2x = 'PROD'
        else:
            self.e2x = 'non-PROD'

        if (self.e1x == self.e2x):
            return('Inside: Environment matched', self.e1x, self.e2x)
        else:
            return('Inside: Environment mismatched', self.e1x, self.e2x)


    def decision(self, outcome):
        self.outcome = None
        if all(x in self.env_prod for x in self.env_pair) or all(x in self.env_nonprod for x in self.env_pair):
            if (self.e3x == 'permitted'):
                self.outcome = 'allowed'
            else:
                self.outcome = 'denied'
        else:
            self.outcome = 'denied'

        return(self.outcome)
