from typing import Callable, Generator, Iterable, T, Optional


def ft_filter(func: Optional[Callable[[T], bool]], it: Iterable[T]) \
                                                -> Generator[T, None, None]:
    '''
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
'''
    if func is None:
        return [x for x in it if x]
    return [x for x in it if func(x)]
