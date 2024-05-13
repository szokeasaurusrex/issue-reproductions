#! /bin/zsh

if [[ -z $SENTRY_DSN ]] then
    echo "SENTRY_DSN must be set!"
    exit 1
fi

if ! [[ -d .venv ]] then
    echo "Virtual environment missing!"
    exit 2
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Starting Celery Worker..."
celery -A tasks worker
