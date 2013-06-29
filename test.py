import unittest
from exif_parser import ExifParser

class TestExifExtraction(unittest.TestCase):

    def test_focal_length(self):
        # I wonder where the 21.2 value I see on Preview.app comes from
        # self.assertEqual(exif_parser.focal_length('test/1.jpg'), 21.2)
        self.assertEqual(ExifParser('test/1.jpg').focal_length(), 21)
        self.assertEqual(ExifParser('test/2.jpg').focal_length(), 105)
        self.assertEqual(ExifParser('test/3.jpg').focal_length(), None)
        self.assertEqual(ExifParser('test/4.jpg').focal_length(), 84)
        self.assertEqual(ExifParser('test/5.jpg').focal_length(), 33)
        self.assertEqual(ExifParser('test/6.jpg').focal_length(), 35)

if __name__ == '__main__':
    unittest.main()
