import array
import matplotlib as mpl
import matplotlib.pyplot as plt
from load_image import ft_load

mpl.rcParams['toolbar'] = 'None'


def ft_original(img: array):
    '''
Display the image received.
'''
    plt.axis('off')
    plt.imshow(img)
    plt.show()


def ft_red(img: array):
    '''
Displays the image with only the red channel active.
'''
    copy = img.copy()
    copy[:, :, 1] = copy[:, :, 2] = 0
    plt.axis('off')
    plt.imshow(copy)
    plt.show()


def ft_blue(img: array):
    '''
Displays the image with only the blue channel active.
'''
    copy = img.copy()
    copy[:, :, 0] = copy[:, :, 1] = 0
    plt.axis('off')
    plt.imshow(copy)
    plt.show()


def ft_green(img: array):
    '''
Displays the image with only the green channel active.
'''
    copy = img.copy()
    copy[:, :, 0] = copy[:, :, 2] = 0
    plt.axis('off')
    plt.imshow(copy)
    plt.show()


def ft_grey(img: array):
    '''
Converts the image to grayscale using weighted RGB coefficients.
'''
    copy = img.copy()
    gray = 0.299 * copy[:, :, 0] + 0.587 \
        * copy[:, :, 1] + 0.114 * copy[:, :, 2]
    copy[:, :, 0] = copy[:, :, 1] = copy[:, :, 2] = gray
    plt.axis('off')
    plt.imshow(copy)
    plt.show()


def ft_invert(img: array):
    '''
Inverts the color of the image received.
'''
    copy = img.copy()
    copy[:, :, 0] = 255 - copy[:, :, 0]
    copy[:, :, 1] = 255 - copy[:, :, 1]
    copy[:, :, 2] = 255 - copy[:, :, 2]
    plt.axis('off')
    plt.imshow(copy)
    plt.show()


def main():
    '''
Example usage of zoom function
'''
    try:
        img = ft_load("../Ressources/landscape.jpeg")
        ft_original(img)
        ft_red(img)
        ft_blue(img)
        ft_green(img)
        ft_grey(img)
        ft_invert(img)
        print(ft_invert.__doc__)
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
