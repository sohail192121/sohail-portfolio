from collections import deque
from copy import deepcopy
from threading import Lock

class Intake:
    def __init__(self, capacity=100):
        if capacity < 1: raise ValueError('capacity')
        self.capacity=capacity; self.pending=deque(); self.log=[]; self.ids=set(); self.lock=Lock()
    def accept(self, tenant, event):
        if not tenant or event.get('version') != 1 or not event.get('id') or not isinstance(event.get('payload'),dict):
            raise ValueError('invalid tenant or schema')
        with self.lock:
            key=(tenant,event['id'])
            if key in self.ids: return False
            if len(self.pending)>=self.capacity: raise BufferError('backpressure: retry later')
            self.pending.append((tenant,deepcopy(event))); self.ids.add(key); return True
    def drain(self):
        with self.lock:
            while self.pending: self.log.append(self.pending.popleft())
    def replay(self, tenant, after=0):
        if after < 0: raise ValueError('cursor')
        with self.lock:
            return [(i+1,deepcopy(e)) for i,(t,e) in enumerate(self.log) if i>=after and t==tenant]
