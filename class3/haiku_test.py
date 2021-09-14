from haiku import check_haiku, num_syllables
import unittest


class TestHaiku(unittest.TestCase):
    def test_check_haiku(self):
        VALID_HAIKU = (5, 7, 5, 'Yes')
        haiku1 = 'happy purple frog/eating bugs in the marshes/get indigestion'
        haiku2 = 'computer programs/the bugs try to eat my code/i will not let them'
        self.assertEqual(VALID_HAIKU, check_haiku(haiku1))
        self.assertNotEqual(VALID_HAIKU, check_haiku(haiku2))

    def test_num_syllables(self):
        word = 'hello'
        self.assertEqual(2, num_syllables(word))

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
