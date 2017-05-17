def min(*args,**kwargs):
    #key = kwargs.get("key", None)
    minimum = None
    iterables = args[:] if len(args)>1 else args[0]
    key = kwargs.get('key',lambda x: x)
    for i in iterables:
        if minimum == None:
            minimum = i
        minimum = i if key(i) < key(minimum) else minimum
    return minimum          



def max(*args, **kwargs):
    #key = kwargs.get("key", None)
    iterables = args[:] if len(args)>1 else args[0]
    key = kwargs.get('key',lambda x: x)
    maximum = None
    for i in iterables:
        if maximum == None:
            maximum = i
        maximum = i if key(i) > key(maximum) else maximum
    return maximum          


if __name__ == '__main__':
    
#    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert min([1, 2, 0, 3, 4]) == 0, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
