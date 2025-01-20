

import math 

#TRIGONOMIC FUNCTION ---------

def find_function(fun_name, x):
    if fun_name.lower().strip() == "sin" or "sine":
        print(math.degrees(math.sin(x)))
    elif fun_name.lower().strip() == "tan" or "tangent":
        print(math.degrees(math.tan(x)))
    elif fun_name.lower().strip() == "cos" or "cosine":
        print(math.degrees(math.cos(x)))
    elif fun_name.lower().strip() == "cosec" or "cosecant":
        print(math.degrees(math.asin(x)))
    elif fun_name.lower().strip() == "sec" or "secant":
        print(math.degrees(math.acos(x)))
    elif fun_name.lower().strip() == "cot" or "cotangent":
        print(math.degrees(math.atan(x)))



print(find_function("sin", 12))
print(find_function("tan", 12))
print(find_function("cos", 12))


# Trigonomic functions
#f = 1
#print(math.degrees(math.tan(f)))
#print(math.degrees(math.sin(f)))
#print(math.degrees(math.cos(f)))

# Inverse Trigonomic functions

#print(math.degrees(math.atan(f)))
#print(math.degrees(math.asin(f)))
#print(math.degrees(math.acos(f)))