lens-stats
==========

Ever been curious to know which focal lengths (or ISO, or lens) you're using the most often in your pictures? This script extracts these values (if available) from the JPEG EXIF data and shows the usage count, optionally grouping the records by camera model.

Setup
-----

You need the PIL library:

```
pip install PIL
```

Usage
-----

```
usage: python lens-stats.py [-h] [-g] [-i | -l] DIRECTORY

Extracts stats from a picture folder

positional arguments:
  DIRECTORY             the directory to scan

optional arguments:
  -h, --help            show this help message and exit
  -g, --group-by-camera
                        group by camera model
  -i, --iso             extract ISO value
  -l, --lens            extract lens model
```

The script will look recursively for all JPEG files within the folder. Example output:

```
 » python lens-stats.py .
N/A:  1
21mm: 1
33mm: 1
35mm: 1
84mm: 1
105mm:  1
Total files: 6
```

Links
-----

* http://www.endlesslycurious.com/2011/05/11/extracting-image-exif-data-with-python/

