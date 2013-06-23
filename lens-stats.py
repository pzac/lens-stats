import sys
import glob
import exif_parser

def get_files(root = None):
    "Returns an array of matching filenames"
    if root:
        print "Parsing files in %s" % root
        selector = "%s/**/*.jpg" % root
    else:
        selector = "**/*.jpg"

    files = glob.glob(selector)
    print "Total files: %s" % len(files)
    return files

def run():
    data = {}
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = None
    files = get_files(root)
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
