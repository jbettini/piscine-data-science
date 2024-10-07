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
