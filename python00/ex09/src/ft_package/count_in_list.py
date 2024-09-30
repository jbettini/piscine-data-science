def count_in_list(lst: list, occurence: str) -> int:
    '''
Counts how many times a specific element appears in a list.
'''
    i = 0
    for elements in lst:
        if elements == occurence:
            i += 1
    return i


def main():
    '''
Test count_list function, output must be 2
'''
    print(count_in_list(["toto", "tata", "toto"], "toto"))


if __name__ == "__main__":
    main()
