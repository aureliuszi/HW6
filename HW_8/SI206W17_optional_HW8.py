import unittest # just in case
import json # just in case
from PIL import Image, ImageFilter, ImageColor, ImageFile, ImagePalette, ImageMorph, ImageFilter
import random
# tons of options, and OK to add more: http://pillow.readthedocs.io/en/3.4.x/index.html to import directly...
import glob, os # tools to help you deal with files, in standard library, not necessary

## SI 206 Winter 2017
## Optional HW: Building an Album

## Comment with your name:
## Anyone you worked with on this assignment:

## The score for this assignment can replace your lowest score on HW 2 - HW 7. 
## It is due THURSDAY, APRIL 13 at 11:59 PM and cannot be submitted late, because it is due so soon before the end of classes.

#########

## Your goal for this assignment is to use image manipulation code to create a photo album and manipulate it!

## PART 1: Define a class PhotoAlbum, which will represent one Photo Album.
# It should accept, at minimum, a list of strings, which each represent filenames.

## Creating an instance won't work if the file names don't exist, and won't work if the fnames_lst input is empty.
# There must be at least one photo file, and all file names in that list must represent real image files.

## PART 2: The class should contain at least 6 additional methods which allow you to manipulate either
# one particular image in the album or all of the images in the album at once.

## It also might be nice to include a string method that represents a printed (non-image)
# representation of this photo album data...

## At least one of the methods you create MUST show either one of the images
# (per input specification, e.g. invoke a method to say "show me the first one" or "show me the image at index 4"...)
# or show ALL of the images somehow. Everything else is up to you. Here are some suggestions/possibilities:

## A method that creates thumbnails of all the images and saves a list of them in a thumbnails instance variable
## A method that allows you to change the cover photo
## A method that allows you to blend a random set of 2 photos, or a specific set of 2 photos x
# (note that the photos must all be the same size and the same mode for this to work!)
## A method that makes all or one of the photos greyscaled and shows the first one x
## A method that allows you to pick a new size and resize one of the album images x
## A method that allows you to select part of an image, given certain input to determine what image to select from, and how much to select
## ...

## The methods you create should vary, not be exactly the same as one another with a few characters' difference.

## You can use as your references, among other things:
# http://pillow.readthedocs.io/en/3.4.x/reference/Image.html
# http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html#concept-modes

## Be careful: you're manipulating references to files, which can be tricky.
# Pay attention to what Image methods return a value, and which modify objects in place!

## After you define your class (which you should be testing out as you go to make sure everything works as you expect),
# you should create at least 2 PhotoAlbum instances with real images, beneath your class definition,
# and invoke the methods you've defined to show how they all work, including brief comments.

## You should submit your edited file to the HW8-Optional assignment, along with all of the image files you refer to/use in your sample code.

## Note that the default photo-editing programs on your computer AND PIL Image methods themselves can help with resizing/cropping as needed!

## As goes without saying, make sure all images you submit are totally in-school-sharing-appropriate or your assignment will not be accepted.
# Fine to use screenshots of e.g. astronomy pictures, flickr photos you download, famous photographs from the NYTimes you find online (though note that for some of these things it's probably most fun to work with photographs in color!)...anything you want.


# Define your PhotoAlbum class here:

image_list = ["reddit.png.png", "orchid.jpg.jpg", "funny.jpg.jpg"]
image_list_too = ["Chrysanthemum.jpg", "Jellyfish.jpg", "Desert.jpg", "Hydrangeas.jpg"]

class PhotoAlbum(list):

    def __init__(self, list):
        self.filenames = list
        self.num_files = len(list)
        self.cover_photo=self.filenames[0]

    def __str__(self):
        return str(self.filenames)

    def change_cover_photo(self,num):
        self.filenames[0], self.filenames[num] = self.filenames[num], self.filenames[0]
        self.cover_photo = self.filenames[0]

    def show_image(self,num):
        num = num - 1
        item = self.filenames[num]
        im = Image.open(item)
        im.show()

    def show_random_image(self):
        k = random.randrange(0,(len(self.filenames)))
        print (k)
        item = self.filenames[k]
        im = Image.open(item)
        im.show()

    def rotate_45(self):
        for item in self.filenames:
            im = Image.open(item)
            im.rotate(45).show()

    def rotate(self,num):
        for item in self.filenames:
            im = Image.open(item)
            im.rotate(num).show()

    def create_composite(self,n=0,m=1):
        im1=Image.open(self.filenames[n])
        im2=Image.open(self.filenames[m])
        im1 = im1.crop(box=(100, 200, 300, 500))
        im2 = im2.crop(box=(100, 200, 300, 500))
        Image.blend(im1, im2, 0.5).show()

    def black_and_white(self):
        for item in self.filenames:
            im = Image.open(item)
            im.convert(mode='L', matrix=None, dither=None, palette=0, colors=256).show()
            im.convert(mode='L', matrix=None, dither=None, palette=0, colors=256).save("bw"+item)

    def filter_BLUR(self, num = 0):
        im1=Image.open(self.filenames[num])
        im1.filter(ImageFilter.BLUR).show()

    def filter_CONTOUR(self, num = 0):
        im1 = Image.open(self.filenames[num])
        im1.filter(ImageFilter.CONTOUR).show()


Album1 = PhotoAlbum(image_list)
Album1.rotate_45() # rotates and shows each image by 45 degrees
Album1.show_image(3) # shows the third image in the album
Album1.create_composite() # crops two images and creates a composite. defaults to the second and third image
Album1.black_and_white() # creates black and white versions of the photos and shows them. will also save them as long as not run in pycharm
Album1.change_cover_photo(2) # changes order of the images in the album, print(Album1)
# now produces [funny, orchid, reddit]; print (Album1.cover_photo) now produces funny.jpg.jpg
Album1.filter_BLUR(1)

Album2 = PhotoAlbum(image_list_too)
Album2.filter_CONTOUR() #displays image with contour filter
Album2.show_random_image() #shows random image from Album2













# Write some sample code with comments to show how your PhotoAlbum class methods work, here:




# No tests: you decide what it means for your code to work. Make sure your file runs! We won't grade code that does not run.

# And please share the cool images you come up with during the process on Piazza!
# If someone is curious how you made it happen, share the code and explain!