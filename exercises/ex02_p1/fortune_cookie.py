"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730331250"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(str(fortune_cookie()))
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """This function gives fortunes."""
    fortune_cookie = randint(1, 4)
    
    if fortune_cookie == 1:
        return str("A beautiful, smart, and loving person will be coming into your life.")
    else: 
        if fortune_cookie == 2:
            return str("Your life will be happy and peaceful.")
        else:
            if fortune_cookie == 3: 
                return str("Soon life will become more interesting.")
            else:
                return str("Your life will be happy and peaceful young one.")
                if fortune_cookie == 4:
                    return str("Soon life will become more interesting young one.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
