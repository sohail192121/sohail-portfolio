import unittest
from core import Search
class Tests(unittest.TestCase):
 def test_rank_and_isolation(self):
  s=Search();s.put('a','1','Redis queue','workers');s.put('a','2','Workers','Redis');s.put('b','3','Redis','Redis')
  hits=s.query('a','redis');self.assertEqual([h['id'] for h in hits],['1','2']);self.assertEqual(s.query('a','missing'),[])
 def test_update(self):
  s=Search();s.put('a','1','old','');s.put('a','1','new','');self.assertEqual(s.query('a','old'),[])
