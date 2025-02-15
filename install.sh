sudo apk add gcc p3-dev musl-dev linux-headers
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt