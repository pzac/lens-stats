import sys
import glob
import exif_parser

def get_files(root = None):
    "Returns an array of matching filenames"
    extensions = ['JPG', 'jpg']
    files = []
    for ext in extensions:
        files = files + get_files_with_extension(root, ext)
    if root:
        print "Parsing files in %s" % root
    print "Total files: %s" % len(files)
    return files

def get_files_with_extension(root, ext):
    if root:
      selector = "%s/**/*.%s" % (root, ext)
    else:
      selector = "**/*.%s" % ext
    return glob.glob(selector)

def run():
    data = {}
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = None
    files = get_files(root)
    for file in files:
        focal = exif_parser.focal_length(file)
        print "%s: %s" % (file, focal)
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
