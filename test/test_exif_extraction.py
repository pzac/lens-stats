import unittest
import photo_analyzer

class TestExifExtraction(unittest.TestCase):

    def test_focal_length(self):
        exif = get_exif_data('1.jpg')
        self.assertEqual(exif.focal_length, 21.2)
        exif = get_exif_data('2.jpg')
        self.assertEqual(exif.focal_length, 105)
        exif = get_exif_data('3.jpg')
        self.assertEqual(exif.focal_length, 'N/A')
        exif = get_exif_data('4.jpg')
        self.assertEqual(exif.focal_length, 13.9)
        exif = get_exif_data('5.jpg')
        self.assertEqual(exif.focal_length, 33)
        exif = get_exif_data('6.jpg')
        self.assertEqual(exif.focal_length, 35)

if __name__ == '__main__':
    unittest.main()
