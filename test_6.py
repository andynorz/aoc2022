import unittest
import aoc22_6


class TestCommSystem(unittest.TestCase):
    def test_commsystem(self):
        inputs = ["bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
        self.assertEqual(aoc22_6.main(inputs), [5, 6, 10, 11])

if __name__ == '__main__':
    unittest.main()

    