# -------------------------------------
# MAKEFILE
# -------------------------------------

#
# project settings
#

HEROKU_PROJECT=pyhawaii


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


#
# commands for database maintenance
#

PHONY: db.clean
db.clean:
	rm -f db.sqlite

PHONY: db.reset
db.reset: db.clean db.migrate
	$(VIRTUAL_ENV)/bin/python site/manage.py loaddata ../fixtures/bootstrap.json

PHONY: db.dump
db.dump:
	$(VIRTUAL_ENV)/bin/python site/manage.py dumpdata --indent 2 -e contenttypes -e auth.permission -e sessions -e admin.logentry > fixtures/bootstrap.json

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

PHONY: sitepackages.sync
sitepackages.sync:
	pipenv update && pipenv clean && pipenv lock --requirements > scripts/containerize/requirements.txt


#
# commands for deployment and production adjustments
#

PHONY: deploy
deploy: deploy.indexes deploy.queue deploy.app deploy.dispatch
