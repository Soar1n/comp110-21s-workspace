from random import randint
 
 
def main() -> None:
	print("x")
	print(function1())
	print("y")
 
def function1() -> str:
    """Dumb func."""

    function1 = randint(1, 4)

    if function1 == 1:
        return "You smell."
    else:
        if function1== 2:
            return "You stink"
        else:
            if function1== 3: 
                return "You smell good"
            else:
               	 return "You don’t smell"
               	 if function1== 4:
                   	return "You might smell"
 

if __name__ == "__main__":
    main()
