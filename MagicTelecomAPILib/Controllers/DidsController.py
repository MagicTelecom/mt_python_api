# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib.Controllers.DidsController

   This file was automatically generated by APIMATIC BETA v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.APIHelper import APIHelper
from MagicTelecomAPILib.APIException import APIException
from MagicTelecomAPILib.Configuration import Configuration
from MagicTelecomAPILib.Http.HttpRequest import HttpRequest
from MagicTelecomAPILib.Http.HttpResponse import HttpResponse
from MagicTelecomAPILib.Http.RequestsClient import RequestsClient
from MagicTelecomAPILib.Controllers.BaseController import BaseController



class DidsController(BaseController):

    """A Controller to access Endpoints in the MagicTelecomAPILib API."""

    def __init__(self, http_client = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client)

    def get_countries(self,
                      page=None,
                      limit=None):
        """Does a GET request to /dids/location/countries.

        Allow clients to get the list of available countries

        Args:
            page (int, optional): Zero based offset index for the results.
                e.g. 0 would start at the first result and 10 would start at
                the eleventh result
            limit (int, optional): Maximum number of results to return in the
                response

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/dids/location/countries"

        # Process optional query parameters
        query_parameters = {
            "page": page,
            "limit": limit
        }
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "X-Auth-Token": Configuration.x_auth_token,
            "X-Auth-Token": Configuration.x_auth_token
        }

        # Prepare the API call.
        http_request = self.http_client.get(query_url, headers=headers, query_parameters=query_parameters)

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Endpoint error handling using HTTP status codes.
        if response.status_code == 401:
            raise APIException("You are not authenticated", 401, response.raw_body)
        elif response.status_code == 403:
            raise APIException("This action needs a valid WSSE header", 403, response.raw_body)
        elif response.status_code == 404:
            raise APIException("Resource not found", 404, response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body



    def get_country_by_iso_2(self,
                             country_iso_2):
        """Does a GET request to /dids/location/countries/{country_iso2}.

        Allow clients to get a specific country

        Args:
            country_iso_2 (string): Country ISO2

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/dids/location/countries/{country_iso2}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "country_iso2": country_iso_2
        })
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "X-Auth-Token": Configuration.x_auth_token,
            "X-Auth-Token": Configuration.x_auth_token
        }

        # Prepare the API call.
        http_request = self.http_client.get(query_url, headers=headers)

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Endpoint error handling using HTTP status codes.
        if response.status_code == 401:
            raise APIException("You are not authenticated", 401, response.raw_body)
        elif response.status_code == 403:
            raise APIException("This action needs a valid WSSE header", 403, response.raw_body)
        elif response.status_code == 404:
            raise APIException("Resource not found", 404, response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body



    def get_regions(self,
                    country_iso_2,
                    page=None,
                    limit=None):
        """Does a GET request to /dids/location/countries/{country_iso2}/regions.

        Allow clients to get the list of available regions per country

        Args:
            country_iso_2 (string): Country ISO2
            page (int, optional): Zero based offset index for the results.
                e.g. 0 would start at the first result and 10 would start at
                the eleventh result
            limit (int, optional): Maximum number of results to return in the
                response

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/dids/location/countries/{country_iso2}/regions"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "country_iso2": country_iso_2
        })

        # Process optional query parameters
        query_parameters = {
            "page": page,
            "limit": limit
        }
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "X-Auth-Token": Configuration.x_auth_token,
            "X-Auth-Token": Configuration.x_auth_token
        }

        # Prepare the API call.
        http_request = self.http_client.get(query_url, headers=headers, query_parameters=query_parameters)

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Endpoint error handling using HTTP status codes.
        if response.status_code == 401:
            raise APIException("You are not authenticated", 401, response.raw_body)
        elif response.status_code == 403:
            raise APIException("This action needs a valid WSSE header", 403, response.raw_body)
        elif response.status_code == 404:
            raise APIException("Resource not found", 404, response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body



    def get_regions_by_handle(self,
                              country_iso_2,
                              region_handle):
        """Does a GET request to /dids/location/countries/{country_iso2}/regions/{region_handle}.

        Allow clients to get a specific region for a specific country

        Args:
            country_iso_2 (string): Country ISO2
            region_handle (string): Region handle

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/dids/location/countries/{country_iso2}/regions/{region_handle}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "country_iso2": country_iso_2,
            "region_handle": region_handle
        })
        
        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "X-Auth-Token": Configuration.x_auth_token,
            "X-Auth-Token": Configuration.x_auth_token
        }

        # Prepare the API call.
        http_request = self.http_client.get(query_url, headers=headers)

        # Invoke the API call  to fetch the response.
        response = self.http_client.execute_as_string(http_request);

        # Endpoint error handling using HTTP status codes.
        if response.status_code == 401:
            raise APIException("You are not authenticated", 401, response.raw_body)
        elif response.status_code == 403:
            raise APIException("This action needs a valid WSSE header", 403, response.raw_body)
        elif response.status_code == 404:
            raise APIException("Resource not found", 404, response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(response)    

        return response.raw_body


