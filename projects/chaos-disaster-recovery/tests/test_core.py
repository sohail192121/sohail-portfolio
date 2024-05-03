import unittest
from core import drill
class Tests(unittest.TestCase):
 def test_restore_integrity(self):
  r=drill(31);self.assertTrue(r['verified']);self.assertEqual(r['rows'],31);self.assertGreaterEqual(r['restore_seconds'],0)
 def test_bounds(self):
  with self.assertRaises(ValueError):drill(0)
