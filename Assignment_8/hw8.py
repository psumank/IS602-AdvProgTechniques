__author__ = 'Suman'

import scipy.ndimage as ndimage
import scipy.misc as spm
import Tkinter
import tkFileDialog

def load_file():
    root = Tkinter.Tk()
    root.withdraw()
    f = tkFileDialog.askopenfilename(defaultextension='.png', title="Select an image for analysis")
    return f


def save_file(img):
    root = Tkinter.Tk()
    root.withdraw()
    print 'Saving the binary file..please choose a file name....'
    try:
        f = tkFileDialog.asksaveasfilename(title="Save the binary image as ....", defaultextension='.png')
        spm.imsave(f, img)
    except KeyError:
        print 'Please select a proper file name with extension to save !'
        quit()


def processimage(inputfile, n, t = 0):
    try:
        rawimg = spm.imread(inputfile)
        img = ndimage.filters.gaussian_filter(rawimg, n)
        if t == 0:
            maskimg = img > img.mean()
        else:
            maskimg = img > t

        # Count the objects
        label_im,nr_objects = ndimage.label(maskimg)
        centers = ndimage.center_of_mass(maskimg, label_im, range(1, nr_objects+1, 1))

        print 'Number of objects in the image: %d' % nr_objects
        print 'Center of mass for each object in the image:'
        for center in centers:
            print 'x-coordinate: %f, y-coordinate: %f' % (center[0], center[1])
        save_file(maskimg)
    except IOError:
        print 'Please select proper file type (.png) for analysis.'
        quit()

if __name__ == '__main__':

    file = load_file()
    name = file.strip().split('/')
    print 'Image being analyzed: %s' % name[-1]
    if name[-1] == 'circles.png':
        processimage(file, 1.5,95)
    elif name[-1] == 'objects.png':
        processimage(file, 2.0,95)
    elif name[-1] == 'peppers.png':
        processimage(file, 2.0, 160)
    else:
        processimage(file, 1.5)