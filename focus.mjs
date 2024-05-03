export const paths = [
  {key:'java',group:'Java',description:'Balanced transactions, event handling and reliable service coordination.'},
  {key:'dotnet',group:'.NET',description:'Application boundaries, tenant isolation, identity and recoverable business workflows.'},
  {key:'python',group:'Python',description:'Data ingestion, background processing and search relevance.'},
  {key:'go',group:'Go',description:'Concurrency, admission control, queue workers and booking invariants.'},
  {key:'fullstack',group:'Full Stack',description:'Product workflows backed by clear permissions, consent rules and execution logic.'},
  {key:'devops',group:'DevOps',description:'Developer automation, recovery verification and infrastructure policy checks.'}
];
export function readFocus(search){
  const value=new URLSearchParams(search).get('focus');
  return paths.find(p=>p.key===value)?.group ?? (value==='all'?'All':'Selected');
}
export function focusUrl(group){
  const key=paths.find(p=>p.group===group)?.key;
  return key?'?focus='+key:group==='All'?'?focus=all':'?';
}
export function selectProjects(projects,group,query=''){
  const q=query.trim().toLowerCase();
  if(group==='Selected'&&!q){
    return paths.map(path=>projects.find(p=>p.group===path.group)).filter(Boolean);
  }
  return projects.filter(p=>(group==='All'||group==='Selected'||p.group===group)&&
    [p.title,p.group,p.stack,p.implemented,...p.features].join(' ').toLowerCase().includes(q));
}
