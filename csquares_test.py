import unittest
from csquares import *

class TestCSquareConvertor(unittest.TestCase):
    examples = [
    (38.84, -77.03, '7307:487:380:143'),
    (-37.24, 100.0, '3310:370:120:140'),
    (-37.24, 10.0,  '3301:370:120:140'),
    (-37.24, 1.0, '3300:371:120:140'),
    (-37.8193,145.1625,'3314:475:381:216:392:235'),
    (25, 100, '1210:350'),
    (1, 1, '1000:111'),
    (1.0, -1.0, '7000:111'),
    (1.0, 1.0, '1000:111'),
    (0.0, 0.0, '1000:100'),
    (-0.0, -0.0, '1000:100'),
    (-1.0, -1.0, '5000:111'),
    (1.0, -1.0, '7000:111'),
    (90.0, -180.0, '7817:499'),
    (90.0, 180.0, '1817:499'),
    (0, -180.0, '7017:209'),
    (-90.0, -180.0, '5817:499'),
    (-90.0, 180.0, '3817:499'),
    (-90.0, 0, '3800:390'),
    (90.0, 0.0, '1800:390'),
    (0.0, 180.0, '1017:209'),
    ]

    def test_auto_examples(self):
        for latitude, longitude, expected in self.examples:
            name = 'latitude={} longitude={}'.format(latitude, longitude)
            with self.subTest(name=name):
                self.assertEqual(to_csquare(latitude, longitude), expected)


class TestCSQuareValidator(unittest.TestCase):
    examples = [
        (1.0,-1.0, '7'),
        (90.0, -180.0, '7'),
        (0, -180.0, '7'),
        (1.0, 1.0, '1'),
        (0.0, 0.0, '1'),
        (-0.0, -0.0, '1'),
        (-1.0, -1.0, '5'),
        (-90.0, -180.0, '5'),
        (1.0, -1.0, '7'),
        (-90.0, 180.0, '3'),
        (-90.0, 0, '3'),
        (90.0, 180.0, '1'),
        (90.0, 0.0, '1'),
        (0.0, 180.0, '1'),
    ]

    def test_global_quadrant_NE_edge_NW(self):
        for latitude, longitude, expected in self.examples:
            name = 'latitude={} longitude={}'.format(latitude, longitude)
            with self.subTest(name=name):
                self.assertEqual(global_quadrant(latitude, longitude), expected)


if __name__ == '__main__':
    unittest.main()
