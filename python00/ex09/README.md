# ft_package

A simple Python package to count occurrences of an element in a list.

## Installation

First build the package :

'''
python -m build
'''

Install the package :

-   pip install ./dist/ft_package-0.0.1.tar.gz
-   pip install ./dist/ft_package-0.0.1-py3-none-any.whl

## Function

-   count_in_list(lst: list, occurence: str) -> int: Returns how many times occurence appears in lst.

### Usage

'''
    from ft_package import count_in_list

    print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
'''

### Appendix

To show package iformation :

'''
python show -v ft_package
'''