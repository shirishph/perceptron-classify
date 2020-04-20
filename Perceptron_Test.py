import unittest
import Perceptron


class Perceptron_Test(unittest.TestCase):

    def setUp(self):
        self.perceptron = Perceptron.Perceptron()

    def test_run(self):
        response = self.perceptron.train()
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()