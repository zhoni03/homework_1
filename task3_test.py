import unittest
from Task3 import time_to_cyclic, cyclic_time_difference

class TestCyclicTimeFeatures(unittest.TestCase):

    def test_time_to_cyclic(self):
        # Test key times to check cyclic conversion
        self.assertAlmostEqual(time_to_cyclic(0)[0], 0)
        self.assertAlmostEqual(time_to_cyclic(0)[1], 1)
        
        self.assertAlmostEqual(time_to_cyclic(6)[0], 1, places=1)   # 6:00 should be at the top
        self.assertAlmostEqual(time_to_cyclic(6)[1], 0, places=1)
        
        self.assertAlmostEqual(time_to_cyclic(12)[0], 0, places=1)  # 12:00 should be on the left
        self.assertAlmostEqual(time_to_cyclic(12)[1], -1, places=1)
        
        self.assertAlmostEqual(time_to_cyclic(18)[0], -1, places=1) # 18:00 should be at the bottom
        self.assertAlmostEqual(time_to_cyclic(18)[1], 0, places=1)

    def test_cyclic_time_difference(self):
        # Test for expected time differences
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2, places=1)
        self.assertAlmostEqual(cyclic_time_difference(1, 23), 2, places=1)
        
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12, places=1)
        self.assertAlmostEqual(cyclic_time_difference(6, 18), 12, places=1)
        
        self.assertAlmostEqual(cyclic_time_difference(0, 0), 0, places=1)
        self.assertAlmostEqual(cyclic_time_difference(0, 24), 0, places=1)

    def test_full_circle(self):
        # Check that going full circle results in a 0-hour difference
        self.assertAlmostEqual(cyclic_time_difference(0, 24), 0, places=1)
        self.assertAlmostEqual(cyclic_time_difference(6, 30), 0, places=1)
        self.assertAlmostEqual(cyclic_time_difference(12, 36), 0, places=1)

if __name__ == "__main__":
    unittest.main()
