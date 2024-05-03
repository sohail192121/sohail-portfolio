import sqlite3,tempfile,time,hashlib,json
from contextlib import closing
from pathlib import Path
def checksum(db):
 return hashlib.sha256(json.dumps(db.execute('select id,value from records order by id').fetchall()).encode()).hexdigest()
def drill(rows=1000):
 if not 1<=rows<=100000:raise ValueError('rows')
 with tempfile.TemporaryDirectory(prefix='sohail-drill-') as directory:
  source=sqlite3.connect(str(Path(directory)/'source.db'));source.execute('create table records(id integer primary key,value text)')
  source.executemany('insert into records values (?,?)',((i,f'synthetic-{i}') for i in range(rows)));source.commit();expected=checksum(source)
  start=time.perf_counter()
  with closing(sqlite3.connect(str(Path(directory)/'backup.db'))) as backup:source.backup(backup)
  backup_seconds=time.perf_counter()-start
  # Only the synthetic source inside this temporary directory is disrupted.
  source.execute('delete from records');source.commit()
  start=time.perf_counter()
  with closing(sqlite3.connect(str(Path(directory)/'backup.db'))) as backup:backup.backup(source)
  restore_seconds=time.perf_counter()-start;actual=checksum(source);source.close()
  return {'scope':'local synthetic SQLite drill; not Kubernetes/PostgreSQL RTO','rows':rows,'verified':actual==expected,'backup_seconds':backup_seconds,'restore_seconds':restore_seconds,'checksum':actual}
if __name__=='__main__':print(json.dumps(drill(),indent=2))
