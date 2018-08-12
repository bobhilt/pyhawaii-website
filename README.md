# PyHawaii Website/CMS

The PyHawaii website/CMS project.


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

To create migrations:

```bash
(env) $ make makemigrations
```

To migrate the database to the latest migrations:

```bash
(env) $ make migrate
```


## Versions

Right now, this installs the following versions of requisite packages:

* `Django`: 1.11 latest
* `psycopg2`: latest
* `django-session-csrf`: latest
* `GoogleAppEngineCloudStorageClient`: latest


## Testing

This is set up to install the following packages for testing:

* `mock`
* `flake8`


## Maintenance

# switching between google sdk versions

`gcloud components update --version 170.0.0`
