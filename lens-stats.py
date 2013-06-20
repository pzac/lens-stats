import glob
import photo_analyzer

def get_files():
    "Returns an array of matching filenames"
    files = glob.glob("**/*.jpg")
    return files

def run():
    files = get_files()
    for file in files:
        exif_data = photo_analyzer.get_exif_data(file)
        focal = photo_analyzer.focal_length(exif_data)
        if focal:
            print "{0} : {1}mm".format(file, focal)
        else:
            print "{0} : N/A".format(file)

run()
