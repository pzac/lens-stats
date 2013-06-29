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

    def test_camera(self):
        self.assertEqual(ExifParser('test/1.jpg').camera(), 'FC-S3x')
        self.assertEqual(ExifParser('test/2.jpg').camera(), 'DMC-FX9')
        self.assertEqual(ExifParser('test/3.jpg').camera(), 'HTC Hero')
        self.assertEqual(ExifParser('test/4.jpg').camera(), 'DMC-FX9')
        self.assertEqual(ExifParser('test/5.jpg').camera(), 'NIKON D40')
        self.assertEqual(ExifParser('test/6.jpg').camera(), 'iPhone 4S')

if __name__ == '__main__':
    unittest.main()
