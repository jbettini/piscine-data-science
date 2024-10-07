from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""
    @abstractmethod
    def __init__(self, name: str, is_alive: bool = True):
        """"Initialize a character with a name and alive status."""
        self.first_name = name
        self.is_alive = is_alive

    def is_alive(self):
        """Return True if the character is alive, False otherwise."""
        return self.is_alive

    def die(self):
        """Change the character's status to dead."""
        self.is_alive = False


class Stark(Character):
    """Represents a member of House Stark in the Game of Thrones universe."""
    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Stark character with a name and alive status."""
        super().__init__(name, is_alive)


def main():
    """Tester for Character and stark class"""
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        # hodor = Character("hodor")
    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
