#! /bin/zsh

if [[ -z $SENTRY_DSN ]] then
    echo "SENTRY_DSN must be set!"
    exit 1
fi

if ! [[ -d .venv ]] then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Starting server..."
python reproduction/manage.py runserver &
sleep 3

echo "Sending request..."
curl http://localhost:8000/reproduction/
sleep 2

echo "Stopping server..."
kill %1
sleep 2