def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # This will cause an error if the function is called with a=0 and b is an object that doesn't support addition
    return a + b

result = function_with_uncommon_error(0, [1, 2, 3])  # This will work because lists can be added to
print(result)

result2 = function_with_uncommon_error(0, {'a': 1, 'b': 2})  # This will cause a TypeError
print(result2)