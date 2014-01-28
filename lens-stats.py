import os
import sys
from exif_parser import ExifParser
import re
import argparse

def get_files(root = None):
    "Returns an array of the JPG files"
    if root == None:
        root = "."
    items = []
    for dir_root, dirs, files in os.walk(root):
        for file in files:
            full_path = os.path.join(dir_root, file)
            if re.match('.*(jpg|JPG)$', file):
                items.append(full_path)
    return items

def sort_by_key(list):
    "Internal sorting function"
    return list[1]

def show_output(data):
    for item in sorted(data, key=sort_by_key):
        print "%s:\t%s" % (item[2], data[item])

def show_grouped_output(data):
    cameras = {}
    for item, value in data.items():
        if cameras.get(item[0]):
            cameras[item[0]][item] = value
        else:
            cameras[item[0]] = {item: value}
    for camera, items in cameras.items():
        print camera
        print "=" * len(camera)
        show_output(items)
        print "\n"

def extract_data(files, args):
    data = {}

    for file in files:
        exif = ExifParser(file)

        if args.lens:
            key = exif.lens()
            if key:
              label = key
            else:
              label = 'N/A'
        elif args.iso:
            key = exif.iso()
            if key:
              label = "ISO%s" % key
            else:
              label = 'N/A'
        else:
            key = exif.focal_length()
            if key:
              label = "%smm" % key
            else:
              label = 'N/A'

        if args.group_by_camera:
            camera = exif.camera()
        else:
            camera = None

        group = (camera, key, label)

        if data.get(group):
            data[group] = data[group] + 1
        else:
            data[group] = 1

    return data



def run():
    parser = argparse.ArgumentParser(description='Extracts stats from a picture folder')
    parser.add_argument('-g', '--group-by-camera', help='group by camera model', action='store_true')

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--iso", action="store_true", help='extract ISO value')
    group.add_argument("-l", "--lens", action="store_true", help='extract lens model')

    parser.add_argument('directory', metavar='DIRECTORY', help='the directory to scan', default=".")
    args = parser.parse_args()

    root = args.directory
    files = get_files(root)

    data = extract_data(files, args)

    if args.group_by_camera:
        show_grouped_output(data)
    else:
        show_output(data)

    print "Total files: %s" % len(files)

if __name__ == '__main__':
    run()
