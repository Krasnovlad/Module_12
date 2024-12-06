from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):


    def test_walk(self):
        walker = Runner('Default')

        for _ in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    def test_run(self):
        default_2 = Runner('Default_2')

        for _ in range(10):
            default_2.run()

        self.assertEqual(default_2.distance, 100)

    def test_challenge(self):
        default_3 = Runner('Default_3')
        default_4 = Runner('Default_4')

        for _ in range(10):
            default_3.walk()
            default_4.run()

        self.assertNotEqual(default_3.distance, default_4.distance)


if __name__ == '__main__':
    unittest.main()