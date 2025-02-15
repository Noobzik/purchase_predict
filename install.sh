apk add --no-cache gcc g++ musl-dev linux-headers python3-dev cmake ninja
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt