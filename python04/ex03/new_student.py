import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase string as an ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with name, surname, and auto-generated fields."""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Initialize login using the first letter of name and full surname."""
        assert self.name and self.surname, \
            "Error: Name and Surname must not be empty"
        self.login = f"{self.name[0]}{self.surname}"


def main():
    """Tester for this exercice."""
    try:
        student = Student(name="Ed", surname="agle")
        print(student)
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
