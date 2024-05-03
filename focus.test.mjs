import {test} from 'node:test';
import assert from 'node:assert/strict';
import {paths,readFocus,focusUrl,selectProjects} from './focus.mjs';
import {readFileSync} from 'node:fs';
const projects=JSON.parse(readFileSync(new URL('./projects.json',import.meta.url)));
test('every resume link opens only its matching three projects',()=>{
  for(const path of paths){
    const focus=readFocus(focusUrl(path.group));
    assert.equal(focus,path.group);
    const items=selectProjects(projects,focus);
    assert.equal(items.length,3);
    assert.ok(items.every(p=>p.group===path.group));
  }
});
test('default selection gives equal space to all six engineering paths',()=>{
  const items=selectProjects(projects,readFocus(''));
  assert.equal(items.length,6);
  assert.equal(new Set(items.map(p=>p.group)).size,6);
  assert.equal(readFocus('?focus=invalid'),'Selected');
});
test('all and search respect the selected role boundary',()=>{
  assert.equal(selectProjects(projects,readFocus('?focus=all')).length,18);
  assert.equal(selectProjects(projects,'Java','ledger')[0].slug,'transactional-payment-ledger');
  assert.equal(selectProjects(projects,'.NET','ledger').length,0);
  assert.equal(selectProjects(projects,'Selected','  booking  ')[0].group,'Go');
});
