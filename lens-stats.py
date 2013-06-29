import os
import sys
from exif_parser import ExifParser
import re

def get_files(root = None):
    "Returns an array of matching filenames"
    if root == None:
        root = "."

    items = []
    for dir_root, dirs, files in os.walk(root):
        for file in files:
            full_path = os.path.join(dir_root, file)
            if re.match('.*(jpg|JPG)$', file):
                items.append(full_path)

    print "Parsed files: %s" % len(items)
    return items

def show_output(data):
    "sorted by lens focal"
    items = sorted([(x, data[x]) for x in data])
    for i in items:
        focal, items = i
        print "%s:\t%s" % (focal, items)

def show_grouped_output(data):
    "grouped by camera and sorted by lens focal"
    cameras = {}
    for datum, ct in data.items():
        focal, camera = datum
        if cameras.get(camera):
            cameras[camera][focal] = ct
        else:
            cameras[camera] = {focal: ct}

    for camera, focals in cameras.items():
        if camera == None:
            label = 'N/A'
        else:
            label = camera

        print ""
        print label
        print "-" * len(label)
        totals = {}
        for focal in sorted(focals.keys()):
            if focal != None:
                focal_label = '%dmm' % focal
            else:
                focal_label = 'N/A'
            print "%s:\t%s" % (focal_label, focals[focal])

def run():
    data = {}
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = None
    files = get_files(root)
    for file in files:
        exif = ExifParser(file)
        focal = exif.focal_length()
        camera = exif.camera()
        combo = (focal, camera)
        if data.get(combo):
            data[combo] = data[combo] + 1
        else:
            data[combo] = 1
    show_grouped_output(data)

if __name__ == '__main__':
    run()
