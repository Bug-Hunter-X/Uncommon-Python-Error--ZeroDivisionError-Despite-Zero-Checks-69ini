def function_with_uncommon_error_fixed(a, b):
    if b == 0:
        if a == 0:
            return 0 # Or raise a more informative exception, depending on your needs.
        else:
            return float('inf') # Or raise an exception
    else:
        return a / b

result = function_with_uncommon_error_fixed(5, 0) 
print(result) # Output: inf
result = function_with_uncommon_error_fixed(0, 0)
print(result) # Output: 0