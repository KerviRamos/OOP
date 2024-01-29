""" Constructor Examples """
#!usr/bin/env python3


class SoccerBall:
    """Instantiation Process - Execution Order"""

    def __new__(cls, *args, **kwargs) -> "SoccerBall":
        """Step 1: Create the empty object"""
        print("Step 1: creates empty object")
        return super().__new__(cls)

    def __init__(self, size: str, color: str) -> None:
        """Step 2: Initalizes the empty object to initial state"""
        self.size: str = size
        self.color: str = color
        print("Step 2: the inital state step")

    def __repr__(self) -> str:
        """Object print represenation"""
        return (
            f"{type(self).__name__}"
            f"id: {id(self)}, data: size= {self.size}, color= {self.color}"
        )


# """ Orders of Operations with caveats """

# """ __new__() - Subclassing Immutable Built-in Types."""

# """ __new__() - Returning instance of a different class."""

# """ __new__() - Single Instance in your Classes."""

# """ __new__() - namedtuple factory functions."""


def main() -> None:
    """Driver"""
    test_instant_process = SoccerBall("Large", "White")
    print(test_instant_process)


if __name__ == "__main__":
    main()
