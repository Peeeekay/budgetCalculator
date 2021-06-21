[![Codacy Badge](https://api.codacy.com/project/badge/Grade/efab859c303d4900a95a3bc2b58fe799)](https://app.codacy.com/gh/Peeeekay/budgetCalculator?utm_source=github.com&utm_medium=referral&utm_content=Peeeekay/budgetCalculator&utm_campaign=Badge_Grade_Settings)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/fd39b56ca60e41ec848c79bbd9302f3e)](https://www.codacy.com/gh/Peeeekay/budgetCalculator/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Peeeekay/budgetCalculator&utm_campaign=Badge_Coverage)

# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
