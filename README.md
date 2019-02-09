# PyHawaii Website/CMS

The PyHawaii website/CMS project.


## Commands

### Initialize everything prior to first run

First you need a python 2.7 virtual environment in `./env`:
[Note: 'env' is literal in this case, as 'env' expected in the script.]

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

### Next, activate the virtualenv and install all requisite packages: ###

```bash
(projectname) $ make sitepackages.sync
```

### Ensure pipenv is installed ###

```bash
$ pipenv --version
```

To install pipvenv:

```bash
$ pip install pipenv
```

### Run migrations to set up database: ###
```bash
(env) $ make db.reset
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
(env) $ make db.reset
```

**NOTE:** the default database contains three users:

1. **admin**: password is *admin*, `is_superuser` is `True`, `is_staff` is `True`
1. **bob**: password is *qwerQWER*, `is_staff` is `True`
1. **carol**: password is *qwerQWER*

To re-create the `bootstrap.json` fixture file:

```bash
(env) $ make db.dump
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
* `django-cms`: latest
* `social-auth-app-django`: latest


## Testing

This is set up to install the following packages for testing:

* `mock`
* `flake8`


## Maintenance

(need heroku docs)
