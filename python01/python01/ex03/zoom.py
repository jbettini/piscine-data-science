import array
import matplotlib as mpl
import matplotlib.pyplot as plt
from load_image import ft_load

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


def zoom(path: str):
    '''
Loads an image, slices a region, and displays,
a zoom on the first channel in grayscale.
'''
    img = ft_load(path)
    print(f"The shape of image is: {img.shape}")
    print_channel(img)
    # print(img)
    new = img[100:500, 450:850, 0]
    print(f"The shape after slicing : \
({len(new)}, {len(new[0])}, 1) or {new.shape}")
    # print(new)
    print_channel(new)
    plt.imshow(new, cmap=plt.cm.gray)
    plt.show()


def main():
    '''
Example usage of zoom function
'''
    try:
        zoom("../Ressources/animal.jpeg")
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
