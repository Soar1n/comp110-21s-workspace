"""fake"""

def f(x: int, y: int) -> int:
    """weird function"""
    if x + y >10:
        print("howdy!")
        return x
    else:
            return x + y
    

def g(x: int) -> int:
    """another weird."""
    if x % 2 == 0:
        print("it's even")
        x = x + 1
    else:
        x = x * 2 
    return x 
    

def bar(x: int, y: int) -> int:
    """weird"""
    if x > y:
        print("woohoo!")
        x = x * y
        if x % 2 ==0:
            x = x + 1 
            return x 
    else:
        print("110")
        x = x + 5 
    return x
    

print(bar(g(8), f(3,4)))
