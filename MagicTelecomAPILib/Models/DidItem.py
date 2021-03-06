# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib.Models.DidItem
 
   This file was automatically generated by APIMATIC v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.APIHelper import APIHelper
from MagicTelecomAPILib.Models.Item import Item
from MagicTelecomAPILib.Models.CallerLocation import CallerLocation

class DidItem(Item):

    """Implementation of the 'Did Item' model.

    Item of type Did
    NOTE: This class inherits from 'Item'.

    Attributes:
        phone_number (string): TODO: type description here.
        trunk_id (int): TODO: type description here.
        did_type_handle (string): TODO: type description here.
        caller_location (CallerLocation): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the DidItem class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    phone_number -- string -- Sets the attribute phone_number
                    trunk_id -- int -- Sets the attribute trunk_id
                    did_type_handle -- string -- Sets the attribute did_type_handle
                    _caller_location -- CallerLocation -- Sets the attribute caller_location
                    item_type -- string -- Sets the attribute item_type
        
        """
        # Call the constructor for the base class
        super(DidItem, self).__init__(**kwargs)

        # Set all of the parameters to their default values
        self.phone_number = None
        self.trunk_id = None
        self.did_type_handle = None
        self.caller_location = None
        self.item_type = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "phone_number": "phone_number",
            "trunk_id": "trunk_id",
            "did_type_handle": "did_type_handle",
            "_caller_location": "caller_location",
            "item_type": "item_type",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "_caller_location" in kwargs:
                self.caller_location = CallerLocation(**kwargs["_caller_location"])

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
            "phone_number": "phone_number",
            "trunk_id": "trunk_id",
            "did_type_handle": "did_type_handle",
            "caller_location": "_caller_location",
            "item_type": "item_type",
        }

        # Start from the base class
        retval = super(DidItem, self).resolve_names()

        return APIHelper.resolve_names(self, replace_names, retval)