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
                # PIL.ExifTags.TAGS lacks the FocalLengthIn35Mm definition
                ret['FocalLengthIn35Mm'] = exifinfo.get(41989)
    except IOError:
        return 'Error'
    return ret

def extract_focal_length(exif_data):
    "Returns the focal length from the EXIF data hash"
    focal_length_in_35_mm = exif_data.get('FocalLengthIn35Mm')
    if focal_length_in_35_mm:
        return focal_length_in_35_mm
    values = exif_data.get('FocalLength')
    if values:
        a, b = values
        if b == 0:
            return a
        else:
            return a / b
    else:
      return None

def focal_length(fname):
    "Returns the focal length for a given filename"
    exif = get_exif_data(fname)
    if exif == 'Error':
        return 'Error'
    else:
        return extract_focal_length(exif)
