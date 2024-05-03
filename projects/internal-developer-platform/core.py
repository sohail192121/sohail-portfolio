import re,json
from pathlib import Path
def generate(name,owner,destination):
 if not re.fullmatch(r'[a-z][a-z0-9-]{1,40}',name) or name.endswith('-'):raise ValueError('invalid service name')
 if not re.fullmatch(r'[A-Za-z0-9_.-]{1,64}',owner):raise ValueError('invalid team')
 root=Path(destination)/name
 root.mkdir(parents=True,exist_ok=False)
 namespace={'apiVersion':'v1','kind':'Namespace','metadata':{'name':name,'labels':{'owner':owner,'pod-security.kubernetes.io/enforce':'restricted'}}}
 deployment={'apiVersion':'apps/v1','kind':'Deployment','metadata':{'name':name,'namespace':name},'spec':{'replicas':2,'selector':{'matchLabels':{'app':name}},'template':{'metadata':{'labels':{'app':name}},'spec':{'securityContext':{'runAsNonRoot':True,'seccompProfile':{'type':'RuntimeDefault'}},'containers':[{'name':name,'image':'REPLACE_WITH_SIGNED_IMAGE_DIGEST','ports':[{'containerPort':8080}],'securityContext':{'allowPrivilegeEscalation':False,'readOnlyRootFilesystem':True,'capabilities':{'drop':['ALL']}},'resources':{'requests':{'cpu':'100m','memory':'128Mi'},'limits':{'cpu':'500m','memory':'256Mi'}},'readinessProbe':{'httpGet':{'path':'/health','port':8080},'initialDelaySeconds':5},'livenessProbe':{'httpGet':{'path':'/health','port':8080},'initialDelaySeconds':15}}]}}}}
 policy={'apiVersion':'networking.k8s.io/v1','kind':'NetworkPolicy','metadata':{'name':'default-deny','namespace':name},'spec':{'podSelector':{},'policyTypes':['Ingress','Egress']}}
 for filename,data in [('namespace.json',namespace),('deployment.json',deployment),('network-policy.json',policy)]:
  (root/filename).write_text(json.dumps(data,indent=2))
 (root/'catalog-info.yaml').write_text(f'apiVersion: backstage.io/v1alpha1\nkind: Component\nmetadata:\n  name: {name}\nspec:\n  type: service\n  lifecycle: experimental\n  owner: {owner}\n')
 return root
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('owner');p.add_argument('--output',default='artifacts');a=p.parse_args();print(generate(a.name,a.owner,a.output))
