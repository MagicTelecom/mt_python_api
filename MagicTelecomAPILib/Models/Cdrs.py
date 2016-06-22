# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib.Models.Cdrs
 
   This file was automatically generated by APIMATIC v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.APIHelper import APIHelper

class Cdrs(object):

    """Implementation of the 'Cdrs' model.

    A Cdrs Structure

    Attributes:
        user_id (string): TODO: type description here.
        service_type (string): TODO: type description here.
        start_date (string): TODO: type description here.
        end_date (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Cdrs class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    user_id -- string -- Sets the attribute user_id
                    service_type -- string -- Sets the attribute service_type
                    start_date -- string -- Sets the attribute start_date
                    end_date -- string -- Sets the attribute end_date
        
        """
        # Set all of the parameters to their default values
        self.user_id = None
        self.service_type = None
        self.start_date = None
        self.end_date = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "user_id": "user_id",
            "service_type": "service_type",
            "start_date": "start_date",
            "end_date": "end_date",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "user_id": "user_id",
            "service_type": "service_type",
            "start_date": "start_date",
            "end_date": "end_date",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)