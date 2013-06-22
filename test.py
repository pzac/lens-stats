import unittest
import exif_parser

class TestExifExtraction(unittest.TestCase):

    def test_focal_length(self):
        self.assertEqual(exif_parser.focal_length('test/1.jpg'), 21.2)
        self.assertEqual(exif_parser.focal_length('test/2.jpg'), 105)
        self.assertEqual(exif_parser.focal_length('test/3.jpg'), 'N/A')
        self.assertEqual(exif_parser.focal_length('test/4.jpg'), 13.9)
        self.assertEqual(exif_parser.focal_length('test/5.jpg'), 33)
        self.assertEqual(exif_parser.focal_length('test/6.jpg'), 35)

if __name__ == '__main__':
    unittest.main()
