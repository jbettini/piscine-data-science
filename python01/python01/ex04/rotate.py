import array
import matplotlib as mpl
import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np

mpl.rcParams['toolbar'] = 'None'


def print_channel(img: array):
    '''
Prints the first three and last three rows of the first channel of an image.
Used to quickly visualize part of the image array content.
'''
    for row in img[:3]:
        print(f"[{row[0]}]")
    print("...")
    for row in img[-3:]:
        print(f"[{row[0]}]")


def ft_transpose(img: array):
    '''
Rotates the image by 90 degrees clockwise.
'''
    rows = len(img)
    cols = len(img)
    new = np.zeros((rows, cols))
    for idx, row in enumerate(img):
        for idx2, pix in enumerate(row):
            new[idx2][idx] = pix
    return new


def rotate(path: str):
    '''
Loads an image, slices a region, and displays,
on the first channel in grayscale with 90 degrees clockwise.
'''
    img = ft_load(path)
    new = img[100:500, 450:850, 0]
    print(f"The shape of image is: \
({len(new)}, {len(new[0])}, 1) or {new.shape}")
    print_channel(new)
    # print(new)
    new = ft_transpose(new)
    print(f"New shape after Transpose: {new.shape}")
    print(f"[{new[0][:3].astype(int)} ... \
{new[0][-3:].astype(int)}\n...\n{new[-1][:3].astype(int)} \
... {new[-1][-3:].astype(int)}]")
    # print(new)
    plt.imshow(new, cmap=plt.cm.gray)
    plt.show()


def main():
    '''
Example usage of zoom function
'''
    try:
        rotate("../Ressources/animal.jpeg")
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
