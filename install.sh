apk add --no-cache gcc musl-dev linux-headers python3-dev
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt