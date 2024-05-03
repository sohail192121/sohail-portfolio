import json
def report(desired,actual):
 wanted={r['id']:r for r in desired};live={r['id']:r for r in actual}
 if len(wanted)!=len(desired) or len(live)!=len(actual):raise ValueError('duplicate resource id')
 findings=[]
 for key in sorted(wanted.keys()|live.keys()):
  if key not in live:findings.append({'resource':key,'rule':'missing'});continue
  if key not in wanted:findings.append({'resource':key,'rule':'unmanaged'})
  resource=live[key]
  for tag in ('owner','environment'):
   if not resource.get('tags',{}).get(tag):findings.append({'resource':key,'rule':'missing-tag','tag':tag})
  if resource.get('cpu_percent',100)<5:findings.append({'resource':key,'rule':'idle-review','action':'manual review; no automatic deletion'})
  if key in wanted:
   for field in ('type','region'):
    if wanted[key].get(field)!=resource.get(field):findings.append({'resource':key,'rule':'drift','field':field,'desired':wanted[key].get(field),'actual':resource.get(field)})
 return {'mode':'offline-read-only','findings':findings,'estimated_savings':None}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('desired');p.add_argument('actual');a=p.parse_args()
 with open(a.desired) as f:d=json.load(f)
 with open(a.actual) as f:l=json.load(f)
 print(json.dumps(report(d,l),indent=2))
