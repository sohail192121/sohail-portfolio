import unittest
from core import Intake
class Tests(unittest.TestCase):
 def test_capacity_replay_and_isolation(self):
  q=Intake(1);e={'version':1,'id':'x','payload':{'a':1}}
  self.assertTrue(q.accept('a',e));self.assertFalse(q.accept('a',e))
  with self.assertRaises(BufferError):q.accept('b',e)
  e['payload']['a']=9;q.drain();self.assertEqual(q.replay('a')[0][1]['payload']['a'],1)
  self.assertEqual(q.replay('b'),[]);self.assertEqual(q.replay('a',1),[])
 def test_schema(self):
  with self.assertRaises(ValueError):Intake().accept('a',{'version':2})
