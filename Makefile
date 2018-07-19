# -------------------------------------
# MAKEFILE
# -------------------------------------

#
# project settings
#

GCP_PROJECT=<project name in GCP>


#
# environment
#

ifndef VIRTUAL_ENV
$(error VIRTUAL_ENV is not set)
endif

ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif


#
# commands for running locally
#

PHONY: serve
serve:
	$(VIRTUAL_ENV)/bin/python site/manage.py runserver

PHONY: shell
shell:
	$(VIRTUAL_ENV)/bin/python site/manage.py shell


#
# commands for testing
#

PHONY: test
test:
	cd site && $(VIRTUAL_ENV)/bin/python manage.py test $(TEST_ARGS)

PHONY: test.coverage.exec
test.coverage.exec:
	cd site && $(VIRTUAL_ENV)/bin/coverage run --source='.' manage.py test --failfast .

PHONY: test.coverage.report
test.coverage.report:
	cd site && $(VIRTUAL_ENV)/bin/coverage report

PHONY: test.coverage
test.coverage: test.coverage.exec test.coverage.report


#
# commands for database maintenance
#

PHONY: db.reset
db.reset:
	git co -- site/index.yaml
	rm -rf site/.storage
	$(VIRTUAL_ENV)/bin/python site/manage.py loaddata ../fixtures/bootstrap.json

PHONY: db.dump
db.dump:
	$(VIRTUAL_ENV)/bin/python site/manage.py dumpdata --indent 2 -e contenttypes -e sessions -e admin.logentry > fixtures/bootstrap.json

PHONY: db.makemigrations
db.makemigrations:
	$(VIRTUAL_ENV)/bin/python site/manage.py makemigrations

PHONY: db.migrate
db.migrate:
	$(VIRTUAL_ENV)/bin/python site/manage.py migrate


#
# commands for virtualenv maintenance
#

PHONY: sitepackages.clean
sitepackages.clean:
	pip freeze | xargs pip uninstall -y

PHONY: sitepackages.install
sitepackages.install:
	pip install -r requirements.txt

PHONY: sitepackages.checkpoint
sitepackages.checkpoint:
	pip freeze > requirements.checkpoint.txt


#
# commands for deployment and production adjustments
#

PHONY: deploy.app
deploy.app:
	gcloud app deploy --project $(GCP_PROJECT) --no-promote --version $(shell git describe --tags --dirty | sed 's/\./-/') site/app.yaml

PHONY: deploy.dispatch
deploy.dispatch:
	gcloud app deploy --project $(GCP_PROJECT) site/dispatch.yaml

PHONY: deploy.indexes
deploy.indexes:
	gcloud datastore --project $(GCP_PROJECT) create-indexes site/index.yaml

PHONY: deploy.queue
deploy.queue:
	gcloud app deploy --project $(GCP_PROJECT) site/queue.yaml

PHONY: deploy
deploy: deploy.indexes deploy.queue deploy.app deploy.dispatch


#
# IN PROGRESS
#

PHONY: shell.remote
shell.remote:
	$(VIRTUAL_ENV)/bin/python site/manage.py --sandbox=remote shell