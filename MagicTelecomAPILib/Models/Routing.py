# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib.Models.Routing
 
   This file was automatically generated by APIMATIC v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.APIHelper import APIHelper
from MagicTelecomAPILib.Models.RoutingBase import RoutingBase

class Routing(RoutingBase):

    """Implementation of the 'Routing' model.

    TODO: type model description here.
    NOTE: This class inherits from 'RoutingBase'.

    Attributes:
        sip_user (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Routing class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    sip_user -- string -- Sets the attribute sip_user
                    logic -- string -- Sets the attribute logic
                    endpoints -- list of Endpoint -- Sets the attribute endpoints
        
        """
        # Call the constructor for the base class
        super(Routing, self).__init__(**kwargs)

        # Set all of the parameters to their default values
        self.sip_user = None
        self.logic = None
        self.endpoints = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "sip_user": "sip_user",
            "logic": "logic",
            "endpoints": "endpoints",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "endpoints" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.endpoints = list()
                for item in kwargs["endpoints"]:
                    self.endpoints.append(Endpoint(**item))

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
            "sip_user": "sip_user",
            "logic": "logic",
            "endpoints": "endpoints",
        }

        # Start from the base class
        retval = super(Routing, self).resolve_names()

        return APIHelper.resolve_names(self, replace_names, retval)