# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Connecting OpenEMM with python suds
"""


# python imports
from suds.client import Client


# project imports
from pyopenemm.config import OPENEMM_URL


def create_connection():
    """
    Function to connect to OpenEMM using suds
    args : None
    returns : suds client object
    """
    try :
        client = Client(OPENEMM_URL)
    except Exception, e :
        pass

    return client # return suds client
