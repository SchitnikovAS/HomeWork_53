import inspect
from pprint import pprint
import sys
import random


def introspection_info(obj):
    dict_ = {}
    dict_['type'] = type(obj).__name__
    dict_['attributes'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    dict_['methods'] = [x for x in dir(obj) if inspect.ismethod(getattr(obj, x))]
    dict_['classes'] = [x for x in dir(obj) if inspect.isclass(getattr(obj, x))]
    dict_['module'] = introspection_info.__module__
    dict_['size'] = sys.getsizeof(obj)
    return dict_


number_info = introspection_info(random)
pprint(number_info)
