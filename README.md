lens-stats
==========

Ever been curious to know which focal lengths you're using the most often in your pictures? This script extracts the focal length value (if available) from the JPEG EXIF data and shows the usage count, grouping the records by Camera model.

It's a simple python experiment so the code quality is pretty low.

Usage
-----

```
python lens-stats.py FOLDER
```

The script will look recursively for all JPEG files within the folder. Example output:

```
python lens-stats.py ~/Pictures/Varie
Parsed files: 43

GT-I9000
--------
3mm:  12

N/A
---
N/A:  28

FinePix S3Pro
---------------
N/A:  1

Canon PowerShot S50
-------------------
12mm: 1

iPhone 4S
---------
35mm: 1
```

