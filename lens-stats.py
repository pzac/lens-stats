import glob
import PIL.Image

from PIL.ExifTags import TAGS

def get_exif_data(fname):
    "Get embedded EXIF data from image file."
    ret = {}
    try:
        img = PIL.Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print 'IOERROR ' + fname
    return ret

def get_files():
    "Returns an array of matching filenames"
    files = glob.glob("**/*.jpg")
    return files

def run():
    files = get_files()
    for file in files:
        print get_exif_data(file)

run()
