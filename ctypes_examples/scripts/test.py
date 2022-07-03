import os
from ctypes import *
from unittest import result

dir_name = os.path.dirname(os.path.realpath(__file__))
lib_path = dir_name + "/TestLib.dll"
lib = CDLL(lib_path)

class SomeStructure(Structure):
    _fields_ = [('i',c_int),('c',c_char),('s',c_char_p)]

lib.someFunction.restype = c_double
lib.someFunction.argtypes = [POINTER(SomeStructure)]

s_obj = SomeStructure(3,'q',b"hello world")
result = lib.someFunction(byref(s_obj))
print("result: %s, new value for text: %s" %(result,str(s_obj.s)))
