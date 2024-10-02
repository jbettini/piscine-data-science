import array
import imageio.v2 as iio


def ft_load(path: str) -> array:
    """
Loads an image from the given path and returns it as an array.
Raises an AssertionError for file-related issues.
"""
    try:
        img = iio.imread(path)
        print(f"The shape of image is: {img.shape}\n{img}")
        return img
    except FileNotFoundError:
        raise AssertionError(f"Error: The file '{path}' was not found.")
    except PermissionError:
        raise AssertionError(f"Error: Permission denied \
            when trying to access '{path}'.")
    except Exception as e:
        raise AssertionError(f"An unexpected error occurred: {str(e)}")
