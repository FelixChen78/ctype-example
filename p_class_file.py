#option 1

# from ctypes import *
# lib = CDLL("./c_struct_file.so")

# class c_struct(Structure):
#     _fields_ = [
#         ('i', c_int),
#         ('c', c_char),
#         ('s', c_char_p)
#     ]

# lib.c_function.restype = c_double
# lib.c_function.argtypes = [ POINTER(c_struct) ]

# s_obj = c_struct(3, 'q', b("hello world"))
# result = lib.c_function(byref(s_obj))

# print("result: %s, new vlaue for text: %s" %
# (result, str(s_obj.s)) )


#option 2

# from basic import *
# from ctypes import *

# lib = CDLL("./c_struct_file.so")
# decorateFunction(lib)
# s_obj = c_struct(3, 'q', "hello world")
# result = lib.c_function(byref(s_obj))
# print("result: %s, new value for text: %s" % (result, str(s_obj.s)))

#option 3

# from CTypeGen import generate, PythonType


# generate(["./c_struct_file.so"], "p_class_file.py", [PythonType("c_struct_file")], ["c_function"])


