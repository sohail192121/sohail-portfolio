import unittest
from core import report
class Tests(unittest.TestCase):
 def test_policy_drift(self):
  r=report([{'id':'a','type':'small'}],[{'id':'a','type':'large','cpu_percent':1}]);rules={f['rule'] for f in r['findings']};self.assertEqual(rules,{'drift','idle-review','missing-tag'});self.assertIsNone(r['estimated_savings'])
 def test_duplicate(self):
  with self.assertRaises(ValueError):report([{'id':'a'},{'id':'a'}],[])
