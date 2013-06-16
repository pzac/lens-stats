import unittest

class TestExifExtraction(unittest.TestCase):

    def test_focal_length(self):
        exif = get_exif_data('1.jpg')
        self.assertEqual(exif.focal_length, 21.2)

if __name__ == '__main__':
    unittest.main()
