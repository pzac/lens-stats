import glob
import exif_parser

def get_files():
    "Returns an array of matching filenames"
    files = glob.glob("**/*.jpg")
    return files

def run():
    data = {}
    files = get_files()
    for file in files:
        focal = exif_parser.focal_length(file)
        if data.get(focal):
            data[focal] = data[focal] + 1
        else:
            data[focal] = 1
    items = sorted([(x, data[x]) for x in data])
    for i in items:
        focal, items = i
        if focal != None:
            focal = "%smm" % focal
        print "%s:\t%s" % (focal, items)

run()
