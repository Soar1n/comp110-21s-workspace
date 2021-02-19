""" test"""


def a(b: str, c: int ) -> float:
    c = c + 2 
    print("func c", c)
    b = str(c) + b
    print("func b", b)
    abc: float = float(b)
    return abc


b: int = 10
print("int b", b)
c: str = "3"
print("str c", c)


print(a(c,b))