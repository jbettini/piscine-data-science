from S1E9 import Character


class Baratheon(Character):
    """Represents a member of Baratheon House in Game of Thrones."""
    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Baratheon character with a name and alive status."""
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Return the same string representation as __str__."""
        return self.__str__()


class Lannister(Character):
    """Represents a member of Lannister House in Game of Thrones."""
    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Lannister character with a name and alive status."""
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Return a string representation of the Lannister character."""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Return the same string representation as __str__."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        """Create and return a new Lannister character."""
        return cls(name, is_alive)


def main():
    """Tester for this exercice."""
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {(Jaine.first_name, type(Jaine).__name__)}, "
              f"Alive : {Jaine.is_alive}")
    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
