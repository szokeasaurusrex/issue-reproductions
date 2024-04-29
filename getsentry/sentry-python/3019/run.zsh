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
uvicorn app:app &

echo "Sleeping 3s to let server start..."
sleep 3

echo "Requesting /..."
curl http://localhost:8000/

echo "Exiting..."
kill %1

sleep 2
