curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12
source $HOME/.local/bin/env
uv pip install -r requirements.txt