import os
import sys
import exif_parser
import re

def get_files(root = None):
    "Returns an array of matching filenames"
    if root == None:
        root = "."
    else:
        print "Parsing files in %s" % root

    items = []
    for dir_root, dirs, files in os.walk(root):
        for file in files:
            full_path = os.path.join(dir_root, file)
            if re.match('.*(jpg|JPG)$', file):
                items.append(full_path)

    print "Total files: %s" % len(items)
    return items

def run():
    data = {}
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = None
    files = get_files(root)
    for file in files:
        focal = exif_parser.focal_length(file)
        # print "%s: %s" % (file, focal)
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
