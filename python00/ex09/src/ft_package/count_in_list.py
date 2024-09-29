def count_in_list(lst: list, occurence: str) -> int:
    i = 0
    for elements in lst:
        if elements == occurence:
            i += 1
    return i


def main():
    print(count_in_list(["toto", "tata", "toto"], "toto"))


if __name__ == "__main__":
    main()
