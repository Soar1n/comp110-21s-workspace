


def main() -> None:
    """aa"""
    foo: bool = True
    bar: int = 11
    baz(not foo, bar)


def baz(my_bool: bool, x: int) -> int:
    """gang"""
    y: int = x
    if my_bool:
        y = y + 1 
    else:
        y = y - 1
    print(y-1)
    return fun(y, my_bool)


def fun(foo: int, bar: bool) -> int:
    """aaa"""
    if bar:
        return foo - 1
    else:
        return foo + 1 


if __name__ == "__main__":
    main()