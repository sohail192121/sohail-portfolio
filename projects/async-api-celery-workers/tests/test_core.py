import unittest
from core import WorkerQueue
class Tests(unittest.TestCase):
 def test_priority_dedup_and_tenant(self):
  q=WorkerQueue();q.submit('a','x','low',9);q.submit('b','x','high',1);self.assertFalse(q.submit('a','x','duplicate'))
  seen=[]
  while q.run_one(lambda p:seen.append(p)):pass
  self.assertEqual(seen,['high','low'])
 def test_bounded_retry(self):
  q=WorkerQueue(2);q.submit('a','x',1)
  def fail(p):raise RuntimeError('failed')
  for _ in range(5):q.run_one(fail)
  self.assertEqual(q.dead[0]['attempts'],2);self.assertEqual(q.jobs,[])
