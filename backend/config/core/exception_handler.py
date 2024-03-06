
import collections
from rest_framework import exceptions
from rest_framework.views import exception_handler
from django.db import IntegrityError
from rest_framework import serializers

import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)



def flatten(d, parent_key="", sep="__"):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def remove_snake_case(val):
    return " ".join(val.split("_")).title()


def custom_exception_handler(exc, context):

    """Custom Exception Handler that returns message for end user and errors for developers

    Args:
        exc ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__

    if isinstance(exc, exceptions.APIException):
        try:
            # print("------- exec detail is -------",exc.detail)
            if isinstance(exc.detail, list):
                # print("------- exec detail is list -------")
                data = {}
                data["errors"] = response.data
                response.data = data
                response.data["message"] = exc.detail[0]
            elif isinstance(exc.detail, dict):
                # print("------- exec detail is dict -------")
                data = {}
                data["errors"] = response.data
                response.data = data
                exc.detail = flatten(exc.detail)
                # print("flatten data is ",exc.detail)
                

                exc_keys = list(exc.detail.keys())
                # print("keys are ",exc_keys) 
                exc_values = list(exc.detail.values())
                # print("Validation Error is : ",exc_values)
                message = {}
                if len(exc_keys) > 0 and len(exc_values) > 0 and len(exc_values[0]) > 0:
                    exc_values[0][0] =  exc_values[0][0].replace('"',"'")
                    if exc_values[0][0] == "This field is required.":
                        key = remove_snake_case(exc_keys[0])
                        message = f"{key} is required."
                    else:
                        message = f"{exc_values[0][0]}"
                    if isinstance(exc_values[0], str):
                        message = f"{exc_values[0]}"
                        if exc_values[0] == "Given token not valid for any token type":
                            message = "Token is invalid or expired"
                # else:
                # print("Detail Error is ",exc.detail)
                # print("---- message is ------ ",message)
                response.data["message"] = f"{message}"
            else:
                response.data["message"] = exc.detail
        except Exception as e:
       
            response.data["message"] = exc.default_detail
    # elif isinstance(exception, IntegrityError):
    #         raise exceptions.ValidationError("A related object already exists.")

    elif exception_class == "Http404":
        response.data["message"] = "Not Found."
    return response
