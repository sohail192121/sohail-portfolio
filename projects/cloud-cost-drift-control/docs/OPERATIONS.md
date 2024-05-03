# Offline report

Run `python core.py fixtures/desired.json fixtures/actual.json`. Fixtures are synthetic. The report identifies missing and unmanaged resources, selected attribute drift, missing owner/environment tags and a simple low-CPU review flag. It never deletes or changes cloud resources. Low CPU alone is not sufficient evidence that a resource can safely be removed. Savings remain null until actual billing evidence exists.
