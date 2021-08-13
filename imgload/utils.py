from PIL import Image
from django.conf import settings

def resize_by_width():
    basewidth = 300
    img = Image.open('fullsized_image.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.NEAREST)
    img.save('resized_image.jpg')


def resize_by_height():
    baseheight = 560
    img = Image.open('fullsized_image.jpg')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.NEAREST)
    img.save('resized_image.jpg')


def resize1(width, height, name):
    img = Image.open(settings.MEDIA_ROOT + '\\' + name)
    proportions = img.size[0] / img.size[1]
    requested = width/height
    if requested != proportions:
        height = width / proportions
    img = img.resize((int(width), int(height)), Image.NEAREST)
    proportions = img.size[0] / img.size[1]
    name = name[:7] + 'resized_' + name[7:]
    #img.save(settings.MEDIA_ROOT + '\\' + name)
    return settings.MEDIA_ROOT + '\\' + name


