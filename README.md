MagicTelecomAPILib
=================
This API SDK was automatically generated by APIMATIC v2.0

This SDK uses the Requests library and will work for Python 2.6 — 3.5.

How To Configure:
=================
The generated code might need to be configured with your API credentials. To do that,
open the file "Configuration.py" and edit its contents.

How To Build: 
=============
The generated code uses Python libraries named Requests and Jsonpickle. 

PIP is a popular tool for managing python packages[1].
To resolve these packages:
1) From terminal/cmd navigate to the root directory
2) Invoke 'pip install -r requirements.txt'

Note: You will need internet access to resolve these dependencies.

How To Use:
===========
The following shows how to make invoke the UsersController controller.
It is also shown in [2].

    1. Create a "UsersControllerTest.py" file in the root directory.
    2. Add the following import statement 
        'from MagicTelecomAPILib.Controllers.UsersController import *'
    3. Create a new instance using 'controller = UsersController()'
    4. Invoke an endpoint with the appropriate parameters, for example
        'response = controller.get_authentications(<required parameters if any>)'
    5. "response" will now be an object of type Dynamic.

[1] PIP - https://pip.pypa.io

[2] from __future__ import print_function
	from MagicTelecomAPILib.Controllers.UsersController import *

	controller = UsersController()
    response = controller.get_authentications()

    print (response)