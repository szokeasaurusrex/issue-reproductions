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

echo ""
echo "##############################"
echo "Setup complete. We will now start the Celery Beat service. Please keep this terminal open, and run \`./run_worker.zsh\` in a new terminal."
echo "##############################"
echo ""
sleep 1

echo "Starting Celery Beat..."
celery -A tasks beat
