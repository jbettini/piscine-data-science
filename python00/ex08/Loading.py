import sys


def ft_tqdm(lst: range) -> None:
    """
Displays a progress bar while iterating over a range.
"""
    total = len(lst)
    for progress in range(1, total + 1):
        per = progress * 100 / total
        bar = chr(0x2588) * int(per / 2)
        sys.stdout.write(f"\r{per:3.0f}%|{bar:50}| {progress}/{total}")
        sys.stdout.flush()
        yield


def main():
    """
Tests for ft_tqdm
"""
    try:
        for elem in ft_tqdm(range(3330)):
            pass
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
