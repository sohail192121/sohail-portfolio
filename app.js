import {paths,readFocus,focusUrl,selectProjects} from './focus.mjs';
const grid=document.querySelector('#projects');
const filters=document.querySelector('#filters');
const search=document.querySelector('#search');
const dialog=document.querySelector('#detail');
let projects=[],selected=readFocus(location.search),opener=null;
function el(tag,text,cls){const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e}
function sourceLink(p){const a=el('a','Source ↗');a.href=p.repositoryUrl;a.setAttribute('aria-label','Source for '+p.title);return a}
function show(p,button){
  opener=button;
  const box=document.querySelector('#detail-content');
  box.replaceChildren(el('p',p.group,'eyebrow'),el('h2',p.title),el('p',p.stack),el('h3','Implemented core'),el('p',p.implemented),el('h3','Next milestones'));
  const list=el('ul');p.pending.forEach(x=>list.append(el('li',x)));
  box.append(list,el('p','Personal engineering prototype. The README documents implemented behavior, tests, limitations and planned integrations.'),sourceLink(p));
  dialog.showModal();
}
function render(){
  const path=paths.find(p=>p.group===selected);
  const items=selectProjects(projects,selected,search.value);
  document.querySelector('#work-title').textContent=path?path.group+' engineering.':'Systems worth explaining.';
  document.querySelector('#work-description').textContent=path?path.description:'Explore a selection across six paths, or choose a focus to see its three projects.';
  document.querySelector('#intro').textContent=path?'I’m Sohail Sharif, a senior software engineer. This '+path.group+' collection explores '+path.description.charAt(0).toLowerCase()+path.description.slice(1):'I build maintainable systems with clear boundaries, thoughtful APIs and well-understood failure behavior. Explore the engineering work that matters to your role.';
  document.querySelector('#focus-label').textContent=path?path.group.toUpperCase()+' / PROJECT COLLECTION':selected==='All'?'ALL PROJECTS':'SELECTED WORK';
  document.querySelector('#share-focus').href=focusUrl(selected);
  document.title=path?'Sohail Sharif | '+path.group+' Engineering':'Sohail Sharif | Senior Software Engineer';
  grid.replaceChildren();
  items.forEach(p=>{
    const card=el('article',null,'project'),top=el('div',null,'project-top');
    top.append(el('span',String(projects.indexOf(p)+1).padStart(2,'0'),'number'),el('span',p.group,'group'));
    const bottom=el('div',null,'project-bottom'),button=el('button','Design & details ↗');
    button.setAttribute('aria-label','Details for '+p.title);button.onclick=()=>show(p,button);
    bottom.append(el('span','● Personal project · core prototype','status'),button,sourceLink(p));
    card.append(top,el('h3',p.title),el('p',p.features.join(' · ')),bottom);grid.append(card);
  });
  if(!items.length)grid.append(el('p','No projects match this search. Try another term or choose All projects.','empty-result'));
  document.querySelector('#count').textContent=items.length+' projects · '+(selected==='All'?'All projects':selected==='Selected'?'Selected work':selected);
  filters.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.group===selected)));
  document.querySelectorAll('[data-focus]').forEach(a=>a.setAttribute('aria-current',String(paths.find(p=>p.key===a.dataset.focus)?.group===selected)));
}
function choose(group,updateUrl=true){selected=group;search.value='';if(updateUrl)history.pushState(null,'',focusUrl(group)+'#work');render()}
document.querySelector('#close').onclick=()=>dialog.close();
dialog.addEventListener('close',()=>opener?.focus());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});
search.addEventListener('input',render);
addEventListener('popstate',()=>choose(readFocus(location.search),false));
fetch('projects.json').then(r=>{if(!r.ok)throw Error('load');return r.json()}).then(data=>{
  projects=data;
  ['Selected',...paths.map(p=>p.group),'All'].forEach(group=>{
    const button=el('button',group==='Selected'?'Selected work':group==='All'?'All projects':group);
    button.dataset.group=group;button.onclick=()=>choose(group);filters.append(button);
  });
  document.querySelectorAll('[data-focus]').forEach(a=>a.addEventListener('click',e=>{
    if(e.ctrlKey||e.metaKey||e.shiftKey||e.altKey||e.button!==0)return;
    e.preventDefault();choose(paths.find(p=>p.key===a.dataset.focus).group);
    document.querySelector('#work').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
  }));
  render();
}).catch(()=>document.querySelector('#error').hidden=false);
