import glob
import exif_parser

def get_files():
    "Returns an array of matching filenames"
    files = glob.glob("**/*.jpg")
    return files

def run():
    files = get_files()
    for file in files:
        focal = exif_parser.focal_length(file)
        if focal:
            print "{0} : {1}mm".format(file, focal)
        else:
            print "{0} : N/A".format(file)

run()
