from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def set_eyes(self, eyes: str):
        self.eyes = eyes

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, hairs: str):
        self.hairs = hairs

    def get_hairs(self):
        return self.hairs


def main():
    """Tester for this exercice."""
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
        # print(King.mro())
    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
