import unittest

class RandomTest(unittest.TestCase):
    def test_random_numpy(self):
        import numpy as np
        mean = 3
        std = 1
        sample_size = 10**6

        sample = np.random.normal(mean, std, sample_size)

        self.assertAlmostEqual(first=mean, second=np.mean(sample), places=2)
        self.assertAlmostEqual(first=std, second=np.std(sample), places=2)
