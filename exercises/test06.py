"""aaa"""


def a(b: int, c: str) -> float:
    b = b + 23
    print(b)
    c = c + str(b)
    print(c)
    abc: float = float(c)
    print(abc)
    return abc


b: str = "1"
c: int = 0
print(b)
print(c)
# Hint: 
print(a(c,b))

    