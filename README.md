# envelope
geniric django json collector

# Setup

## Download the package from git, create the virtual environment and install the dependencies.

    git clone git@github.com:micheg/envelope.git
    cd envelope/
    python3 -m venv .
    . bin/activate
    pip install -r requirements.txt

## Set up django, templates, database and super user.

    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py makemigrations envelope_app
    python manage.py migrate
    python manage.py createsuperuser

## optional step, import one or more existing json files.

    python manage.py import_envelopes "{TITLE}" {JSON_FILE}

## Tokens

tokens do not have an invalidation mechanism, it is possible to run a script that eliminates tokens that are more than one hour old by putting the following script in cron or related systems:

    python manage.py cleanup_tokens
