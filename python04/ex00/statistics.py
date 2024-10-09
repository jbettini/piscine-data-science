from typing import Any


def mean(nums: list) -> float:
    """Return the mean of a list of numbers."""
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)


def median(nums: list) -> float:
    """Return the median of a list of numbers."""
    median = int(len(nums) / 2)
    sorted_nums = sorted(nums)
    if len(nums) % 2:
        return sorted_nums[median]
    else:
        return (sorted_nums[median] + sorted_nums[median - 1]) / 2


def fquart(nums: list):
    """Return the first quartile of a list of numbers."""
    if len(nums) < 4:
        return
    sorted_nums = sorted(nums)
    fq = sorted_nums[int(len(nums) / 4)]
    return fq


def lquart(nums: list):
    """Return the last quartile of a list of numbers."""
    if len(nums) < 4:
        return
    sorted_nums = sorted(nums)
    if len(nums) % 2:
        fq = sorted_nums[int(len(nums) / 4 * 3)]
    elif len(nums) != 4:
        fq = sorted_nums[(int(len(nums) / 4 * 3))]
    else:
        fq = sorted_nums[(int(len(nums) / 4 * 3)) - 1]
    return fq


def stdvar(nums: list, ret: str):
    """Return the variance of the Standard Deviation of a list of numbers."""
    m = mean(nums)
    total = 0
    for i in nums:
        total += abs((i - m)) ** 2
    total = total / len(nums)
    if ret == "std":
        return total ** 0.5
    return total


def check_args(*args: Any) -> bool:
    """Check if args from ft_statistic is valid"""
    if not args:
        return False
    for n in args:
        if not isinstance(n, (int, float)):
            return False
    return True


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    if not check_args(*args):
        print("ERROR\n" * len(kwargs))
        return None

    numbers = [float(n) for n in args]
    for key, value in kwargs.items():
        match value:
            case "mean":
                print(f"mean : {mean(numbers)}")
            case "median":
                print(f"median : {median(numbers)}")
            case "quartile":
                print(f"quartile : [{fquart(numbers)}, {lquart(numbers)}]")
            case "std":
                print(f"std : {stdvar(numbers, value)}")
            case "var":
                print(f"var : {stdvar(numbers, value)}")
            case _:
                print("")


def main():
    """Example usage of statistic function"""
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean")
        ft_statistics(1, 42, 360, 11, 64, toto="median")
        ft_statistics(1, 42, 360, 11, 64, toto="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
