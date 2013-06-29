import PIL.Image
from PIL.ExifTags import TAGS

class ExifParser:
  def __init__(self, fname):
      self.fname = fname
      self.exif_data = self.get_exif_data(fname)

  def get_exif_data(self, fname):
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

  def focal_length(self):
      "Returns the focal length from the EXIF data hash"
      focal_length_in_35_mm = self.exif_data.get('FocalLengthIn35Mm')
      if focal_length_in_35_mm:
          return focal_length_in_35_mm
      values = self.exif_data.get('FocalLength')
      if values:
          a, b = values
          if b == 0:
              return a
          else:
              return a / b
      else:
        return None

  def camera(self):
      "Returns the camera model"
      return self.exif_data.get('Model')
