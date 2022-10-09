import unittest
from agent import GameAgent


class MyTestCase(unittest.TestCase):

    def test_agent(self):
        a = GameAgent(1, 1)
        self.assertEqual(a.power, 6)

    def test_agent2(self):
        a = GameAgent(1, 1)
        a.power = 5
        self.assertEqual(a.power, 5)

    def test_agent3(self):
        a = GameAgent(1, 1)
        a.power = 0
        self.assertEqual(a.power, 0)

    def test_agent4(self):
        a = GameAgent(0, 0)
        a.power = 0
        self.assertEqual(a.power, 0)


if __name__ == '__main__':
    unittest.main()
