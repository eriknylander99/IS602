__author__ = 'Erik Nylander'

import scipy.ndimage as ndimage
import scipy.misc as misc
import Tkinter
import tkFileDialog


def get_file():
    root = Tkinter.Tk()
    root.withdraw()
    print 'Opening File'
    f = tkFileDialog.askopenfilename(defaultextension='.png')
    return f


def save_file(img):
    root = Tkinter.Tk()
    root.withdraw()
    print 'Saving File'
    f = tkFileDialog.asksaveasfilename()
    try:
        misc.imsave(f, img)
    except KeyError:
        print 'No filename selected to save the output image.'
        print 'Exiting the program.'
        quit()


def threshold(filename, n, t=-1):
    try:
        raw = misc.imread(filename)
        img = ndimage.filters.gaussian_filter(raw, n)
        if t == -1:
            mask = img > img.mean()
        else:
            mask = img > t
        label_im, nb_labels = ndimage.label(mask)
        coms = ndimage.center_of_mass(mask, label_im, range(1, nb_labels+1))
        print 'Number of objects in the image: %d' % nb_labels
        print 'Centers of mass for each object in the image:'
        for com in coms:
            print 'x-coordinate: %f, y-coordinate: %f' % (com[0], com[1])
        save_file(mask)
    except IOError:
        print 'Must select an appropriate file type (.png) to be analyzed.'
        print 'Exiting the program.'
        quit()


if __name__ == '__main__':
    image_file = get_file()
    name = image_file.strip().split('/')
    print 'Image to be analyzed: %s' % name[-1]
    if name[-1] == 'circles.png':
        threshold(image_file, 1.5, 90)
    elif name[-1] == 'objects.png':
        threshold(image_file, 2.5, 100)
    elif name[-1] == 'peppers.png':
        threshold(image_file, 3, 150) #150
    else:
        threshold(image_file, 1.5)