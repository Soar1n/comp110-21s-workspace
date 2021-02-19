""" scream and shout"""


def main() -> None:
    print(please(3))
    return None


def free(x: int) -> int:
    return x + 2


def please(x: int) -> str:
    b: str = str( britney(x))
    f: str = str(free(x))
    return f + b


def britney(x: int) -> float:
    return x / 2
    


if __name__ == "__main__":
    main()
