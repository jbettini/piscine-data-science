from typing import Any


def callLimit(limit: int):
    """Decorator factory to limit function calls to a specified number."""
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal limit
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter


def main():
    """Example usage of statistic function"""
    try:
        @callLimit(3)
        def f():
            print("f()")

        @callLimit(1)
        def g():
            print("g()")
        for i in range(3):
            f()
            g()
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
