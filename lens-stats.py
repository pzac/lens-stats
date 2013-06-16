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

def focal_length(exif_data):
    values = exif_data.get('FocalLength')
    if values:
        a, b = values
        return a / b
    else:
      return None

def run():
    files = get_files()
    for file in files:
        exif_data = get_exif_data(file)
        focal = focal_length(exif_data)
        if focal:
            print "{0} : {1}mm".format(file, focal)
        else:
            print "{0} : N/A".format(file)

run()
