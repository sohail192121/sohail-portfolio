import re,math
from collections import Counter
class Search:
 def __init__(self):self.docs={}
 def put(self,tenant,key,title,body):
  if not tenant or not key:raise ValueError('tenant/key')
  self.docs[(tenant,key)]=(title,Counter(re.findall(r'\w+',(title+' '+title+' '+body).lower())))
 def query(self,tenant,text,limit=10):
  if not 1<=limit<=100:raise ValueError('limit')
  terms=set(re.findall(r'\w+',text.lower()));docs=[(k,v) for (t,k),v in self.docs.items() if t==tenant];hits=[]
  for key,(title,counts) in docs:
   score=sum((1+math.log(counts[t]))*math.log(1+len(docs)/(1+sum(t in c for _,(_,c) in docs))) for t in terms if counts[t])
   if score:hits.append({'id':key,'title':title,'score':score})
  return sorted(hits,key=lambda h:(-h['score'],h['id']))[:limit]
