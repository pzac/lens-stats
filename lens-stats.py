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
        focal, camera, iso, lens = datum
        
        groupField = focal

        if sys.argv[1] == "iso":
            groupField = iso
        elif sys.argv[1] == "lens":
            groupField = lens

        if cameras.get(camera):
            cameras[camera][groupField] = ct
        else:
            cameras[camera] = {groupField: ct}

    for camera, exif in cameras.items():
        if camera == None:
            label = 'N/A'
        else:
            label = camera

        print ""
        print label
        print "-" * len(label)
        totals = {}
        for groupField in sorted(exif.keys()):
            if groupField != None:
                exiflabel = groupField
            else:
                exiflabel = 'N/A'
            print "%s:\t%s" % (exiflabel, exif[groupField])

def run():
    data = {}
    if len(sys.argv) > 2:
        root = sys.argv[2]
    else:
        root = None
    files = get_files(root)
    for file in files:
        exif = ExifParser(file)
        focal = exif.focal_length()
        camera = exif.camera()
        iso = exif.iso()
        lens = exif.lens()
        combo = (focal, camera, iso, lens)
        if data.get(combo):
            data[combo] = data[combo] + 1
        else:
            data[combo] = 1
    show_grouped_output(data)

if __name__ == '__main__':
    run()
