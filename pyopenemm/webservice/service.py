# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Method which are provided by OpenEMM
"""


class OpenEMM(object):
    """ Class to manupilate with OpenEmm methods """

    def __init__(self, client, username, password):
        """ Constructor for OpenEmm
        args : suds client, openemm username, openemm password
        """
        self.client = client # python suds client
        self.username = username # openemm username
        self.password = password # openemm password


    def find_subscriber(self,search):
        """ Method to find openemm subscriber
        args : key column and value
        returns : subscriber/customer id
        """
        try :
            key_column = search[0] # get key column
            value = search[1] # get value
            customer_id = self.client.service.findSubscriber(self.username,self.password,
                    key_column,value)
        except Exception, e :
            # TODO : user logger instead
            customer_id = 0

        return customer_id
