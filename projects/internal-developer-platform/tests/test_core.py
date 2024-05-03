import unittest,tempfile,json
from core import generate
class Tests(unittest.TestCase):
 def test_template_and_collision(self):
  with tempfile.TemporaryDirectory() as d:
   p=generate('sample-api','platform',d);data=json.loads((p/'deployment.json').read_text());self.assertEqual(data['spec']['replicas'],2)
   with self.assertRaises(FileExistsError):generate('sample-api','platform',d)
 def test_path_rejection(self):
  with self.assertRaises(ValueError):generate('../escape','team','.')
