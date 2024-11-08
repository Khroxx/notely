# notelydjango

d

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## What you need to run locally

- Docker, Docker-compose
- PostreSQL (+ have a user)
- createdb


## Basic Commands

To install: <br>
1. Clone repository:
```bash
git clone https://github.com/Khroxx/notely.git
```

2. Create a database for it:
```bash
createdb --username=postgres notely
```

3. Change DATABASE_URL to your postgres username
in .envs/.local/.django write:
```bash
DATABASE_URL=postgres://postgresuser:postgrespassword@postgres:5432/notely
```

4. Start the docker localhost
```bash
docker compose -f docker-compose.local.yml build
docker compose -f docker-compose.local.yml run
```

5. Migrate
```bash
docker compose -f docker-compose.local.yml run --rm python manage.py makemigrations
docker compose -f docker-compose.local.yml run --rm python manage.py migrate
```

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy notely

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Email Server

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).
