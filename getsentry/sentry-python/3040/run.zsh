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
python app.py

