def main()  -> None:
    """a"""
    choice: int = int(input())
    if choice > 2:
        if choice < 3:
            print("D")
        else:
            print("C")
    else:
        if choice !=1:
            print("B")
        else: 
            print("A")

3
if __name__ == "__main__":
    main()