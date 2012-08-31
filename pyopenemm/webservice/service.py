# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Method which are provided by OpenEMM
"""


class OpenEMM(object):
    """ Class to manupilate with OpenEmm methods """

    def __init__(self, client):
        self.client = client # python suds client
