import unittest
import commands
import time

class TestDetectKey(unittest.TestCase):
    def setUp(self):
        self.game = commands.Game("vitor",0)

    def tearDown(self):
        pass

    # def test_up(self):
    #     self.assertEqual(self.game.detect_keyboard(), "left")
    #     time.sleep(1)
    #     self.assertEqual(self.game.detect_keyboard(), "right")
    #     time.sleep(1)
    #     self.assertEqual(self.game.detect_keyboard(), "up")
    #     time.sleep(1)
    #     self.assertEqual(self.game.detect_keyboard(), "down")
if __name__ == '__main__':
    unittest.main()
