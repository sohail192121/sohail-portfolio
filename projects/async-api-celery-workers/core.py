import heapq
from itertools import count
class WorkerQueue:
 def __init__(self,max_attempts=3):
  if max_attempts<1:raise ValueError('max attempts')
  self.jobs=[];self.sequence=count();self.dead=[];self.results={};self.ids=set();self.max_attempts=max_attempts
 def submit(self,tenant,key,payload,priority=5):
  if not tenant or not key:raise ValueError('tenant/key')
  identity=(tenant,key)
  if identity in self.ids:return False
  self.ids.add(identity);heapq.heappush(self.jobs,(priority,next(self.sequence),identity,payload,0));return True
 def run_one(self,handler):
  if not self.jobs:return False
  priority,_,identity,payload,attempt=heapq.heappop(self.jobs)
  try:self.results[identity]=handler(payload)
  except Exception as exc:
   attempt+=1
   if attempt>=self.max_attempts:self.dead.append({'identity':identity,'attempts':attempt,'error':type(exc).__name__})
   else:heapq.heappush(self.jobs,(priority,next(self.sequence),identity,payload,attempt))
  return True
