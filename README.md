# Cookie-cutter Django + Djangae Web App

Cookie-cutter to bootstrap a brand-new app using Django in the Google App Engine environment and with Google Cloud Datastore as the back-end. Note that this works with Python 2.7 and *not* with Python 3.x due to limitations of the Google App Engine sandbox.


## Commands

### Initialize everything prior to first run

First you need a python 2.7 virtual environment in `./env`:

```bash
$ virtualenv -p $(which python2) env
$ source env/bin/activate
(env) $
```

Alternately, you can create a virtual environment using `mkvirtualenv` if you have it installed:

```bash
$ mkvirtualenv --python=$(which python2) projectname
(projectname) $ ln -s $VIRTUAL_ENV/ env
(projectname) $
```

**NOTE:** the name `env` is required for links elsewhere in the project to work correctly.

Next, activate the virtualenv and install all requisite packages:

```bash
(projectname) $ pip install -r requirements.txt
```


### Running locally

To enter a shell:

```bash
(env) $ make shell
```

To run the project locally:

```bash
(env) $ make serve
```

To run all unit tests defined in the project:

```bash
(env) $ make test
```


## Database operations

To return the database to a clean state using the bootstrap.json fixture file:

```bash
(env) $ make resetdb
```

**NOTE:** the default database contains three users:

1. **admin**: password is *admin*, `is_superuser` is `True`, `is_staff` is `True`
1. **bob**: password is *qwerQWER*, `is_staff` is `True`
1. **carol**: password is *qwerQWER*

To re-create the `bootstrap.json` fixture file:

```bash
(env) $ make dumpdb
```

### Migrations

*Note that migrations only have relevance if you are using a regular database instead of the datastore.*

To create migrations:

```bash
(env) $ make makemigrations
```

To migrate the database to the latest migrations:

```bash
(env) $ make migrate
```


## Using a dabase instead of the datastore

You can use a database backend instead of the datastore if your project requires this. While there are many changes you will need to make in how you create models (no `ListField`, for instance), the primary difference in using this cookie-cutter is that your settings need to reference the right backend.

In `site/settings.py` change:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine',
    }
}
```

... to:


```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db_test.db'),
    }
}
```

You should be able to split your project between a database and the datastore using the documentation in [Multiple databases](https://docs.djangoproject.com/en/1.11/topics/db/multi-db/) but this has not been tried with this cookie-cutter yet.


## Versions

Right now, this installs the following versions of requisite packages:

* `Django`: 1.8 latest
* `djangae`: latest
* `django-filetransfers`: latest
* `django-session-csrf`: latest
* `GoogleAppEngineCloudStorageClient`: latest


## Testing

This is set up to install the following packages for testing:

* `mock`
* `flake8`


## Maintenance

# switching between google sdk versions

`gcloud components update --version 170.0.0`
