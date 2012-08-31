# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Method which are provided by OpenEMM
"""

# python imports

# project imports
from pyopenemm.config import WEBSERVICE_USER, WEBSERVICE_PASSWORD


class OpenEMM(object):
    """ Class to manupilate with OpenEmm methods """

    def __init__(self, client):
        """ Constructor for OpenEmm
        args : suds client, openemm username, openemm password
        """
        self.client = client # python suds client
        self.username = WEBSERVICE_USER # openemm webservice username
        self.password = WEBSERVICE_PASSWORD # openemm webservice password

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

    def get_subscriber(self,subscriber_id):
        """ Method to get subscriber with id
        args : id
        returns : dict of subscriber info
        """
        try :
            customer = self.client.service.getSubscriber(self.username,self.password,subscriber_id)
            customer_dict = dict(zip(customer.paramNames.x,customer.paramValues.x))
        except Exception, e:
            # TODO : logger needs to be used
            customer_dict = {}

        return customer_dict

    def add_subscriber(self,user_dict,double_check,key_column,overwrite):
        """ Method to add new subscriber
        args :
            user_dict = Dictionary containing user information
            double_check - If True, check if subscriber is already in database
            key_column - column used for double_check
            overwrite - If True, subscriber gets updated
        returns : subscriber id
        """
        try :
            subscriber_label , subscriber_value = zip(*user_dict.items()) # unzip for values
            subscriber_label = { 'x' : subscriber_label } # get in StringArrayType format as openemm expects
            subscriber_value = { 'x' : subscriber_value } # get in StringArrayType format as openemm expects
            customer_id = self.client.service.addSubscriber(self.username,self.password,double_check,
                    key_column,overwrite,subscriber_label,subscriber_value)
        except Exception, e :
            # TODO : use logger instead
            customer_id = 0

        return customer_id
