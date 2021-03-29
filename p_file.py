from ctypes import *

# 2.) entire file path of so file
# To get file path on mac os, right click file ->option key press -> mouse click copy "file" as Pathname. Copy pathname into 
# or use "./fileName.so"
so_file = "/Users/felixchen/Desktop/USING_C_FUNC_PYTHON/c_file.so"
c_functions = CDLL(so_file)

#class ctypes.CDLL
print(type(c_functions))


#all ctypes return int. Need to change function type manually
c_functions.printDb.restype = c_double
c_functions.slope.restype = c_double
c_functions.probability.restype = c_double

#format to call c functions: {CDLL_instance}.{function_name}({function_parameters}).
#format to call c functions (non int param): {CDLL_instance}.{function_name}({c_type({function_parameters})}).

#int
print(c_functions.factorial(5))
print(c_functions.square(10))

#double
print(c_functions.printDb(c_double(3.0)))
print(c_functions.slope(1,4,1,5))
print(c_functions.probability(20,10))


